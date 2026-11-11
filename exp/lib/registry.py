"""registry.yaml of a sub-experiment: the smallest subset of SkillParseUMR's skillsets/REGISTRY.md.

    waves:                      in order
      - name: sentence          a wave may go item by item (for_each, one episode per item) and read
        start: graph            the items around the current one (window), as in SkillParseUMR
        parallel: 8             REGISTRY.md 2.1 and 5.2; parallel: episodes at a time
        init_input:
          for_each: {sentence: annotation.sents}
          context: {line: sentence.line, prev: {window: annotation.sents, range: [-5, 0], pick: line}}
      - name: document
        start: annotate         the first skill of the episode
        init_input:             no for_each: the whole document is one episode
          context: {lang: annotation.lang, doc_id: annotation.name}
          input:   {sentences: annotation.lines}
    skills:
      annotate:
        path: annotate          directory with skill.md, relative to registry.yaml
        guideline: guidelines/umr_guidelines_abridged.md   (this repo's addition) filled into {guideline};
                                relative to exp/
        tools: [search_guidelines]   (this repo's addition) tools of exp/tools/ the skill may call
        input: {sentences: str}
        emit:  {umr: str}       the answer, plain text
        store: [umr]
    dispatcher:                 after a skill, which skills run next (here: none)
      <skill>: [{run: <skill>, input: {<var>: <expression>}}]

Expressions are dot paths: annotation.<attr>, a context variable, an input variable, <skill>_emit.<field>.
annotation has: name, lang, lines (the document, one sentence per line: "<number>\\t<words>"),
sentences (the number of sentences), sents ([{index, line}], one per sentence). worktree.<wave> of a
for_each wave is its episodes' root nodes in order, so a later wave can go over it with for_each and
window (pick: a stored field).

skill.md is filled with str.format (literal braces written {{ }}) and cut at the line "## Input":
what comes before is the system prompt (the same for every document, so it is cached), the rest the
user message. A chat sub-experiment has the same files; its prompt is the two parts one after the other.
"""
import json
import os

import yaml

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP = {"waves", "skills", "dispatcher"}


class RegistryError(Exception):
    pass


def load(path):
    with open(path, encoding="utf-8") as f:
        reg = yaml.safe_load(f)
    if set(reg) != TOP:
        raise RegistryError("%s: top-level keys must be exactly %s" % (path, sorted(TOP)))
    reg["dir"] = os.path.dirname(os.path.abspath(path))
    for name, s in reg["skills"].items():
        for key in ("path", "emit"):
            if key not in s:
                raise RegistryError("skill %s: %s is required" % (name, key))
        md = os.path.join(reg["dir"], s["path"], "skill.md")
        if not os.path.exists(md):
            raise RegistryError("skill %s: no %s" % (name, md))
        s["template"] = open(md, encoding="utf-8").read()
        if "\n## Input" not in s["template"]:
            raise RegistryError("skill %s: skill.md has no '## Input' line" % name)
        s.setdefault("input", {})
        s.setdefault("store", [])
        s.setdefault("tools", [])
        if s.get("guideline"):
            g = os.path.join(EXP, s["guideline"])
            s["guideline_text"] = open(g, encoding="utf-8").read()
    for w in reg["waves"]:
        if w["start"] not in reg["skills"]:
            raise RegistryError("wave %s: start %s is not a skill" % (w["name"], w["start"]))
    for skill, rules in (reg["dispatcher"] or {}).items():
        for r in rules or []:
            if r.get("run") not in reg["skills"]:
                raise RegistryError("dispatcher %s: run %s is not a skill" % (skill, r.get("run")))
    return reg


def value(expr, names):
    """A dot-path expression evaluated over names."""
    parts = str(expr).split(".")
    if parts[0] not in names:
        raise RegistryError("unknown name %s in %s" % (parts[0], expr))
    x = names[parts[0]]
    for p in parts[1:]:
        x = x[p] if isinstance(x, dict) else getattr(x, p)
    return x


def render(skill, variables):
    """(system, user) of a skill filled with its variables. A list of strings is filled in as its items
    one after the other, separated by blank lines (this repo's choice: graphs read better so than as
    JSON); any other list or dict as JSON."""
    variables = dict(variables)
    if "guideline_text" in skill:
        variables["guideline"] = skill["guideline_text"]
    for k, v in list(variables.items()):
        if isinstance(v, list) and all(isinstance(x, str) for x in v):
            variables[k] = "\n\n".join(v) if v else "(none)"
        elif isinstance(v, (list, dict)):
            variables[k] = json.dumps(v, ensure_ascii=False)
    text = skill["template"].format(**variables)
    cut = text.index("\n## Input")
    return text[:cut].rstrip() + "\n", text[cut + 1:]


def _expr(e, names, i):
    """A dot path, or a window {window: <list>, range: [start, stop), pick: <attr>} around item i."""
    if isinstance(e, dict) and "window" in e:
        items = value(e["window"], names)
        a, b = e["range"]
        out = items[max(0, i + a):max(0, i + b)]
        if e.get("pick"):
            out = [value("x." + e["pick"], {"x": x}) for x in out]
        return out
    return value(e, names)


def _episode(reg, w, names, i, call_skill, tag):
    init = w.get("init_input", {})
    try:
        context = {k: _expr(v, names, i) for k, v in (init.get("context") or {}).items()}
        root_input = {k: _expr(v, names, i) for k, v in (init.get("input") or {}).items()}
    except Exception as e:      # e.g. the item of an earlier wave failed and has no stored field
        return [{"id": "0", "skill": w["start"], "status": "error", "error": "input: %s: %s" % (type(e).__name__, e)}]
    queue = [("0", w["start"], root_input)]
    nodes = []
    while queue and len(nodes) < w.get("max_nodes", 20):
        node_id, name, inp = queue.pop(0)
        skill = reg["skills"][name]
        node = {"id": node_id, "skill": name, "input": inp}
        try:
            system, user = render(skill, {**context, **inp})
            emit = call_skill(name, skill, system, user, tag)
            missing = [k for k in skill["emit"] if k not in emit]
            if missing:
                raise RegistryError("%s emitted no %s" % (name, ", ".join(missing)))
            node["status"] = "ok"
            node.update({k: emit[k] for k in skill["store"]})
            node["emit"] = emit
        except Exception as e:
            node["status"] = "error"
            node["error"] = "%s: %s" % (type(e).__name__, str(e)[:500])
            nodes.append(node)
            continue
        nodes.append(node)
        scope = {**context, **inp, name + "_emit": emit}
        for k, r in enumerate((reg["dispatcher"] or {}).get(name) or []):
            child = {v: value(e, scope) for v, e in (r.get("input") or {}).items()}
            queue.append(("%s.%d" % (node_id, k), r["run"], child))
    return nodes


def run(reg, annotation, call_skill):
    """Every wave of the registry over one document. call_skill(name, skill, system, user, tag) -> emit
    dict; tag names the episode ("" for a wave without for_each, else "<wave>-<k>", k from 1).
    Returns {wave name: ...}: for a wave without for_each, its one episode's nodes [{id, skill, input,
    status, <stored fields>}]; with for_each, one entry per item, the episode's root node, in order (so
    worktree.<wave> can be read by a later wave's for_each and window)."""
    from concurrent.futures import ThreadPoolExecutor
    worktree = {}
    for w in reg["waves"]:
        init = w.get("init_input", {})
        names = {"annotation": annotation, "worktree": worktree}
        each = init.get("for_each")
        if not each:
            worktree[w["name"]] = _episode(reg, w, names, 0, call_skill, "")
            continue
        lists = {k: value(v, names) for k, v in each.items()}
        n = len(next(iter(lists.values())))
        if any(len(v) != n for v in lists.values()):
            raise RegistryError("wave %s: for_each lists of different lengths" % w["name"])

        def one(i):
            item = {**names, **{k: v[i] for k, v in lists.items()}}
            return _episode(reg, w, item, i, call_skill, "%s-%d" % (w["name"], i + 1))[0]

        with ThreadPoolExecutor(w.get("parallel", 1)) as pool:
            worktree[w["name"]] = list(pool.map(one, range(n)))
    return worktree

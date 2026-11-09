"""registry.yaml of a sub-experiment: the smallest subset of SkillParseUMR's skillsets/REGISTRY.md.

    waves:                      in order; here every sub-experiment has one wave
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
sentences (the number of sentences).

skill.md is filled with str.format (literal braces written {{ }}) and cut at the line "## Input":
what comes before is the system prompt (the same for every document, so it is cached), the rest the
user message. A chat sub-experiment has the same files; its prompt is the two parts one after the other.
"""
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
        if "for_each" in w.get("init_input", {}):
            raise RegistryError("wave %s: for_each is not supported here (one episode per document)" % w["name"])
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
    """(system, user) of a skill filled with its variables."""
    variables = dict(variables)
    if "guideline_text" in skill:
        variables["guideline"] = skill["guideline_text"]
    text = skill["template"].format(**variables)
    cut = text.index("\n## Input")
    return text[:cut].rstrip() + "\n", text[cut + 1:]


def run(reg, annotation, call_skill):
    """Every wave of the registry over one document. call_skill(name, skill, system, user) -> emit dict.
    Returns {wave name: [nodes]}, each node {id, skill, input, status, <stored fields>}."""
    worktree = {}
    for w in reg["waves"]:
        init = w.get("init_input", {})
        names = {"annotation": annotation, "worktree": worktree}
        context = {k: value(v, names) for k, v in (init.get("context") or {}).items()}
        root_input = {k: value(v, names) for k, v in (init.get("input") or {}).items()}
        queue = [("0", w["start"], root_input)]
        nodes = []
        while queue and len(nodes) < w.get("max_nodes", 20):
            node_id, name, inp = queue.pop(0)
            skill = reg["skills"][name]
            node = {"id": node_id, "skill": name, "input": inp}
            try:
                system, user = render(skill, {**context, **inp})
                emit = call_skill(name, skill, system, user)
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
        worktree[w["name"]] = nodes
    return worktree

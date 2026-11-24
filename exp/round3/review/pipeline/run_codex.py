"""Annotate the documents with Codex (`codex exec`, the ChatGPT/Codex subscription login, never an API key).

    python3 pipeline/run_codex.py --check                      the environment: codex, its login, Python packages
    python3 pipeline/run_codex.py --docs en-0008,arp-0005      a trial: two short documents, every condition, both runs
    python3 pipeline/run_codex.py --docs test                  only the test documents (data/docs.json "test")
    python3 pipeline/run_codex.py                              everything in config.json (what is done is skipped)
    python3 pipeline/run_codex.py --conds s3-all --runs r1 --docs zh-0001,zh-0002
    python3 pipeline/run_codex.py --status                     what is done
    python3 pipeline/run_codex.py --dry-run --docs zh-0032     build the run directories only, print the commands

Options: --jobs N (Codex sessions at a time, default config.json), --redo (run again what is done),
--keep-work (keep the run directories of finished sessions), --allow-api-key (do not refuse an API-key login).

Every condition is run twice with the same model (config.json "models": r1 and r2). r1 has the original task
description (prompts/), r2 a reworded one (prompts-r2/: the same content in other words and another order,
and a reworded one-line instruction); guidelines, tools, output format and input are the same.

One Codex session works in a run directory of its own, <work>/<model>-<run>/<condition>/<doc>[/gN|rN]/, that
holds only what the condition gives: TASK.md (the run's <condition>.TASK.md filled in), guidelines/, tools/
(commands), notes/. Its only instruction is to do TASK.md and write answer.txt.

  whole-document conditions (s1-full, s3-all): one session per document.
  a2-sentence-all: wave 1, one session per sentence, given that sentence only, writes its graph; wave 2, once
  every sentence of the document has a graph, one session per sentence, given the sentence and the five
  before it with their graphs, writes its document-level relations. The two waves are put together as one
  answer (as HarnessOntologyAnnotation/exp/run.py does for the API runs).

Results, runs/<condition>/<model>-<effort>-<run>/:
  <doc>.raw.txt          the answer as written (a2: the pieces put together)
  <doc>.umr              the answer as a .umr file (lib/umrdoc.py: alignment added, relations put per sentence)
  <doc>.trace.json       the parse report (sentences found, problems)
  <doc>.meta.json        time, token usage, lookups, attempts, audit flags
  <doc>.transcript.jsonl the whole session (codex --json); a2: <doc>.calls/gN.*, rN.*

Everything is resumable: a finished piece is not run again. A session that leaves no usable answer is tried
again (config.json "retries"); when Codex reports a usage or rate limit the runner waits and tries again.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import umrdoc  # noqa: E402

CX = C.CONFIG["codex"]
PROMPT = ("Do the task described in TASK.md in this directory and write the answer to answer.txt. Work on your "
          "own, without asking questions, until answer.txt holds the whole answer. Use only this directory.")
STUB = """#!/usr/bin/env python3
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, %r)
from tools.cli import main
main(%r, %r, sys.argv[1:])
"""
LOCK = threading.Lock()
STOP = threading.Event()        # set when the usage limit does not go away: finish nothing more


def say(*a):
    with LOCK:
        print(time.strftime("%H:%M:%S"), *a, flush=True)


# ------------------------------------------------------------------ the environment

def codex_env():
    """The environment of a Codex session: no API key, so that it can only use the saved login."""
    env = {k: v for k, v in os.environ.items() if k not in CX["drop_env"]}
    env["PYTHONIOENCODING"] = "utf-8"
    return env


def check(allow_api_key=False, quiet=False):
    ok = True
    try:
        v = subprocess.run([CX["bin"], "--version"], capture_output=True, text=True, env=codex_env())
        print("codex:", (v.stdout + v.stderr).strip())
    except FileNotFoundError:
        raise SystemExit("no `%s` command: install the Codex CLI and log in (codex login)" % CX["bin"])
    s = subprocess.run([CX["bin"], "login", "status"], capture_output=True, text=True, env=codex_env())
    status = (s.stdout + s.stderr).strip()
    print("codex login status:", status)
    if s.returncode != 0:
        print("  NOT LOGGED IN: run `codex login` and choose the ChatGPT account (the subscription).")
        ok = False
    elif re.search(r"api[ _-]?key", status, re.I) and not allow_api_key:
        print("  This is an API-key login: runs would be billed per token. Run `codex logout`, then `codex login`\n"
              "  with the ChatGPT account. (--allow-api-key runs anyway.)")
        ok = False
    dropped = [k for k in CX["drop_env"] if os.environ.get(k)]
    if dropped and not quiet:
        print("  note: %s set in this shell; not passed to Codex sessions" % ", ".join(dropped))
    for mod in ("penman",):
        try:
            __import__(mod)
        except ImportError:
            print("  missing Python package %s: pip install -r requirements.txt" % mod)
            ok = False
    work = work_root()
    if os.path.commonpath([work, C.PKG]) == C.PKG:
        print("  work_dir %s is inside the package: sessions would read AGENTS.md and the gold. Put it outside." % work)
        ok = False
    print("work directory:", work)
    print("runs:", ", ".join("%s = %s, effort %s, %s/" % (m["key"], m["model"], m["effort"], m.get("prompts", "prompts"))
                             for m in C.CONFIG["models"]))
    return ok


def work_root():
    return os.path.abspath(os.path.join(C.PKG, C.CONFIG["work_dir"]))


# ------------------------------------------------------------------ one session

def build_dir(w, cond, doc_name, task_text):
    if os.path.exists(w):
        shutil.rmtree(w)
    for d in ("guidelines", "notes"):
        os.makedirs(os.path.join(w, d))
    with open(os.path.join(w, "TASK.md"), "w", encoding="utf-8") as f:
        f.write(task_text)
    for g in cond["guidelines"]:
        shutil.copy(os.path.join(C.PKG, "resources", "guidelines", g), os.path.join(w, "guidelines", g))
    if cond["tools"]:
        os.makedirs(os.path.join(w, "tools"))
        for t in cond["tools"]:
            p = os.path.join(w, "tools", t + ".py")
            with open(p, "w", encoding="utf-8") as f:
                f.write(STUB % (C.PKG, t, doc_name))
            os.chmod(p, 0o755)


def command(model, w):
    cmd = [CX["bin"]] + CX["exec_args"] + CX.get("clean_args", [])
    cmd += [CX["model_flag"], model["model"], CX["cd_flag"], w,
            CX["last_message_flag"], os.path.join(w, ".last_message.txt")]
    if CX.get("effort_override") and model.get("effort"):
        cmd += ["-c", CX["effort_override"].format(effort=model["effort"])]
    return cmd + [model.get("instruction") or PROMPT]


def read_events(path):
    """(usage summed over the turns, the commands run, other items, the errors) of a codex --json transcript."""
    usage, commands, others, errors = {}, [], [], []
    try:
        lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    except OSError:
        return usage, commands, others, errors
    for line in lines:
        try:
            e = json.loads(line)
        except ValueError:
            continue
        if not isinstance(e, dict):
            continue
        t = e.get("type", "")
        if t == "turn.completed":
            for k, v in (e.get("usage") or {}).items():
                if isinstance(v, (int, float)):
                    usage[k] = usage.get(k, 0) + v
        elif t in ("error", "turn.failed"):
            errors.append(json.dumps(e, ensure_ascii=False)[:500])
        elif t == "item.completed":
            item = e.get("item") or {}
            kind = item.get("type") or item.get("item_type") or ""
            if kind == "command_execution":
                commands.append(str(item.get("command", "")))
            elif kind not in ("agent_message", "reasoning", "file_change", "todo_list", "plan_update", ""):
                others.append(kind)
    return usage, commands, others, errors


def audit(commands, others, cond):
    """What a session should not have done: reading outside its directory (the gold, the training files, this
    package), the web, a tool the condition does not have. Flags only; nothing is blocked here."""
    flags = []
    allowed = {"python3 tools/%s.py" % t for t in cond["tools"]}
    for c in commands:
        low = c.lower()
        if C.PKG in c or "data/gold" in low or "resources/training" in low or "gold_revised" in low:
            flags.append("reads the package: " + c[:200])
        elif re.search(r"chinese_umr|umr-codex-handoff", low):
            flags.append("names a gold/training file: " + c[:200])
        elif re.search(r"\b(curl|wget|https?://|pip3? install|git clone)\b", low):
            flags.append("network: " + c[:200])
        elif "tools/" in c and not any(a in c for a in allowed):
            flags.append("tool not in this condition: " + c[:200])
    for o in others:
        if "search" in o or "mcp" in o:
            flags.append("item " + o)
    return sorted(set(flags))[:20]


def session(model, cond, doc_name, w, task_text, out_base, timeout, valid, dry=False):
    """Run Codex in w until `valid(answer text)` gives a usable answer. -> (answer or None, meta)."""
    meta = {"attempts": 0, "seconds": 0.0, "usage": {}, "commands": 0, "lookups": 0, "audit": [], "errors": []}
    answer, best = None, None
    for attempt in range(1 + C.CONFIG["retries"]):
        if STOP.is_set():
            break
        build_dir(w, cond, doc_name, task_text)
        cmd = command(model, w)
        if dry:
            say("dry run:", " ".join(json.dumps(x, ensure_ascii=False) if " " in x else x for x in cmd))
            return None, meta
        waits = 0
        while True:
            t0 = time.time()
            log_path = out_base + ".transcript.jsonl"
            with open(log_path, "w", encoding="utf-8") as log:
                try:
                    p = subprocess.run(cmd, cwd=w, env=codex_env(), stdin=subprocess.DEVNULL, stdout=log,
                                       stderr=subprocess.STDOUT, text=True, timeout=timeout * 60)
                    code = p.returncode
                except subprocess.TimeoutExpired:
                    code = -9
            meta["seconds"] += round(time.time() - t0, 1)
            usage, commands, others, errors = read_events(log_path)
            tail = open(log_path, encoding="utf-8", errors="replace").read()[-4000:].lower()
            limited = code != 0 and not os.path.exists(os.path.join(w, "answer.txt")) and any(
                x in tail for x in CX["limit_patterns"])
            if limited and waits < CX["limit_max_waits"]:
                waits += 1
                say("usage/rate limit reported (%s); waiting %d min (%d/%d)" % (
                    os.path.basename(out_base), CX["limit_wait_minutes"], waits, CX["limit_max_waits"]))
                time.sleep(CX["limit_wait_minutes"] * 60)
                continue
            if limited:
                STOP.set()
                say("the limit did not go away: stopping. Run the same command again later; finished work is kept.")
            break
        meta["attempts"] += 1
        for k, v in usage.items():
            meta["usage"][k] = meta["usage"].get(k, 0) + v
        meta["commands"] += len(commands)
        meta["audit"] = sorted(set(meta["audit"] + audit(commands, others, cond)))
        meta["errors"] += errors[:3] + (["exit %d" % code] if code else [])
        tc = os.path.join(w, ".tool_calls.jsonl")
        if os.path.exists(tc):
            meta["lookups"] += sum(1 for _ in open(tc, encoding="utf-8"))
        path = os.path.join(w, "answer.txt")
        text = open(path, encoding="utf-8", errors="replace").read() if os.path.exists(path) else ""
        if not text.strip() and os.path.exists(os.path.join(w, ".last_message.txt")):
            # the answer was given as the last message instead of the file
            text = open(os.path.join(w, ".last_message.txt"), encoding="utf-8", errors="replace").read()
            if text.strip():
                meta["errors"].append("answer.txt missing: took the last message")
        quality, problem = valid(text)
        if best is None or quality > best[0]:
            best = (quality, text)
        if problem is None:
            answer = text
            break
        meta["errors"].append("attempt %d: %s" % (attempt + 1, problem))
    if answer is None and best is not None and best[0] > 0:
        answer = best[1]            # an imperfect answer is still kept (the parse report says what is wrong)
        meta["errors"].append("kept the best imperfect answer")
    return answer, meta


# ------------------------------------------------------------------ what counts as an answer

def valid_document(doc):
    def f(text):
        if not text.strip():
            return 0, "no answer"
        _, report = umrdoc.parse_answer(doc, text)
        bad = [p for p in report["problems"] if "missing" in p or "does not parse" in p]
        q = report["sentences_found"] - len([p for p in bad if "does not parse" in p]) + (1 if report["relations"] else 0)
        if report["sentences_found"] < report["sentences"]:
            return q, "%d of %d sentences" % (report["sentences_found"], report["sentences"])
        if report["relations"] == 0:
            return q, "no document-level relations"
        if any("does not parse" in p for p in bad):
            return q, "; ".join(bad)[:200]
        return q, None
    return f


def clean_graph(index, text):
    """A wave-1 answer as '# ::snt N / # sentence level graph: / graph'; None when there is no graph."""
    text = re.sub(r"^\s*```\w*\s*$", "", text.replace("\r", ""), flags=re.M)
    m = re.search(r"^\s*\(", text, re.M)
    if not m:
        return None
    graph = text[m.start():].strip()
    graph = re.split(r"^\s*#", graph, flags=re.M)[0].strip()       # anything after the graph is dropped
    return "# ::snt %d\n# sentence level graph:\n%s" % (index, graph)


def valid_graph(index):
    def f(text):
        g = clean_graph(index, text)
        if g is None:
            return 0, "no graph"
        problems = []
        umrdoc.sentence_sections(index, g.split("\n", 2)[2], "", problems=problems)
        bad = [p for p in problems if "does not parse" in p or "brackets repaired" in p]
        if bad or " / " not in g:        # one sentence is cheap to do again: only a clean graph is accepted
            return 1, (bad or ["no concept in the graph"])[0][:200]
        return 2, None
    return f


def valid_relations(text):
    if not text.strip():
        return 0, "no answer"
    if "(d / document" not in text and not umrdoc.read_doc(text):
        return 1, "no document-level graph"
    return 2, None


# ------------------------------------------------------------------ the work

EX_GRAPH_START, EX_GRAPH_END = "    (s1t / taste-01\n", "        :aspect performance)\n"
EX_DOC_START, EX_DOC_END = "    (d / document\n        :temporal ((document-creation-time :depends-on s1t2)", ":coref ((s1p :same-entity s2p)))\n"
EX_CLAUSE = '(in English its lemma: `taste-01` for "tasted")'
LANGUAGES = json.load(open(os.path.join(C.PKG, "prompts", "languages.json"), encoding="utf-8"))["languages"]


def template(name, model, lang="zh"):
    """The task description of a condition in the wording of the run (config.json "prompts"), for a language.

    Chinese gets the template as it is (the first round's text). For another language (prompts/languages.json)
    three things are put in: the example under Output format becomes an annotated sentence of that language's
    training data (the English one in the templates is a sentence of the test file en-0008); the remark on how
    a concept is written; and, before Output format, a section of notes on the language: how its data writes
    concepts and roles, and what the tools have for it (only in a condition with tools; none in the baseline)."""
    text = open(os.path.join(C.PKG, model.get("prompts", "prompts"), name + ".TASK.md"), encoding="utf-8").read()
    L = LANGUAGES.get(lang)
    if lang == "zh" or L is None:
        return text

    def swap(start, end, new):
        nonlocal text
        if start in text:
            i = text.index(start)
            j = text.index(end, i) + len(end)
            text = text[:i] + new.replace("{", "{{").replace("}", "}}") + text[j:]

    swap(EX_GRAPH_START, EX_GRAPH_END, L["graph"])
    swap(EX_DOC_START, EX_DOC_END, L["doc"])
    text = text.replace(EX_CLAUSE, L["clause"])
    notes = []
    if not name.startswith("s0-") and L.get("notes"):
        notes.append(L["notes"])
    if "tools/propbank_lookup.py" in text and L.get("tools"):
        notes.append(L["tools"])
    if "(d / document" in L["doc"] and L.get("doc_is_illustration") and EX_DOC_START not in text and "# document level relations:" in text \
            and not name.startswith("s0-") and not name.endswith(".relations") and not name.endswith(".graph"):
        notes.append("The document-level graph in the example under Output format shows the format only: the training "
                     "sentence it belongs to has no document-level annotation.")
    if notes:
        section = "## Notes for %s\n\n%s\n\n" % (L["name"], "\n\n".join(notes))
        i = text.index("## Output format")
        text = text[:i] + section.replace("{", "{{").replace("}", "}}") + text[i:]
    return text


def write_meta(path, meta, **more):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({**more, **meta}, f, ensure_ascii=False, indent=1)


def finish_document(out_dir, d, doc, text, meta, model, cond):
    """<doc>.raw.txt, .umr, .trace.json, .meta.json of a finished document."""
    name = d["doc"]
    with open(os.path.join(out_dir, name + ".raw.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    umr, report = umrdoc.parse_answer(doc, text)
    with open(os.path.join(out_dir, name + ".umr"), "w", encoding="utf-8") as f:
        f.write(umr)
    with open(os.path.join(out_dir, name + ".trace.json"), "w", encoding="utf-8") as f:
        json.dump({"doc": name, "parse": report}, f, ensure_ascii=False, indent=1)
    write_meta(os.path.join(out_dir, name + ".meta.json"), meta, doc=name, condition=cond["name"],
               model=model["model"], effort=model["effort"], run=model.get("run"), prompts=model.get("prompts"),
               harness="codex exec")
    say("%s %s %s: %d/%d sentences, %d relations, %d problems, %d lookups, %.0f min%s" % (
        cond["name"], model["key"], name, report["sentences_found"], report["sentences"], report["relations"],
        len(report["problems"]), meta.get("lookups", 0), meta.get("seconds", 0) / 60,
        ", AUDIT FLAGS %d" % len(meta["audit"]) if meta.get("audit") else ""))


def whole_document(model, cond, d, a):
    out_dir = os.path.join(C.RUNS, cond["name"], C.label(model))
    os.makedirs(out_dir, exist_ok=True)
    name = d["doc"]
    if os.path.exists(os.path.join(out_dir, name + ".umr")) and not a.redo:
        return
    doc = C.load_input(d)
    task = template(cond["name"], model, doc["lang"]).format(lang=doc["lang"], lang_label=C.lang_label(doc["lang"]), doc_id=name,
                                         n=len(doc["sents"]), sentences=umrdoc.input_lines(doc))
    w = os.path.join(work_root(), C.label(model), cond["name"], name)
    t = CX["timeout_minutes"]
    answer, meta = session(model, cond, name, w, task, os.path.join(out_dir, name),
                           t["whole_base"] + t["whole_per_sentence"] * len(doc["sents"]), valid_document(doc), a.dry_run)
    if answer is None:
        if not a.dry_run:
            say("%s %s %s: NO ANSWER (%s)" % (cond["name"], model["key"], name, "; ".join(meta["errors"])[-300:]))
            write_meta(os.path.join(out_dir, name + ".failed.json"), meta, doc=name)
        return
    finish_document(out_dir, d, doc, answer, meta, model, cond)
    if os.path.exists(os.path.join(out_dir, name + ".failed.json")):
        os.remove(os.path.join(out_dir, name + ".failed.json"))
    if not a.keep_work:
        shutil.rmtree(w, ignore_errors=True)


def piece(model, cond, d, doc, kind, s, a):
    """One wave-1 (kind 'g') or wave-2 (kind 'r') session of sentence s. The answer is kept in
    <doc>.calls/<kind><N>.txt; True when it is there."""
    name, i = d["doc"], s["index"]
    calls = os.path.join(C.RUNS, cond["name"], C.label(model), name + ".calls")
    os.makedirs(calls, exist_ok=True)
    base = os.path.join(calls, "%s%d" % (kind, i))
    if os.path.exists(base + ".txt") and not a.redo:
        return True
    line = "%d\t%s" % (i, " ".join(s["words"]))
    common = dict(lang=doc["lang"], lang_label=C.lang_label(doc["lang"]), doc_id=name, n=len(doc["sents"]), num=i, line=line)
    if kind == "g":
        task = template(cond["name"] + ".graph", model, doc["lang"]).format(**common)
        valid = valid_graph(i)
    else:
        prev = [x for x in doc["sents"] if i - 5 <= x["index"] < i]
        graphs = {x["index"]: open(os.path.join(calls, "g%d.txt" % x["index"]), encoding="utf-8").read().strip()
                  for x in prev + [s]}
        task = template(cond["name"] + ".relations", model, doc["lang"]).format(
            prev_lines="\n\n".join("%d\t%s" % (x["index"], " ".join(x["words"])) for x in prev) or "(none)",
            prev_graphs="\n\n".join(graphs[x["index"]] for x in prev) or "(none)", graph=graphs[i], **common)
        valid = valid_relations
    w = os.path.join(work_root(), C.label(model), cond["name"], name, "%s%d" % (kind, i))
    answer, meta = session(model, cond, name, w, task, base, CX["timeout_minutes"]["sentence"], valid, a.dry_run)
    if answer is None:
        if not a.dry_run:
            say("%s %s %s %s%d: NO ANSWER (%s)" % (cond["name"], model["key"], name, kind, i,
                                                 "; ".join(meta["errors"])[-200:]))
            write_meta(base + ".failed.json", meta)
        return False
    text = clean_graph(i, answer) if kind == "g" else answer.strip()
    if text is None:            # an unparseable graph kept as written: the parser will report it
        text = "# ::snt %d\n# sentence level graph:\n%s" % (i, answer.strip())
    with open(base + ".txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    write_meta(base + ".meta.json", meta)
    if os.path.exists(base + ".failed.json"):
        os.remove(base + ".failed.json")
    if not a.keep_work:
        shutil.rmtree(w, ignore_errors=True)
    return True


def assemble(model, cond, d, doc, a):
    """The two waves of a document as one answer, when every piece is there."""
    name = d["doc"]
    out_dir = os.path.join(C.RUNS, cond["name"], C.label(model))
    calls = os.path.join(out_dir, name + ".calls")
    if os.path.exists(os.path.join(out_dir, name + ".umr")) and not a.redo:
        return
    graphs, rels, meta = [], [], {"attempts": 0, "seconds": 0.0, "usage": {}, "commands": 0, "lookups": 0,
                                  "audit": [], "errors": [], "sessions": 0}
    for s in doc["sents"]:
        for kind in ("g", "r"):
            p = os.path.join(calls, "%s%d.txt" % (kind, s["index"]))
            if not os.path.exists(p):
                return
            text = open(p, encoding="utf-8").read().strip()
            if kind == "g":
                graphs.append(text)
            else:
                rels.append(re.sub(r"(?im)^\s*#\s*document level relations:?\s*$", "", text).strip())
            m = json.load(open(p[:-4] + ".meta.json", encoding="utf-8"))
            meta["sessions"] += 1
            for k in ("attempts", "seconds", "commands", "lookups"):
                meta[k] += m.get(k, 0)
            for k, v in m.get("usage", {}).items():
                meta["usage"][k] = meta["usage"].get(k, 0) + v
            meta["audit"] += ["%s%d: %s" % (kind, s["index"], x) for x in m.get("audit", [])]
            meta["errors"] += ["%s%d: %s" % (kind, s["index"], x) for x in m.get("errors", [])]
    meta["seconds"] = round(meta["seconds"], 1)
    text = "\n\n".join(graphs) + "\n\n# document level relations:\n" + "\n".join(rels) + "\n"
    finish_document(out_dir, d, doc, text, meta, model, cond)


def run(a):
    conds, mods, ds = C.conditions(a.conds), C.models(a.models), C.docs(a.docs)
    if a.smoke:
        ds = C.docs("zh-0032")
    if not a.dry_run and not check(a.allow_api_key, quiet=True):
        raise SystemExit("fix the above first (python3 pipeline/run_codex.py --check)")
    jobs = a.jobs or C.CONFIG["jobs"]
    say("%d documents, conditions %s, runs %s, %d sessions at a time" % (
        len(ds), ", ".join(c["name"] for c in conds), ", ".join(C.label(m) for m in mods), jobs))
    loaded = {d["doc"]: C.load_input(d) for d in ds}
    sentence_conds = [c for c in conds if c["kind"] == "sentence"]
    first, second = [], []
    def finished(m, c, d):      # the document's .umr is there: nothing of it is run again
        return os.path.exists(os.path.join(C.RUNS, c["name"], C.label(m), d["doc"] + ".umr")) and not a.redo

    for d in ds:                # document by document, so that whole documents finish early
        for m in mods:
            for c in conds:
                if d not in C.cond_docs(c, ds) or finished(m, c, d):
                    continue
                if c["kind"] == "whole":
                    first.append(lambda m=m, c=c, d=d: whole_document(m, c, d, a))
                else:
                    for s in loaded[d["doc"]]["sents"]:
                        first.append(lambda m=m, c=c, d=d, s=s: piece(m, c, d, loaded[d["doc"]], "g", s, a))

    def guarded(f):
        if STOP.is_set():
            return None
        try:
            return f()
        except Exception as e:      # one failed piece must not end the run
            say("ERROR %s: %s" % (type(e).__name__, str(e)[:300]))
            return None

    with ThreadPoolExecutor(jobs) as pool:
        list(pool.map(guarded, first))
    for d in ds:
        for m in mods:
            for c in sentence_conds:
                if d not in C.cond_docs(c, ds) or finished(m, c, d):
                    continue
                calls = os.path.join(C.RUNS, c["name"], C.label(m), d["doc"] + ".calls")
                doc = loaded[d["doc"]]
                if all(os.path.exists(os.path.join(calls, "g%d.txt" % s["index"])) for s in doc["sents"]):
                    for s in doc["sents"]:
                        second.append(lambda m=m, c=c, d=d, s=s, doc=doc: piece(m, c, d, doc, "r", s, a))
                elif not a.dry_run:
                    say("%s %s %s: some sentence graphs are missing; relations not started" % (c["name"], m["key"], d["doc"]))
    with ThreadPoolExecutor(jobs) as pool:
        list(pool.map(guarded, second))
    if not a.dry_run:
        for d in ds:
            for m in mods:
                for c in sentence_conds:
                    if d in C.cond_docs(c, ds):
                        assemble(m, c, d, loaded[d["doc"]], a)
        status(conds, mods, ds)
    if STOP.is_set():
        sys.exit(3)


def status(conds=None, mods=None, ds=None):
    conds, mods, all_ds = conds or C.conditions(), mods or C.models(), ds or C.docs()
    print("\n| condition | run | documents | sentences found | parse problems | audit flags | failed |")
    print("|---|---|---|---|---|---|---|")
    done_all = True
    for c in conds:
        for m in mods:
            out = os.path.join(C.RUNS, c["name"], C.label(m))
            n = found = problems = flags = failed = 0
            ds = C.cond_docs(c, all_ds)
            total = sum(d["sents"] for d in ds)
            for d in ds:
                t = os.path.join(out, d["doc"] + ".trace.json")
                if os.path.exists(t):
                    n += 1
                    r = json.load(open(t, encoding="utf-8"))["parse"]
                    found += r["sentences_found"] - sum(1 for p in r["problems"] if "does not parse" in p)
                    problems += len(r["problems"])
                    flags += len(json.load(open(os.path.join(out, d["doc"] + ".meta.json"), encoding="utf-8")).get("audit", []))
                if os.path.exists(os.path.join(out, d["doc"] + ".failed.json")):
                    failed += 1
                calls = os.path.join(out, d["doc"] + ".calls")
                if os.path.isdir(calls):
                    failed += sum(1 for x in os.listdir(calls) if x.endswith(".failed.json"))
            done_all = done_all and n == len(ds)
            print("| %s | %s | %d/%d | %d/%d | %d | %d | %d |" % (c["name"], C.label(m), n, len(ds), found, total,
                                                                problems, flags, failed))
    print("\nall done" if done_all else "\nnot complete: run the same command again (finished work is kept)")
    return done_all


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--conds", default="")
    ap.add_argument("--runs", "--models", dest="models", default="", help="r1, r2 (default both)")
    ap.add_argument("--docs", default="")
    ap.add_argument("--jobs", type=int, default=0)
    ap.add_argument("--redo", action="store_true")
    ap.add_argument("--keep-work", action="store_true")
    ap.add_argument("--allow-api-key", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.check:
        sys.exit(0 if check(a.allow_api_key) else 1)
    if a.status:
        status(C.conditions(a.conds), C.models(a.models), C.docs(a.docs))
        return
    run(a)


if __name__ == "__main__":
    main()

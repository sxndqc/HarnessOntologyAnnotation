"""Run the conditions of config.json with the claude CLI (the subscription's Claude Sonnet 5.5, effort medium).

    python3 run_claude.py --conds s0-oneline,s1-abridged --group test [--variants 1-5] [--reps 1-2] [--jobs 6]
    python3 run_claude.py --conds s3-full-two-tool --group train --reps 1 --skill skills/m1-r1.md --tag m1-r1

One run = one document in one prompt: the instruction (one of five wordings), the guideline of the condition,
one sentence on the tools if there are any, the parse skill if one is given, the output format, the document.
The model has no built-in tool (--tools ""), no settings, no project files; the lookup tools are served by
mcp_tools.py. The final message is the answer. Output: runs/<condition>[+tag]/p<wording>r<rep>/<doc>.raw.txt,
.umr (with the alignment computed as in round 2), .meta.json (usage, seconds, turns, lookups, attempts).
"""
import argparse
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
sys.path.insert(0, os.path.join(R2, "lib"))
import umrdoc  # noqa: E402

CONFIG = json.load(open(os.path.join(HERE, "config.json"), encoding="utf-8"))
GUIDE = os.path.join(R2, "resources", "guidelines-revised")
ONELINE = os.path.join(R2, "resources", "guidelines", "umr_guidelines_oneline.md")
LANG = {"zh": "Chinese", "en": "English"}
LOCK = threading.Lock()


def say(*a):
    with LOCK:
        print(time.strftime("%H:%M:%S"), *a, flush=True)


def guideline(name):
    p = ONELINE if name == "umr_guidelines_oneline.md" else os.path.join(GUIDE, name)
    return open(p, encoding="utf-8").read().strip()


def task(cond, variant, doc, skill=None):
    parts = [CONFIG["instructions"][variant - 1], "## Guidelines\n\n" + guideline(cond["guideline"])]
    if cond["tools"]:
        parts.append("## Tools\n\n" + CONFIG["tool_sentences"][",".join(cond["tools"])])
    if skill:
        parts.append("## Parse skill\n\nPoints learned from earlier annotations of this kind; follow them.\n\n" + skill.strip())
    parts.append(open(os.path.join(HERE, "OUTPUT_FORMAT.md"), encoding="utf-8").read().strip())
    parts.append("## Input\n\nLanguage: %s\nDocument: %s (%d sentences)\n\nThe document, one sentence per line: the sentence "
                 "number, a tab, then its words separated by spaces.\n\n%s" % (
                     LANG[doc["lang"]], doc["name"], len(doc["sents"]), umrdoc.input_lines(doc)))
    return "\n\n".join(parts) + "\n"


def check(doc, text):
    """(None or what is wrong, parse report)."""
    if not text.strip():
        return "no answer", {}
    _, report = umrdoc.parse_answer(doc, text)
    if report["sentences_found"] < report["sentences"]:
        return "%d of %d sentences" % (report["sentences_found"], report["sentences"]), report
    if report["relations"] == 0:
        return "no document-level relations", report
    return None, report


def call(prompt, tools, log, timeout):
    work = tempfile.mkdtemp(prefix="r3-")
    cmd = ["claude", "-p", "--model", CONFIG["model"], "--effort", CONFIG["effort"], "--tools", "",
           "--strict-mcp-config", "--setting-sources", "", "--output-format", "json",
           "--system-prompt", "You are an expert annotator of Uniform Meaning Representation (UMR)."]
    if tools:
        cfg = os.path.join(work, "mcp.json")
        json.dump({"mcpServers": {"umr": {"command": sys.executable, "args": [
            os.path.join(HERE, "mcp_tools.py"), "--tools", ",".join(tools), "--log", log]}}}, open(cfg, "w"))
        cmd += ["--mcp-config", cfg, "--allowedTools"] + ["mcp__umr__" + t for t in tools]
    t0 = time.time()
    try:
        r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, cwd=work)
        out = r.stdout
    except subprocess.TimeoutExpired:
        return None, {"error": "timeout after %d s" % timeout, "seconds": time.time() - t0}
    try:
        j = json.loads(out)
    except ValueError:
        return None, {"error": "no JSON: " + (out or r.stderr)[-300:], "seconds": time.time() - t0}
    meta = {"seconds": round(time.time() - t0, 1), "turns": j.get("num_turns"), "stop": j.get("stop_reason"),
            "list_cost_usd": j.get("total_cost_usd"), "served": list((j.get("modelUsage") or {}).keys()),
            "usage": {k: j.get("usage", {}).get(k) for k in ("input_tokens", "output_tokens", "cache_read_input_tokens",
                                                             "cache_creation_input_tokens")},
            "thinking_tokens": (j.get("usage", {}).get("output_tokens_details") or {}).get("thinking_tokens")}
    if j.get("is_error"):
        meta["error"] = str(j.get("result"))[:300]
        return None, meta
    return j.get("result") or "", meta


def one(job):
    cond, variant, rep, name, tag, skill, redo = job
    out_dir = os.path.join(HERE, "runs", cond["name"] + ("+" + tag if tag else ""), "p%dr%d" % (variant, rep))
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.join(out_dir, name)
    if os.path.exists(base + ".umr") and not redo:
        return
    doc = umrdoc.load_blind(os.path.join(HERE, "data", "input", name + ".txt"))
    prompt = task(cond, variant, doc, skill)
    log = base + ".calls.jsonl"
    attempts, best = [], None
    for attempt in range(3):
        if os.path.exists(log):
            os.remove(log)
        text, meta = call(prompt, cond["tools"], log, 3600)
        problem = meta.get("error")
        if text is not None:
            problem, report = check(doc, text)
        attempts.append({"problem": problem, **meta})
        if text is not None and (best is None or problem is None):
            best = (text, meta, problem)
        if problem is None:
            break
        say("%s p%dr%d %s attempt %d: %s" % (cond["name"] + ("+" + tag if tag else ""), variant, rep, name, attempt + 1, problem))
        if meta.get("error") and any(w in str(meta["error"]).lower() for w in ("limit", "overloaded", "rate", "429", "529")):
            time.sleep(300)
    if best is None:
        json.dump({"doc": name, "attempts": attempts}, open(base + ".failed.json", "w"), ensure_ascii=False, indent=1)
        say("%s p%dr%d %s: NO ANSWER" % (cond["name"], variant, rep, name))
        return
    text, meta, problem = best
    open(base + ".raw.txt", "w", encoding="utf-8").write(text)
    umr, report = umrdoc.parse_answer(doc, text)
    open(base + ".umr", "w", encoding="utf-8").write(umr)
    calls = [json.loads(l) for l in open(log, encoding="utf-8")] if os.path.exists(log) else []
    json.dump({"doc": name, "condition": cond["name"], "tag": tag, "wording": variant, "rep": rep, "model": CONFIG["model"],
               "effort": CONFIG["effort"], "harness": "claude -p", "prompt_chars": len(prompt), "problem": problem,
               "lookups": len(calls), "lookups_by_tool": {t: sum(1 for c in calls if c["tool"] == t) for t in cond["tools"]},
               "parse": {k: report[k] for k in ("sentences", "sentences_found", "relations")}, "parse_problems": report["problems"],
               "attempts": len(attempts), **meta}, open(base + ".meta.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if os.path.exists(base + ".failed.json"):
        os.remove(base + ".failed.json")
    say("%s p%dr%d %s: %d/%d sentences, %d relations, %d lookups, %.0f min, %s out tokens%s" % (
        cond["name"] + ("+" + tag if tag else ""), variant, rep, name, report["sentences_found"], report["sentences"],
        report["relations"], len(calls), meta["seconds"] / 60, meta["usage"]["output_tokens"], " (%s)" % problem if problem else ""))


def span(s):
    a, _, b = s.partition("-")
    return list(range(int(a), int(b or a) + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--conds", required=True)
    ap.add_argument("--group", default="test")
    ap.add_argument("--docs", default="")
    ap.add_argument("--variants", default="1-5")
    ap.add_argument("--reps", default="1-2")
    ap.add_argument("--skill", default="")
    ap.add_argument("--tag", default="")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--redo", action="store_true")
    ap.add_argument("--show", action="store_true", help="print the first prompt and stop")
    a = ap.parse_args()
    conds = [c for c in CONFIG["conditions"] if c["name"] in a.conds.split(",")]
    names = a.docs.split(",") if a.docs else CONFIG["groups"][a.group]
    skill = open(a.skill, encoding="utf-8").read() if a.skill else None
    jobs = [(c, v, r, n, a.tag, skill, a.redo) for r in span(a.reps) for v in span(a.variants) for c in conds for n in names]
    if a.show:
        doc = umrdoc.load_blind(os.path.join(HERE, "data", "input", names[0] + ".txt"))
        print(task(conds[0], span(a.variants)[0], doc, skill))
        return
    say("%d runs, %d at a time" % (len(jobs), a.jobs))
    with ThreadPoolExecutor(a.jobs) as pool:
        list(pool.map(one, jobs))
    say("done")


if __name__ == "__main__":
    main()

"""Method 3 with Claude Code: each document is annotated by Claude Code (`claude -p`, no interaction) in a
working directory of its own, then scored like the chat answers.

    python3 exp/harness/claude_code.py s1-abridged --docs zh-0028,zh-0032
    python3 exp/harness/claude_code.py all --langs zh                 # the five sub-experiments, every zh file
    python3 exp/harness/claude_code.py s2-gold --docs zh-0028 --prepare-only   # only build the directory

Options: --model (default claude-opus-5-5), --effort (default medium), --label (default claude-code),
--work (default /tmp/umr-harness), --jobs (documents at a time, default 1), --max-budget-usd (per
document), --login (use the claude login instead of the key, see below).

The working directory <work>/<sub>/<doc>/ holds only what the condition gives:

    TASK.md                 harness/<sub>/TASK.md filled with the document (scripts/make_subexps.py writes it)
    guidelines/             the abridged guidelines, or the full ones (s1-full), as in the API sub-experiments
    tools/<tool>.py         the sub-experiment's tool as a command (harness/cc_tools.py; same code and data
                            as the API tools)
    notes/                  for the agent's notes
    .claude/settings.json   permissions: read this directory, run the tools, write answer.txt and notes/;
                            nothing else (no other command, no web, no subagent; this repository, the web
                            repo and the home directory cannot be read, so neither can the test gold)

Claude Code runs there with `--bare` (no CLAUDE.md, hooks, plugins, memory or MCP servers of this machine)
on the key in $UMR_MODEL_KEY (given to it as ANTHROPIC_API_KEY, sent to $UMR_API_BASE or api.anthropic.com), the model and effort asked for, and
`--permission-mode dontAsk` (anything the settings do not allow is refused, never asked). With --login
it runs without --bare on the machine's claude login instead (a subscription), with a small environment
(no CLAUDE_* variables of a Claude Code it runs inside, no API key) and `--setting-sources project` (only
the working directory's settings).

Results: harness/<sub>/answers/<label>/<doc>.txt (answer.txt), <doc>.meta.json (cost, turns, time, usage
per model, every tool call), <doc>.prompt.md (the command, the settings and TASK.md as given),
<doc>.transcript.jsonl (the whole session, stream-json); then the scores
in runs/harness/<sub>/<label>/ (as `python3 exp/run.py harness-score <sub> --label <label>` does).
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(EXP, "lib"))
sys.path.insert(0, EXP)
import registry  # noqa: E402
import run as R  # noqa: E402

PROMPT = ("Do the task described in TASK.md in this directory: annotate the document it gives and write the "
          "answer to answer.txt. Work on your own until answer.txt holds the whole answer.")
GUIDE = {"abridged": "umr_guidelines_abridged.md", "full": "umr_guidelines.md"}
FILES = {"s1-abridged": ["abridged"], "s1-full": ["full"], "s2-search": ["abridged"],
         "s2-propbank": ["abridged"], "s2-gold": ["abridged"]}
STUB = """#!/usr/bin/env python3
import sys
sys.path.insert(0, %r)
from harness.cc_tools import main
main(%r, sys.argv[1:])
"""


def tools_of(sub):
    reg = registry.load(os.path.join(EXP, "api", sub, "registry.yaml"))
    return reg["skills"]["annotate"].get("tools") or []


def permissions(tools):
    repo = os.path.dirname(EXP)
    web = os.path.normpath(os.environ.get("SP_RESOURCES") or os.path.join(repo, "..", "ai-native-annotator.github.io"))
    allow = ["Read(./**)", "Glob", "Grep", "Edit(./answer.txt)", "Edit(./notes/**)", "Write(./answer.txt)",
             "Write(./notes/**)", "TodoWrite"] + ["Bash(python3 tools/%s.py *)" % t for t in tools]
    deny = ["Read(/%s/**)" % repo, "Read(/%s/**)" % web, "Read(~/**)", "Edit(/%s/**)" % repo,
            "WebFetch", "WebSearch", "Agent", "Task"]
    return allow, deny


def prepare(sub, name, work):
    doc = R.doc_of(name)
    ann = R.annotation(doc)
    w = os.path.join(work, sub, name)
    if os.path.exists(w):
        shutil.rmtree(w)
    for d in ("guidelines", "tools", "notes", ".claude"):
        os.makedirs(os.path.join(w, d))
    template = open(os.path.join(EXP, "harness", sub, "TASK.md"), encoding="utf-8").read()
    with open(os.path.join(w, "TASK.md"), "w", encoding="utf-8") as f:
        f.write(template.format(lang=ann["lang"], doc_id=ann["name"], n=ann["sentences"], sentences=ann["lines"]))
    for k in FILES[sub]:
        shutil.copy(os.path.join(EXP, "guidelines", GUIDE[k]), os.path.join(w, "guidelines", GUIDE[k]))
    tools = tools_of(sub)
    for t in tools:
        p = os.path.join(w, "tools", t + ".py")
        with open(p, "w", encoding="utf-8") as f:
            f.write(STUB % (EXP, t))
        os.chmod(p, 0o755)
    allow, deny = permissions(tools)
    with open(os.path.join(w, ".claude", "settings.json"), "w", encoding="utf-8") as f:
        json.dump({"permissions": {"allow": allow, "deny": deny}}, f, indent=1)
    return w, allow, deny


def write_prompt(out, name, w, cmd):
    """<doc>.prompt.md: what Claude Code was given: the command line (its one-line prompt), the permission
    settings and TASK.md as filled for the document."""
    settings = open(os.path.join(w, ".claude", "settings.json"), encoding="utf-8").read()
    task = open(os.path.join(w, "TASK.md"), encoding="utf-8").read()
    with open(os.path.join(out, name + ".prompt.md"), "w", encoding="utf-8") as f:
        f.write("<!-- command (in %s) -->\n%s\n\n<!-- .claude/settings.json -->\n%s\n\n<!-- TASK.md -->\n%s" % (
            w, " ".join(json.dumps(c, ensure_ascii=False) if (" " in c or not c) else c for c in cmd), settings, task))


def summarise(lines):
    """The result message and every tool call of a stream-json transcript."""
    result, calls = {}, []
    for line in lines:
        try:
            m = json.loads(line)
        except ValueError:
            continue
        if m.get("type") == "result":
            result = m
        elif m.get("type") == "assistant":
            for b in (m.get("message") or {}).get("content") or []:
                if b.get("type") == "tool_use":
                    calls.append({"name": b.get("name"), "input": json.dumps(b.get("input"), ensure_ascii=False)[:300]})
    return result, calls


def one(sub, name, a):
    w, allow, deny = prepare(sub, name, a.work)
    if a.prepare_only:
        print("prepared", w)
        return
    cmd = ["claude", "-p", PROMPT, "--model", a.model, "--effort", a.effort, "--output-format", "stream-json",
           "--verbose", "--permission-mode", "dontAsk", "--settings", os.path.join(w, ".claude", "settings.json"),
           "--strict-mcp-config", "--no-session-persistence", "--allowedTools", ",".join(allow),
           "--disallowedTools", ",".join(deny)]
    if a.login:
        # the machine's claude login (a subscription): a small environment of its own, so that a Claude Code
        # this runs inside (CLAUDE_* variables) or an API key does not take over; no user settings
        keep = ("HOME", "PATH", "LANG", "LC_ALL", "TMPDIR", "HTTPS_PROXY", "HTTP_PROXY", "NO_PROXY", "https_proxy",
                "http_proxy", "no_proxy", "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE",
                "ANTHROPIC_BASE_URL", "UMR22", "SP_RESOURCES", "GOLD_SOURCE")
        env = {k: os.environ[k] for k in keep if k in os.environ}
        env["PYTHONIOENCODING"] = "utf-8"
        cmd += ["--setting-sources", "project"]
    else:
        env = dict(os.environ)
        cmd.insert(1, "--bare")
        if not env.get("UMR_MODEL_KEY"):
            raise SystemExit("UMR_MODEL_KEY is not set (or run with --login)")
        env["ANTHROPIC_API_KEY"] = env["UMR_MODEL_KEY"]
        env["ANTHROPIC_BASE_URL"] = env.get("UMR_API_BASE", "https://api.anthropic.com")
        env.pop("ANTHROPIC_AUTH_TOKEN", None)
    if a.max_budget_usd:
        cmd += ["--max-budget-usd", str(a.max_budget_usd)]
    out = os.path.join(EXP, "harness", sub, "answers", a.label)
    os.makedirs(out, exist_ok=True)
    write_prompt(out, name, w, cmd)
    logs = out
    t0 = time.time()
    with open(os.path.join(logs, name + ".transcript.jsonl"), "w", encoding="utf-8") as log:
        p = subprocess.run(cmd, cwd=w, env=env, stdout=log, stderr=subprocess.STDOUT, text=True)
    lines = open(os.path.join(logs, name + ".transcript.jsonl"), encoding="utf-8").read().splitlines()
    result, calls = summarise(lines)
    answer = os.path.join(w, "answer.txt")
    if os.path.exists(answer):
        shutil.copy(answer, os.path.join(out, name + ".txt"))
    meta = {"doc": name, "harness": "claude-code", "model": a.model, "effort": a.effort, "exit": p.returncode,
            "seconds": round(time.time() - t0, 1), "answer": os.path.exists(answer),
            "subtype": result.get("subtype"), "is_error": result.get("is_error"),
            "num_turns": result.get("num_turns"), "cost_usd": result.get("total_cost_usd"),
            "usage": result.get("usage"), "models": result.get("modelUsage"),
            "permission_denials": result.get("permission_denials"), "tool_calls": calls}
    with open(os.path.join(out, name + ".meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print("%s %s: exit %d, answer %s, %s turns, %d tool calls, $%s, %.0fs" % (
        sub, name, p.returncode, "yes" if meta["answer"] else "NO", meta["num_turns"], len(calls),
        meta["cost_usd"], meta["seconds"]), flush=True)
    if not meta["answer"]:
        print("  no answer.txt; the end of the transcript:", "\n  ".join(lines[-3:])[:1500], flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("sub", choices=R.SUBS + ["all"])
    ap.add_argument("--docs", default="")
    ap.add_argument("--langs", default="zh")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--label", default="claude-code")
    ap.add_argument("--work", default="/tmp/umr-harness")
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--max-budget-usd", type=float, default=None)
    ap.add_argument("--login", action="store_true")
    ap.add_argument("--prepare-only", action="store_true")
    a = ap.parse_args()
    a.work = os.path.abspath(a.work)
    if a.work.startswith(os.path.dirname(EXP) + os.sep) or a.work.startswith(os.path.expanduser("~") + os.sep):
        raise SystemExit("--work must be outside this repository and the home directory (they cannot be read)")
    langs = R.LANGS if a.langs == "all" else a.langs.split(",")
    docs = a.docs.split(",") if a.docs else [d["doc"] for d in R.ALL_DOCS if d["lang"] in langs]
    R.DOCS = [d for d in R.ALL_DOCS if d["doc"] in docs]
    for sub in (R.SUBS if a.sub == "all" else [a.sub]):
        with ThreadPoolExecutor(a.jobs) as pool:
            list(pool.map(lambda n: one(sub, n, a), docs))
        if not a.prepare_only:
            R.answers_score(sub, a.label, "harness")


if __name__ == "__main__":
    main()

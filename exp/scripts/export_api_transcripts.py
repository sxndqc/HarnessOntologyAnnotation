"""Write <doc>.prompt.md and <doc>.transcript.json for API runs made before run.py wrote them, from the
answer cache (.cache/answers/), without asking the API again and without scoring again.

    python3 exp/scripts/export_api_transcripts.py claude-opus-5-5 --rev 6fa791b --runs ../obsolete/exp/runs
                                                   # prompts as at that commit; the run is archived in obsolete/exp/runs
    python3 exp/scripts/export_api_transcripts.py claude-opus-5-5-v2

For every runs/api/<sub>/<label>/<doc>.trace.json: the prompt is rendered from api/<sub>/ as at --rev
(default: as it is now), the model and effort are the trace's, and the conversation is replayed from the
cache (tool results computed again; the tools are deterministic). A missing cache entry is an error.
"""
import argparse
import json
import os
import subprocess
import sys

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(EXP, "lib"))
sys.path.insert(0, EXP)
import llm  # noqa: E402
import registry  # noqa: E402
import run as R  # noqa: E402


def at_rev(rev, rel):
    return subprocess.run(["git", "show", "%s:exp/%s" % (rev, rel)], cwd=EXP, check=True, capture_output=True,
                          text=True).stdout


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("label")
    ap.add_argument("--rev", default="")
    ap.add_argument("--runs", default="runs", help="where the runs are, relative to exp/ (runs, or ../obsolete/exp/runs)")
    a = ap.parse_args()
    import tools.search as search
    R.skip_test(search)
    for sub in R.SUBS:
        out_dir = os.path.join(EXP, a.runs, "api", sub, a.label)
        if not os.path.isdir(out_dir):
            continue
        reg = registry.load(os.path.join(EXP, "api", sub, "registry.yaml"))
        skill = reg["skills"]["annotate"]
        if a.rev:
            skill["template"] = at_rev(a.rev, "api/%s/annotate/skill.md" % sub)
            if skill.get("guideline"):
                skill["guideline_text"] = at_rev(a.rev, skill["guideline"])
        for f in sorted(os.listdir(out_dir)):
            if not f.endswith(".trace.json"):
                continue
            name = f[:-len(".trace.json")]
            trace = json.load(open(os.path.join(out_dir, f), encoding="utf-8"))
            ann = R.annotation(R.doc_of(name))
            system, user = registry.render(skill, {"lang": ann["lang"], "doc_id": ann["name"], "n": ann["sentences"],
                                                   "sentences": ann["lines"]})
            tools = skill.get("tools") or []
            r = llm.answer(trace["model"], system, user, tools, trace["effort"], os.path.join(R.CACHE, "answers"),
                           cache_only=True)
            raw = open(os.path.join(out_dir, name + ".raw.txt"), encoding="utf-8").read()
            if r["text"] != raw:
                raise SystemExit("%s %s: the cached answer is not the run's answer" % (sub, name))
            R.write_transcript(out_dir, name, trace["model"], trace["effort"], system, user, tools, r)
            print("%s %s: %d turns, %d tool calls" % (sub, name, r["turns"], len(r["tool_calls"])))


if __name__ == "__main__":
    main()

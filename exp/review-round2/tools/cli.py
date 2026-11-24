"""The tools as commands, for an agent working in a run directory.

    python3 tools/search_guidelines.py KEYWORD [KEYWORD ...] [--max N]
    python3 tools/propbank_lookup.py --language zh LEMMA [LEMMA ...]
    python3 tools/search_annotations.py --language zh KEYWORD [KEYWORD ...] [--max N]

pipeline/run_codex.py writes these three small scripts into tools/ of each run directory; each calls
main() here with its tool's name and the document being annotated. The answers are those of the API
experiments' tools (the same code and data).

search_annotations never returns the document being annotated: every sentence of the training file of
the same name (chinese_umr-0005 for zh-0005) and every training sentence whose text equals one of the
document's sentences is left out. With UMR_SKIP=all it leaves out every document of data/docs.json
(all 31), which leaves only chinese_umr-0019, -0020 and the AMR-converted -0025 to search.
"""
import argparse
import json
import os
import sys
import time

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("SP_RESOURCES", os.path.join(PKG, "resources"))
os.environ.setdefault("UMR22", os.path.join(PKG, "resources", "training"))
sys.path.insert(0, PKG)

from tools import propbank, search  # noqa: E402


def _input_texts(doc):
    with open(os.path.join(PKG, "data", "input", doc + ".txt"), encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def _set_skip(doc):
    docs = json.load(open(os.path.join(PKG, "data", "docs.json"), encoding="utf-8"))["docs"]
    mine = [d for d in docs if d["doc"] == doc]
    if os.environ.get("UMR_SKIP") == "all":
        mine = docs
    search.set_skip(docs=[d["gold"] for d in mine], texts=[t for d in mine for t in _input_texts(d["doc"])])


def main(name, doc, argv):
    ap = argparse.ArgumentParser(prog="python3 tools/%s.py" % name)
    if name in ("propbank_lookup", "search_annotations"):
        ap.add_argument("--language", required=True, choices=["zh", "en", "cs", "it", "la", "arp", "nv"])
    if name == "propbank_lookup":
        ap.add_argument("lemmas", nargs="+")
    else:
        ap.add_argument("keywords", nargs="+")
        ap.add_argument("--max", type=int, default=3, help="how many to return, 1-10 (default 3)")
    a = ap.parse_args(argv)
    try:
        if name == "propbank_lookup":
            out = propbank.propbank_lookup(a.lemmas, a.language)
        elif name == "search_annotations":
            _set_skip(doc)
            out = search.search_annotations(a.language, a.keywords, a.max)
        elif name == "search_guidelines":
            out = search.search_guidelines(a.keywords, a.max)
        else:
            raise SystemExit("no tool named %s" % name)
        err = False
    except Exception as e:      # the same message the API tool loop gave the model
        out, err = "%s failed: %s" % (name, str(e)[:300]), True
    text = out if isinstance(out, str) else json.dumps(out, ensure_ascii=False)
    try:        # a record of the call in the run directory (pipeline/run_codex.py counts them)
        with open(".tool_calls.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": round(time.time(), 1), "tool": name, "args": argv, "chars": len(text),
                                "error": err}, ensure_ascii=False) + "\n")
    except OSError:
        pass
    print(text)
    sys.exit(1 if err else 0)

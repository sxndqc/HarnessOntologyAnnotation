"""The tools of exp/tools/ as commands, for an agent working in a harness directory.

    python3 tools/search_guidelines.py KEYWORD [KEYWORD ...] [--max N]
    python3 tools/propbank_lookup.py --language zh LEMMA [LEMMA ...]
    python3 tools/search_annotations.py --language zh KEYWORD [KEYWORD ...] [--max N]

exp/harness/claude_code.py writes the three small scripts in tools/ of the working directory; each calls
main() here with its tool's name, so the answers are those the API sub-experiments' tools give (the same
code, the same data; search_annotations never returns a test sentence).
"""
import argparse
import os
import sys

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(EXP, "lib"))
sys.path.insert(0, EXP)


def main(name, argv):
    ap = argparse.ArgumentParser(prog="python3 tools/%s.py" % name)
    if name in ("propbank_lookup", "search_annotations"):
        ap.add_argument("--language", required=True, choices=["zh", "en"])
    if name == "propbank_lookup":
        ap.add_argument("lemmas", nargs="+")
    else:
        ap.add_argument("keywords", nargs="+")
        ap.add_argument("--max", type=int, default=3, help="how many to return, 1-10 (default 3)")
    a = ap.parse_args(argv)
    import tools as T
    if name == "search_annotations":
        import run
        run.skip_test(T.search)
    if name == "propbank_lookup":
        args = {"lemmas": a.lemmas, "language": a.language}
    elif name == "search_annotations":
        args = {"language": a.language, "keywords": a.keywords, "max_results": a.max}
    else:
        args = {"keywords": a.keywords, "max_results": a.max}
    text, err = T.call(name, args)
    print(text)
    sys.exit(1 if err else 0)

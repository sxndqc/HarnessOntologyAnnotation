"""Paths, the configuration and the documents, shared by the pipeline scripts."""
import json
import os
import sys

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PKG, "lib"))
sys.path.insert(0, PKG)

CONFIG = json.load(open(os.path.join(PKG, "config.json"), encoding="utf-8"))
DOCS = json.load(open(os.path.join(PKG, "data", "docs.json"), encoding="utf-8"))["docs"]
RUNS = os.path.join(PKG, "runs")
ANALYSIS = os.path.join(PKG, "analysis")
GOLD = os.path.join(PKG, "data", "gold")
GOLD_REV = os.path.join(PKG, "data", "gold_revised")


def label(m):
    """The run folder of an entry of config.json "models": gpt-6.1-sol-medium-r1 (model, effort, run)."""
    return "-".join(x for x in (m["model"], m["effort"], m.get("run", "")) if x)


def conditions(names=""):
    want = [x for x in names.split(",") if x]
    out = [c for c in CONFIG["conditions"] if not want or c["name"] in want or c["key"] in want]
    if want and len(out) != len(want):
        raise SystemExit("unknown condition in %r (have: %s)" % (names, ", ".join(c["name"] for c in CONFIG["conditions"])))
    return out


def models(names=""):
    want = [x for x in names.split(",") if x]
    out = [m for m in CONFIG["models"] if not want or m["model"] in want or m["key"] in want]
    if want and len(out) != len(want):
        raise SystemExit("unknown run in %r (have: %s)" % (names, ", ".join(m["key"] for m in CONFIG["models"])))
    return out


def docs(names=""):
    want = [x for x in names.split(",") if x and x != "all"]
    if want == ["test"]:                # the test set of the shared task
        return [d for d in DOCS if d.get("test")]
    out = [d for d in DOCS if not want or d["doc"] in want]
    if want and len(out) != len(want):
        raise SystemExit("unknown document in %r" % names)
    return out


def cond_docs(cond, ds):
    """The documents a condition runs on: all of ds, or only the test documents ("docs": "test")."""
    return [d for d in ds if d.get("test")] if cond.get("docs") == "test" else list(ds)


def lang_label(lang):
    """How a task description names the language: zh and en as before, others with their name."""
    return CONFIG.get("lang_labels", {}).get(lang, lang)


def systems():
    """[(key 's3/r1', condition, model entry, run dir)] in the order of config.json: condition / run."""
    return [("%s/%s" % (c["key"], m["key"]), c, m, os.path.join(RUNS, c["name"], label(m)))
            for c in CONFIG["conditions"] for m in CONFIG["models"]]


def gold_path(d):
    return os.path.join(GOLD, d["gold"] + ".umr")


def revised_path(d):
    """The corrected gold of a document, if there is one (data/gold_revised/<doc>.umr)."""
    p = os.path.join(GOLD_REV, d["doc"] + ".umr")
    return p if os.path.exists(p) else None


def official_path(d):
    """The released gold of a test file (data/gold_official/<doc>.umr), when it is another file than the
    gold the document is scored against (the 13 Chinese test files of the first round)."""
    p = os.path.join(PKG, "data", "gold_official", d["doc"] + ".umr")
    if not os.path.exists(p):
        return None
    same = open(p, encoding="utf-8-sig").read().split() == open(gold_path(d), encoding="utf-8-sig").read().split()
    return None if same else p


def load_input(d):
    """The document as a model gets it: the tokens of the gold file, nothing else."""
    import umrdoc
    return umrdoc.load_blind(os.path.join(PKG, "data", "input", d["doc"] + ".txt"))


def gold_text(d):
    """The gold file as the review tools read it: with the text repairs of data/gold_text_repairs.json (places
    where the file itself does not parse, such as a missing bracket). Returns (text, the repairs applied)."""
    lines = open(gold_path(d), encoding="utf-8").read().split("\n")
    p = os.path.join(PKG, "data", "gold_text_repairs.json")
    done = []
    for r in (json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}).get(d["doc"], []):
        if lines[r["line"] - 1] == r["from"]:
            lines[r["line"] - 1] = r["to"]
            done.append(r)
    return "\n".join(l for l in lines if l is not None), done

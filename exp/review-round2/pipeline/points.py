"""Agreement, accuracy and voting at the annotation comparison points.

    python3 pipeline/points.py            -> analysis/points.md (and the same text on the screen)

Reads review/points/<doc>.json, one file per document: the diff report of the document coded into points
(AGENTS.md, step 6). A point is one place where the annotations differ, with the annotations sorted into
choices:

    {"sent": 1, "item": "1a", "topic": "...", "cat": "sense",
     "choices": [{"label": "...", "systems": ["gold", "s1f/r1"], "status": "ok"},
                 {"label": "...", "systems": ["s1f/r2", ...], "status": "bad"}],
     "gold_fix": true, "best": "label of the best choice, or null"}

cat: sense | role | concept | structure | attr | doc-temporal | doc-modal | doc-coref
status of a choice: ok (correct by the guidelines) | minor (acceptable, slightly worse) | bad (wrong) |
open (cannot be decided). gold_fix: the gold should change here. Every system of config.json and "gold" must
be in exactly one choice of every point.

Three parts: (1) agreement between systems = share of the points where two systems made the same choice,
counted on the points where the systems do not all agree; (2) accuracy = ok / (ok + minor + bad) per system
and per category; (3) voting: for subsets of the systems, a strict majority vote at every point; a flag is a
point where the vote differs from the gold; a good flag = the vote is ok and the gold is wrong there; harm =
the vote is wrong where the gold was ok.
"""
import collections
import itertools
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

CATS = ["sense", "role", "concept", "structure", "attr", "doc-temporal", "doc-modal", "doc-coref"]
ALLK = [k for k, *_ in C.systems()]
K = list(ALLK)
out_lines = []


def say(s=""):
    print(s)
    out_lines.append(s)


def load():
    pts, bad = [], 0
    folder = os.path.join(C.PKG, "review", "points")
    for d in C.DOCS:
        p = os.path.join(folder, d["doc"] + ".json")
        if not os.path.exists(p):
            continue
        for x in json.load(open(p, encoding="utf-8")):
            x["doc"], x["g"], x["st"] = d["doc"], {}, {}
            for i, c in enumerate(x["choices"]):
                for s in c["systems"]:
                    if s in x["g"]:
                        print("ERROR %s %s: %s is in two choices" % (d["doc"], x.get("item"), s))
                        bad += 1
                    x["g"][s], x["st"][s] = i, c.get("status", "open")
            x["cst"] = [c.get("status", "open") for c in x["choices"]]
            have = [k for k, _, _, rd in C.systems() if os.path.exists(os.path.join(rd, d["doc"] + ".umr"))]
            x["lang"], x["test"] = d.get("lang"), bool(d.get("test"))
            missing = [s for s in have + ["gold"] if s not in x["g"]]
            if missing or x.get("cat") not in CATS:
                print("ERROR %s sentence %s item %s: missing %s, cat %s" % (d["doc"], x.get("sent"), x.get("item"), missing, x.get("cat")))
                bad += 1
                continue
            pts.append(x)
    if bad:
        print("%d points with errors were left out: fix the points files" % bad)
    return pts


def agree(a, b, P):
    return 100 * sum(p["g"][a] == p["g"][b] for p in P) / len(P) if P else 0


def av(l):
    l = [x for x in l if x is not None]
    return round(sum(l) / len(l), 1) if l else None


def rate(k, P):
    c = collections.Counter(p["st"][k] for p in P)
    n = c["ok"] + c["minor"] + c["bad"]
    return c, (100 * c["ok"] / n if n else 0), (100 * c["bad"] / n if n else 0)


def report(title, pts, K, sizes=(2, 3, 4)):
    for p in pts:
        p["nsys"] = len({p["g"][k] for k in K})
    docs = sorted({p["doc"] for p in pts})
    say("\n\n# %s" % title)
    say("\nSystems: %s. %d points in %d documents (%s); %d where the gold should change." % (
        ", ".join(K), len(pts), len(docs), ", ".join(docs), sum(bool(p.get("gold_fix")) for p in pts)))

    # ---------------------------------------------------------------- 1. agreement
    div = [p for p in pts if p["nsys"] > 1]
    say("\n## 1. Agreement between systems (%d points where the systems differ)\n" % len(div))
    say("| | " + " | ".join(K + ["gold"]) + " |")
    say("|---|" + "---|" * (len(K) + 1))
    for a in K:
        say("| **%s** | %s |" % (a, " | ".join("–" if a == b else "%.0f" % agree(a, b, div) for b in K + ["gold"])))
    L = sorted(((agree(a, b, div), a, b) for a, b in itertools.combinations(K, 2)), reverse=True)
    say("\nPairs from closest to farthest: " + "; ".join("%s ~ %s %.0f" % (a, b, v) for v, a, b in L))
    cond = lambda s: s.split("/")[0]
    model = lambda s: s.split("/")[1]
    say("\n| pairs | mean agreement |\n|---|---|")
    say("| same condition, the two runs | %s |" % av([v for v, a, b in L if cond(a) == cond(b)]))
    say("| different conditions, same run | %s |" % av([v for v, a, b in L if cond(a) != cond(b) and model(a) == model(b)]))
    say("| different conditions, different runs | %s |" % av([v for v, a, b in L if cond(a) != cond(b) and model(a) != model(b)]))
    for c in dict.fromkeys(cond(k) for k in K):
        say("| %s: r1 ~ r2 | %s |" % (c, av([v for v, a, b in L if cond(a) == cond(b) == c])))
    for m in sorted({model(k) for k in K}):
        say("| within run %s | %s |" % (m, av([v for v, a, b in L if model(a) == model(b) == m])))
    say("\nMean agreement with the other systems: " + ", ".join("%s %s" % (k, av([v for v, a, b in L if k in (a, b)])) for k in K))
    say("\n| category | points | mean number of different choices | mean pairwise agreement |\n|---|---|---|---|")
    for cat in CATS:
        P = [p for p in div if p["cat"] == cat]
        if P:
            say("| %s | %d | %s | %s |" % (cat, len(P), av([p["nsys"] for p in P]),
                                         av([agree(a, b, P) for a, b in itertools.combinations(K, 2)])))
    say("\nHow often a system is alone with its choice: " + ", ".join(
        "%s %d" % (k, sum(1 for p in div if sum(p["g"][j] == p["g"][k] for j in K) == 1)) for k in K))

    # ---------------------------------------------------------------- 2. accuracy
    say("\n## 2. Accuracy at the points (ok / (ok + minor + bad); open points left out)\n")
    say("| annotation | ok % | bad % | ok | minor | bad | open |\n|---|---|---|---|---|---|---|")
    for k in ["gold"] + K:
        c, o, b = rate(k, pts)
        say("| %s | %.1f | %.1f | %d | %d | %d | %d |" % (k, o, b, c["ok"], c["minor"], c["bad"], c["open"]))
    say("\nok % by category:\n")
    cats = [c for c in CATS if any(p["cat"] == c for p in pts)]
    say("| annotation | " + " | ".join("%s (%d)" % (c, sum(p["cat"] == c for p in pts)) for c in cats) + " |")
    say("|---|" + "---|" * len(cats))
    for k in ["gold"] + K:
        say("| %s | %s |" % (k, " | ".join("%.1f" % rate(k, [p for p in pts if p["cat"] == c])[1] for c in cats)))
    GF = [p for p in pts if p.get("gold_fix")]
    GOK = [p for p in pts if p["st"]["gold"] == "ok" and not p.get("gold_fix")]
    if GF and GOK:
        say("\nWhere the gold is wrong (%d points) and where it is right (%d points):\n" % (len(GF), len(GOK)))
        say("| system | fixes the gold % | repeats the gold's error % | wrong or minor where the gold is right % |\n|---|---|---|---|")
        for k in K:
            say("| %s | %.1f | %.1f | %.1f |" % (
                k, 100 * sum(p["st"][k] == "ok" and p["g"][k] != p["g"]["gold"] for p in GF) / len(GF),
                100 * sum(p["g"][k] == p["g"]["gold"] for p in GF) / len(GF),
                100 * sum(p["st"][k] in ("bad", "minor") for p in GOK) / len(GOK)))

    # ---------------------------------------------------------------- 3. voting
    def vote(S, p, thr):
        c = collections.Counter(p["g"][k] for k in S)
        top, n = c.most_common(1)[0]
        if n < thr or sum(1 for v in c.values() if v == n) > 1:
            return None
        return top

    def ev(S, thr=None):
        thr = thr or len(S) // 2 + 1
        r = collections.Counter()
        for p in pts:
            v = vote(S, p, thr)
            if v is None:
                r["nodec"] += 1
                continue
            st = p["cst"][v]
            r["dec_" + st] += 1
            if v != p["g"]["gold"]:
                r["flag"] += 1
                gs = p["st"]["gold"]
                if st == "ok" and (p.get("gold_fix") or gs in ("bad", "minor")):
                    r["good"] += 1
                elif st in ("bad", "minor") and gs == "ok" or st == "bad":
                    r["harm"] += 1
                else:
                    r["neutral"] += 1
        dec = r["dec_ok"] + r["dec_minor"] + r["dec_bad"]
        return {"S": list(S), "thr": thr, "acc": 100 * r["dec_ok"] / dec if dec else 0, "nodec": r["nodec"],
                "flags": r["flag"], "good": r["good"], "harm": r["harm"], "neutral": r["neutral"],
                "prec": 100 * r["good"] / r["flag"] if r["flag"] else 0, "rec": 100 * r["good"] / len(GF) if GF else 0}

    def row(name, e):
        return "| %s | %s | %d | %.1f | %d | %d | %d | %d | %d | %.0f | %.0f |" % (
            name, " + ".join(e["S"]), e["thr"], e["acc"], e["nodec"], e["flags"], e["good"], e["harm"], e["neutral"],
            e["prec"], e["rec"])

    head = ("| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | "
            "gold errors caught % |\n|---|---|---|---|---|---|---|---|---|---|---|")
    say("\n## 3. Voting (strict majority; a flag = the vote differs from the gold)\n")
    say(head)
    say(row("all", ev(K)))
    say(row("all, unanimous", ev(K, len(K))))
    for m in sorted({model(k) for k in K}):
        say(row("run " + m, ev([k for k in K if model(k) == m])))
    for c in dict.fromkeys(cond(k) for k in K):
        say(row("without " + c, ev([k for k in K if cond(k) != c])))
        say(row("only " + c, ev([k for k in K if cond(k) == c])))
    for k in K:
        say(row("single", ev([k])))
    for size in sizes:
        if len(K) >= size:
            E = [ev(S) for S in itertools.combinations(K, size)]
            say("\nBest sets of %d by gold errors caught (then less harm):\n" % size)
            say(head)
            for e in sorted(E, key=lambda e: (-e["good"], e["harm"]))[:6]:
                say(row("size %d" % size, e))
    if GF:
        cover = sum(any(p["st"][k] == "ok" and p["g"][k] != p["g"]["gold"] for k in K) for p in GF)
        say("\nGold errors for which at least one system has a correct different choice: %d of %d." % (cover, len(GF)))


LANGS = ["zh", "en", "cs", "it", "la", "arp", "nv"]


def by_language(pts, K):
    say("\n\n# Test set by language: ok % at the points (ok / (ok + minor + bad))\n")
    langs = [l for l in LANGS if any(p["lang"] == l for p in pts)]
    say("| annotation | " + " | ".join("%s (%d)" % (l, sum(p["lang"] == l for p in pts)) for l in langs) + " | all |")
    say("|---|" + "---|" * (len(langs) + 1))
    for k in ["gold"] + K:
        say("| %s | %s | %.1f |" % (k, " | ".join("%.1f" % rate(k, [p for p in pts if p["lang"] == l])[1] for l in langs), rate(k, pts)[1]))
    say("\nbad % by language:\n")
    say("| annotation | " + " | ".join(langs) + " | all |")
    say("|---|" + "---|" * (len(langs) + 1))
    for k in ["gold"] + K:
        say("| %s | %s | %.1f |" % (k, " | ".join("%.1f" % rate(k, [p for p in pts if p["lang"] == l])[2] for l in langs), rate(k, pts)[2]))
    say("\nPoints where the gold should change, by language: " + ", ".join(
        "%s %d of %d" % (l, sum(bool(p.get("gold_fix")) for p in pts if p["lang"] == l), sum(p["lang"] == l for p in pts)) for l in langs))


def main():
    pts = load()
    if not pts:
        raise SystemExit("no points yet: review/points/<doc>.json")
    six = [k for k in ALLK if not k.startswith("s0/")]
    test = [p for p in pts if p["test"]]
    say("# Comparison points: agreement, accuracy, voting")
    say("\nFour groups: (A) the 30 test files with all 8 systems; (B) the test files by language; "
        "(C) all 48 documents with the 6 systems that ran on all of them; (D) the 31 Chinese documents with those 6 "
        "(the group of the first round).")
    report("A. Test set, 8 systems", test, ALLK)
    by_language(test, ALLK)
    report("C. All documents, 6 systems (no baseline)", pts, six)
    report("D. Chinese documents, 6 systems (no baseline)", [p for p in pts if p["lang"] == "zh"], six)
    os.makedirs(C.ANALYSIS, exist_ok=True)
    with open(os.path.join(C.ANALYSIS, "points.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines) + "\n")
    print("\nwrote analysis/points.md")


if __name__ == "__main__":
    main()

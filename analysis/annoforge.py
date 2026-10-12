"""Data, tables, figures and number macros of the AnnoForge paper.

    python3 analysis/annoforge.py extract --src ../SkillParseUMR    # snapshot -> data/annoforge/
    python3 analysis/annoforge.py make                               # data/annoforge/ -> tables/, figures/

extract reads experiment/annoforge of a SkillParseUMR checkout (runs/, harness/, results/) and writes small
JSON files; make needs only those files (Overleaf does not run Python: commit what make writes).
A missing run is a red TBD cell, never a guess.
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data", "annoforge")
TABLES = os.path.join(ROOT, "tables")
FIGURES = os.path.join(ROOT, "figures")
BENCHES = ["umr-zh", "umr-en", "timeml"]
BNAME = {"umr-zh": "UMR Chinese", "umr-en": "UMR English", "timeml": "TimeML"}
MAIN = {"umr-zh": "F", "umr-en": "F", "timeml": "tlink_f1"}
CONFIGS = ["HH", "HG", "GH", "GG"]
TRAJ = {"umr-zh": "HH", "umr-en": "HH", "timeml": "HHp"}     # the main trajectory of each benchmark
ALT = {"timeml": ("HH", "TimeBank-trained")}                   # a second trajectory, reported alongside
ROUNDS = 10
GAP = r"\gapcell{}"
SEED = 20261012


# ================================================================ extract

def extract(src):
    af = os.path.join(src, "experiment", "annoforge")
    sys.path.insert(0, os.path.join(af, "af"))
    os.makedirs(DATA, exist_ok=True)
    runs = {}
    for b in BENCHES:
        runs[b] = {}
        for path in sorted(glob.glob(os.path.join(af, "runs", b, "**", "scores.json"), recursive=True)):
            cond = os.path.relpath(os.path.dirname(path), os.path.join(af, "runs", b))
            with open(path, encoding="utf-8") as f:
                s = json.load(f)
            keep = {"overall": s["overall"], "judge": {k: v for k, v in s.get("judge", {}).items()},
                    "docs": {d: {k: v for k, v in row.items() if k != "judge"} for d, row in s.get("docs", {}).items()},
                    "seconds": s.get("seconds")}
            if b == "timeml" and "/train/" not in "/" + cond + "/" and os.path.isdir(os.path.join(os.path.dirname(path), "pred", "pred")):
                keep["tlink_counts"] = tlink_counts(src, os.path.dirname(path))
            if b != "timeml" and "/train/" not in "/" + cond + "/":
                keep["sentences"] = umr_sentences(os.path.dirname(path))
            keep["calls"] = call_stats(os.path.join(os.path.dirname(path), "calls.jsonl"))
            runs[b][cond] = keep
    dump(runs, "runs.json")

    rsi, versions = {}, {}
    for b in BENCHES:
        rsi[b], versions[b] = {}, {}
        for traj in sorted(os.listdir(os.path.join(af, "harness", b))):
            hdir = os.path.join(af, "harness", b, traj)
            if not os.path.isdir(hdir) or not os.path.exists(os.path.join(hdir, "H0")):
                continue
            versions[b][traj] = {}
            for v in sorted((p for p in glob.glob(os.path.join(hdir, "H*")) if re.fullmatch(r"H\d+", os.path.basename(p))),
                            key=lambda p: int(p.rsplit("H", 1)[1])):
                versions[b][traj][os.path.basename(v)] = version_info(v)
            rsi[b][traj] = {}
            for g in sorted(glob.glob(os.path.join(af, "runs", b, traj, "rsi", "g*")), key=lambda p: int(p.rsplit("g", 1)[1])):
                n = int(g.rsplit("g", 1)[1])
                rec = {}
                for name in ("reflect.json", "applied.json"):
                    p = os.path.join(g, name)
                    if os.path.exists(p):
                        with open(p, encoding="utf-8") as f:
                            rec[name[:-5]] = json.load(f)
                p = os.path.join(g, "edits.diff")
                if os.path.exists(p):
                    with open(p, encoding="utf-8") as f:
                        rec["diff_lines"] = sum(1 for l in f if l.startswith(("+", "-")) and not l.startswith(("+++", "---")))
                rsi[b][traj][n] = rec
    dump(rsi, "rsi.json")
    dump(versions, "versions.json")
    for name in ("sota.json", "cost.json"):
        p = os.path.join(af, "results", name)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                dump(json.load(f), name)
    with open(os.path.join(af, "data", "splits.json"), encoding="utf-8") as f:
        dump(json.load(f), "splits.json")
    print("extracted to", DATA)


def call_stats(path):
    """Model calls of a run: how many, how many used a tool (a claude-sdk call with more than two turns,
    i.e. a tool call before the answer), output tokens."""
    if not os.path.exists(path):
        return None
    n = tool = out = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("cached"):
                continue
            n += 1
            if d.get("backend") == "claude-sdk":
                tool += 1 if (d.get("turns") or 0) > 2 else 0
                out += (d.get("usage") or {}).get("output_tokens") or 0
            else:
                out += d.get("output_tokens") or 0
    return {"calls": n, "tool_calls": tool, "output_tokens": out}


def version_info(v):
    import yaml
    with open(os.path.join(v, "harness.yaml"), encoding="utf-8") as f:
        spec = yaml.safe_load(f)
    sizes = {}
    for p in glob.glob(os.path.join(v, "skills", "*.md")):
        with open(p, encoding="utf-8") as f:
            sizes[os.path.basename(p)[:-3]] = len(f.read())
    tools = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(v, "tools", "*.py")))
    return {"steps": spec["steps"], "sizes": sizes, "tools": tools}


def tlink_counts(src, run_dir):
    sys.path.insert(0, os.path.join(src, "judges"))
    import te3
    try:
        return te3.tlink_counts(os.path.join(run_dir, "pred", "gold"), os.path.join(run_dir, "pred", "pred"))
    except Exception as e:
        print("tlink counts failed", run_dir, e)
        return None


def umr_sentences(run_dir):
    """Per sentence: umrjudge's AnCast smatch of the final graph (for a sentence-level bootstrap)."""
    import score
    out = {}
    for gp in sorted(glob.glob(os.path.join(run_dir, "pred", "*.gold.umr"))):
        pp = gp.replace(".gold.umr", ".umr")
        try:
            _, sents = score.judge_umr(pp, gp)
        except Exception as e:
            print("judge failed", pp, e)
            continue
        for s in sents:
            out["%s:%s" % (s["doc"], s["sent"])] = s.get("smatch")
    return out


def dump(obj, name):
    with open(os.path.join(DATA, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)


# ================================================================ make

def load(name):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def num(x, d=1):
    return GAP if x is None else ("%.*f" % (d, x))


def sgn(x, d=1):
    if x is None:
        return GAP
    return ("+%.*f" % (d, x)) if x >= 0 else ("$-$%.*f" % (d, -x))


def get(runs, b, cond, key):
    r = runs.get(b, {}).get(cond)
    if not r:
        return None
    v = r["overall"].get(key)
    return float(v) if isinstance(v, (int, float)) else None


def boot_docs(runs, b, a, c, n=20000):
    """Paired document bootstrap of (c - a) on the main metric: (mean, lo, hi, p). TimeML: corpus-level TLINK
    F1 recomputed from per-document counts."""
    import numpy as np
    ra, rc = runs[b].get(a), runs[b].get(c)
    if not ra or not rc:
        return None
    rng = np.random.default_rng(SEED)
    if b == "timeml":
        ca, cc = ra.get("tlink_counts"), rc.get("tlink_counts")
        if not ca or not cc:
            return None
        docs = sorted(set(ca) & set(cc))

        def f(counts, idx):
            s = np.sum([counts[docs[i]] for i in idx], axis=0)
            p = s[0] / s[2] if s[2] else 0
            r = s[1] / s[3] if s[3] else 0
            return 100 * 2 * p * r / (p + r) if p + r else 0
        base = f(cc, range(len(docs))) - f(ca, range(len(docs)))
        diffs = []
        for _ in range(n):
            idx = rng.integers(0, len(docs), len(docs))
            diffs.append(f(cc, idx) - f(ca, idx))
    else:
        docs = sorted(set(ra["docs"]) & set(rc["docs"]))
        x = np.array([rc["docs"][d]["F"] - ra["docs"][d]["F"] for d in docs])
        base = x.mean()
        diffs = [x[rng.integers(0, len(x), len(x))].mean() for _ in range(n)]
    diffs = np.array(diffs)
    p = 2 * min((diffs <= 0).mean(), (diffs >= 0).mean())
    return base, float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5)), float(min(1.0, p))


def boot_sents(runs, b, a, c, n=20000):
    """Paired sentence bootstrap of AnCast smatch (UMR): (mean diff, lo, hi, better, worse, count)."""
    import numpy as np
    ra, rc = runs[b].get(a), runs[b].get(c)
    if not ra or not rc or "sentences" not in ra or "sentences" not in rc:
        return None
    keys = [k for k in ra["sentences"] if k in rc["sentences"] and ra["sentences"][k] is not None
            and rc["sentences"][k] is not None]
    x = np.array([rc["sentences"][k] - ra["sentences"][k] for k in keys]) * 100
    rng = np.random.default_rng(SEED)
    means = [x[rng.integers(0, len(x), len(x))].mean() for _ in range(n)]
    return (x.mean(), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5)),
            int((x > 1).sum()), int((x < -1).sum()), len(x))


def make():
    runs, rsi, versions, sota, cost, splits = (load(x) for x in
                                               ("runs.json", "rsi.json", "versions.json", "sota.json", "cost.json", "splits.json"))
    macros = {}
    os.makedirs(TABLES, exist_ok=True)
    os.makedirs(FIGURES, exist_ok=True)
    table_main(runs, sota, macros)
    table_seed(runs, macros)
    table_rounds(runs, rsi, versions, macros)
    table_judge(runs, macros)
    table_ops(rsi, versions, macros)
    table_cost(cost, runs, macros)
    table_ablation(runs, macros)
    extra_macros(runs, macros)
    figure_curves(runs, sota)
    figure_judge(runs)
    figure_ops(rsi, versions)
    stats(runs, macros)
    data_macros(splits, macros)
    with open(os.path.join(TABLES, "numbers.tex"), "w", encoding="utf-8") as f:
        f.write("% generated by analysis/annoforge.py make; do not edit\n")
        for k, v in sorted(macros.items()):
            f.write("\\newcommand{\\%s}{%s\\xspace}\n" % (k, v))
    print("made", len(macros), "macros")


def data_macros(splits, m):
    for b, key in (("umr-zh", "Zh"), ("umr-en", "En"), ("timeml", "Tml")):
        sp = splits.get(b, {})
        m["nTest" + key] = str(sp.get("test_sentences", "?"))
        m["nTestDocs" + key] = str(len(sp.get("test", [])))


def macro_name(*parts):
    return "".join(re.sub(r"[^A-Za-z]", "", p.title()) for p in parts)


# ---------------------------------------------------------------- tables

def table_main(runs, sota, m):
    """One row per system, the main metrics of every benchmark."""
    rows = []
    cols = [("umr-zh", "F"), ("umr-zh", "Comprehensive"), ("umr-zh", "jumach"),
            ("umr-en", "F"), ("umr-en", "Comprehensive"), ("umr-en", "jumach"),
            ("timeml", "tlink_f1"), ("timeml", "event_f1"), ("timeml", "timex_value")]

    def row(label, conds):
        cells = []
        for b, k in cols:
            c = conds.get(b)
            if isinstance(c, dict):
                v = c.get(k)
                cells.append(num(float(v)) if isinstance(v, (int, float)) else "--")
            else:
                cells.append(num(get(runs, b, c, k)) if c else "--")
        return label + " & " + " & ".join(cells) + r" \\"

    sz = sota.get("umr-zh", {})
    se = sota.get("umr-en", {})
    st = sota.get("timeml", {})
    rows.append(r"\multicolumn{10}{@{}l}{\emph{Fine-tuned and feature-based systems (re-scored on our test documents)}} \\")
    rows.append(row("UMR shared task: Orange", {"umr-zh": sz.get("orange", {}).get("overall"), "umr-en": se.get("orange", {}).get("overall")}))
    rows.append(row("UMR shared task: Sema", {"umr-zh": sz.get("sema", {}).get("overall"), "umr-en": se.get("sema", {}).get("overall")}))
    for name, label in (("TIPSem/key", "TempEval-3: TIPSem"), ("cleartk/2-timebank-verbclause", "TempEval-3: ClearTK-2"),
                        ("chambers/NavyTime1", "TempEval-3: NavyTime")):
        if name in st:
            rows.append(row(label, {"timeml": st[name]["overall"]}))
    rows.append(r"\midrule \multicolumn{10}{@{}l}{\emph{Guideline in the prompt, one call per sentence}} \\")
    for mdl, label in (("haiku", "Haiku 5.5"), ("sonnet", "Sonnet 5.5"), ("gpt", "GPT-6.1-sol")):
        rows.append(row(label, {b: "baseline/" + mdl for b in BENCHES}))
    rows.append(r"\midrule \multicolumn{10}{@{}l}{\emph{Seed harness $H_0$ (generator / critic)}} \\")
    for c in CONFIGS + ["SS"]:
        rows.append(row(cfg_label(c), {b: "R0/" + c for b in BENCHES}))
    rows.append(r"\midrule \multicolumn{10}{@{}l}{\emph{Learned harness $H_{10}$ (\sys, built with Haiku / Haiku)}} \\")
    rows.append(row(cfg_label("HH"), {b: T(b, "test/H10") for b in BENCHES}))
    for c in ("HG", "GH", "GG", "SS"):
        rows.append(row(cfg_label(c) + " (transfer)", {b: "R10/" + c for b in BENCHES}))
    for b, (traj, label) in ALT.items():
        rows.append(row("Haiku / Haiku, %s" % label, {b: T(b, "test/H10", traj)}))
    text = r"""\begin{table*}[t]
\centering\small
\setlength{\tabcolsep}{3.6pt}
\begin{tabular}{@{}lccccccccc@{}}
\toprule
& \multicolumn{3}{c}{UMR Chinese} & \multicolumn{3}{c}{UMR English} & \multicolumn{3}{c}{TimeML} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(l){8-10}
System & F & Comp. & ju\textipa{:}m\ae{}\textipa{tS} & F & Comp. & ju\textipa{:}m\ae{}\textipa{tS} & TLINK & Event & Value \\
\midrule
%s
\bottomrule
\end{tabular}
\caption{All systems on the test documents (UMR: %s Chinese and %s English sentences of the shared task's test set; TimeML: %s TempEval-3 platinum sentences). F: AnCast++ sentence-graph F; Comp.: AnCast++ comprehensive score with document-level relations; juːmæʧ: the shared task's official score against its test gold. TLINK: TempEval-3 temporal awareness F1; Event: event extent F1; Value: TIMEX3 value F1. Transfer: $H_{10}$, built with Haiku annotators, run with other generator/critic pairs.}
\label{tab:main}
\end{table*}
""" % ("\n".join(rows), r"\nTestZh", r"\nTestEn", r"\nTestTml")
    text = text.replace("ju\\textipa{:}m\\ae{}\\textipa{tS}", "\\jumach{}").replace("juːmæʧ", "\\jumach{}")
    write("main.tex", text)
    for b in BENCHES:
        key = MAIN[b]
        tag = {"umr-zh": "Zh", "umr-en": "En", "timeml": "Tml"}[b]
        for cond, name in (("R0/HH", "Seed"), (T(b, "test/H10"), "Learned"), ("baseline/haiku", "BaseHaiku"),
                           ("baseline/sonnet", "BaseSonnet"), ("baseline/gpt", "BaseGpt"), ("R0/GG", "SeedGG"),
                           ("R10/GG", "LearnedGG"), ("R0/HG", "SeedHG"), ("R0/GH", "SeedGH"), ("R10/HG", "LearnedHG"),
                           ("R10/GH", "LearnedGH")):
            m["main%s%s" % (name, tag)] = num(get(runs, b, cond, key))
        if b != "timeml":
            for cond, name in (("R0/HH", "Seed"), (T(b, "test/H10"), "Learned")):
                m["comp%s%s" % (name, tag)] = num(get(runs, b, cond, "Comprehensive"))
                m["jumach%s%s" % (name, tag)] = num(get(runs, b, cond, "jumach"))
            s = sota.get(b, {}).get("orange", {}).get("overall", {})
            m["sotaF" + tag] = num(s.get("F"))
            m["sotaComp" + tag] = num(s.get("Comprehensive"))
            m["sotaJumach" + tag] = num(s.get("jumach"))
        else:
            t = sota.get("timeml", {})
            m["sotaTlinkTipsem"] = num(t.get("TIPSem/key", {}).get("overall", {}).get("tlink_f1"))
            m["sotaTlinkCleartk"] = num(t.get("cleartk/2-timebank-verbclause", {}).get("overall", {}).get("tlink_f1"))
            for cond, name in (("R0/HH", "Seed"), (T(b, "test/H10"), "Learned")):
                for k, n2 in (("event_f1", "Event"), ("timex_value", "Value"), ("timex_strict_f1", "Timex"),
                              ("event_class", "Class"), ("tlink_p", "TlinkP"), ("tlink_r", "TlinkR")):
                    m["%s%s%s" % (n2.lower(), name, tag)] = num(get(runs, b, cond, k))


def T(b, rest, traj=None):
    """The path of a run of benchmark b's main trajectory (or of `traj`)."""
    return "%s/%s" % (traj or TRAJ[b], rest)


def cfg_label(c):
    names = {"H": "Haiku", "G": "GPT", "S": "Sonnet"}
    return "%s / %s" % (names[c[0]], names[c[1]])


def table_seed(runs, m):
    """The 2x2 of generator and critic models at H0 and H10, main metric."""
    rows = []
    for c in CONFIGS:
        cells = []
        for b in BENCHES:
            a = get(runs, b, "R0/" + c, MAIN[b])
            z = get(runs, b, T(b, "test/H10") if c == "HH" else "R10/" + c, MAIN[b])
            cells += [num(a), num(z), sgn(z - a) if a is not None and z is not None else GAP]
        rows.append(cfg_label(c) + " & " + " & ".join(cells) + r" \\")
    write("seed2x2.tex", r"""\begin{table}[t]
\centering\small
\setlength{\tabcolsep}{2.6pt}
\begin{tabular}{@{}lccccccccc@{}}
\toprule
& \multicolumn{3}{c}{UMR zh (F)} & \multicolumn{3}{c}{UMR en (F)} & \multicolumn{3}{c}{TimeML (TLINK)} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(l){8-10}
G / C & $H_0$ & $H_{10}$ & $\Delta$ & $H_0$ & $H_{10}$ & $\Delta$ & $H_0$ & $H_{10}$ & $\Delta$ \\
\midrule
%s
\bottomrule
\end{tabular}
\caption{Generator (G) and critic (C) models. $H_{10}$ was built with Haiku in both roles; for the other pairs it is used as it is.}
\label{tab:seed2x2}
\end{table}
""" % "\n".join(rows))


def table_rounds(runs, rsi, versions, m):
    """Per round: training group score before/after, test score, operations applied, harness size."""
    for b in BENCHES:
        rows = []
        tag = {"umr-zh": "Zh", "umr-en": "En", "timeml": "Tml"}[b]
        rs = rsi.get(b, {}).get(TRAJ[b], {})
        vs = versions.get(b, {}).get(TRAJ[b], {})
        for n in range(0, ROUNDS + 1):
            test = get(runs, b, T(b, "test/H%d" % n), MAIN[b])
            if n == 0:
                size = sum(vs.get("H0", {}).get("sizes", {}).values()) if vs.get("H0") else None
                rows.append("$H_0$ & -- & -- & %s & -- & %s & %s \\\\" % (num(test), num(size / 1000 if size else None), "3 / 0 / 0"))
                continue
            before = get(runs, b, T(b, "train/g%d/H%d" % (n, n - 1)), MAIN[b])
            after = get(runs, b, T(b, "train/g%d/H%d" % (n, n)), MAIN[b])
            r = rs.get(str(n), {})
            ap = r.get("applied") or []
            ok = sum(1 for x in ap if x["applied"])
            v = vs.get("H%d" % n, {})
            size = sum(v.get("sizes", {}).values()) if v else None
            steps = len([s for s in v.get("steps", []) if s.get("kind") != "rule"]) if v else None
            rules = len([s for s in v.get("steps", []) if s.get("kind") == "rule"]) if v else None
            tools = len(v.get("tools", [])) if v else None
            rows.append("$H_{%d}$ & %s & %s & %s & %s & %s & %s \\\\" % (
                n, num(before), num(after), num(test), "%d/%d" % (ok, len(ap)) if ap else GAP,
                num(size / 1000 if size else None), "%s / %s / %s" % (steps if steps is not None else "?",
                                                                     rules if rules is not None else "?",
                                                                     tools if tools is not None else "?")))
        write("rounds_%s.tex" % b, r"""\begin{tabular}{@{}lcccccc@{}}
\toprule
& \multicolumn{2}{c}{Group $n$} & Test & Ops & Skills & Model steps / \\
& $H_{n-1}$ & $H_n$ & $H_n$ & applied & (K chars) & rules / tools \\
\midrule
%s
\bottomrule
\end{tabular}
""" % "\n".join(rows))


CHECK_LABEL = {}


def table_judge(runs, m):
    """Per-check judge scores of H0 and H10 (HH) on the test set."""
    for b in BENCHES:
        a = runs.get(b, {}).get("R0/HH", {}).get("judge", {})
        z = runs.get(b, {}).get(T(b, "test/H10"), {}).get("judge", {})
        rows = []
        for check in a or z:
            ra, rz = a.get(check, {}), z.get(check, {})
            sa, sz = ra.get("score"), rz.get("score")
            if (ra.get("units") or 0) + (rz.get("units") or 0) < 6:
                continue
            group = ra.get("module") or ra.get("group") or rz.get("module") or rz.get("group") or ""
            rows.append("%s & \\texttt{%s} & %s & %s & %s & %s \\\\" % (
                group.replace("_", "\\_"), check.replace("_", "\\_"), ra.get("units", "--"),
                num(100 * sa if sa is not None else None), num(100 * sz if sz is not None else None),
                sgn(100 * (sz - sa)) if sa is not None and sz is not None else GAP))
        write("judge_%s.tex" % b, r"""\begin{tabular}{@{}llcccc@{}}
\toprule
Group & Check & Units & $H_0$ & $H_{10}$ & $\Delta$ \\
\midrule
%s
\bottomrule
\end{tabular}
""" % "\n".join(rows))


def op_kind(op):
    o = op.get("op", "")
    if o == "edit_skill":
        return "edit:" + (op.get("action") or "?")
    return o


def table_ops(rsi, versions, m):
    kinds = ["edit:add", "edit:modify", "edit:delete", "rewrite_skill", "add_step", "delete_step", "add_tool",
             "replace_tool", "delete_tool", "set_step_tools"]
    rows = []
    for b in BENCHES:
        rs = rsi.get(b, {}).get(TRAJ[b], {})
        prop, app = Counter(), Counter()
        whys = Counter()
        for r in rs.values():
            for x in r.get("applied", []):
                k = op_kind(x["op"])
                prop[k] += 1
                if x["applied"]:
                    app[k] += 1
                else:
                    whys[re.sub(r"[\d%r\'].*", "", x["why"])[:40]] += 1
        rows.append(BNAME[b] + " & " + " & ".join("%d/%d" % (app[k], prop[k]) if prop[k] else "0" for k in kinds) + r" \\")
        tag = {"umr-zh": "Zh", "umr-en": "En", "timeml": "Tml"}[b]
        m["opsProposed" + tag] = str(sum(prop.values()))
        m["opsApplied" + tag] = str(sum(app.values()))
        m["toolsApplied" + tag] = str(app["add_tool"] + app["replace_tool"])
        m["toolsProposed" + tag] = str(prop["add_tool"] + prop["replace_tool"])
        m["stepsApplied" + tag] = str(app["add_step"])
        m["stepsProposed" + tag] = str(prop["add_step"])
        m["rewritesApplied" + tag] = str(app["rewrite_skill"])
        vs = versions.get(b, {}).get(TRAJ[b], {})
        if "H0" in vs:
            m["sizeSeed" + tag] = "%.1f" % (sum(vs["H0"]["sizes"].values()) / 1000)
        last = "H%d" % ROUNDS
        if last in vs:
            m["sizeLast" + tag] = "%.1f" % (sum(vs[last]["sizes"].values()) / 1000)
            m["toolsLast" + tag] = ", ".join("\\texttt{%s}" % t.replace("_", "\\_") for t in vs[last]["tools"]) or "none"
            m["stepsLast" + tag] = ", ".join("\\skill{%s}" % s["name"].replace("_", "\\_") for s in vs[last]["steps"])
    write("ops.tex", r"""\begin{table*}[t]
\centering\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}lcccccccccc@{}}
\toprule
& \multicolumn{3}{c}{\texttt{edit\_skill}} & \texttt{rewrite} & \texttt{add} & \texttt{delete} & \texttt{add} & \texttt{replace} & \texttt{delete} & \texttt{set step} \\
Benchmark & add & modify & delete & \texttt{\_skill} & \texttt{\_step} & \texttt{\_step} & \texttt{\_tool} & \texttt{\_tool} & \texttt{\_tool} & \texttt{\_tools} \\
\midrule
%s
\bottomrule
\end{tabular}
\caption{Operations applied / proposed over the ten rounds, by type.}
\label{tab:ops}
\end{table*}
""" % "\n".join(rows))


def extra_macros(runs, m):
    for b, (traj, label) in ALT.items():
        for k, n in (("tlink_f1", "Tlink"), ("tlink_p", "TlinkP"), ("tlink_r", "TlinkR"), ("event_f1", "Event"),
                     ("timex_value", "Value")):
            m["alt%sLearnedTml" % n] = num(get(runs, b, T(b, "test/H10", traj), k))
    for b, t in (("umr-zh", "Zh"), ("umr-en", "En")):
        for v, w in (("H0", "Seed"), ("H10", "Learned")):
            a = get(runs, b, "R0/HH" if v == "H0" else T(b, "test/H10"), "F")
            z = get(runs, b, "rep2/" + v, "F")
            m["rep%s%s" % (w, t)] = num(z)
            m["repDiff%s%s" % (w, t)] = num(abs(z - a)) if a is not None and z is not None else GAP
        for v in ("R0/SS", "R10/SS"):
            for k, n in (("F", "F"), ("Comprehensive", "Comp"), ("jumach", "Jumach")):
                m["sonnet%s%s%s" % ("Seed" if v.startswith("R0") else "Learned", n, t)] = num(get(runs, b, v, k))
        c = runs.get(b, {}).get(T(b, "test/H10"), {}).get("calls") or {}
        m["toolUse" + t] = "%.0f" % (100 * c["tool_calls"] / c["calls"]) if c.get("calls") else GAP
    for v in ("R0/SS", "R10/SS"):
        m["sonnet%sTlinkTml" % ("Seed" if v.startswith("R0") else "Learned")] = num(get(runs, "timeml", v, "tlink_f1"))


def table_ablation(runs, m):
    rows = []
    for cond, label in (("R0/HH", "$H_0$ (seed)"), (None, "$H_{10}$"), ("ablation/notools", "$H_{10}$ without tools"),
                        ("ablation/norules", "$H_{10}$ without rule steps"),
                        ("ablation/seedskills", "$H_{10}$ with the seed's skills")):
        cells = []
        for b in ("umr-zh", "umr-en"):
            c = cond or T(b, "test/H10")
            for k in ("F", "Comprehensive", "jumach"):
                cells.append(num(get(runs, b, c, k)))
        rows.append(label + " & " + " & ".join(cells) + r" \\")
        tag = {"ablation/notools": "NoTools", "ablation/norules": "NoRules", "ablation/seedskills": "SeedSkills"}.get(cond)
        if tag:
            for b, t in (("umr-zh", "Zh"), ("umr-en", "En")):
                v, z = get(runs, b, cond, "F"), get(runs, b, T(b, "test/H10"), "F")
                m["abl%s%s" % (tag, t)] = num(v)
                m["abl%s%sDelta" % (tag, t)] = sgn(v - z) if v is not None and z is not None else GAP
    write("ablation.tex", r"""\begin{table}[t]
\centering\small
\setlength{\tabcolsep}{3pt}
\resizebox{\columnwidth}{!}{%%
\begin{tabular}{@{}lcccccc@{}}
\toprule
& \multicolumn{3}{c}{UMR Chinese} & \multicolumn{3}{c}{UMR English} \\
\cmidrule(lr){2-4}\cmidrule(l){5-7}
Harness (Haiku / Haiku) & F & Comp. & \jumach & F & Comp. & \jumach \\
\midrule
%s
\bottomrule
\end{tabular}}
\caption{What the parts of $H_{10}$ contribute: the learned harness without its tools, without its rule steps, and with the seed's instructions in place of the learned ones (tools and rules kept).}
\label{tab:ablation}
\end{table}
""" % "\n".join(rows))


def table_cost(cost, runs, m):
    if not cost:
        return
    tot = cost.get("TOTAL", {})
    m["costOpenRouter"] = "%.0f" % tot.get("usd_openrouter", 0)
    m["callsTotal"] = "{:,}".format(tot.get("calls", 0)).replace(",", "{,}")


# ---------------------------------------------------------------- figures

def figure_curves(runs, sota):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 3.2))
    for ax, b in zip(axes, BENCHES):
        key = MAIN[b]
        xs, ys = [], []
        for n in range(ROUNDS + 1):
            v = get(runs, b, T(b, "test/H%d" % n), key)
            if v is not None:
                xs.append(n)
                ys.append(v)
        ax.plot(xs, ys, "-o", color="#1f5fa8", lw=2, ms=4, label="test, $H_n$", zorder=3)
        if b in ALT:
            traj, label = ALT[b]
            pts = [(n, get(runs, b, T(b, "test/H%d" % n, traj), key)) for n in range(ROUNDS + 1)]
            pts = [p for p in pts if p[1] is not None]
            if pts:
                ax.plot([p[0] for p in pts], [p[1] for p in pts], "--s", color="#7f7f7f", lw=1.2, ms=3,
                        label="test, %s" % label, zorder=2)
        for n in range(1, ROUNDS + 1):
            a = get(runs, b, T(b, "train/g%d/H%d" % (n, n - 1)), key)
            z = get(runs, b, T(b, "train/g%d/H%d" % (n, n)), key)
            if a is not None and z is not None:
                ax.plot([n - 1, n], [a, z], "-", color="#e08a1e", lw=1.2, alpha=0.9,
                        label="group $n$: $H_{n-1}\\to H_n$" if n == 1 else None)
                ax.plot([n - 1], [a], "o", color="#e08a1e", ms=3)
                ax.plot([n], [z], "^", color="#e08a1e", ms=4)
        for cond, style, lab in (("baseline/haiku", ":", "guideline prompt, Haiku"), ("baseline/sonnet", "--", "guideline prompt, Sonnet")):
            v = get(runs, b, cond, key)
            if v is not None:
                ax.axhline(v, ls=style, color="grey", lw=1, label=lab)
        if b == "timeml":
            t = sota.get("timeml", {}).get("TIPSem/key", {}).get("overall", {}).get("tlink_f1")
            if t:
                ax.axhline(t, ls="-.", color="#a01f1f", lw=1, label="TIPSem (2013)")
        else:
            t = sota.get(b, {}).get("orange", {}).get("overall", {}).get("F")
            if t:
                ax.axhline(t, ls="-.", color="#a01f1f", lw=1, label="shared-task best")
        ax.set_title(BNAME[b] + (" (AnCast++ F)" if b != "timeml" else " (TLINK F1)"), fontsize=10)
        ax.set_xlabel("round $n$")
        ax.set_xticks(range(ROUNDS + 1))
        ax.grid(alpha=0.3)
    h, l = axes[0].get_legend_handles_labels()
    for ax in axes[1:]:
        for hh, ll in zip(*ax.get_legend_handles_labels()):
            if ll not in l:
                h.append(hh)
                l.append(ll)
    fig.legend(h, l, loc="lower center", ncol=6, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.04))
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    fig.savefig(os.path.join(FIGURES, "curves.pdf"), bbox_inches="tight")
    plt.close(fig)


def figure_judge(runs):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 4.2))
    for ax, b in zip(axes, BENCHES):
        a = runs.get(b, {}).get("R0/HH", {}).get("judge", {})
        z = runs.get(b, {}).get(T(b, "test/H10"), {}).get("judge", {})
        items = []
        for check in a:
            if check in z and a[check].get("score") is not None and z[check].get("score") is not None \
                    and (a[check].get("units") or 0) >= 6:
                items.append((check, 100 * a[check]["score"], 100 * z[check]["score"]))
        items.sort(key=lambda x: x[2] - x[1])
        ys = range(len(items))
        ax.barh(ys, [i[2] - i[1] for i in items], color=["#1f5fa8" if i[2] >= i[1] else "#e08a1e" for i in items])
        ax.set_yticks(list(ys))
        ax.set_yticklabels([i[0] for i in items], fontsize=6.5)
        ax.axvline(0, color="black", lw=0.6)
        ax.set_title(BNAME[b] + ": $H_{10}-H_0$ per check", fontsize=9.5)
        ax.grid(axis="x", alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES, "judge.pdf"), bbox_inches="tight")
    plt.close(fig)


def figure_ops(rsi, versions):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    kinds = [("edit:add", "edit add", "#9ecae1"), ("edit:modify", "edit modify", "#4292c6"),
             ("edit:delete", "edit delete", "#08519c"), ("rewrite_skill", "rewrite skill", "#74c476"),
             ("add_step", "add/delete step", "#e08a1e"), ("add_tool", "add/replace tool", "#a01f1f")]
    fig, axes = plt.subplots(1, 3, figsize=(12.5, 2.8))
    for ax, b in zip(axes, BENCHES):
        rs = rsi.get(b, {}).get(TRAJ[b], {})
        bottom = [0] * ROUNDS
        for k, lab, col in kinds:
            vals = []
            for n in range(1, ROUNDS + 1):
                ap = rs.get(str(n), {}).get("applied", [])
                vals.append(sum(1 for x in ap if x["applied"] and (op_kind(x["op"]) == k or
                                (k == "add_step" and x["op"]["op"] == "delete_step") or
                                (k == "add_tool" and x["op"]["op"] in ("replace_tool", "delete_tool")))))
            ax.bar(range(1, ROUNDS + 1), vals, bottom=bottom, color=col, label=lab)
            bottom = [x + y for x, y in zip(bottom, vals)]
        ax2 = ax.twinx()
        vs = versions.get(b, {}).get(TRAJ[b], {})
        xs = [n for n in range(ROUNDS + 1) if "H%d" % n in vs]
        ax2.plot(xs, [sum(vs["H%d" % n]["sizes"].values()) / 1000 for n in xs], "k-o", ms=3, lw=1.2, label="skills (K chars)")
        ax2.set_ylim(bottom=0)
        ax.set_title(BNAME[b], fontsize=10)
        ax.set_xlabel("round")
        ax.set_xticks(range(1, ROUNDS + 1))
        if b == "umr-zh":
            ax.set_ylabel("operations applied")
        if b == "timeml":
            ax2.set_ylabel("skill characters (K)")
    h, l = axes[0].get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    fig.legend(h + h2, l + l2, loc="lower center", ncol=7, fontsize=8, frameon=False, bbox_to_anchor=(0.5, -0.06))
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(os.path.join(FIGURES, "ops.pdf"), bbox_inches="tight")
    plt.close(fig)


def stats(runs, m):
    for b in BENCHES:
        tag = {"umr-zh": "Zh", "umr-en": "En", "timeml": "Tml"}[b]
        for a, c, name in (("R0/HH", T(b, "test/H10"), "Learned"), ("baseline/haiku", T(b, "test/H10"), "VsBase"),
                           ("R0/GG", "R10/GG", "LearnedGG")):
            r = boot_docs(runs, b, a, c)
            for suffix in ("", "Lo", "Hi", "P"):
                m.setdefault("gain%s%s%s" % (name, tag, suffix), GAP)
            if r:
                m["gain%s%s" % (name, tag)] = sgn(r[0])
                m["gain%s%sLo" % (name, tag)] = sgn(r[1])
                m["gain%s%sHi" % (name, tag)] = sgn(r[2])
                m["gain%s%sP" % (name, tag)] = "%.3f" % r[3] if r[3] >= 0.001 else "<0.001"
            if b != "timeml":
                for suffix in ("", "Lo", "Hi", "Better", "Worse", "N"):
                    m.setdefault("sent%s%s%s" % (name, tag, suffix), GAP)
                s = boot_sents(runs, b, a, c)
                if s:
                    m["sent%s%s" % (name, tag)] = sgn(s[0])
                    m["sent%s%sLo" % (name, tag)] = sgn(s[1])
                    m["sent%s%sHi" % (name, tag)] = sgn(s[2])
                    m["sent%s%sBetter" % (name, tag)] = str(s[3])
                    m["sent%s%sWorse" % (name, tag)] = str(s[4])
                    m["sent%s%sN" % (name, tag)] = str(s[5])
        # generalization: does a round's training gain predict its test gain?
        tr, te = [], []
        for n in range(1, ROUNDS + 1):
            a = get(runs, b, T(b, "train/g%d/H%d" % (n, n - 1)), MAIN[b])
            z = get(runs, b, T(b, "train/g%d/H%d" % (n, n)), MAIN[b])
            t0 = get(runs, b, T(b, "test/H%d" % (n - 1)), MAIN[b])
            t1 = get(runs, b, T(b, "test/H%d" % n), MAIN[b])
            if None not in (a, z, t0, t1):
                tr.append(z - a)
                te.append(t1 - t0)
        if len(tr) >= 3:
            from scipy import stats as st
            rho, p = st.spearmanr(tr, te)
            m["genRho" + tag] = "%.2f" % rho
            m["genRhoP" + tag] = "%.2f" % p
            m["trainGain" + tag] = sgn(sum(tr) / len(tr))
            m["testStepGain" + tag] = sgn(sum(te) / len(te))
            m["roundsTestUp" + tag] = str(sum(1 for x in te if x > 0))
            m["roundsTrainUp" + tag] = str(sum(1 for x in tr if x > 0))
        best = [(get(runs, b, T(b, "test/H%d" % n), MAIN[b]), n) for n in range(ROUNDS + 1)]
        best = [x for x in best if x[0] is not None]
        if best:
            v, n = max(best)
            m["bestTest" + tag] = num(v)
            m["bestRound" + tag] = str(n)


def write(name, text):
    with open(os.path.join(TABLES, name), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["extract", "make"])
    ap.add_argument("--src", default=os.path.join(os.path.dirname(ROOT), "SkillParseUMR"))
    a = ap.parse_args()
    extract(a.src) if a.what == "extract" else make()

"""Tables, figures and number macros of the paper, from data/ (see data/PROVENANCE.md).

    python analysis/make_tables.py

Writes paper/tables/*.tex, paper/figures/*.pdf and paper/tables/numbers.tex (\\newcommand macros the text uses,
so the numbers in the prose follow the data). A cell without data is written as \\gapcell and listed in
notes/GAPS.md; when the experiment is done, put its numbers into data/ and add them here.
"""
import csv
import json
import math
import os
from collections import Counter, defaultdict

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")
TABLES = os.path.join(ROOT, "paper", "tables")
FIGURES = os.path.join(ROOT, "paper", "figures")
GAP = r"\gapcell{}"
RNG = np.random.default_rng(20261010)


def load(*parts):
    with open(os.path.join(DATA, *parts), encoding="utf-8") as f:
        return json.load(f)


def f1(x):
    return GAP if x is None else "%.1f" % x


def sgn2(x):
    return ("%+.2f" % x) if x >= 0 else ("$-$%.2f" % -x)


def sgn(x):
    if x is None:
        return GAP
    return ("+%.1f" % x) if x >= 0 else ("$-$%.1f" % -x)


def pval(p):
    return "<0.001" if p < 0.001 else "%.3f" % p


def write(name, text):
    with open(os.path.join(TABLES, name), "w", encoding="utf-8") as f:
        f.write(text)


def boot_ci(values, n=20000):
    values = np.asarray(values, dtype=float)
    means = [RNG.choice(values, len(values)).mean() for _ in range(n)]
    return np.percentile(means, [2.5, 97.5])


# ---------------------------------------------------------------------------------------------- UMR, critique chain

def critique():
    scores = load("umr", "critique_scores.json")["train"]
    steps = load("umr", "critique_steps.json")
    judge = load("umr", "critique_scores.json")["train_judge"]
    tree = load("umr", "tree_scores.json")
    docs = sorted(scores)
    zero = tree["test"]["generate-guidelines"]["docs"]          # one call per sentence, 0001-0007

    sentences = defaultdict(dict)
    with open(os.path.join(DATA, "umr", "critique_sentences.csv"), newline="") as f:
        for r in csv.DictReader(f):
            smatch = float(r["smatch"]) if r["smatch"] not in ("", "None") else None
            sentences[(r["doc"], r["parse"])][int(r["sent"])] = (r["status"], smatch)

    rows = []
    for k, doc in enumerate(docs, 1):
        s = scores[doc]
        seed = s.get("R0") or (s["iter1"] if k == 1 else None)
        first = s["iter1"]
        rows.append({
            "k": k, "doc": doc, "n_sent": len(sentences[(doc, "iter1")]),
            "version": "R0" if k == 1 else "R%d3" % (k - 1),
            "zero": zero[doc]["F"] if doc in zero else None,
            "seed": seed["F"] if seed else None, "seed_c": seed["Comprehensive"] if seed else None,
            "first": first["F"], "first_c": first["Comprehensive"],
            "after": s["after"]["F"] if "after" in s else None,
            "after_c": s["after"]["Comprehensive"] if "after" in s else None,
        })
    paired = [r for r in rows if r["k"] > 1 and r["seed"] is not None]
    dF = np.array([r["first"] - r["seed"] for r in paired])
    dC = np.array([r["first_c"] - r["seed_c"] for r in paired])
    lo, hi = boot_ci(dF)
    loc, hic = boot_ci(dC)
    ks = np.array([r["k"] for r in paired])
    rho, rho_p = stats.spearmanr(ks, dF)

    # sentence-level smatch, documents as clusters
    diffs = {}
    for r in paired:
        a, b = sentences[(r["doc"], "R0")], sentences[(r["doc"], "iter1")]
        diffs[r["doc"]] = np.array([b[i][1] - a[i][1] for i in a
                                    if i in b and a[i][1] is not None and b[i][1] is not None])
    allsent = np.concatenate(list(diffs.values()))
    names = list(diffs)
    boots = []
    for _ in range(10000):
        pick = RNG.choice(len(names), len(names))
        boots.append(np.concatenate([RNG.choice(diffs[names[i]], len(diffs[names[i]])) for i in pick]).mean() * 100)
    slo, shi = np.percentile(boots, [2.5, 97.5])

    zero_rows = [r for r in paired if r["zero"] is not None]
    num = {
        "nDocs": len(rows), "nSentences": sum(r["n_sent"] for r in rows), "nPaired": len(paired),
        "gainF": dF.mean(), "gainFLo": lo, "gainFHi": hi, "gainFMedian": np.median(dF),
        "gainFPos": int((dF > 0).sum()), "gainFSign": stats.binomtest(int((dF > 0).sum()), len(dF), 0.5).pvalue,
        "gainFWilcoxon": stats.wilcoxon(dF).pvalue, "gainFt": stats.ttest_1samp(dF, 0).pvalue,
        "gainC": dC.mean(), "gainCLo": loc, "gainCHi": hic, "gainCPos": int((dC > 0).sum()),
        "gainCWilcoxon": stats.wilcoxon(dC).pvalue,
        "gainFirstHalf": dF[:5].mean(), "gainSecondHalf": dF[5:].mean(),
        "gainRho": rho, "gainRhoP": rho_p,
        "seedMean": np.mean([r["seed"] for r in paired]), "firstMean": np.mean([r["first"] for r in paired]),
        "seedMeanZ": np.mean([r["seed"] for r in zero_rows]), "firstMeanZ": np.mean([r["first"] for r in zero_rows]),
        "zeroMeanZ": np.mean([r["zero"] for r in zero_rows]), "nZero": len(zero_rows),
        "afterMean": np.mean([r["after"] for r in rows if r["after"] is not None]),
        "nAfter": sum(1 for r in rows if r["after"] is not None),
        "sentGain": allsent.mean() * 100, "sentGainLo": slo, "sentGainHi": shi,
        "sentBetter": (allsent > 0.01).mean() * 100, "sentWorse": (allsent < -0.01).mean() * 100,
        "nSentPaired": len(allsent),
        "gainMax": dF.max(), "gainMin": dF.min(),
        "trainFitGain": np.mean([r["after"] - r["first"] for r in rows if r["after"] is not None]),
        "afterMax": max(r["after"] for r in rows if r["after"] is not None),
    }

    # --- Table 1: prequential results
    lines = [r"\begin{table*}[t]", r"\centering\small", r"\setlength{\tabcolsep}{3.6pt}",
             r"\begin{tabular}{@{}lrlcccccccc@{}}", r"\toprule",
             r"Doc & Sent. & Annotated by & Zero-shot & Seed $H_0$ & Learned & $\Delta$ F & Seed & Learned & $\Delta$ C & Trained \\",
             r" & & & prompt F & F & F & & C & C & & on it, F \\", r"\midrule"]
    for r in rows:
        d = None if r["seed"] is None else r["first"] - r["seed"]
        dc = None if r["seed_c"] is None else r["first_c"] - r["seed_c"]
        if r["k"] == 1:
            seed_f, learned_f, seed_c, learned_c, dcs, dfs = f1(r["seed"]), "--", f1(r["seed_c"]), "--", "--", "--"
        else:
            seed_f, learned_f = f1(r["seed"]), f1(r["first"])
            seed_c, learned_c = f1(r["seed_c"]), f1(r["first_c"])
            dfs, dcs = sgn(d), sgn(dc)
        lines.append("%s & %d & $H_{%s}$ & %s & %s & %s & %s & %s & %s & %s & %s \\\\" % (
            r["doc"][-4:], r["n_sent"], "0" if r["k"] == 1 else "%d" % (r["k"] - 1),
            f1(r["zero"]) if r["zero"] is not None else GAP, seed_f, learned_f, dfs, seed_c, learned_c, dcs,
            f1(r["after"]) if r["after"] is not None else "--"))
    lines += [r"\midrule",
              "Mean, %d paired documents & & & -- & %s & %s & %s & %s & %s & %s & \\\\" % (
                  len(paired), f1(num["seedMean"]), f1(num["firstMean"]), sgn(num["gainF"]),
                  f1(np.mean([r["seed_c"] for r in paired])), f1(np.mean([r["first_c"] for r in paired])),
                  sgn(num["gainC"])),
              "Mean, 0002--0007 & & & %s & %s & %s & %s & & & & \\\\" % (
                  f1(num["zeroMeanZ"]), f1(num["seedMeanZ"]), f1(num["firstMeanZ"]),
                  sgn(num["firstMeanZ"] - num["seedMeanZ"])),
              r"\bottomrule", r"\end{tabular}",
              r"\caption{Sequential (test-then-train) evaluation on Chinese UMR. Document $n$ is annotated by the harness "
              r"built from documents $1..n{-}1$ (``Learned''), then used to improve it. ``Seed'' is $H_0$ on the same "
              r"document, the paired control. ``Zero-shot prompt'' is one call per sentence with no harness "
              r"(sentence graph only, so only F is comparable). F = AnCast++ sentence F; C = comprehensive score "
              r"(sentence graphs plus document-level relations). The last column is the harness trained on the "
              r"document itself (training fit, not generalization). Document 0001 has no earlier harness; "
              r"0011 has no seed run yet; zero-shot is missing for 0008--0011.}",
              r"\label{tab:prequential}", r"\end{table*}"]
    write("prequential.tex", "\n".join(lines) + "\n")

    # --- the effect of the critique step: generate vs generate+critique
    by = {(s["doc"], s["parse"]): s for s in steps}
    def gain_crit(parse):
        out = []
        for doc in docs:
            s = by.get((doc, parse))
            if s and len(s["steps"]) >= 2:
                out.append(s["steps"][1]["F"] - s["steps"][0]["F"])
        return np.array(out)
    gcs = {p: gain_crit(p) for p in ("R0", "iter1", "after")}
    gcs["R0"] = np.array([by[(d, "iter1")]["steps"][1]["F"] - by[(d, "iter1")]["steps"][0]["F"] if d.endswith("0001")
                          else by[(d, "R0")]["steps"][1]["F"] - by[(d, "R0")]["steps"][0]["F"]
                          for d in docs if (d, "R0") in by or d.endswith("0001")])
    first_gain = np.array([by[(d, "iter1")]["steps"][1]["F"] - by[(d, "iter1")]["steps"][0]["F"]
                           for d in docs[1:] if (d, "iter1") in by])
    num.update({"critSeed": gcs["R0"].mean(), "critSeedPos": int((gcs["R0"] > 0).sum()), "critSeedN": len(gcs["R0"]),
                "critFirst": first_gain.mean(), "critFirstPos": int((first_gain > 0).sum()),
                "critFirstN": len(first_gain), "critFirstMin": first_gain.min(), "critFirstMax": first_gain.max(),
                "critAfter": gcs["after"].mean(), "critAfterPos": int((gcs["after"] > 0).sum()),
                "critAfterN": len(gcs["after"])})
    # generate alone, learned vs seed
    gen_gain = []
    for d in docs[1:]:
        if (d, "R0") in by and (d, "iter1") in by:
            gen_gain.append(by[(d, "iter1")]["steps"][0]["F"] - by[(d, "R0")]["steps"][0]["F"])
    num["genGain"] = float(np.mean(gen_gain))
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{4pt}",
             r"\begin{tabular}{@{}lccc@{}}", r"\toprule",
             r"Annotated by & Mean & Docs $>0$ & Range \\", r"\midrule",
             "Seed $H_0$ & %s & %d/%d & %s to %s \\\\" % (sgn(num["critSeed"]), num["critSeedPos"], num["critSeedN"],
                                                     sgn(gcs["R0"].min()), sgn(gcs["R0"].max())),
             "Learned, unseen doc. & %s & %d/%d & %s to %s \\\\" % (sgn(num["critFirst"]), num["critFirstPos"],
                                                                  num["critFirstN"], sgn(num["critFirstMin"]),
                                                                  sgn(num["critFirstMax"])),
             "Trained on the doc. & %s & %d/%d & %s to %s \\\\" % (sgn(num["critAfter"]), num["critAfterPos"],
                                                                 num["critAfterN"], sgn(gcs["after"].min()),
                                                                 sgn(gcs["after"].max())),
             r"\bottomrule", r"\end{tabular}",
             r"\caption{What the \skill{critique} step adds to the \skill{generate} draft (AnCast++ sentence F, "
             r"sentence graphs only, before the document layer).}", r"\label{tab:critique}", r"\end{table}"]
    write("critique_step.tex", "\n".join(lines) + "\n")

    # --- per-category gain, learned vs seed (figure data + appendix table)
    cats = [c for c in judge[docs[1]]["R0"] if c not in ("a_granularity", "c_modstr", "f_wiki", "j_coref_subset")]
    cat_rows = []
    for c in cats:
        seed_v, first_v = [], []
        for d in docs[1:]:
            if "R0" in judge[d] and "iter1" in judge[d]:
                a, b = judge[d]["R0"].get(c), judge[d]["iter1"].get(c)
                if a is not None and b is not None:
                    seed_v.append(a)
                    first_v.append(b)
        if seed_v:
            g = np.array(first_v) - np.array(seed_v)
            cat_rows.append((c, len(g), np.mean(seed_v), np.mean(first_v), g.mean(), int((g > 0).sum())))
    cat_rows.sort(key=lambda r: -r[4])
    with open(os.path.join(DATA, "umr", "category_gain.json"), "w") as f:
        json.dump(cat_rows, f, indent=1)
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{4pt}",
             r"\begin{tabular}{@{}lrrrr@{}}", r"\toprule",
             r"Check & Seed & Learned & $\Delta$ & Docs $\uparrow$ \\", r"\midrule"]
    for c, n, s, fi, g, pos in cat_rows:
        lines.append("\\texttt{%s} & %.2f & %.2f & %s & %d/%d \\\\" % (c.replace("_", r"\_"), s, fi, sgn2(g), pos, n))
    lines += [r"\bottomrule", r"\end{tabular}",
              r"\caption{Judge score per check on unseen documents, seed vs.\ learned harness (mean over the paired "
              r"documents; ``Docs $\uparrow$'' counts documents where the learned harness is higher).}",
              r"\label{tab:category}", r"\end{table}"]
    write("category.tex", "\n".join(lines) + "\n")
    by_cat = {c: g for c, n, s, fi, g, pos in cat_rows}
    for key, c in [("catRefer", "c_refer"), ("catModal", "i_modal"), ("catPeriph", "e_peripheral_labels"),
                   ("catAbstract", "d_core_args_abstract"), ("catEntity", "a_entity_concept"),
                   ("catSense", "b_event_sense"), ("catAspect", "c_aspect"), ("catCoreEvent", "d_core_args_event"),
                   ("catPolarity", "c_polarity"), ("catCoref", "j_coref_chain"), ("catTemporal", "h_temporal"),
                   ("catPeriphEvent", "d_peripheral_event"), ("catReentrancy", "g_reentrancy"),
                   ("catName", "f_name_tokens")]:
        num[key] = by_cat[c] * 100

    # --- the edits
    rounds = load("umr", "critique_rounds.json")
    totals = Counter()
    rejected = Counter()
    n_rounds = len(rounds)
    for r in rounds.values():
        for key, v in r["edits"].items():
            totals[key] += v
        for why in r["rejected"]:
            rejected[why.split(" ")[0] + " " + why.split(" ")[1] if why else "?"] += 1
    by_skill = defaultdict(Counter)
    for key, v in totals.items():
        skill, file, action = key.split("/")
        by_skill[skill][action] += v
    n_applied = sum(totals.values())
    n_rejected = sum(len(r["rejected"]) for r in rounds.values())
    num.update({"nRounds": n_rounds, "nEditsApplied": n_applied, "nEditsRejected": n_rejected,
                "nEditsAttempted": n_applied + n_rejected,
                "nDelete": sum(v for k, v in totals.items() if k.endswith("/delete")),
                "nModify": sum(v for k, v in totals.items() if k.endswith("/modify")),
                "nAdd": sum(v for k, v in totals.items() if k.endswith("/add"))})
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{5pt}",
             r"\begin{tabular}{@{}lrrrr@{}}", r"\toprule", r"Skill & Modify & Add & Delete & Total \\", r"\midrule"]
    for skill in ("generate", "critique", "document"):
        c = by_skill[skill]
        lines.append("\\skill{%s} & %d & %d & %d & %d \\\\" % (skill, c["modify"], c["add"], c["delete"], sum(c.values())))
    lines += [r"\midrule", "All & %d & %d & %d & %d \\\\" % (num["nModify"], num["nAdd"], num["nDelete"], n_applied),
              r"\bottomrule", r"\end{tabular}",
              r"\caption{Applied edits over %d improvement rounds (%d further edits were rejected: anchor not found, "
              r"copied document text, or depending on a rejected tool).}" % (n_rounds, n_rejected),
              r"\label{tab:edits}", r"\end{table}"]
    write("edits.tex", "\n".join(lines) + "\n")
    for skill in ("generate", "critique", "document"):
        num["edits" + skill.capitalize()] = sum(by_skill[skill].values())

    # per-round table (appendix)
    sc_rounds = load("umr", "critique_scores.json")["rounds"]
    lines = [r"\begin{table}[t]", r"\centering\scriptsize", r"\setlength{\tabcolsep}{3pt}",
             r"\begin{tabular}{@{}lrrrrrrl@{}}", r"\toprule",
             r"Round & Probl. & D-lvl & Gen. & Crit. & Doc. & Rej. & Proposal \\", r"\midrule"]
    for k, v in sc_rounds.items():
        r = rounds.get(k, {"edits": {}, "rejected": [], "structural": []})
        per = Counter()
        for key, n in r["edits"].items():
            per[key.split("/")[0]] += n
        prop = "; ".join("%s (%s)" % (x["name"].replace("_", r"\_"), "adm." if x["status"] == "applied" else "rej.")
                         for x in r["structural"]) or "--"
        lines.append("$R_{%s}$ & %d & %d & %d & %d & %d & %d & %s \\\\" % (
            k[1:], v["problems"], v["document_level"], per["generate"], per["critique"], per["document"],
            len(r["rejected"]), prop))
    lines += [r"\bottomrule", r"\end{tabular}",
              r"\caption{Every improvement round of the sequential run: divergences found (of them document-level), "
              r"edits applied per skill, edits rejected, and tool or step proposals.}", r"\label{tab:rounds}",
              r"\end{table}"]
    write("rounds.tex", "\n".join(lines) + "\n")

    # structural proposals
    prop = [(k, s) for k, r in rounds.items() for s in r["structural"]]
    num["nProposals"] = len(prop)
    num["nProposalsAccepted"] = sum(1 for k, s in prop if s["status"] == "applied")

    # --- harness size
    sizes = load("umr", "critique_sizes.json")
    order = sorted((v for v in sizes), key=lambda v: (v != "R0", int(v[1:-1] or 0), v[-1]))
    total = {v: sizes[v]["generate"] + sizes[v]["critique"] + sizes[v]["document"] for v in order}
    last = order[-1]
    num.update({"sizeSeed": total["R0"], "sizeLast": total[last], "sizeLastName": last,
                "sizeGen": sizes[last]["generate"], "sizeCrit": sizes[last]["critique"],
                "sizeDoc": sizes[last]["document"], "sizePerRound": (total[last] - total["R0"]) / (len(order) - 1),
                "sizeFactor": total[last] / total["R0"]})

    # --- problems per round
    scores_all = load("umr", "critique_scores.json")["rounds"]
    first_rounds = [(k, v) for k, v in scores_all.items() if k.endswith("1")]
    per_sent = []
    for k, v in first_rounds:
        doc = int(k[1:-1])
        n_sent = rows[doc - 1]["n_sent"]
        per_sent.append(v["problems"] / n_sent)
    num["problemsPerSentFirst"] = float(np.mean(per_sent))

    figure_curve(rows, order, total, paired, dF)
    figure_category(cat_rows)
    return rows, num, paired


# ---------------------------------------------------------------------------------------------- figures

PALETTE = {"ink": "#0b0b0b", "muted": "#52514e", "blue": "#2a78d6", "orange": "#eb6834", "grey": "#a3a29c"}


def figure_curve(rows, order, total, paired, dF):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8, "font.family": "serif", "axes.spines.top": False,
                         "axes.spines.right": False, "pdf.fonttype": 42})
    fig, (a, b) = plt.subplots(1, 2, figsize=(6.4, 2.35), gridspec_kw={"width_ratios": [1.25, 1]})
    x = [r["k"] for r in rows]
    xs = [r["k"] for r in rows if r["seed"] is not None]
    a.plot(xs, [r["seed"] for r in rows if r["seed"] is not None], color=PALETTE["grey"], marker="o", ms=3, lw=1.5,
           label="seed $H_0$")
    a.plot(x, [r["first"] for r in rows], color=PALETTE["blue"], marker="o", ms=3.5, lw=1.5,
           label="learned $H_{n-1}$ (unseen)")
    xa = [r["k"] for r in rows if r["after"] is not None]
    a.plot(xa, [r["after"] for r in rows if r["after"] is not None], color=PALETTE["orange"], marker="s", ms=3, lw=1.2,
           ls="--", label="trained on the document")
    a.set_xticks(x)
    a.set_xlabel("document $n$ (training order)")
    a.set_ylabel("sentence F")
    a.set_ylim(22, 102)
    a.legend(frameon=False, fontsize=6.5, loc="lower right", ncol=1)
    # right: gain against harness size
    kk = [r["k"] for r in paired]
    b.bar(kk, dF, color=PALETTE["blue"], width=0.65)
    b.axhline(0, color=PALETTE["muted"], lw=0.6)
    b.axhline(dF.mean(), color=PALETTE["muted"], lw=0.8, ls=":")
    b.set_xticks(kk)
    b.set_xlabel("document $n$")
    b.set_ylabel("F gain over seed")
    c = b.twinx()
    version_of_doc = {k: "R%d3" % (k - 1) for k in range(2, 12)}
    sizes_kb = [total[version_of_doc[k]] for k in kk]
    c.plot(kk, sizes_kb, color=PALETTE["orange"], marker="o", ms=2.5, lw=1.2)
    c.set_ylabel("harness size (KB)", color=PALETTE["orange"])
    c.tick_params(axis="y", colors=PALETTE["orange"])
    c.spines["right"].set_visible(True)
    c.spines["top"].set_visible(False)
    a.set_title("(a) sentence F per document", fontsize=8, loc="left")
    b.set_title("(b) gain vs. harness size", fontsize=8, loc="left")
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES, "curve.pdf"))
    plt.close(fig)


def figure_category(cat_rows):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 7.5, "font.family": "serif", "axes.spines.top": False,
                         "axes.spines.right": False, "pdf.fonttype": 42})
    rows = sorted(cat_rows, key=lambda r: r[4])
    fig, ax = plt.subplots(figsize=(3.1, 3.5))
    for i, (c, n, s, fi, g, pos) in enumerate(rows):
        ax.plot([s, fi], [i, i], color="#c9c8c3", lw=1.2, zorder=1)
        ax.scatter([s], [i], color=PALETTE["grey"], s=14, zorder=2)
        ax.scatter([fi], [i], color=PALETTE["blue"] if g >= 0 else PALETTE["orange"], s=14, zorder=3)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=6.3, family="monospace")
    ax.set_xlabel("judge score (seed $\\rightarrow$ learned)")
    ax.set_xlim(0, 1.02)
    ax.grid(axis="x", color="#ececea", lw=0.5)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES, "category.pdf"))
    plt.close(fig)


# ---------------------------------------------------------------------------------------------- other settings

def settings(num):
    """Seed vs learned on unseen documents for each chain / model that has such a run."""
    tree = load("umr", "tree_scores.json")["test"]
    rows = []
    rows.append(("Sonnet 5.5 / Opus 5.5", "\\textsc{critique}", "sequential", num["nPaired"], num["seedMean"],
                 num["firstMean"]))
    rows.append(("Sonnet 5.5 / Opus 5.5", "\\textsc{tree}", "4 docs, then test",
                 2, np.mean([tree["R0"]["docs"][d]["F"] for d in tree["R0"]["docs"]]),
                 np.mean([tree["R23"]["docs"][d]["F"] for d in tree["R0"]["docs"]])))
    ds = load("other", "deepseek_zh_scores.json")
    ds_rows = parse_deepseek(ds)
    rows.append(("DeepSeek (no thinking)", "\\textsc{tree}", "2 docs, then test", len(ds_rows),
                 np.mean([a for a, b in ds_rows]), np.mean([b for a, b in ds_rows])))
    q = load("other", "qwen9b_zh_scores.json")["rows"]
    pr = [(r["seed"]["F"], r["before"]["F"]) for r in q if r["k"] > 1 and r.get("seed") and r.get("before")]
    rows.append(("Qwen3.5-9B", "\\textsc{tree}", "sequential", len(pr), np.mean([a for a, b in pr]),
                 np.mean([b for a, b in pr])))
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{2pt}",
             r"\begin{tabular}{@{}llrrrr@{}}", r"\toprule",
             r"Builder / annotator & Harness & $n$ & Seed & Learned & $\Delta$ \\", r"\midrule"]
    names = ["Opus / Sonnet 5.5", "Opus / Sonnet 5.5", "DeepSeek (no thinking)", "Qwen3.5-9B"]
    harness = ["ours$^s$", "proc.", "proc.", "proc.$^s$"]
    for (model, chain, proto, n, a, b), nm, hn in zip(rows, names, harness):
        lines.append("%s & %s & %d & %.1f & %.1f & %s \\\\" % (nm, hn, n, a, b, sgn(b - a)))
    lines += [r"\midrule",
              r"Qwen3.5-27B & proc.$^s$ & \gapcell{} & \gapcell{} & \gapcell{} & \gapcell{} \\",
              r"Opus / small model & ours & \gapcell{} & \gapcell{} & \gapcell{} & \gapcell{} \\",
              r"Small model / Sonnet & ours$^s$ & \gapcell{} & \gapcell{} & \gapcell{} & \gapcell{} \\",
              r"\bottomrule", r"\end{tabular}",
              r"\caption{Seed vs.\ learned harness on unseen documents, sentence F. One name: the same model builds and "
              r"annotates. proc.: procedural harness. $^s$sequential protocol; otherwise a few training documents and "
              r"separate test documents. DeepSeek's seed reaches 49.1 F with thinking on vs.\ 35.9 off (document 0002).}",
              r"\label{tab:models}", r"\end{table}"]
    write("models.tex", "\n".join(lines) + "\n")
    num["qwenSmallGain"] = rows[3][5] - rows[3][4]
    num["qwenSmallN"] = rows[3][3]
    num["deepseekGain"] = rows[2][5] - rows[2][4]
    num["deepseekN"] = rows[2][3]
    num["treeGain"] = rows[1][5] - rows[1][4]
    qs = [(r["seed"]["F"], r["before"]["F"], r["k"]) for r in q if r["k"] > 1 and r.get("seed") and r.get("before")]
    d9 = np.array([b - a for a, b, k in qs])
    num["qwenSmallFirst"] = d9[: len(d9) // 2].mean()
    num["qwenSmallSecond"] = d9[len(d9) // 2:].mean()
    num["qwenSmallPos"] = int((d9 > 0).sum())


def parse_deepseek(ds):
    """(seed F, R42 F) for the test documents, from the scores.json of experiment/rsi-zh-deepseek."""
    out = []
    test = ds.get("test", {})
    r0 = test.get("R0", {}).get("docs", {})
    r42 = test.get("R42", {}).get("docs", {})
    for d in sorted(r0):
        if d in r42:
            out.append((r0[d]["F"], r42[d]["F"]))
    return out


def tree_vs_critique(num, rows):
    tree = load("umr", "tree_scores.json")["test"]
    crit = {r["doc"]: r for r in rows}
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{3.5pt}",
             r"\begin{tabular}{@{}lccc@{}}", r"\toprule",
             r"Held-out doc & Procedural & Ours & Few-shot \\", r"\midrule"]
    t5 = tree["R42"]["docs"]["chinese_umr-0005"]["F"]
    c5 = crit["chinese_umr-0005"]["first"]
    lines.append("0005 & %.1f & %.1f & %s \\\\" % (t5, c5, GAP))
    for d in ("0006", "0007"):
        lines.append("%s & %.1f & %s & %s \\\\" % (d, tree["R42"]["docs"]["chinese_umr-" + d]["F"], GAP, GAP))
    lines += [r"\bottomrule", r"\end{tabular}",
              r"\caption{Trained on documents 0001--0004 with the same models, tested on 0005--0007, sentence F. The procedural "
              r"harness ($R_{42}$) has had 10 rounds (two on each of 0003 and 0004), ours ($H_4$) 12.}", r"\label{tab:matched}", r"\end{table}"]
    write("matched.tex", "\n".join(lines) + "\n")
    num["matchedTree"] = t5
    num["matchedCrit"] = c5


# ---------------------------------------------------------------------------------------------- refine, other tasks

def refine(num):
    """umr-refine: generate followed by five checking steps; what the five checks add, on trained and unseen documents."""
    steps = load("umr", "refine_steps.json")
    trained, unseen = [], []
    for s in steps:
        gain = s["steps"][-1]["F"] - s["steps"][0]["F"]
        if s["parse"] == "after":
            trained.append((s["doc"], s["version"], s["steps"][0]["F"], s["steps"][-1]["F"], gain))
        elif s["version"] != "R0" and (s["parse"] == "test" or s["parse"] == "iter1"):
            unseen.append((s["doc"], s["version"], s["steps"][0]["F"], s["steps"][-1]["F"], gain))
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{4pt}",
             r"\begin{tabular}{@{}llcccc@{}}", r"\toprule",
             r"& Doc & Version & \skill{generate} & +5 checks & $\Delta$ \\", r"\midrule"]
    for i, (d, v, a, b, g) in enumerate(trained):
        lines.append("%s & %s & $%s_{%s}$ & %.1f & %.1f & %s \\\\" % (
            r"\multirow{%d}{*}{trained}" % len(trained) if i == 0 else "", d[-4:], v[0], v[1:], a, b, sgn(g)))
    lines.append(r"\midrule")
    for i, (d, v, a, b, g) in enumerate(unseen):
        lines.append("%s & %s & $%s_{%s}$ & %.1f & %.1f & %s \\\\" % (
            r"\multirow{%d}{*}{unseen}" % len(unseen) if i == 0 else "", d[-4:], v[0], v[1:], a, b, sgn(g)))
    lines += [r"\bottomrule", r"\end{tabular}",
              r"\caption{A variant with five checking steps after \skill{generate} (concepts, arguments, attributes, "
              r"entities, reentrancy), improved by the same loop. Sentence F after \skill{generate} and after the five "
              r"checks, on the document the version was trained on and on documents it had not seen.}",
              r"\label{tab:refine}", r"\end{table}"]
    write("refine.tex", "\n".join(lines) + "\n")
    g_tr = np.array([x[4] for x in trained])
    g_un = np.array([x[4] for x in unseen])
    num.update({"refineTrainMin": g_tr.min(), "refineTrainMax": g_tr.max(), "refineUnseen": g_un.mean(),
                "refineUnseenMin": g_un.min(), "refineUnseenMax": g_un.max(), "refineUnseenN": len(g_un)})


def other_tasks(num):
    """TempEval-3 and manifesto tables: the baselines that are done, TBD for the learned harness."""
    t = load("other", "timeml_scores.json")
    cols = ["timex_strict_f1", "timex_relaxed_f1", "timex_value", "event_f1", "event_class", "tlink_f1"]

    def trow(name, key):
        if key not in t:
            return name + " & " + " & ".join([GAP] * len(cols)) + r" \\"
        r = t[key]
        return name + " & " + " & ".join("--" if r[c] == 0 else "%.1f" % r[c] for c in cols) + r" \\"
    lines = [r"\begin{table}[t]", r"\centering\footnotesize", r"\setlength{\tabcolsep}{1.9pt}",
             r"\begin{tabular}{@{}lcccccc@{}}", r"\toprule",
             r"& \multicolumn{3}{c}{TIMEX3} & \multicolumn{2}{c}{EVENT} & TLINK \\",
             r"\cmidrule(lr){2-4}\cmidrule(lr){5-6}\cmidrule(lr){7-7}",
             r"System & strict & relaxed & value & F1 & class & F1 \\", r"\midrule",
             trow("HeidelTime (2013)", "sota2013/HeidelTime (unihd english-3)"),
             trow("ClearTK (2013)", "sota2013/ClearTK 1"),
             trow("TIPSem (2013)", "sota2013/TIPSem (TE2)"),
             r"\midrule",
             trow("Zero-shot prompt", "test/B-zero"),
             trow("Few-shot (10 docs)", "test/B-few"),
             trow("Seed $H_0$", "test/R0"),
             trow("Learned harness", "test/R-final"),
             r"\bottomrule", r"\end{tabular}",
             r"\caption{TempEval-3 platinum test (20 documents), official scorer. 2013 systems rescored from their "
             r"released outputs \citep{uzzaman2013semeval}; ``--'': the system does not produce this layer.}",
             r"\label{tab:timeml}", r"\end{table}"]
    write("timeml.tex", "\n".join(lines) + "\n")

    m = load("other", "manifesto_scores.json")

    def mrow(name, key):
        if key not in m:
            return "%s & %s & %s \\\\" % (name, GAP, GAP)
        return "%s & %.1f & %.1f \\\\" % (name, m[key]["accuracy"], m[key]["macro_f1"])
    lines = [r"\begin{table}[t]", r"\centering\small", r"\setlength{\tabcolsep}{4pt}",
             r"\begin{tabular}{@{}lcc@{}}", r"\toprule", r"System & Acc. & Macro-F1 \\", r"\midrule",
             mrow("Majority class", "test/B-majority"),
             mrow("TF-IDF + LR, same 1{,}200 sentences", "test/B-tfidf"),
             mrow("TF-IDF + LR, 33k sentences", "test/B-tfidf-full"),
             mrow("ManifestoBERTa$^\\ast$", "test/B-manifestoberta"),
             r"\midrule",
             mrow("Zero-shot prompt", "test/B-zero"),
             mrow("Few-shot, 30 retrieved examples", "test/B-few"),
             mrow("Seed harness $H_0$", "test/R0"),
             mrow("Learned harness", "test/R-final"),
             r"\bottomrule", r"\end{tabular}",
             r"\caption{Manifesto coding into eight policy domains, 800 test sentences. $^\ast$Trained on the "
             r"Manifesto Corpus, which these sentences come from: a reference, not a fair comparison.}",
             r"\label{tab:manifesto}", r"\end{table}"]
    write("manifesto.tex", "\n".join(lines) + "\n")


# ---------------------------------------------------------------------------------------------- macros

def macros(num):
    lines = ["% generated by analysis/make_tables.py; do not edit"]
    for k in sorted(num):
        v = num[k]
        if isinstance(v, (int, np.integer)):
            s = str(int(v))
        elif isinstance(v, str):
            s = v
        elif k.endswith(("Wilcoxon", "Sign", "RhoP")) or k in ("gainFt",):
            s = pval(float(v))
        elif k in ("gainRho",):
            s = "%.2f" % float(v)
        elif k in ("sizeLast", "sizeGen", "sizeCrit", "sizeDoc"):
            s = "%.0f" % float(v)
        else:
            s = "%.1f" % float(v)
        s = s.replace("-", "\\ensuremath{-}")
        lines.append("\\newcommand{\\%s}{%s}" % (k, s))
    write("numbers.tex", "\n".join(lines) + "\n")


def main():
    os.makedirs(TABLES, exist_ok=True)
    os.makedirs(FIGURES, exist_ok=True)
    rows, num, paired = critique()
    settings(num)
    tree_vs_critique(num, rows)
    refine(num)
    other_tasks(num)
    num["sizeFactorInt"] = int(round(num["sizeFactor"]))
    tree = load("umr", "tree_scores.json")["test"]
    num["treeSeedFive"] = tree["R0"]["docs"]["chinese_umr-0005"]["F"]
    num["treeGainFive"] = tree["R42"]["docs"]["chinese_umr-0005"]["F"] - num["treeSeedFive"]
    num["critGainFive"] = num["matchedCrit"] - load("umr", "critique_scores.json")["train"]["chinese_umr-0005"]["R0"]["F"]
    with open(os.path.join(DATA, "umr", "suggestions_coded.csv"), newline="", encoding="utf-8") as f:
        codes = Counter(r["code"] for r in csv.DictReader(f))
    num.update({"nSuggestions": sum(codes.values()), "sugGold": codes["gold"], "sugRule": codes["rule_code"],
                "sugContext": codes["context"], "sugEval": codes["evaluator"]})
    q = load("other", "qwen9b_zh_scores.json")["rows"]
    noise = [abs(r["seed"]["F"] - r["seed2"]["F"]) for r in q if r.get("seed") and r.get("seed2")]
    num["qwenSeedNoise"] = float(np.mean(noise))
    num["qwenSeedNoiseN"] = len(noise)
    macros(num)
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    with open(os.path.join(HERE, "out", "stats.json"), "w") as f:
        json.dump({k: (float(v) if not isinstance(v, str) else v) for k, v in num.items()}, f, indent=1)
    for k in sorted(num):
        print("%-18s %s" % (k, num[k] if isinstance(num[k], str) else round(float(num[k]), 4)))


if __name__ == "__main__":
    main()

"""Scores of one predicted .umr against its gold .umr.

    ancast(pred, gold)   AnCast++ (umr4nlp/ancast, `python -m ancast -s doc -df umr`): sentence-graph P/R/F
                         and the Modal, Temporal, Coref and Comprehensive scores, after Chun & Xue's cleanup
                         (a :modal-strength in the sentence graph moves to the document-level :modal block),
                         as SkillParseUMR's scripts/compare_ancast.py and experiment/annoforge/af/score.py do
    jumach(pred, gold)   juːmæʧ, the DMR 2026 shared task's metric (ufal/umrtools compare_umr.pl): counts
                         (correct, gold, predicted); needs perl and the umrtools checkout ($UMRTOOLS, default
                         exp/.cache/umrtools)
    smatch(pred, gold)   Smatch (pip smatch) over the sentence-level graphs, counts summed over sentences
    judge(pred, gold)    umrjudge (judges/umrjudge.py from SkillParseUMR): per-check units and scores

All four read the same two files: the gold as lib/umrdoc.gold_umr writes it and the prediction as
lib/umrdoc.parse_answer writes it. The gold is the newdata/ gold of SkillParseUMR (not the shared task's
official test gold, which is not in git), so juːmæʧ here is not the official number of the shared task.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

import penman

HERE = os.path.dirname(os.path.abspath(__file__))
EXP = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(EXP, "judges"))
sys.path.insert(0, HERE)
import umrdoc  # noqa: E402

SECTIONS = umrdoc.SECTIONS
UMRTOOLS = os.environ.get("UMRTOOLS", os.path.join(EXP, ".cache", "umrtools"))


# ------------------------------------------------------------------ AnCast++

def clean(bs):
    """Chun & Xue's cleanup: sentence-graph modal strength moves to the document level."""
    for _, sections in bs:
        graph = sections.get(SECTIONS[0], "").strip()
        doc = sections.get(SECTIONS[2], "")
        doc = re.sub(r":AFF\b", ":full-affirmative", doc)
        moved = []
        if graph:
            try:
                g = penman.decode(graph)
                keep = []
                present = {" ".join(p.split()) for p in re.findall(r"\(\s*author\s+:[\w-]+\s+[^\s()]+\s*\)", doc)}
                for s, r, t in g.triples:
                    if r in (":modal-strength", ":modstr"):
                        rel = "(author :%s %s)" % (str(t).strip('"'), s)
                        if rel not in present and rel not in moved:
                            moved.append(rel)
                    else:
                        keep.append((s, r, t))
                if len(keep) < len(g.triples):
                    graph = penman.encode(penman.Graph(keep, top=g.top), indent=4)
            except Exception:
                pass
        if moved:
            if ":modal" in doc:
                doc = re.sub(r":modal\s*\(", ":modal (" + " ".join(moved) + " ", doc, count=1)
            elif doc.strip().endswith(")"):
                doc = doc.rstrip()[:-1] + "\n    :modal (" + " ".join(moved) + "))\n"
        sections[SECTIONS[0]] = graph + "\n"
        sections[SECTIONS[2]] = doc
    return bs


def render(bs, heads=None):
    out = []
    for i, (head, sections) in enumerate(bs):
        if heads and i < len(heads):
            head = heads[i]
        pieces = [head.strip()] + ["%s\n%s" % (m, sections.get(m, "").strip()) for m in SECTIONS]
        out.append(re.sub(r"\n{3,}", "\n\n", "\n\n".join(pieces)))
    return "\n\n\n".join(out) + "\n"


AGG = re.compile(r"(Sent Micro|Modality|Temporal|Coref):\s*Precision:\s*([0-9.]+)%\s*Recall:\s*([0-9.]+)%\s*Fscore:\s*([0-9.]+)%")
COMP = re.compile(r"Comprehensive Score:\s*([0-9.]+)%")


def _run_ancast(pred, gold):
    proc = subprocess.run([sys.executable, "-m", "ancast", "-p", pred, "-g", gold, "-s", "doc", "-df", "umr",
                           "-o", os.path.splitext(pred)[0] + ".ancast.csv"],
                          capture_output=True, text=True, timeout=1800, cwd=os.path.dirname(pred))
    text = proc.stdout + proc.stderr
    found = AGG.findall(text)
    f = {m: float(fs) for m, _, _, fs in found}
    prf = [x[1:] for x in found if x[0] == "Sent Micro"]
    comp = COMP.findall(text)
    return {"Modal": f.get("Modality"), "Temporal": f.get("Temporal"), "Coref": f.get("Coref"),
            "Comprehensive": float(comp[-1]) if comp else None, "sent_prf": prf[-1] if prf else None,
            "tail": text[-800:]}


def _blank(sections, n):
    sections[SECTIONS[0]] = "(s%dx0 / empty)\n" % n
    sections[SECTIONS[1]] = "s%dx0: 0-0\n" % n
    sections[SECTIONS[2]] = "(s%ds0 / sentence)\n" % n


def ancast(pred_path, gold_path):
    """AnCast++ of a predicted file against its gold. When AnCast cannot score the document, the predicted
    sentences umrjudge cannot match are scored as empty and AnCast is run again (as annoforge does)."""
    gold_text, pred_text = open(gold_path, encoding="utf-8").read(), open(pred_path, encoding="utf-8").read()
    work = tempfile.mkdtemp()
    try:
        gp, pp = os.path.join(work, "doc.gold.umr"), os.path.join(work, "doc.pred.umr")
        gold_blocks = clean(umrdoc.blocks(gold_text))
        heads = [h for h, _ in gold_blocks]
        pred_blocks = clean(umrdoc.blocks(pred_text))
        open(gp, "w", encoding="utf-8").write(render(gold_blocks))
        open(pp, "w", encoding="utf-8").write(render(pred_blocks, heads))
        r = _run_ancast(pp, gp)
        blanked = []
        if r["sent_prf"] is None:
            blanked = sorted(_unmatchable(pp, gp))
            for i, (_, sections) in enumerate(pred_blocks):
                if i + 1 in blanked:
                    _blank(sections, i + 1)
            open(pp, "w", encoding="utf-8").write(render(pred_blocks, heads))
            r = _run_ancast(pp, gp)
        if r["sent_prf"] is None:
            return {"error": "AnCast could not score the document", "tail": r["tail"], "blanked": blanked}
        p, rc, fs = (float(x) for x in r["sent_prf"])
        return {"P": p, "R": rc, "F": fs, "Modal": r["Modal"], "Temporal": r["Temporal"], "Coref": r["Coref"],
                "Comprehensive": r["Comprehensive"], "blanked": blanked}
    finally:
        shutil.rmtree(work, ignore_errors=True)


def _unmatchable(pred_path, gold_path):
    import umrjudge
    spec = umrjudge.load_spec()
    move = spec.get("cleanup", {}).get("move_modal_strength", False)
    gold, pred = umrjudge.read_umr(gold_path, move), umrjudge.read_umr(pred_path, move)
    out = set()
    for n in gold:
        if n in pred:
            m = umrjudge.match_sentences(pred[n]["graph"], gold[n]["graph"], pred[n]["words"], gold[n]["words"], n, spec)
            if m.get("pred_invalid") or m.get("error"):
                out.add(n)
    return out


# ------------------------------------------------------------------ juːmæʧ

def jumach(pred_path, gold_path):
    """(correct, gold total, predicted total) of juːmæʧ, or None when umrtools is not there."""
    script = os.path.join(UMRTOOLS, "compare_umr.pl")
    if not os.path.exists(script):
        return None
    proc = subprocess.run(["perl", script, "GOLD", gold_path, "SYS", pred_path, "--tsv"],
                          capture_output=True, text=True, timeout=1200)
    for line in proc.stdout.splitlines():
        cells = line.split("\t")
        if len(cells) >= 6 and cells[0].strip().startswith("ju"):
            return int(cells[3]), int(cells[4]), int(cells[5])
    return None


# ------------------------------------------------------------------ Smatch

def _one_line(graph):
    """A sentence graph as Smatch reads it: one line, every concept a plain token."""
    g = penman.decode(graph)
    return penman.encode(g, indent=None)


def smatch(pred_path, gold_path):
    """(matched, predicted, gold) triple counts of Smatch, summed over the sentence graphs."""
    import smatch as S
    gold = umrdoc.blocks(open(gold_path, encoding="utf-8").read())
    pred = umrdoc.blocks(open(pred_path, encoding="utf-8").read())
    total = [0, 0, 0]
    for k, (_, gs) in enumerate(gold):
        ps = pred[k][1] if k < len(pred) else {}
        try:
            g1 = _one_line(gs.get(SECTIONS[0], ""))
        except Exception:
            continue
        try:
            p1 = _one_line(ps.get(SECTIONS[0], "") or "(x / empty)")
        except Exception:
            p1 = "(x / empty)"
        try:
            S.match_triple_dict.clear()
            m, t, g = S.get_amr_match(p1, g1)
        except Exception:
            m, t, g = 0, 1, len(penman.decode(g1).triples) + 1
        total[0] += m
        total[1] += t
        total[2] += g
    return tuple(total)


# ------------------------------------------------------------------ umrjudge

def judge(pred_path, gold_path):
    """(scores, units) of umrjudge."""
    import umrjudge
    spec = umrjudge.load_spec()
    r = umrjudge.judge_file(pred_path, gold_path, spec)
    for u in r["units"]:
        u["credit"] = umrjudge.credit_of(u, spec)
    return umrjudge.score(r["units"], spec), r["units"]


def prf(correct, gold, pred):
    p = correct / pred if pred else 0.0
    r = correct / gold if gold else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)

"""Run and score the sub-experiments.

    python3 exp/run.py api <sub> [--model M] [--effort E] [--docs d1,d2] [--jobs N] [--label L]
        annotate every test document with the Messages API (registry api/<sub>/registry.yaml), then score
    python3 exp/run.py chat-prompts <sub>
        write chat/<sub>/prompts/<doc>.md (and chat/<sub>/attachments/<doc>.* for the step-2 resources):
        what to paste into a chat window
    python3 exp/run.py chat-score <sub> [--label L]
        read the chat answers chat/<sub>/answers/<doc>.txt and score them
    python3 exp/run.py harness-score <sub> [--label L]
        the same for harness/<sub>/answers/<doc>.txt (method 3, not done yet)
    python3 exp/run.py score <run dir>        score a run directory again
    python3 exp/run.py table                  results.md: every scored run in one table

<sub> is one of s1-abridged, s1-full, s2-search, s2-propbank, s2-gold. A run directory is
runs/<method>/<sub>/<label>/ with <doc>.raw.txt (the answer as written), <doc>.umr (as scored),
<doc>.trace.json (parse report, usage, tool calls) and scores.json / scores.md.
"""
import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

EXP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(EXP, "lib"))
sys.path.insert(0, EXP)
import registry  # noqa: E402
import score  # noqa: E402
import umrdoc  # noqa: E402

SUBS = ["s1-abridged", "s1-full", "s2-search", "s2-propbank", "s2-gold"]
DOCS = json.load(open(os.path.join(EXP, "data", "docs.json"), encoding="utf-8"))["docs"]
RUNS = os.path.join(EXP, "runs")
CACHE = os.path.join(EXP, ".cache")


def doc_of(name):
    return umrdoc.load(os.path.join(EXP, "data", "gold", name + ".umr"))


def annotation(doc):
    return {"name": doc["name"], "lang": doc["lang"], "lines": umrdoc.input_lines(doc), "sentences": len(doc["sents"])}


def gold_path(doc):
    path = os.path.join(CACHE, "gold", doc["name"] + ".umr")
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(umrdoc.gold_umr(doc))
    return path


def test_texts():
    return [" ".join(s["words"]) for d in DOCS for s in doc_of(d["doc"])["sents"]]


# ------------------------------------------------------------------ API

def run_api(sub, model, effort, docs, jobs, label):
    import llm
    import tools.search as search
    search.set_skip(docs=[d["doc"] for d in DOCS], texts=test_texts())
    reg = registry.load(os.path.join(EXP, "api", sub, "registry.yaml"))
    out_dir = os.path.join(RUNS, "api", sub, label or model)
    os.makedirs(out_dir, exist_ok=True)

    def one(name):
        doc = doc_of(name)
        t0 = time.time()
        traces = []

        def call_skill(skill_name, skill, system, user):
            r = llm.answer(model, system, user, skill.get("tools") or [], effort, os.path.join(CACHE, "answers"))
            traces.append({k: v for k, v in r.items() if k != "text"} | {"skill": skill_name})
            return {"umr": r["text"]}

        tree = registry.run(reg, annotation(doc), call_skill)
        node = tree[reg["waves"][-1]["name"]][-1]
        text = node.get("umr", "") if node["status"] == "ok" else ""
        with open(os.path.join(out_dir, name + ".raw.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        umr, report = umrdoc.parse_answer(doc, text)
        with open(os.path.join(out_dir, name + ".umr"), "w", encoding="utf-8") as f:
            f.write(umr)
        with open(os.path.join(out_dir, name + ".trace.json"), "w", encoding="utf-8") as f:
            json.dump({"doc": name, "model": model, "effort": effort, "seconds": round(time.time() - t0, 1),
                       "status": node["status"], "error": node.get("error"), "parse": report, "calls": traces},
                      f, ensure_ascii=False, indent=1)
        print("%s %s: %s, %d/%d sentences, %d relations, %d problems, %.0fs" % (
            sub, name, node["status"], report["sentences_found"], report["sentences"], report["relations"],
            len(report["problems"]), time.time() - t0), flush=True)

    with ThreadPoolExecutor(jobs) as pool:
        list(pool.map(one, docs))
    score_dir(out_dir)


# ------------------------------------------------------------------ chat

def chat_prompts(sub):
    import tools.search as search
    import tools.propbank as propbank
    search.set_skip(docs=[d["doc"] for d in DOCS], texts=test_texts())
    reg = registry.load(os.path.join(EXP, "chat", sub, "registry.yaml"))
    base = os.path.join(EXP, "chat", sub)
    os.makedirs(os.path.join(base, "prompts"), exist_ok=True)
    os.makedirs(os.path.join(base, "answers"), exist_ok=True)
    skill_name = reg["waves"][0]["start"]
    skill = reg["skills"][skill_name]
    for d in DOCS:
        doc = doc_of(d["doc"])
        ann = annotation(doc)
        names = {"annotation": ann}
        init = reg["waves"][0]["init_input"]
        variables = {k: registry.value(v, names) for k, v in {**init.get("context", {}), **init.get("input", {})}.items()}
        system, user = registry.render(skill, variables)
        with open(os.path.join(base, "prompts", d["doc"] + ".md"), "w", encoding="utf-8") as f:
            f.write(system + "\n" + user)
        attach = skill.get("attachment")
        if attach and attach != "guidelines":      # the guidelines file is exp/guidelines/umr_guidelines.md itself
            os.makedirs(os.path.join(base, "attachments"), exist_ok=True)
            if attach == "propbank":
                text = propbank_attachment(doc, propbank)
            elif attach == "gold":
                text = gold_attachment(doc, search)
            else:
                raise SystemExit("unknown attachment %s" % attach)
            with open(os.path.join(base, "attachments", d["doc"] + "." + attach + ".md"), "w", encoding="utf-8") as f:
                f.write(text)
    print("wrote %s/prompts/*.md for %d documents" % (base, len(DOCS)))


def propbank_attachment(doc, propbank):
    """Every PropBank entry of a word of the document (Chinese: every word; English: every word, with
    the lookup's own suffix stripping), so a chat model has the frames a tool would have given it."""
    lang = doc["lang"]
    words, forms, parts = set(), set(), []
    for s in doc["sents"]:
        for w in s["words"]:
            if w in words or not any(ch.isalpha() for ch in w):
                continue
            words.add(w)
            form, found = propbank._find(w, lang)
            if found and form not in forms:
                forms.add(form)
                parts.append(propbank._markdown(w, form, found))
    head = ("# PropBank entries for the words of %s\n\nFrom ai-native-annotator.github.io data/skillparse/resources/"
            "propbank/%s.json: every roleset of every word of the document that PropBank has.\n\n" % (doc["name"], lang))
    return head + "\n\n".join(parts) + "\n"


def gold_attachment(doc, search, per_sentence=3, limit=60):
    """Gold annotations of similar sentences (never of a test document): for each sentence, the gold
    sentences sharing most of its content words, as search_annotations finds them."""
    picked, order = {}, []
    for s in doc["sents"]:
        words = [w for w in s["words"] if len(w) > (1 if doc["lang"] == "zh" else 3) and any(c.isalpha() for c in w)]
        if not words:
            continue
        r = search.search_annotations(doc["lang"], words[:12], per_sentence)
        for g in r["gold"]:
            key = (g["doc"], g["sentence_number"])
            if key not in picked:
                picked[key] = g
                order.append(key)
        if len(order) >= limit:
            break
    head = ("# Gold UMR annotations of sentences like those of %s\n\nFrom ai-native-annotator.github.io "
            "data/skillparse/resources/gold/%s/gold.json (no test document).\n\n" % (doc["name"], doc["lang"]))
    body = ["## %s, sentence %s\n\n%s" % (picked[k]["doc"], picked[k]["sentence_number"], picked[k]["annotation"])
            for k in order[:limit]]
    return head + "\n\n".join(body) + "\n"


def answers_score(sub, label, method="chat"):
    """Score answers saved by hand: <method>/<sub>/answers/<doc>.txt -> runs/<method>/<sub>/<label>/."""
    base = os.path.join(EXP, method, sub, "answers")
    out_dir = os.path.join(RUNS, method, sub, label)
    if not any(os.path.exists(os.path.join(base, d["doc"] + ".txt")) for d in DOCS):
        raise SystemExit("no answers in %s (save each answer as <doc>.txt there)" % base)
    os.makedirs(out_dir, exist_ok=True)
    for d in DOCS:
        path = os.path.join(base, d["doc"] + ".txt")
        if not os.path.exists(path):
            continue
        doc = doc_of(d["doc"])
        text = open(path, encoding="utf-8").read()
        umr, report = umrdoc.parse_answer(doc, text)
        open(os.path.join(out_dir, d["doc"] + ".raw.txt"), "w", encoding="utf-8").write(text)
        open(os.path.join(out_dir, d["doc"] + ".umr"), "w", encoding="utf-8").write(umr)
        json.dump({"doc": d["doc"], "parse": report}, open(os.path.join(out_dir, d["doc"] + ".trace.json"), "w",
                  encoding="utf-8"), ensure_ascii=False, indent=1)
        print("%s %s: %d/%d sentences, %d relations, %d problems" % (sub, d["doc"], report["sentences_found"],
              report["sentences"], report["relations"], len(report["problems"])))
    score_dir(out_dir)


# ------------------------------------------------------------------ scoring

def score_dir(out_dir):
    per = {}
    for d in DOCS:
        pred = os.path.join(out_dir, d["doc"] + ".umr")
        if not os.path.exists(pred):
            continue
        doc = doc_of(d["doc"])
        gp = gold_path(doc)
        r = {"lang": doc["lang"], "sents": len(doc["sents"])}
        r["ancast"] = score.ancast(pred, gp)
        r["smatch"] = score.smatch(pred, gp)
        r["jumach"] = score.jumach(pred, gp)
        s, units = score.judge(pred, gp)
        r["judge"] = {k: v.get("score") for k, v in s.items()}
        r["judge_counts"] = {k: [v.get("correct", 0), v.get("units", 0)] for k, v in s.items()}
        per[d["doc"]] = r
    out = {"docs": per, "summary": summary(per)}
    with open(os.path.join(out_dir, "scores.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out_dir, "scores.md"), "w", encoding="utf-8") as f:
        f.write(scores_md(out_dir, out))
    for lang, s in out["summary"].items():
        print("%s %s: AnCast F %s, Comp %s, Smatch F %s, juːmæʧ F %s, judge %s" % (
            os.path.relpath(out_dir, EXP), lang, fmt(s["ancast_F"]), fmt(s["ancast_Comprehensive"]),
            fmt(s["smatch_F"]), fmt(s["jumach_F"]), fmt(s["judge_mean"])), flush=True)
    return out


METRICS = ["F", "Comprehensive", "Modal", "Temporal", "Coref"]


def summary(per):
    out = {}
    for lang in ("zh", "en"):
        rs = [r for r in per.values() if r["lang"] == lang]
        if not rs:
            continue
        s = {"docs": len(rs), "sents": sum(r["sents"] for r in rs)}
        for m in METRICS:     # AnCast++: mean over documents
            xs = [r["ancast"].get(m) for r in rs if r["ancast"].get(m) is not None]
            s["ancast_" + m] = round(sum(xs) / len(xs), 1) if xs else None
        c = [sum(r["smatch"][k] for r in rs) for k in range(3)]      # matched, predicted, gold
        s["smatch_F"] = round(100 * score.prf(c[0], c[2], c[1])[2], 1)
        jc = [r["jumach"] for r in rs if r["jumach"]]
        s["jumach_F"] = round(100 * score.prf(sum(x[0] for x in jc), sum(x[1] for x in jc), sum(x[2] for x in jc))[2], 1) \
            if len(jc) == len(rs) else None
        checks = sorted({k for r in rs for k in r["judge"]})
        s["judge"] = {}
        for k in checks:
            vals = [r["judge"][k] for r in rs if r["judge"].get(k) is not None]
            s["judge"][k] = round(100 * sum(vals) / len(vals), 1) if vals else None
        vals = [v for v in s["judge"].values() if v is not None]
        s["judge_mean"] = round(sum(vals) / len(vals), 1) if vals else None
        out[lang] = s
    return out


def fmt(x):
    return "–" if x is None else "%.1f" % x


def scores_md(out_dir, out):
    rel = os.path.relpath(out_dir, EXP)
    lines = ["# %s" % rel, "",
             "AnCast++ (mean over documents), Smatch and juːmæʧ (micro over sentences), umrjudge (mean of the checks). "
             "Gold: SkillParseUMR newdata/.", "",
             "| doc | sents | AnCast F | Comp | Modal | Temporal | Coref | Smatch F | juːmæʧ F | judge |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for name, r in out["docs"].items():
        sm = score.prf(r["smatch"][0], r["smatch"][2], r["smatch"][1])[2] * 100
        ju = score.prf(*[r["jumach"][k] for k in (0, 1, 2)])[2] * 100 if r["jumach"] else None
        jv = [v for v in r["judge"].values() if v is not None]
        lines.append("| %s | %d | %s | %s | %s | %s | %s | %.1f | %s | %s |" % (
            name, r["sents"], *[fmt(r["ancast"].get(m)) for m in METRICS], sm, fmt(ju),
            fmt(100 * sum(jv) / len(jv) if jv else None)))
    for lang, s in out["summary"].items():
        lines.append("| **%s** | %d | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            lang, s["sents"], *[fmt(s["ancast_" + m]) for m in METRICS], fmt(s["smatch_F"]), fmt(s["jumach_F"]),
            fmt(s["judge_mean"])))
    lines += ["", "## umrjudge per check", "", "| check | " + " | ".join(out["summary"]) + " |",
              "|---|" + "---|" * len(out["summary"])]
    checks = sorted({k for s in out["summary"].values() for k in s["judge"]})
    for k in checks:
        lines.append("| %s | %s |" % (k, " | ".join(fmt(s["judge"].get(k)) for s in out["summary"].values())))
    return "\n".join(lines) + "\n"


def table():
    rows = []
    for method in ("api", "chat", "harness"):
        for sub in SUBS:
            d = os.path.join(RUNS, method, sub)
            if not os.path.isdir(d):
                continue
            for label in sorted(os.listdir(d)):
                p = os.path.join(d, label, "scores.json")
                if os.path.exists(p):
                    rows.append((method, sub, label, json.load(open(p, encoding="utf-8"))["summary"]))
    lines = ["# Results", "", "Generated by `python3 exp/run.py table`. AnCast++ F / Comprehensive: mean over documents; "
             "Smatch, juːmæʧ: micro; judge: mean of umrjudge's checks. Gold: SkillParseUMR newdata/ "
             "(juːmæʧ here is against that gold, not the shared task's official test gold).", ""]
    for lang, title in (("zh", "Chinese (7 documents, 99 sentences)"), ("en", "English (4 documents, 95 sentences)")):
        lines += ["## " + title, "", "| method | sub-experiment | model | docs | AnCast F | Comp | Modal | Temporal | Coref "
                  "| Smatch F | juːmæʧ F | judge |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for method, sub, label, s in rows:
            if lang in s:
                x = s[lang]
                lines.append("| %s | %s | %s | %d | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                    method, sub, label, x["docs"], *[fmt(x["ancast_" + m]) for m in METRICS], fmt(x["smatch_F"]),
                    fmt(x["jumach_F"]), fmt(x["judge_mean"])))
        lines.append("")
    with open(os.path.join(EXP, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["api", "chat-prompts", "chat-score", "harness-score", "score", "table"])
    ap.add_argument("target", nargs="?")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--docs", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--label", default="")
    a = ap.parse_args()
    if a.command in ("api", "chat-prompts", "chat-score", "harness-score") and a.target not in SUBS:
        raise SystemExit("sub-experiment must be one of %s" % ", ".join(SUBS))
    docs = [d for d in a.docs.split(",") if d] or [d["doc"] for d in DOCS]
    if a.command == "api":
        run_api(a.target, a.model, a.effort, docs, a.jobs, a.label)
    elif a.command == "chat-prompts":
        chat_prompts(a.target)
    elif a.command == "chat-score":
        answers_score(a.target, a.label or "chat", "chat")
    elif a.command == "harness-score":
        answers_score(a.target, a.label or "harness", "harness")
    elif a.command == "score":
        score_dir(os.path.abspath(a.target))
    else:
        table()


if __name__ == "__main__":
    main()

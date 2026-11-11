"""Run and score the sub-experiments.

    python3 exp/run.py api <sub> [--model M] [--effort E] [--docs d1,d2] [--jobs N] [--label L]
        annotate every test document with the Messages API (registry api/<sub>/registry.yaml), then score
    python3 exp/run.py chat-prompts <sub>
        write chat/<sub>/prompts/<doc>.md (and chat/<sub>/attachments/<doc>.* for the step-2 resources):
        what to paste into a chat window
    python3 exp/run.py chat-score <sub> [--label L]
        read the chat answers chat/<sub>/answers/<doc>.txt and score them
    python3 exp/run.py harness-score <sub> [--label L]
        the same for harness/<sub>/answers/<label>/<doc>.txt (method 3; harness/claude_code.py runs it)
    python3 exp/run.py score <run dir>        score a run directory again
    python3 exp/run.py verify-st              re-score the shared task's two systems (UMR 2.2 system-outputs)
                                              with this scoring, next to the overview paper's numbers
    python3 exp/run.py table                  results.md: every scored run in one table

The test set is the DMR 2026 UMR parsing shared task's (UMR 2.2 test-blind / test-gold, fetched by
exp/data/fetch_umr22.sh): by default its Chinese (15 files, 236 sentences) and English (5 files, 195
sentences) files; --langs takes any of zh, en, cs, la, it, arp, nv, or "all".

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
ALL_DOCS = json.load(open(os.path.join(EXP, "data", "docs.json"), encoding="utf-8"))["docs"]
DOCS = [d for d in ALL_DOCS if d["lang"] in ("zh", "en")]      # set by --langs
LANGS = ["zh", "en", "cs", "la", "it", "arp", "nv"]
RUNS = os.path.join(EXP, "runs")
CACHE = os.path.join(EXP, ".cache")
UMR22 = os.environ.get("UMR22", os.path.join(CACHE, "umr22"))
# the overview paper (Štěpánek et al. 2026), Tables 2 and 5: juːmæʧ and Smatch per language
PAPER = {"orange": {"jumach": {"arp": .0815, "zh": .3651, "cs": .1587, "en": .2219, "it": .1394, "la": .1724, "nv": .2155},
                    "smatch": {"arp": .4308, "zh": .5194, "cs": .4921, "en": .4625, "it": .3567, "la": .4446, "nv": .3754}},
         "sema": {"jumach": {"arp": .1115, "zh": .2585, "cs": .2652, "en": .1919, "it": .2137, "la": .1918, "nv": .1273},
                  "smatch": {"arp": .3447, "zh": .4363, "cs": .4456, "en": .4169, "it": .3796, "la": .3879, "nv": .2568}}}


def need_umr22():
    if not os.path.isdir(os.path.join(UMR22, "test-gold")):
        raise SystemExit("no UMR 2.2 in %s: run bash exp/data/fetch_umr22.sh" % UMR22)


def doc_of(name):
    """The input: the shared task's blind test file (one sentence per line, tokens separated by spaces)."""
    need_umr22()
    return umrdoc.load_blind(os.path.join(UMR22, "test-blind", name + ".txt"))


def official_gold(name):
    return os.path.join(UMR22, "test-gold", name + ".umr")


def annotation(doc):
    return {"name": doc["name"], "lang": doc["lang"], "lines": umrdoc.input_lines(doc), "sentences": len(doc["sents"])}


def written_gold(name):
    """The official gold read and written back by lib/umrdoc (for AnCast and umrjudge)."""
    path = os.path.join(CACHE, "gold", name + ".umr")
    if not os.path.exists(path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(umrdoc.gold_umr(umrdoc.load(official_gold(name))))
    return path


def test_texts():
    """Every sentence of every test file (all languages): search_annotations never returns them."""
    return [" ".join(s["words"]) for d in ALL_DOCS for s in doc_of(d["doc"])["sents"]]


def skip_test(search):
    search.set_skip(docs=[], texts=test_texts())


# ------------------------------------------------------------------ API

def write_transcript(out_dir, name, model, effort, system, user, tools, r):
    """<doc>.prompt.md: the prompt as sent (system, then the user message); <doc>.transcript.json: the
    whole conversation (every answer with its thinking blocks and tool calls, every tool result)."""
    import llm
    with open(os.path.join(out_dir, name + ".prompt.md"), "w", encoding="utf-8") as f:
        f.write("<!-- system -->\n" + system + "\n<!-- user -->\n" + user)
    with open(os.path.join(out_dir, name + ".transcript.json"), "w", encoding="utf-8") as f:
        json.dump({"model": model, "effort": effort, "max_tokens": llm.MAX_TOKENS, "thinking": {"type": "adaptive"},
                   "system": "see %s.prompt.md" % name, "tools": llm.T.schemas(tools) if tools else [],
                   "responses": r["responses"], "messages": r["messages"]}, f, ensure_ascii=False, indent=1)


def run_api(sub, model, effort, docs, jobs, label, cache_only=False):
    import llm
    import tools.search as search
    skip_test(search)
    reg = registry.load(os.path.join(EXP, "api", sub, "registry.yaml"))
    out_dir = os.path.join(RUNS, "api", sub, label or model)
    os.makedirs(out_dir, exist_ok=True)

    def one(name):
        doc = doc_of(name)
        t0 = time.time()
        traces = []

        def call_skill(skill_name, skill, system, user):
            tools = skill.get("tools") or []
            r = llm.answer(model, system, user, tools, effort, os.path.join(CACHE, "answers"), cache_only)
            traces.append({k: v for k, v in r.items() if k not in ("text", "messages", "responses")} | {"skill": skill_name})
            write_transcript(out_dir, name, model, effort, system, user, tools, r)
            return {"umr": r["text"]}

        tree = registry.run(reg, annotation(doc), call_skill)
        node = tree[reg["waves"][-1]["name"]][-1]
        text = node.get("umr", "") if node["status"] == "ok" else ""
        with open(os.path.join(out_dir, name + ".raw.txt"), "w", encoding="utf-8") as f:
            f.write(text)
        umr, report = umrdoc.parse_answer(doc, text)
        with open(os.path.join(out_dir, name + ".umr"), "w", encoding="utf-8") as f:
            f.write(umr)
        seconds = round(time.time() - t0, 1)
        old = os.path.join(out_dir, name + ".trace.json")
        if traces and all(c["cached_turns"] == c["turns"] for c in traces) and os.path.exists(old):
            seconds = json.load(open(old, encoding="utf-8")).get("seconds", seconds)   # from the cache: keep the real time
        with open(os.path.join(out_dir, name + ".trace.json"), "w", encoding="utf-8") as f:
            json.dump({"doc": name, "model": model, "effort": effort, "seconds": seconds,
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
    skip_test(search)
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
    head = ("# Gold UMR annotations of sentences like those of %s\n\nFrom the training data of the UMR parsing "
            "shared task (UMR 2.2 training-clean and training-dirty; no test sentence).\n\n" % doc["name"])
    body = ["## %s, sentence %s\n\n%s" % (picked[k]["doc"], picked[k]["sentence_number"], picked[k]["annotation"])
            for k in order[:limit]]
    return head + "\n\n".join(body) + "\n"


def answers_score(sub, label, method="chat"):
    """Score saved answers: chat/<sub>/answers/<label>/<doc>.txt (saved by hand; or answers/<doc>.txt) or
    harness/<sub>/answers/<label>/<doc>.txt
    (written by harness/claude_code.py, with <doc>.meta.json) -> runs/<method>/<sub>/<label>/."""
    base = os.path.join(EXP, method, sub, "answers")
    if method == "harness" or os.path.isdir(os.path.join(base, label)):
        base = os.path.join(base, label)      # answers/<label>/<doc>.txt (chat: one folder per chat model)
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
        trace = {"doc": d["doc"], "parse": report}
        meta = os.path.join(base, d["doc"] + ".meta.json")
        if os.path.exists(meta):
            trace["run"] = json.load(open(meta, encoding="utf-8"))
        json.dump(trace, open(os.path.join(out_dir, d["doc"] + ".trace.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("%s %s: %d/%d sentences, %d relations, %d problems" % (sub, d["doc"], report["sentences_found"],
              report["sentences"], report["relations"], len(report["problems"])))
    score_dir(out_dir)


# ------------------------------------------------------------------ scoring

def score_file(pred, name, extra=True):
    """The scores of one predicted file. juːmæʧ and Smatch are against the official gold file itself."""
    gold = official_gold(name)
    r = {"lang": umrdoc.lang_of(name), "jumach": score.jumach(pred, gold), "smatch": score.smatch(pred, gold),
         "valid": score.validate(pred)}
    if extra:
        wg = written_gold(name)
        r["ancast"] = score.ancast(pred, wg)
        s, _ = score.judge(pred, wg)
        r["judge"] = {k: v.get("score") for k, v in s.items()}
    return r


def score_dir(out_dir, extra=True):
    per = {}
    for d in DOCS:
        pred = os.path.join(out_dir, d["doc"] + ".umr")
        if os.path.exists(pred):
            per[d["doc"]] = {"sents": d["sents"], **score_file(pred, d["doc"], extra)}
    out = {"docs": per, "summary": summary(per)}
    with open(os.path.join(out_dir, "scores.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(os.path.join(out_dir, "scores.md"), "w", encoding="utf-8") as f:
        f.write(scores_md(out_dir, out))
    for lang, s in out["summary"].items():
        print("%s %s (%d/%d files): juːmæʧ %s, Smatch %s, AnCast F %s, judge %s, valid %d/%d" % (
            os.path.relpath(out_dir, EXP), lang, s["files"], s["test_files"], fmt(s["jumach_F"]), fmt(s["smatch_F"]),
            fmt(s.get("ancast_F")), fmt(s.get("judge_mean")), s["valid"], s["files"]), flush=True)
    return out


METRICS = ["F", "Comprehensive", "Modal", "Temporal", "Coref"]


def summary(per):
    """Per language. juːmæʧ and Smatch: F1 of the counts summed over the files (micro, as the shared task
    reports a language). A test file with no prediction counts as an empty prediction (its gold counts
    are added), so a partial run is not scored as if it were complete; `files` says how many there were."""
    out = {}
    for lang in LANGS:
        test = [d for d in DOCS if d["lang"] == lang]
        rs = {n: r for n, r in per.items() if r["lang"] == lang}
        if not rs:
            continue
        s = {"files": len(rs), "test_files": len(test), "sents": sum(r["sents"] for r in rs.values())}
        ju = [0, 0, 0]
        for d in test:
            c = rs[d["doc"]]["jumach"] if d["doc"] in rs else None
            if c is None:
                c = (0, _gold_jumach_total(d["doc"]), 0)
            ju = [a + b for a, b in zip(ju, c)]
        s["jumach_P"], s["jumach_R"], s["jumach_F"] = (round(100 * x, 2) for x in score.prf(*ju))
        sm = [0, 0, 0]     # matched, predicted, gold
        for d in test:
            c = rs[d["doc"]]["smatch"] if d["doc"] in rs else (0, 0, _gold_smatch_total(d["doc"]))
            sm = [a + b for a, b in zip(sm, c)]
        s["smatch_F"] = round(100 * score.prf(sm[0], sm[2], sm[1])[2], 2)
        s["valid"] = sum(1 for r in rs.values() if r["valid"] and r["valid"]["passed"])
        if any("ancast" in r for r in rs.values()):
            for m in METRICS:      # AnCast++: mean over the files that have a value
                xs = [r["ancast"].get(m) for r in rs.values() if r.get("ancast") and r["ancast"].get(m) is not None]
                s["ancast_" + m] = round(sum(xs) / len(xs), 1) if xs else None
            checks = sorted({k for r in rs.values() for k in r.get("judge", {})})
            s["judge"] = {}
            for k in checks:
                vals = [r["judge"][k] for r in rs.values() if r.get("judge", {}).get(k) is not None]
                s["judge"][k] = round(100 * sum(vals) / len(vals), 1) if vals else None
            vals = [v for v in s["judge"].values() if v is not None]
            s["judge_mean"] = round(sum(vals) / len(vals), 1) if vals else None
        out[lang] = s
    return out


_totals = {}


def _gold_jumach_total(name):
    """The gold side of juːmæʧ for a file with no prediction: gold scored against itself."""
    if ("j", name) not in _totals:
        _totals[("j", name)] = score.jumach(official_gold(name), official_gold(name))[1]
    return _totals[("j", name)]


def _gold_smatch_total(name):
    if ("s", name) not in _totals:
        _totals[("s", name)] = score.smatch(official_gold(name), official_gold(name))[2]
    return _totals[("s", name)]


def fmt(x):
    return "–" if x is None else "%.1f" % x


def scores_md(out_dir, out):
    rel = os.path.relpath(out_dir, EXP)
    lines = ["# %s" % rel, "",
             "Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold "
             "of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and "
             "umrjudge (mean of its checks) are extra. valid: validate.py --level 2.", "",
             "| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for name, r in out["docs"].items():
        jp, jr, jf = (100 * x for x in score.prf(*r["jumach"])) if r["jumach"] else (None, None, None)
        sm = score.prf(r["smatch"][0], r["smatch"][2], r["smatch"][1])[2] * 100
        jv = [v for v in r.get("judge", {}).values() if v is not None]
        v = r["valid"]
        lines.append("| %s | %d | %s | %s | %s | %.1f | %s | %s | %s | %s |" % (
            name, r["sents"], fmt(jp), fmt(jr), fmt(jf), sm,
            "–" if v is None else ("yes" if v["passed"] else "no (%d)" % v["n_errors"]),
            fmt(r.get("ancast", {}).get("F")), fmt(r.get("ancast", {}).get("Comprehensive")),
            fmt(100 * sum(jv) / len(jv) if jv else None)))
    for lang, s in out["summary"].items():
        lines.append("| **%s** (%d/%d files) | %d | %s | %s | %s | %s | %d/%d | %s | %s | %s |" % (
            lang, s["files"], s["test_files"], s["sents"], fmt(s["jumach_P"]), fmt(s["jumach_R"]), fmt(s["jumach_F"]),
            fmt(s["smatch_F"]), s["valid"], s["files"], fmt(s.get("ancast_F")), fmt(s.get("ancast_Comprehensive")),
            fmt(s.get("judge_mean"))))
    if any("judge" in s for s in out["summary"].values()):
        langs = [l for l, s in out["summary"].items() if "judge" in s]
        lines += ["", "## umrjudge per check", "", "| check | " + " | ".join(langs) + " |", "|---|" + "---|" * len(langs)]
        for k in sorted({k for l in langs for k in out["summary"][l]["judge"]}):
            lines.append("| %s | %s |" % (k, " | ".join(fmt(out["summary"][l]["judge"].get(k)) for l in langs)))
    return "\n".join(lines) + "\n"


def verify_st():
    """The two shared-task systems, scored here, next to the overview paper's numbers."""
    need_umr22()
    rows = {}
    for team in ("orange", "sema"):
        out_dir = os.path.join(RUNS, "shared-task", team)
        os.makedirs(out_dir, exist_ok=True)
        for d in DOCS:
            src = os.path.join(UMR22, "system-outputs", team, d["doc"] + ".umr")
            with open(src, encoding="utf-8") as f, open(os.path.join(out_dir, d["doc"] + ".umr"), "w", encoding="utf-8") as g:
                g.write(f.read())
        rows[team] = score_dir(out_dir, extra=True)["summary"]
    lines = ["| system | language | juːmæʧ here | paper (Table 2) | Smatch here | paper (Table 5) |", "|---|---|---|---|---|---|"]
    for team, s in rows.items():
        for lang, x in s.items():
            lines.append("| %s | %s | %.2f | %.2f | %.2f | %.2f |" % (team, lang, x["jumach_F"], 100 * PAPER[team]["jumach"][lang],
                                                               x["smatch_F"], 100 * PAPER[team]["smatch"][lang]))
    text = "\n".join(lines) + "\n"
    with open(os.path.join(RUNS, "shared-task", "verify.md"), "w", encoding="utf-8") as f:
        f.write("# The shared task's systems scored by exp/lib/score.py\n\n" + text)
    print(text)


def table():
    rows = []
    for method in ("shared-task", "api", "chat", "harness"):
        base = os.path.join(RUNS, method)
        if not os.path.isdir(base):
            continue
        subs = [""] if method == "shared-task" else SUBS
        for sub in subs:
            d = os.path.join(base, sub)
            if not os.path.isdir(d):
                continue
            for label in sorted(os.listdir(d)):
                p = os.path.join(d, label, "scores.json")
                if os.path.exists(p):
                    rows.append((method, sub or "–", label, json.load(open(p, encoding="utf-8"))["summary"]))
    lines = ["# Results", "",
             "Generated by `python3 exp/run.py table`. The test set and scoring of the DMR 2026 UMR parsing shared task: "
             "juːmæʧ (main metric) and Smatch against the official test gold (UMR 2.2), F1 over counts summed over "
             "a language's files; a missing file counts as empty. AnCast++ (mean over files) and umrjudge are extra. "
             "`shared-task` rows are the two participating systems' released outputs scored the same way.", ""]
    for lang in LANGS:
        if not any(lang in s for *_, s in rows):
            continue
        n = [d for d in ALL_DOCS if d["lang"] == lang]
        lines += ["## %s (%d files, %d sentences)" % (lang, len(n), sum(d["sents"] for d in n)), "",
                  "| method | sub-experiment | model | files | juːmæʧ F | P | R | Smatch F | valid | AnCast F | Comp | judge |",
                  "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for method, sub, label, s in rows:
            if lang in s:
                x = s[lang]
                lines.append("| %s | %s | %s | %d/%d | %s | %s | %s | %s | %d/%d | %s | %s | %s |" % (
                    method, sub, label, x["files"], x["test_files"], fmt(x["jumach_F"]), fmt(x["jumach_P"]),
                    fmt(x["jumach_R"]), fmt(x["smatch_F"]), x["valid"], x["files"], fmt(x.get("ancast_F")),
                    fmt(x.get("ancast_Comprehensive")), fmt(x.get("judge_mean"))))
        lines.append("")
    with open(os.path.join(EXP, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\n".join(lines))


def main():
    global DOCS
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["api", "chat-prompts", "chat-score", "harness-score", "score", "verify-st", "table"])
    ap.add_argument("target", nargs="?")
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--langs", default="zh,en", help="comma-separated language codes, or all")
    ap.add_argument("--docs", default="")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--label", default="")
    a = ap.parse_args()
    langs = LANGS if a.langs == "all" else a.langs.split(",")
    DOCS = [d for d in ALL_DOCS if d["lang"] in langs]
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
        answers_score(a.target, a.label or "claude-code", "harness")
    elif a.command == "score":
        score_dir(os.path.abspath(a.target))
    elif a.command == "verify-st":
        verify_st()
    else:
        table()


if __name__ == "__main__":
    main()

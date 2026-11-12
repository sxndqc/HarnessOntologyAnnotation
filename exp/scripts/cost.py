"""What the whole experiment would cost through the API: the usage measured on the sample files, scaled
to the full test set of a language.

    python3 exp/scripts/cost.py [--langs zh,en]

For each model and API sub-experiment, the usage of the sample files (runs/api/<sub>/<label>/*.trace.json)
is priced, split into its input side (input, cache writes, cache reads) and its output side (output,
thinking or reasoning included), per language, and scaled to all the test files of that language
(data/docs.json):

- output side: by the number of words (a longer document is a longer answer);
- input side: s1-abridged and s1-full, by the number of files (the system prompt with the guidelines,
  the same for every file, is most of it); every other sub-experiment, by the number of words (tool
  results grow with the document); the sentence-by-sentence ones, by the number of sentences.

An estimate from three files: take it as ±50%. Prices per million tokens (Anthropic and OpenAI price
pages, November 2026): claude-opus-5-5 input $4, 5-minute cache write $5, cache read $0.20, output $20;
gpt-6.1-sol input $2, cached input $0.10, output $10; gpt-6-astra input $10, cached $1, output $50.
"""
import argparse
import json
import os

EXP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(EXP, "runs", "api")     # the current runs; ../obsolete/exp/runs (gpt-6-astra, old prompts) is not estimated
PRICES = {  # per million tokens: input, cache write, cache read, output
    "claude-opus-5-5-v2": ("claude-opus-5-5", 4.0, 5.0, 0.20, 20.0),
    "gpt-6.1-sol-medium": ("gpt-6.1-sol", 2.0, 2.0, 0.10, 10.0),
    "gpt-6-astra-medium": ("gpt-6-astra", 10.0, 10.0, 1.00, 50.0),
}
SUBS = ["s1-abridged", "s1-full", "s2-search", "s2-propbank", "s2-gold", "s3-all", "a1-sentence-propbank",
        "a2-sentence-all"]
BY_FILES = {"s1-abridged", "s1-full"}
BY_SENTENCES = {"a1-sentence-propbank", "a2-sentence-all"}
DOCS = json.load(open(os.path.join(EXP, "data", "docs.json"), encoding="utf-8"))["docs"]


def priced(label, usage):
    _, pi, pw, pr, po = PRICES[label]
    inp = (usage.get("input_tokens", 0) * pi + usage.get("cache_creation_input_tokens", 0) * pw +
           usage.get("cache_read_input_tokens", 0) * pr) / 1e6
    return inp, usage.get("output_tokens", 0) * po / 1e6


def measured(sub, label):
    """{doc: (input $, output $)} of the sample files of a run."""
    d = os.path.join(RUNS, sub, label)
    out = {}
    if not os.path.isdir(d):
        return out
    for f in sorted(os.listdir(d)):
        if f.endswith(".trace.json"):
            t = json.load(open(os.path.join(d, f), encoding="utf-8"))
            ins = outs = 0.0
            for c in t["calls"]:
                i, o = priced(label, c["usage"])
                ins += i
                outs += o
            out[f[:-len(".trace.json")]] = (ins, outs)
    return out


def size(docs):
    rows = [d for d in DOCS if d["doc"] in docs]
    return len(rows), sum(d["sents"] for d in rows), sum(d["tokens"] for d in rows)


def estimate(langs=("zh", "en")):
    """[{label, model, sub, sample_cost, sample_docs, full: {lang: $}, total}] for every run measured."""
    rows = []
    for label, (model, *_) in PRICES.items():
        for sub in SUBS:
            m = measured(sub, label)
            if not m:
                continue
            full, sample = {}, 0.0
            for lang in langs:
                have = [d for d in m if d.startswith(lang)]
                if not have:
                    full[lang] = None
                    continue
                n_s, s_s, w_s = size(have)
                n_f, s_f, w_f = size([d["doc"] for d in DOCS if d["lang"] == lang])
                ins = sum(m[d][0] for d in have)
                outs = sum(m[d][1] for d in have)
                sample += ins + outs
                k_in = (n_f / n_s) if sub in BY_FILES else (s_f / s_s) if sub in BY_SENTENCES else (w_f / w_s)
                full[lang] = ins * k_in + outs * (w_f / w_s)
            rows.append({"label": label, "model": model, "sub": sub, "sample_cost": sample, "sample_docs": sorted(m),
                         "full": full, "total": sum(v for v in full.values() if v is not None)})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--langs", default="zh,en")
    a = ap.parse_args()
    langs = a.langs.split(",")
    rows = estimate(langs)
    for lang in langs:
        print("%s: %d files, %d sentences, %d words" % ((lang,) + size([d["doc"] for d in DOCS if d["lang"] == lang])))
    print("| model | sub-experiment | sample (3 files) | " + " | ".join("full %s" % l for l in langs) + " | full total |")
    for r in rows:
        print("| %s | %s | $%.2f | %s | $%.0f |" % (r["model"], r["sub"], r["sample_cost"], " | ".join(
            "–" if r["full"][l] is None else "$%.0f" % r["full"][l] for l in langs), r["total"]))
    for label, (model, *_) in PRICES.items():
        t = sum(r["total"] for r in rows if r["label"] == label)
        print("%s, every sub-experiment measured: $%.0f" % (model, t))


if __name__ == "__main__":
    main()

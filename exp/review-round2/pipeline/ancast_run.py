"""AnCast++ (document scope) of one file against another, cached by the contents of the two files.

    r = pair(pred_path, gold_path)
    r["doc"]    {"sent", "modal", "temporal", "coref", "comp"}   F scores, 0-100 (None when AnCast gives none)
    r["sent"]   {sentence number: {"ancast", "concept", "smatch"}}

Needs the `ancast` command (pip install ./vendor/umrancast, or pip install ancast). The per-sentence CSV it
writes also carries Smatch, so no separate Smatch run is needed. The seed is fixed (--seed 0).
"""
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading

import common as C

CACHE = os.path.join(C.ANALYSIS, ".cache", "ancast")
PATTERNS = [("sent", r"Sent Micro:.*?Fscore: ([\d.]+)%"), ("modal", r"Modality:.*?Fscore: ([\d.]+)%"),
            ("temporal", r"Temporal:.*?Fscore: ([\d.]+)%"), ("coref", r"Coref:.*?Fscore: ([\d.]+)%"),
            ("comp", r"Comprehensive Score:\s*([\d.]+)%")]
csv.field_size_limit(10 ** 9)
_lock = threading.Lock()


def _num(x):
    if x in ("", None):
        return None
    s = str(x).strip()
    try:
        v = float(s.strip("%"))
    except ValueError:
        return None
    return round(v * (100 if v <= 1 and "%" not in s else 1), 1)


def _sha(path):
    return hashlib.sha1(open(path, "rb").read()).hexdigest()


def pair(pred, gold):
    key = hashlib.sha1((_sha(pred) + _sha(gold)).encode()).hexdigest()
    cached = os.path.join(CACHE, key + ".json")
    if os.path.exists(cached):
        try:
            return json.load(open(cached, encoding="utf-8"))
        except ValueError:          # half-written by another thread: compute it again
            pass
    out_dir = tempfile.mkdtemp(prefix="ancast-")
    try:
        # AnCast pairs files by name: give both the same name
        a, b = os.path.join(out_dir, "p", "doc.umr"), os.path.join(out_dir, "g", "doc.umr")
        for src, dst in ((pred, a), (gold, b)):
            os.makedirs(os.path.dirname(dst))
            text = open(src, encoding="utf-8").read()
            # AnCast reads one span per alignment line; the Latin gold has several ("s1h: 2-2, 4-5"):
            # the copy it scores keeps the first span (the gold file itself is not changed)
            text = re.sub(r"(?m)^(s\d+\w*:\s*-?\d+--?\d+)\s*,.*$", r"\1", text)
            with open(dst, "w", encoding="utf-8") as f:
                f.write(text)
        # the copy in vendor/umrancast (one line patched: no division by zero in coref recall), not an installed one
        env = dict(os.environ, PYTHONPATH=os.path.join(C.PKG, "vendor", "umrancast"))
        r = subprocess.run([sys.executable, "-m", "ancast", "-p", a, "-g", b, "-s", "doc", "-o", os.path.join(out_dir, "o"), "--seed", "0"],
                           capture_output=True, text=True, env=env)
        log = r.stdout + r.stderr
        if r.returncode != 0:
            return {"error": log[-800:], "doc": {}, "sent": {}}
        res = {"doc": {}, "sent": {}}
        for name, pat in PATTERNS:
            m = re.search(pat, log)
            res["doc"][name] = round(float(m.group(1)), 1) if m else None
        files = [x for x in os.listdir(os.path.join(out_dir, "o")) if x.endswith(".csv")]
        for row in csv.DictReader(open(os.path.join(out_dir, "o", files[0]), encoding="utf-8")) if files else []:
            m = re.search(r"# ::\s*id (\d+)|# ::\s*snt\s*(\d+)", row.get("umr_gold") or "")
            if not m:
                continue
            res["sent"][m.group(1) or m.group(2)] = {"ancast": _num(row.get("LRM F-Score")),
                                                     "concept": _num(row.get("Concept Match F Score")),
                                                     "smatch": _num(row.get("Smatch Score"))}
    finally:
        shutil.rmtree(out_dir, ignore_errors=True)
    with _lock:
        os.makedirs(CACHE, exist_ok=True)
        tmp = "%s.%d.%d.tmp" % (cached, os.getpid(), threading.get_ident())
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(res, f)
        os.replace(tmp, cached)
    return res


def mean(xs):
    xs = [x for x in xs if x is not None]
    return round(sum(xs) / len(xs), 1) if xs else None

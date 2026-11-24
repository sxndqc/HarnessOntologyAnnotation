"""resources/guidelines-revised/: the two guidelines with the decisions of analysis/guideline-revision-checklist.md.

    python3 pipeline/revise_guidelines.py     -> resources/guidelines-revised/*.md, REPLACEMENTS.md

Step 1 (this script): the spellings and values of section 2 of the checklist, 3.1 (:includes), 3.6 (:location)
and 4.2 (the space before the slash). Every rule is (checklist item, pattern, replacement); REPLACEMENTS.md
lists how often each one applied in each file. The files in resources/guidelines/ are left as the runs of this
round read them.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402

SRC = os.path.join(C.PKG, "resources", "guidelines")
DST = os.path.join(C.PKG, "resources", "guidelines-revised")
STRENGTH = {"FullAff": "full-affirmative", "PrtAff": "partial-affirmative", "NeutAff": "neutral-affirmative",
            "FullNeg": "full-negative", "PrtNeg": "partial-negative", "NeutNeg": "neutral-negative",
            "Unsp": "unspecified"}


def low(m):
    return m.group(1) + m.group(2).lower()


RULES = [
    ("2.1", r":poss\b(?!essor)", ":possessor"),
    ("2.2", r":(?:modstr|MODSTR)\b", ":modal-strength"),
    ("2.2", r"\bmodstr:", ":modal-strength"),                       # two examples write "modstr: Aff"
    ("2.3", r"\b(%s)\b" % "|".join(STRENGTH), lambda m: STRENGTH[m.group(1)]),
    ("2.3", r"(:modal-strength )Aff\b", r"\1full-affirmative"),
    ("2.4", r":ref-(number|person)(?![a-z-])", r":refer-\1"),
    ("2.5", r"(:refer-(?:number|person) )([A-Z][A-Za-z]+)", low),
    ("2.7", r":Aspect\b", ":aspect"),
    ("2.6", r"(:aspect )([A-Z][A-Za-z]+)", low),
    ("2.8", r":quot\b", ":quote"),
    ("2.9", r"\bDCT\b", "document-creation-time"),
    ("2.9", r"\bAUTH\b", "author"),
    ("2.9", r"\bROOT\b", "root"),
    ("2.10", r"\b(PAST|PRESENT|FUTURE|Past|Present|Future)_R(?:EF|ef)\b", lambda m: m.group(1).lower() + "-reference"),
    ("2.11", r":MODAL\b", ":modal"),
    ("2.11", r":AFF\b", ":full-affirmative"),
    ("2.11", r":NEUT\b", ":neutral-affirmative"),
    ("2.12", r"\bamr-unknown\b", "umr-unknown"),
    ("2.13", r":arg(\d)", r":ARG\1"),
    ("2.14", r":(Actor|Undergoer)\b", lambda m: ":" + m.group(1).lower()),
    ("3.1", r":includes\b", ":contained"),                          # (A :includes B) = B inside A = (A :contained B)
    ("3.6", r":location\b", ":place"),
    ("4.2", r"\(([a-z][A-Za-z0-9]*)/ *(?=\S)", r"(\1 / "),
]


def main():
    os.makedirs(DST, exist_ok=True)
    log = ["# 替换清单（第 1 步：拼写、取值、斜杠空格）", "",
           "由 `python3 pipeline/revise_guidelines.py` 生成。“条目”是 analysis/guideline-revision-checklist.md 的编号；"
           "数字是这条规则在该文件里替换的次数。", ""]
    for name in ("umr_guidelines.md", "umr_guidelines_abridged.md"):
        text = open(os.path.join(SRC, name), encoding="utf-8").read()
        if name == "umr_guidelines_abridged.md":
            a, b = text.index(" Where the full guideline uses the older short names"), text.index("\n\n## 1.")
            text = text[:a] + " Both files use the names of the UMR release data\n(`author`, `document-creation-time`, " \
                "`full-affirmative`, `:modal-strength`, `:refer-person`, `performance`)." + text[b:]
        log += ["## " + name, "", "| 条目 | 模式 | 改成 | 次数 |", "|---|---|---|---|"]
        for item, pat, rep in RULES:
            text, n = re.subn(pat, rep, text)
            if n:
                shown = rep if isinstance(rep, str) else "（见脚本）"
                log.append("| %s | `%s` | `%s` | %d |" % (item, pat.replace("|", "\\|"), shown.replace("|", "\\|"), n))
        log.append("")
        open(os.path.join(DST, name), "w", encoding="utf-8").write(text)
    open(os.path.join(DST, "REPLACEMENTS.md"), "w", encoding="utf-8").write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()

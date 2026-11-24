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
import revise_guidelines2 as F  # noqa: E402

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


CONVENTIONS = """## Conventions of this revised version

This file is a local revision of the UMR 0.9 specification (August 8, 2022). The spellings follow the UMR 2.2
release data, and the points below were decided for this project; where an older passage disagrees with
them, they hold.

* Names: `:possessor`, `:modal-strength` with the values `full-affirmative`, `partial-affirmative`,
  `neutral-affirmative`, `neutral-negative`, `partial-negative`, `full-negative`, `unspecified`;
  `:refer-person`, `:refer-number` and `:aspect` with lower-case values; `:quote`; the constants `author`,
  `root`, `document-creation-time`, `past-reference`, `present-reference`, `future-reference`; `umr-unknown`
  for a questioned element.
* Temporal containment is always written `:contained`: `(A :contained B)` says that B lies inside A.
  `:contains` and `:includes` are not used.
* Part and whole: with the part as the parent the relation is `:part-of`, `(s / string :part-of (g / guitar))`;
  with the whole as the parent it is `:part`, `(g / guitar :part (s / string))`.
* Organizational roles are `have-org-role-92` and kinship or other personal relations `have-rel-role-92`
  (not -91).
* A measure word or classifier is always kept as `:unit`.
* A place is `:place` (not `:location`). A time is `:temporal`; `:time` is only the clock time inside a
  `date-entity`.
* `:cause` is what brings an event about (its cause); `:reason` is the motive or justification given for it.
* `:degree` is an intensifier or downtoner of a property (`very`, `somewhat`); `:extent` is how far or how much
  an event or state reaches (a measure or amount).
* `:modpred` is not used. An event under the scope of a modal or other complement-taking event is linked to it
  in the document-level modal dependency: `(s1w :unspecified s1v)`, or with the strength the modal event gives.
* `:subset-of` is written member (or subset) first: `(s2p :subset-of s1p)` says that s2p is one of, or a part
  of, s1p.
* A person can be `person` or `individual-person`, and a place name can have an AMR type (`city`, `state`,
  `country`) or a UMR type (`human-settlement`, `country-partition`): both are accepted.
* The examples carry no `:wiki`.
* Variables are written `s1x`: `s` and the sentence number, then the variable's letter.

"""

FULL = [    # (checklist item, old, new) applied to the full guideline after the reformatting
    ("5.4", "# Uniform Meaning Representation (UMR) 0.9 Specification\n=======================================================\n\n**August 8, 2022**\n\n-AUTHORS-\n",
     "# Uniform Meaning Representation (UMR) guidelines, local revised version\n\n" + CONVENTIONS),
    ("3.2", "UMR uses `:possessor` and `:part` relations with the possessum or part as the parent and the possessor or whole as the daughter, as in (1).",
     "UMR uses the `:possessor` and `:part-of` relations with the possessum or part as the parent and the possessor or whole as the daughter, as in (1). When the whole is the parent and the part the daughter, the relation is `:part`."),
    ("3.2", "**:possessor**, **:part**, or", "**:possessor**, **:part-of** (the part is the parent; **:part** when the whole is the parent), or"),
    ("3.10", "##### Part 4-3-1-2. modpred relation", "##### Part 4-3-1-2. Events under the scope of a modal event"),
    ("3.10", "* Part 4-3-1-2. modpred relation", "* Part 4-3-1-2. Events under the scope of a modal event"),
    ("3.10", "Events under the scope of a modal identified as its own event are only\nannotated with a `:modpred` relation to the\nrelevant modal. This is shown below in (1).",
     "Events under the scope of a modal identified as its own event get no `:modal-strength` of their own in the\nsentence-level graph. They are linked to the relevant modal event in the document-level modal dependency,\n`(modal event :strength event)`, as shown below in (1). (Earlier versions wrote a sentence-level `:modpred`\nrelation for this; it is no longer used.)"),
    ("3.10", "Events that are linked with a `:modpred` relation in the sentence-level modal annotation should also be linked in the temporal dependency.",
     "Events that are linked to a complement-taking predicate in the modal dependency should also be linked in the temporal dependency."),
    ("3.10", "There are two dependency\nrelations: `:modpred` for the link between a\nmodal event and the event(s) that it modalizes, and\n`:quote` for the link between a reporting\nevent and the event(s) that it reports.",
     "The link between a modal event and the event(s) that it modalizes is written in the document-level modal\ndependency; `:quote` marks the link between a reporting\nevent and the event(s) that it reports."),
    ("3.10", "| Events under the scope of modals | `:modpred` relation to CPT |", "| Events under the scope of modals | child of the modal event (CPT) in the document-level modal dependency |"),
    ("3.10", "a **:modpred** rela", "a link to that modal event in the document-level modal dependency (formerly the :modpred rela"),
    ("3.11", "(s2a :subset-of s1a2)", "(s1a2 :subset-of s2a)"),
    ("3.11", "(s2a :subset-of s1a3)", "(s1a3 :subset-of s2a)"),
    ("3.8", ":time (s1s / soon", ":temporal (s1s / soon"),
    ("5.3", "Back to Table of Contents", ""),
    ("5.1", "**Table of Contents**", "## Table of Contents"),
]
ABRIDGED = [
    ("3.2", "`:part` / `:part-of`", "`:part-of` (the part is the parent: `(s / string :part-of (g / guitar))`) and `:part` (the whole is the parent)"),
    ("3.1", "`:contained` (child inside parent), `:contains`, `:depends-on`", "`:contained` (child inside parent; `:contains` is not used), `:depends-on`"),
    ("3.7", "`:instrument`, `:cause`,\n`:reason`,", "`:instrument`, `:cause` (what brings the event about),\n`:reason` (the motive or justification given for it),"),
    ("3.9", "`:frequency`, `:extent`, `:degree`,", "`:frequency`, `:extent` (how far or how much, a measure), `:degree` (intensifier or downtoner),"),
    ("3.11", "`:subset-of`, `:name`, `:wiki`,", "`:subset-of`, `:name`,"),
    ("4.9", "`(c / country :wiki \"Russia\" :name (n / name :op1 \"Russia\"))`", "`(c / country :name (n / name :op1 \"Russia\"))`"),
]


def apply(text, rules, log):
    for item, old, new in rules:
        n = text.count(old)
        text = text.replace(old, new)
        log.append("| %s | %s | %s | %d |" % (item, old[:70].replace("\n", " ").replace("|", "/"),
                                              new[:70].replace("\n", " ").replace("|", "/"), n))
    return text


def main():
    os.makedirs(DST, exist_ok=True)
    log = ["# 替换清单", "",
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
        if name == "umr_guidelines.md":
            text, counts = F.format_text(text)
            log += ["", "格式和结构（第 2 步）：", ""] + ["- %s：%d" % (k, v) for k, v in counts.items()]
            a = text.index("```")                                   # examples only: :part-of, no :modpred
            def code(m):
                b = re.sub(r":part\b(?!-)", ":part-of", m.group(0))
                return re.sub(r"\n?[ \t]*:modpred[ \t]+[A-Za-z0-9]+", "", b)
            n1, n2 = len(re.findall(r"^\s*:part\b(?!-)", text, flags=re.M)), text.count(":modpred s") + text.count(":modpred b") + text.count(":modpred w")
            text = re.sub(r"```\n.*?\n```", code, text, flags=re.S)
            text = re.sub(r"\n?[ \t]*:modpred[ \t]+[A-Za-z0-9]+(?=[\s)])", "", text)
            text = re.sub(r"(?m)^(\s+):part\b(?!-)", r"\1:part-of", text)
            text = re.sub(r"UMR uses\s+`:possessor`\s+and\s+`:part`\s+relations\s+with", "UMR uses the `:possessor` and `:part-of` relations with", text)
            text = text.replace("the possessor or whole as the daughter, as in (1).", "the possessor or whole as the daughter, as in (1). When the whole is the parent and the part the daughter, the relation is `:part`.")
            log += ["- 示例里 `:part` 改 `:part-of`（3.2，都是部分为父节点）：%d" % n1, "- 示例里删掉 `:modpred`（3.10）：%d" % n2,
                    "", "内容改写（第 3 步）：", "", "| 条目 | 原文（开头） | 改成（开头） | 次数 |", "|---|---|---|---|"]
            text = apply(text, FULL, log)
            # 5.1: the table of contents written again from the headings
            body = re.sub(r"```.*?```", "", text, flags=re.S)
            heads = [(len(m.group(1)), m.group(2)) for m in re.finditer(r"(?m)^(#{2,6}) (Part .*)$", body)]
            toc = "\n".join("    " * (lvl - 2) + "* " + t for lvl, t in heads)
            a = text.index("## Table of Contents")
            b = text.index("\n## ", a + 5)
            text = text[:a] + "## Table of Contents\n\n" + toc + "\n" + text[b:]
            log += ["", "- 目录按正文标题重新生成（5.1）：%d 项" % len(heads)]
            text = re.sub(r"\n{3,}", "\n\n", text)
        else:
            log += ["", "内容改写（第 3 步）：", "", "| 条目 | 原文（开头） | 改成（开头） | 次数 |", "|---|---|---|---|"]
            text = apply(text, ABRIDGED, log)
        log.append("")
        open(os.path.join(DST, name), "w", encoding="utf-8").write(text)
    open(os.path.join(DST, "REPLACEMENTS.md"), "w", encoding="utf-8").write("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()

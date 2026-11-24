"""Step 2 of the guideline revision (structure and example format); called by pipeline/revise_guidelines.py.

    format_text(text) -> (text, counts)

Checklist items: 4.1 variables s1x, 4.4 side-by-side examples one under the other, 4.5 indentation, 4.6 glosses
out of the graphs, 4.7 no HTML, 4.8 example numbers as plain lines, 4.9 no :wiki in the examples, 5.1/5.2
headings, 5.3 links as plain text.
"""
import collections
import html
import re
from html.parser import HTMLParser

import penman

N = collections.Counter()
VAR_OK = re.compile(r"^s\d+[a-z]")


# ----------------------------------------------------------------- examples (inside ``` fences)

def split_side_by_side(lines):
    """Two graphs printed next to each other (a run of tabs between them) -> one under the other."""
    gap = re.compile(r"^(.*?\S)[ ]*\t{2,}[ \t]*(\S.*)$")
    wide = [bool(gap.match(l)) for l in lines]
    if sum(wide) < 3:
        return lines
    first = wide.index(True)
    head, left, right = lines[:first], [], []
    for l in lines[first:]:
        m = gap.match(l)
        if m:
            left.append(m.group(1))
            r = re.sub(r"^Or\b[ \t]*", "", m.group(2))
            if r:
                right.append(r)
        elif re.match(r"^\s*\t{4,}\s*\S", l):
            right.append(l.strip())
        elif l.strip():
            left.append(l)
    N["side-by-side examples split (4.4)"] += 1
    return head + left + ["", "Or:"] + right


def graph_spans(lines):
    """[(first line, last line)] of the bracketed graphs of a block (a line that opens with "(" up to the line
    where its brackets close)."""
    spans, k = [], 0
    while k < len(lines):
        if lines[k].lstrip().startswith("("):
            depth, j = 0, k
            while j < len(lines):
                s = re.sub(r'"[^"]*"', '""', lines[j])
                depth += s.count("(") - s.count(")")
                if depth <= 0:
                    break
                j += 1
            if j < len(lines) and depth == 0:
                spans.append((k, j))
                k = j + 1
                continue
        k += 1
    return spans


def fix_graph(text, number):
    """One example graph: glosses out, no :wiki, variables s<number>x, four-space indentation."""
    glosses = []

    def gloss(m):
        glosses.append("%s = '%s'" % (m.group(1), m.group(2)))
        return "/ " + m.group(1)
    text2 = re.sub(r"/[ \t]*([^\s()'‘’\"]+)[ \t]+['‘]([^'‘’\n]*)['’]", gloss, text)
    if glosses:
        N["glosses moved out of a graph (4.6)"] += len(glosses)
    text2, n = re.subn(r"[ \t]*:wiki[ \t]+(\"[^\"\n]*\"|-)", "", text2)
    N[":wiki removed from an example (4.9)"] += n
    top = re.match(r"\s*\(\s*([A-Za-z0-9]+)\s*/\s*([^\s()]+)", text2)
    if top and top.group(2) == "sentence":                      # the document-level graph
        text2 = re.sub(r"^(\s*\(\s*)s(\d+)(\s*/\s*sentence)", r"\1s\2s0\3", text2)
        text2 = re.sub(r":(temporal|modal|coref)\s*\(", r":\1 (", text2)
        lines = [l.expandtabs(4).rstrip() for l in text2.split("\n") if l.strip()]
        out = []
        for l in lines:
            s = l.strip()
            out.append(s if s.startswith("(s") and "sentence" in s else
                       "    " + s if s.startswith(":") else "            " + s)
        return "\n".join(out), glosses
    decl = re.findall(r"\(\s*([A-Za-z][A-Za-z0-9]*)\s*/", text2)
    todo = [v for v in dict.fromkeys(decl) if not VAR_OK.match(v)]
    if todo and len(todo) == len(set(decl)):                    # no variable has the s1x form yet
        names = "|".join(sorted(map(re.escape, todo), key=len, reverse=True))
        pre = "s%d" % number
        text2 = re.sub(r"\(\s*(%s)\s*/" % names, lambda m: "(%s%s /" % (pre, m.group(1)), text2)
        text2 = re.sub(r"(:[A-Za-z0-9-]+[ \t]+)(%s)(?=[\s)]|$)" % names, lambda m: m.group(1) + pre + m.group(2), text2)
        N["graphs with variables renamed to s1x (4.1)"] += 1
    try:
        if re.search(r"\d:\d", text2):
            raise ValueError
        new = penman.encode(penman.decode(text2), indent=4)
        if re.sub(r"\s+", "", new) != re.sub(r"\s+", "", text2):      # penman changed more than the layout
            raise ValueError
        text2 = new
        N["graphs re-indented (4.5)"] += 1
    except Exception:
        text2 = "\n".join(l.expandtabs(4).rstrip() for l in text2.split("\n"))
        N["graphs that do not parse, left as written"] += 1
    return text2, glosses


def fix_block(lines):
    lines = [re.sub(r"</?u>", "", l) for l in lines]
    lines = split_side_by_side(lines)
    spans = graph_spans(lines)
    # the sentence number of a block's graphs: that of its document-level graph, else 1
    number = 1
    for a, b in spans:
        m = re.match(r"\s*\(\s*s(\d+)(?:s0)?\s*/\s*sentence", lines[a])
        if m:
            number = int(m.group(1))
    out, k = [], 0
    for a, b in spans:
        out += [l.expandtabs(4).rstrip() for l in lines[k:a]]
        text, glosses = fix_graph("\n".join(lines[a:b + 1]), number)
        out += text.split("\n")
        if glosses:
            out.append("Glosses: " + "; ".join(dict.fromkeys(glosses)))
        k = b + 1
    out += [l.expandtabs(4).rstrip() for l in lines[k:]]
    done = []
    for l in out:                                               # what the graphs that do not parse still hold
        if re.match(r"^\s*[:(]", l):
            l2 = re.sub(r"[ \t]*:wiki[ \t]+(\"[^\"\n]*\"|-)", "", l)
            l2 = re.sub(r"(/[ \t]*[^\s()'‘’\"]+)[ \t]+['‘][^'‘’\n]*['’]", r"\1", l2)
            if l2 != l:
                N["leftover :wiki or gloss removed line by line"] += 1
                if not l2.strip():
                    continue
                l = l2
        done.append(l)
    out = done
    while out and not out[-1].strip():
        out.pop()
    return out


# ----------------------------------------------------------------- HTML, tables, headings (outside fences)

class Table(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows, self.cell, self.span, self.pre = [], None, {}, False

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.rows.append([])
        elif tag in ("td", "th"):
            self.cell = []
            a = dict(attrs)
            self.cur = (int(a.get("rowspan", 1) or 1), int(a.get("colspan", 1) or 1))
        elif tag == "br" and self.cell is not None:
            self.cell.append("; ")
        elif tag == "pre" and self.cell is not None:
            self.cell.append("`")

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None:
            text = re.sub(r"\s+", " ", "".join(self.cell)).strip().replace("` ", "`").replace(" `", "`")
            text = re.sub(r"`([^`]*)`", lambda m: "`%s`" % m.group(1).strip(), text).replace("|", "/")
            text = re.sub(r"(\S)`(\S[^`]*)`", r"\1 `\2`", text)
            self.rows[-1].append((text, self.cur))
            self.cell = None
        elif tag == "pre" and self.cell is not None:
            self.cell.append("`")

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)


def html_table(block):
    p = Table()
    p.feed(block)
    grid, carry = [], {}                                        # carry: column -> (rows left, text)
    for row in p.rows:
        out, col, cells = [], 0, list(row)
        while cells or any(c >= col for c in carry):
            if col in carry:
                left, text = carry[col]
                out.append(text)
                if left > 1:
                    carry[col] = (left - 1, text)
                else:
                    del carry[col]
                col += 1
                continue
            if not cells:
                break
            text, (rs, cs) = cells.pop(0)
            for _ in range(cs):
                out.append(text)
                if rs > 1:
                    carry[col] = (rs - 1, text)
                col += 1
        grid.append(out)
    width = max(len(r) for r in grid)
    lines = []
    for k, r in enumerate(grid):
        lines.append("| " + " | ".join(r + [""] * (width - len(r))) + " |")
        if k == 0:
            lines.append("|" + "---|" * width)
    N["HTML tables turned into Markdown tables (4.7)"] += 1
    return "\n".join(lines)


def level_of(title):
    m = re.match(r"Part (\d+(?:-\d+)*)\.", title)
    return 1 + len(m.group(1).split("-")) if m else None


def fix_prose(text):
    text = re.sub(r"<table>.*?</table>", lambda m: "\n" + html_table(m.group(0)) + "\n", text, flags=re.S)

    def anchor(m):
        if not re.match(r"\d", m.group(1)):
            return m.group(1).strip()
        N["example numbers as plain lines (4.8)"] += 1
        return "Example " + m.group(1).strip()
    text = re.sub(r"<span id=\"[^\"]*\"(?: label=\"[^\"]*\")?>\s*(.*?)\s*</span>", anchor, text)
    text, n = re.subn(r"<a\b[^>]*>(.*?)</a>", r"\1", text, flags=re.S)
    N["HTML links turned into plain text (5.3)"] += n
    text, n = re.subn(r"\[([^\]\n]+)\]\(#[^)\n]*\)", r"\1", text)
    N["Markdown links to anchors turned into plain text (5.3)"] += n
    text, n = re.subn(r"</?(?:span|div|u|br|pre)\b[^>]*>", "", text)
    N["other HTML tags removed (4.7)"] += n
    out = []
    for line in text.split("\n"):
        m = re.match(r"^\s*(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if m:
            title = re.sub(r"\s+", " ", m.group(2))
            lvl = level_of(title) or len(m.group(1))
            if line != "#" * lvl + " " + title:
                N["headings repaired (leading space, level) (5.1, 5.2)"] += 1
            out.append("#" * lvl + " " + title)
        elif line.lstrip().startswith("|") and line.rstrip().endswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.match(r"^:?-+:?$", c) for c in cells):
                out.append("|" + "---|" * len(cells))
            else:
                out.append("| " + " | ".join(re.sub(r"\s+", " ", c) for c in cells) + " |")
            if out[-1] != line:
                N["table rows with the padding squeezed out"] += 1
        else:
            out.append(line.expandtabs(4).rstrip())
    return "\n".join(out)


def format_text(text):
    N.clear()
    text = text.replace("\r\n", "\n").replace(" ", " ")
    parts, buf, inside = [], [], False
    for line in text.split("\n"):
        if line.strip().startswith("```") and (inside or line.strip() == "```" or re.match(r"^\s*```\w*\s*$", line)):
            if inside:
                parts.append(("code", buf))
            else:
                parts.append(("prose", buf))
            buf, inside = [], not inside
        else:
            buf.append(line)
    parts.append(("code" if inside else "prose", buf))
    out = []
    for kind, lines in parts:
        if kind == "prose":
            out.append(fix_prose("\n".join(lines)))
        else:
            out.append("```\n" + "\n".join(fix_block(lines)) + "\n```")
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text, collections.Counter(N)

"""umrjudge: compare a predicted .umr file with a gold one, one small question at a time.

    python judges/umrjudge.py --pred pred.umr --gold gold.umr --out out/

What gets measured is written in umrjudge.yaml; this file only reads it.

The one thing this judge does not decide by itself is which predicted node
corresponds to which gold node. AnCast decides that: MatchResolution gives
match_list01 (predicted variable -> gold variable) and match_list10 (the other
way round); a node with no counterpart maps to "NULL" + its own variable.
Everything below is built on those two dictionaries.

Variable names in the two files do not have to agree (s1a / apple can be gold's
s1x / apple), so the judge never compares variable names.
"""

import argparse
import csv
import json
import os
import re
import sys

import penman
import yaml
from ancast.matches import MatchResolution
from ancast.node import Attribute
from ancast.resource_utils import ALLOWED_TAGS, load_abt_vocab, load_reify_rels
from ancast.sentence import Sentence

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SPEC = os.path.join(HERE, "umrjudge.yaml")


def load_spec(path=DEFAULT_SPEC):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


# ------------------------------------------------------------------ reading

def read_umr(path, move_modal_strength=False):
    """{sentence index: {"index", "words", "graph", "alignment", "doc"}} from a .umr file.

    A sentence block starts with a line of #### and carries `# :: snt3`, a
    `Words:` line, a `# sentence level graph:` section, a `# alignment:`
    section (var: start-end, 1-based word positions, 0-0 = no word) and a
    `# document level annotation:` section. `doc` is that section read as
    relations, see read_doc_level.

    move_modal_strength: Chun & Xue's cleanup, the one AnCast++ is scored
    with (scripts/compare_ancast.py): a :modal-strength in the sentence graph
    leaves the graph and becomes (author :value var) in the :modal relations,
    unless that relation is already there.
    """
    with open(path, encoding="utf-8-sig") as f:
        text = f.read()
    sents = {}
    for block in re.split(r"^#{20,}\s*$", text, flags=re.M):
        found = re.search(r"#\s*::\s*snt(\d+)", block)
        if not found:
            continue
        index = int(found.group(1))
        words = re.search(r"^Words:\s*(.*)$", block, re.M)
        graph = re.search(
            r"#\s*sentence level graph:\s*\n(.*?)(?=\n\s*#\s*(?:alignment|document level annotation)|\Z)",
            block, re.S)
        alignment = re.search(r"#\s*alignment:\s*\n(.*?)(?=\n\s*#\s*document level annotation|\Z)", block, re.S)
        doc = re.search(r"#\s*document level annotation:\s*\n(.*)", block, re.S)
        graph = graph.group(1).strip() if graph else ""
        rels = read_doc_level(doc.group(1) if doc else "", index)
        if move_modal_strength:
            graph, moved = take_modal_strength(graph)
            for var, value in moved:
                if not any(r["section"] == "modal" and (r["parent"], r["relation"], r["child"]) == ("author", value, var)
                           for r in rels):
                    rels.append({"section": "modal", "parent": "author", "relation": value, "child": var,
                                 "sent": index, "from": "sentence-graph modal-strength"})
        aligned = {}
        for line in (alignment.group(1) if alignment else "").splitlines():
            a = re.match(r"\s*([^\s:]+)\s*:\s*(-?\d+)-(-?\d+)", line)
            if a:
                aligned[a.group(1)] = (int(a.group(2)), int(a.group(3)))
        sents[index] = {
            "index": index,
            "words": words.group(1).strip() if words else "",
            "graph": graph,
            "alignment": aligned,
            "doc": rels,
        }
    return sents


DOC_SECTION = re.compile(r":(temporal|modal|coref)\s*\(\s*\(")
DOC_TRIPLE = re.compile(r"\(\s*([^\s()]+)\s+:([^\s()]+)\s+([^\s()]+)\s*\)")


def read_doc_level(text, index):
    """The relations of one sentence's document-level annotation:
    [{"section": temporal | modal | coref, "parent", "relation", "child", "sent"}].
    `(s3x :before s5y)` under :temporal is parent s3x, relation before, child s5y."""
    marks = [(m.start(), m.group(1)) for m in DOC_SECTION.finditer(text)]
    rels = []
    for k, (start, section) in enumerate(marks):
        end = marks[k + 1][0] if k + 1 < len(marks) else len(text)
        for parent, relation, child in DOC_TRIPLE.findall(text[start:end]):
            rels.append({"section": section, "parent": parent, "relation": relation.lower(),
                         "child": child, "sent": index, "from": "document level"})
    return rels


def take_modal_strength(graph):
    """(the graph without :modal-strength / :modstr, [(var, value)] taken out)."""
    if not re.search(r":(modal-strength|modstr)\b", graph):
        return graph, []
    try:
        g = penman.decode(graph)
    except Exception:
        return graph, []
    keep, moved = [], []
    for s, r, t in g.triples:
        if r in (":modal-strength", ":modstr"):
            moved.append((s, str(t).strip('"')))
        else:
            keep.append((s, r, t))
    try:
        return penman.encode(penman.Graph(keep, top=g.top), indent=4), moved
    except penman.exceptions.LayoutError:   # a :modstr edge to a node: without it the graph falls apart
        return graph, []


# ------------------------------------------------------------------- graphs
# Each graph becomes plain dictionaries so the checks do not touch AnCast
# objects:
#   nodes[var] = {"var", "concept", "sense", "attrs", "type"}
#       attrs  = {role: [literal values]}      (:aspect state, :quant 3)
#   edges      = [(parent var, role, child var), ...]
# Roles are read as written: `X :ARG1-of Y` is the edge (Y, "arg1", X); every
# other role keeps its direction. Names are lower case, as in AnCast.

def invert(role):
    """(role in the file) -> (is it written from the child's side, plain role)."""
    if role.endswith("-of"):
        return True, role[:-3]
    return False, role


def read_graph(sentence):
    """Nodes and edges of a parsed ancast Sentence."""
    nodes = {}
    for var, word in sentence.var2node.items():
        nodes[var] = {"var": var, "concept": word.name, "sense": word.sense_id,
                      "attrs": {}, "type": None}
    edges = []
    seen = set()
    for word in sentence.var2node.values():
        for relations in word.relations.values():
            for r in relations:
                if id(r) in seen or not (r.tags <= ALLOWED_TAGS):
                    continue
                seen.add(id(r))
                role = r.raw_name.lower()
                if isinstance(r.child, Attribute):
                    nodes[r.focus.var]["attrs"].setdefault(role, []).append(r.child.name)
                elif isinstance(r.focus, Attribute):
                    continue
                else:
                    from_child, plain = invert(role)
                    if from_child:
                        edges.append((r.child.var, plain, r.focus.var))
                    else:
                        edges.append((r.focus.var, plain, r.child.var))
    return nodes, edges


def reentrant_edges(text):
    """Edges written as a bare reference to a node declared elsewhere.

    `(a / run :ARG0 (p / person) :ARG1 p)` has the reentrant edge (a, arg1, p).
    The edge to the first-declared occurrence is an ordinary edge.
    """
    text = re.sub(r"\(\s*([^\s()/]+)\s*/\s*", r"( \1 / ", text)
    declared = set(re.findall(r"\(\s*([^\s()/]+)\s*/", text))
    tokens = re.findall(r'\(|\)|"[^"]*"|[^\s()]+', text)
    found = set()
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "(":
            stack.append(tokens[i + 1])
            i += 4                                   # ( var / concept
            continue
        if token == ")":
            if stack:
                stack.pop()
        elif token.startswith(":") and i + 1 < len(tokens) and stack:
            target = tokens[i + 1]
            if target not in ("(", ")") and not target.startswith('"') and target in declared:
                from_child, plain = invert(token[1:].lower())
                if from_child:
                    found.add((target, plain, stack[-1]))
                else:
                    found.add((stack[-1], plain, target))
        i += 1
    return found


# --------------------------------------------------------------- node types

def type_of(node, nodes, edges, attributes_of, spec):
    """The first entry of spec['node_types'] whose condition holds."""
    for entry in spec["node_types"]:
        when = entry["when"]
        if "has_relation" in when:
            if any(parent == node["var"] and role == when["has_relation"] for parent, role, _ in edges):
                return entry["name"]
        elif "has_attribute" in when:
            if when["has_attribute"] in attributes_of:
                return entry["name"]
        elif "concept_in" in when:
            if node["concept"] in when["concept_in"]:
                return entry["name"]
        elif "concept_regex" in when:
            # against the concept as written, with its sense: AnCast splits have-org-role-91
            # into have-org-role and 91
            if re.search(when["concept_regex"], describe(node)):
                return entry["name"]
        elif "has_sense" in when:
            if (node["sense"] > 0) == bool(when["has_sense"]):
                return entry["name"]
        elif when.get("default"):
            return entry["name"]
    return "entity"


def role_group(role, spec):
    """The first role group whose pattern matches the role."""
    for group in spec["role_groups"]:
        if any(re.search(p, role) for p in group["patterns"]):
            return group["name"]
    return "other"


def build_graph(sentence, graph_text, spec):
    """A graph as the checks see it: nodes with types, edges, reentrant edges."""
    nodes, edges = read_graph(sentence)
    for node in nodes.values():
        node["type"] = type_of(node, nodes, edges, node["attrs"], spec)
    reentrant = reentrant_edges(graph_text) & set(edges)
    return {"nodes": nodes, "edges": edges, "reentrant": reentrant}


EMPTY_GRAPH = {"nodes": {}, "edges": [], "reentrant": set()}


# ----------------------------------------------------------------- matching

_resources_loaded = False


def load_ancast_resources():
    """AnCast's own evaluate() does this before parsing: abstract-role
    vocabulary (have-*-91) and the reification relations."""
    global _resources_loaded
    if not _resources_loaded:
        load_abt_vocab(global_cache=True)
        load_reify_rels(global_cache=True)
        _resources_loaded = True


def match_sentences(pred_text, gold_text, pred_words, gold_words, index, spec):
    """Parse both graphs and let AnCast match them.

    Returns a dict:
      pred, gold      graphs (see build_graph); pred is EMPTY_GRAPH when the
                      prediction cannot be parsed
      p2g, g2p        matched variables, predicted -> gold and gold -> predicted
                      (nodes with no counterpart are simply absent)
      quality         gold variable -> AnCast's Q-level of its match
      ancast          AnCast's own whole-graph scores for this sentence
      error           why the sentence could not be judged, or None
    """
    load_ancast_resources()
    pred_sentence = Sentence(sent=pred_words, semantic_text=pred_text, alignment={},
                             sent_num=index, format="umr")
    gold_sentence = Sentence(sent=gold_words, semantic_text=gold_text, alignment={},
                             sent_num=index, format="umr")
    if gold_sentence.invalid:
        return {"error": "gold graph cannot be parsed"}
    gold = build_graph(gold_sentence, gold_text, spec)
    if pred_sentence.invalid or not pred_sentence.var2node:
        return {"pred": EMPTY_GRAPH, "gold": gold, "p2g": {}, "g2p": {}, "quality": {},
                "ancast": {}, "error": None, "pred_invalid": True}
    pred = build_graph(pred_sentence, pred_text, spec)

    m = spec["match"]
    try:
        result = MatchResolution(
            pred_sentence, gold_sentence,
            Cneighbor=m["cneighbor"], sense_coefficient=m["sense_coefficient"],
            separate_1_and_2=m["separate_1_and_2"], use_alignment=m["use_alignment"],
            use_smatch_top=m["use_smatch_top"])
    except (TypeError, KeyError, IndexError, AttributeError, ValueError):
        # a malformed prediction AnCast parses but cannot match (e.g. a string as the head):
        # judged like one that cannot be parsed at all
        return {"pred": EMPTY_GRAPH, "gold": gold, "p2g": {}, "g2p": {}, "quality": {},
                "ancast": {}, "error": None, "pred_invalid": True}
    p2g = {p: g for p, g in result.match_list01.items() if not g.startswith("NULL")}
    g2p = {g: p for g, p in result.match_list10.items() if not p.startswith("NULL")}
    ancast = {
        "smatch": float(result.smatch_format_score),
        "concept_f": float(result.concept_match_fscore),
        "labeled_f": float(result.lbd_fscore),
        "unlabeled_f": float(result.ulbd_fscore),
        "weighted_labeled_f": float(result.wlbd_fscore),
    }
    return {"pred": pred, "gold": gold, "p2g": p2g, "g2p": g2p,
            "quality": dict(result.quality_list10), "ancast": ancast, "error": None}


# ------------------------------------------------------------------- checks
# A check looks at one thing and returns units:
#   {"unit": id, "gold": what gold has, "pred": what the prediction has,
#    "verdict": correct | partial | wrong | missing | extra, "detail": text}
# plus an optional "credit" when the check can say how right a unit is.
# Each check takes the match `m` from match_sentences and its own yaml entry.

def describe(node):
    """run-02, apple."""
    if node["sense"]:
        return "%s-%02d" % (node["concept"], node["sense"])
    return node["concept"]


def mk(unit_id, gold, pred, verdict, detail="", **more):
    u = {"unit": unit_id, "gold": gold, "pred": pred, "verdict": verdict, "detail": detail}
    u.update(more)
    return u


def matched_pairs(m, types):
    """(gold var, predicted var) for matched nodes whose gold type is in types."""
    return [(g, m["g2p"][g]) for g, node in m["gold"]["nodes"].items()
            if g in m["g2p"] and node["type"] in types]


def same_value(a, b, tolerance):
    """'3' and '3.0' agree; so do 'State' and 'state'."""
    a = str(a).strip().strip('"').lower()
    b = str(b).strip().strip('"').lower()
    try:
        return abs(float(a) - float(b)) <= tolerance
    except ValueError:
        return a == b


def same_values(gold_values, pred_values, tolerance):
    if len(gold_values) != len(pred_values):
        return False
    rest = list(pred_values)
    for g in gold_values:
        hit = next((p for p in rest if same_value(g, p, tolerance)), None)
        if hit is None:
            return False
        rest.remove(hit)
    return True


def node_coverage(check, m, spec):
    units = []
    for g, node in m["gold"]["nodes"].items():
        if node["type"] not in check["types"]:
            continue
        p = m["g2p"].get(g)
        if p:
            units.append(mk(g, describe(node), describe(m["pred"]["nodes"][p]), "correct",
                            "matched to %s" % p, q=m["quality"].get(g)))
        else:
            units.append(mk(g, describe(node), None, "missing", "no node in the prediction matches it"))
    for p, node in m["pred"]["nodes"].items():
        if node["type"] in check["types"] and p not in m["p2g"]:
            units.append(mk(p, None, describe(node), "extra", "matches no gold node"))
    return units


def concept_value(check, m, spec):
    units = []
    for g, p in matched_pairs(m, check["types"]):
        gold, pred = m["gold"]["nodes"][g], m["pred"]["nodes"][p]
        same = gold["concept"] == pred["concept"]
        units.append(mk(g, gold["concept"], pred["concept"], "correct" if same else "wrong",
                        "" if same else "%s -> %s" % (gold["concept"], pred["concept"]),
                        q=m["quality"].get(g)))
    return units


def sense_value(check, m, spec):
    units = []
    for g, p in matched_pairs(m, check["types"]):
        gold, pred = m["gold"]["nodes"][g], m["pred"]["nodes"][p]
        if gold["concept"] != pred["concept"]:
            continue                                  # a wrong concept is a's finding
        same = gold["sense"] == pred["sense"]
        units.append(mk(g, describe(gold), describe(pred), "correct" if same else "wrong",
                        "" if same else "%s -> %s" % (describe(gold), describe(pred)),
                        q=m["quality"].get(g)))
    return units


def attribute_value(check, m, spec):
    tolerance = spec["scoring"]["numeric_tolerance"]
    units = []
    for g, p in matched_pairs(m, check["types"]):
        gold_attrs, pred_attrs = m["gold"]["nodes"][g]["attrs"], m["pred"]["nodes"][p]["attrs"]
        if check["attributes"] == "*":
            names = sorted(set(gold_attrs) | set(pred_attrs))
            names = [n for n in names if n not in check.get("except", [])]
        else:
            names = check["attributes"]
        for name in names:
            gv, pv = gold_attrs.get(name), pred_attrs.get(name)
            unit_id = "%s:%s" % (g, name)
            if gv is not None and pv is not None:
                same = same_values(gv, pv, tolerance)
                units.append(mk(unit_id, " ".join(gv), " ".join(pv), "correct" if same else "wrong",
                                "" if same else "%s -> %s" % (" ".join(gv), " ".join(pv)),
                                q=m["quality"].get(g)))
            elif gv is not None:
                units.append(mk(unit_id, " ".join(gv), None, "missing", "the prediction has no :%s" % name))
            elif pv is not None:
                units.append(mk(unit_id, None, " ".join(pv), "extra", "gold has no :%s" % name))
    return units


def edges_of(graph, head, roles, spec, skip_reentrant):
    """(role, child) of the edges that leave head with a role in the groups."""
    out = []
    for parent, role, child in graph["edges"]:
        if parent != head or role_group(role, spec) not in roles:
            continue
        if skip_reentrant and (parent, role, child) in graph["reentrant"]:
            continue
        out.append((role, child))
    return out


def argument_set(check, m, spec):
    """How far apart are the argument sets of a matched head.

    Arguments are (role, child) pairs, with the predicted child translated to
    the gold node it matches. credit is the share of the union that agrees.
    """
    skip = check.get("skip_reentrant", False)
    gold, pred = m["gold"], m["pred"]
    units = []
    for g, p in matched_pairs(m, check["heads"]):
        G = set(edges_of(gold, g, check["roles"], spec, skip))
        P = set((role, m["p2g"].get(child, "?" + child))
                for role, child in edges_of(pred, p, check["roles"], spec, skip))
        union = G | P
        if not union:
            continue
        agree = G & P

        def name(child):
            if child in gold["nodes"]:
                return "%s/%s" % (child, describe(gold["nodes"][child]))
            return "%s/%s (not in gold)" % (child[1:], describe(pred["nodes"][child[1:]]))

        gold_children = {c for _, c in G}
        notes = []
        for role, child in sorted(G - P):
            other = [r for r, c in P if c == child]
            notes.append("%s %s: predicted as %s" % (role, name(child), other[0]) if other
                         else "missing %s %s" % (role, name(child)))
        for role, child in sorted(P - G):
            if child not in gold_children:
                notes.append("extra %s %s" % (role, name(child)))
        if G == P:
            verdict = "correct"
        elif not P:
            verdict = "missing"             # the head has arguments in gold, none predicted
        elif not G:
            verdict = "extra"               # arguments predicted where gold has none
        else:
            verdict = "wrong" if not agree else "partial"
        units.append(mk(g, "; ".join(sorted("%s %s" % (r, name(c)) for r, c in G)),
                        "; ".join(sorted("%s %s" % (r, name(c)) for r, c in P)),
                        verdict, "; ".join(notes), credit=len(agree) / len(union),
                        n_gold=len(G), n_pred=len(P), n_agree=len(agree), diff=len(G ^ P),
                        q=m["quality"].get(g)))

    if spec["scoring"]["count_arguments_of_unmatched_heads"]:
        for g, node in gold["nodes"].items():
            if g in m["g2p"] or node["type"] not in check["heads"]:
                continue
            G = edges_of(gold, g, check["roles"], spec, skip)
            if G:
                units.append(mk(g, "%d arguments" % len(G), None, "missing",
                                "the head has no match", credit=0.0, n_gold=len(G), n_pred=0,
                                n_agree=0, diff=len(G)))
        for p, node in pred["nodes"].items():
            if p in m["p2g"] or node["type"] not in check["heads"]:
                continue
            P = edges_of(pred, p, check["roles"], spec, skip)
            if P:
                units.append(mk(p, None, "%d arguments" % len(P), "extra",
                                "the head matches no gold node", credit=0.0, n_gold=0,
                                n_pred=len(P), n_agree=0, diff=len(P)))
    return units


def role_label(check, m, spec):
    """For a gold edge whose two ends both have matches and whose predicted
    counterpart exists, is the label the same? (A missing edge is d's finding.)"""
    skip = check.get("skip_reentrant", False)
    gold, pred = m["gold"], m["pred"]
    units = []
    for parent, role, child in gold["edges"]:
        if role_group(role, spec) not in check["roles"]:
            continue
        if skip and (parent, role, child) in gold["reentrant"]:
            continue
        p, c = m["g2p"].get(parent), m["g2p"].get(child)
        if p is None or c is None:
            continue
        roles = [r for a, r, b in pred["edges"]
                 if a == p and b == c and not (skip and (a, r, b) in pred["reentrant"])]
        if not roles:
            continue
        label = "%s -%s-> %s" % (parent, role, child)
        if role in roles:
            units.append(mk(label, role, role, "correct", q=m["quality"].get(parent)))
        else:
            units.append(mk(label, role, "/".join(roles), "wrong",
                            "%s -> %s" % (role, "/".join(roles)), q=m["quality"].get(parent)))
    return units


def name_of(graph, var):
    """The name tokens of a named entity: op1, op2, ... of its :name child."""
    for parent, role, child in graph["edges"]:
        if parent == var and role == "name":
            attrs = graph["nodes"][child]["attrs"]
            ops = sorted((k for k in attrs if re.fullmatch(r"op\d+", k)), key=lambda k: int(k[2:]))
            return [attrs[k][0] for k in ops]
    return None


def name_ops(check, m, spec):
    """Names are compared token by token, in order. AnCast lower-cases
    everything it reads, so a difference in capitals is not visible here."""
    units = []
    for g, p in [(g, m["g2p"][g]) for g in m["gold"]["nodes"] if g in m["g2p"]]:
        gold_ops, pred_ops = name_of(m["gold"], g), name_of(m["pred"], p)
        if gold_ops is None and pred_ops is None:
            continue
        if gold_ops is not None and pred_ops is not None:
            same = gold_ops == pred_ops
            units.append(mk(g, " ".join(gold_ops), " ".join(pred_ops), "correct" if same else "wrong",
                            "" if same else "%s -> %s" % (" ".join(gold_ops), " ".join(pred_ops))))
        elif gold_ops is not None:
            units.append(mk(g, " ".join(gold_ops), None, "missing", "the prediction has no :name"))
        else:
            units.append(mk(g, None, " ".join(pred_ops), "extra", "gold has no :name"))
    return units


def reentrancy(check, m, spec):
    """Edges that point back at a node declared elsewhere, compared in gold terms."""
    gold, pred = m["gold"], m["pred"]
    pred_in_gold = {}
    for a, role, b in pred["reentrant"]:
        key = (m["p2g"].get(a, "?" + a), role, m["p2g"].get(b, "?" + b))
        pred_in_gold[key] = (a, role, b)

    def show(graph, edge):
        a, role, b = edge
        return "%s/%s -%s-> %s/%s" % (a, describe(graph["nodes"][a]), role, b, describe(graph["nodes"][b]))

    units = []
    for edge in sorted(gold["reentrant"]):
        if edge in pred_in_gold:
            units.append(mk(show(gold, edge), show(gold, edge), show(pred, pred_in_gold[edge]), "correct"))
            continue
        a, role, b = edge
        if a not in m["g2p"] or b not in m["g2p"]:
            why = "an end of the edge has no match in the prediction"
        elif (m["g2p"][a], role, m["g2p"][b]) in pred["edges"]:
            why = "the prediction has the edge but not as a reentrancy"
        else:
            why = "the prediction has no such edge"
        units.append(mk(show(gold, edge), show(gold, edge), None, "missing", why))
    for key, edge in sorted(pred_in_gold.items()):
        if key not in gold["reentrant"]:
            units.append(mk(show(pred, edge), None, show(pred, edge), "extra", "gold has no such reentrancy"))
    return units


def char_spans(words, alignment):
    """{var: (first char, end char)} on the sentence with spaces removed, from
    1-based word alignments (0-0 = no span), and that sentence text. Gold and
    prediction may cut words differently (gold 指挥家, a prediction 指 挥 家);
    on characters they agree."""
    tokens = words.split()
    starts, k = [], 0
    for t in tokens:
        starts.append(k)
        k += len(t)
    out = {}
    for var, (a, b) in alignment.items():
        if 1 <= a <= b <= len(tokens):
            out[var] = (starts[a - 1], starts[b - 1] + len(tokens[b - 1]))
    return out, "".join(tokens)


def granularity(check, m, spec):
    """Are the nodes cut at the same words? Every distinct aligned span of
    gold (gold side) and of the prediction (prediction side) is a unit. A span
    both have is correct. Otherwise the unit says how it differs: inside a
    wider node of the other side (the prediction is too coarse: one node for
    several gold nodes), split into narrower ones (too fine), crossing
    boundaries. Words only one side has a node on, and nodes aligned to
    nothing (0-0), are not judged here (a_*_found judges whether a node is
    there at all)."""
    if "align" not in m:            # matched without the files' alignments
        return []
    gold_spans, gold_text = char_spans(m["words"]["gold"], m["align"]["gold"])
    pred_spans, pred_text = char_spans(m["words"]["pred"], m["align"]["pred"])
    if not gold_spans or not pred_spans or gold_text != pred_text:
        return []
    G, P = {}, {}
    for v, sp in gold_spans.items():
        if v in m["gold"]["nodes"]:
            G.setdefault(sp, []).append(v)
    for v, sp in pred_spans.items():
        if v in m["pred"]["nodes"]:
            P.setdefault(sp, []).append(v)

    def show(sp, vs, graph):
        return "«%s» %s" % (gold_text[sp[0]:sp[1]], "/".join(describe(graph["nodes"][v]) for v in vs))

    def relation(sp, other):
        """The spans of `other` around sp: wider, narrower, crossing."""
        wider = [o for o in other if o != sp and o[0] <= sp[0] and sp[1] <= o[1]]
        inner = [o for o in other if o != sp and sp[0] <= o[0] and o[1] <= sp[1]]
        cross = [o for o in other if o not in wider and o not in inner and o != sp
                 and o[0] < sp[1] and sp[0] < o[1]]
        return wider, inner, cross

    units = []
    for sp in sorted(G):
        g = show(sp, G[sp], m["gold"])
        if sp in P:
            units.append(mk(g, g, show(sp, P[sp], m["pred"]), "correct", pvar=P[sp][0], granularity="same"))
            continue
        wider, inner, cross = relation(sp, P)
        if wider:
            o = min(wider, key=lambda o: o[1] - o[0])
            units.append(mk(g, g, show(o, P[o], m["pred"]), "missing",
                            "inside a wider predicted node", pvar=P[o][0], granularity="too coarse"))
        elif inner:
            units.append(mk(g, g, "; ".join(show(o, P[o], m["pred"]) for o in sorted(inner)), "missing",
                            "only narrower predicted nodes", pvar=P[sorted(inner)[0]][0], granularity="too fine"))
        elif cross:
            units.append(mk(g, g, "; ".join(show(o, P[o], m["pred"]) for o in sorted(cross)), "missing",
                            "predicted nodes cross its boundary", pvar=P[sorted(cross)[0]][0],
                            granularity="boundary"))
        # nothing at all on these words: a_*_found counts that
    for sp in sorted(P):
        if sp in G:
            continue
        p = show(sp, P[sp], m["pred"])
        wider, inner, cross = relation(sp, G)
        if len(inner) >= 2:
            units.append(mk(p, "; ".join(show(o, G[o], m["gold"]) for o in sorted(inner)), p, "extra",
                            "one predicted node for %d gold nodes" % len(inner), pvar=P[sp][0],
                            granularity="too coarse"))
        elif inner:
            units.append(mk(p, show(inner[0], G[inner[0]], m["gold"]), p, "extra",
                            "wider than the gold node", pvar=P[sp][0], granularity="too coarse"))
        elif wider:
            o = min(wider, key=lambda o: o[1] - o[0])
            units.append(mk(p, show(o, G[o], m["gold"]), p, "extra",
                            "part of a gold node", pvar=P[sp][0], granularity="too fine"))
        elif cross:
            units.append(mk(p, "; ".join(show(o, G[o], m["gold"]) for o in sorted(cross)), p, "extra",
                            "crosses gold nodes' boundaries", pvar=P[sp][0], granularity="boundary"))
        # nothing in gold on these words: gold aligns names and pronouns to 0-0,
        # so that is often only a missing alignment; a_*_found counts real extras
    return units


KINDS = {
    "granularity": granularity,
    "node_coverage": node_coverage,
    "concept_value": concept_value,
    "sense_value": sense_value,
    "attribute_value": attribute_value,
    "argument_set": argument_set,
    "role_label": role_label,
    "name_ops": name_ops,
    "reentrancy": reentrancy,
}


def run_checks(m, spec):
    """Every check in the yaml, over one matched sentence."""
    units = []
    for check in spec["checks"]:
        if check.get("level") == "document":
            continue
        if check["kind"] not in KINDS:
            raise ValueError("check %s: unknown kind %s" % (check["id"], check["kind"]))
        for u in KINDS[check["kind"]](check, m, spec):
            u["check"], u["module"] = check["id"], check["module"]
            if "pvar" not in u:
                u["pvar"] = predicted_var(u, m)
            units.append(u)
    return units


def predicted_var(u, m):
    """The predicted variable a unit is about, for tracing it to a skill: an
    extra unit is named by its predicted variable, the others by a gold
    variable (s3x, s3x:aspect, "s3x -arg0-> s3y"), whose match it is."""
    base = re.split(r"[: ]", str(u["unit"]))[0]
    if u["verdict"] == "extra":
        return base if base in m["pred"]["nodes"] else None
    return m["g2p"].get(base)


# --------------------------------------------------------- document level
# Temporal, modal and coreference relations link nodes of different sentences,
# and variable names do not agree between the two files. So every predicted
# variable is first turned into the gold variable AnCast matched it to in its
# own sentence (the same matching as above; AnCast++ scores the document level
# the same way). A predicted node with no match stays itself, marked with "?".
# Constants (author, document-creation-time, root, ...) are the same on both
# sides. Every unit says, for each node, its concept and the words it is
# aligned to, so a wrong relation can be found in the sentence.

def is_var(x):
    return re.match(r"^s\d+[a-z]", x) is not None


def sent_of(x, default):
    found = re.match(r"^\??s(\d+)", x)
    return int(found.group(1)) if found else default


class DocView:
    """Both files' document-level relations in gold terms, and how to show a node."""

    def __init__(self, pred, gold, matches):
        self.p2g, self.g2p = {}, {}
        self.nodes = {"gold": {}, "pred": {}}
        for index, m in matches.items():
            self.p2g.update(m["p2g"])
            self.g2p.update(m["g2p"])
            self.nodes["gold"].update({v: (index, n) for v, n in m["gold"]["nodes"].items()})
            self.nodes["pred"].update({v: (index, n) for v, n in m["pred"]["nodes"].items()})
        self.files = {"gold": gold, "pred": pred}
        self.gold = [dict(r) for s in gold.values() for r in s["doc"]]
        self.pred = []
        for s in pred.values():
            for r in s["doc"]:
                r = dict(r, pred_parent=r["parent"], pred_child=r["child"])
                r["parent"], r["child"] = self.to_gold(r["parent"]), self.to_gold(r["child"])
                self.pred.append(r)

    def to_gold(self, x):
        if not is_var(x):
            return x
        return self.p2g.get(x, "?" + x)

    def show(self, x):
        """宣布-01 «宣布» (snt3 s3x2 = pred s3x5); a ? node is shown from the prediction."""
        if re.match(r"^\d+:", x):
            return x + " (a tree-node reference the output never turned into a variable)"
        if not is_var(x.lstrip("?")):
            return x
        side, var = ("pred", x[1:]) if x.startswith("?") else ("gold", x)
        found = self.nodes[side].get(var)
        if not found:
            return x + " (no such node in its sentence graph)"
        index, node = found
        sent = self.files[side].get(index, {})
        words = sent.get("words", "").split()
        a, b = sent.get("alignment", {}).get(var, (0, 0))
        text = " ".join(words[a - 1:b]) if 0 < a <= b <= len(words) else ""
        same = " = pred %s" % self.g2p[var] if side == "gold" and var in self.g2p else ""
        return "%s%s%s (snt%d %s%s)" % ("?" if side == "pred" else "", describe(node),
                                        " «%s»" % text if text else "", index, var, same)

    def node(self, x):
        """(sentence, node dict) of a gold variable or a ? predicted one, or None."""
        if x.startswith("?"):
            return self.nodes["pred"].get(x[1:])
        return self.nodes["gold"].get(x)

    def pred_var(self, x):
        """The predicted variable standing for x (a gold variable or ?var)."""
        if x.startswith("?"):
            return x[1:]
        return self.g2p.get(x)

    def kind_of(self, x):
        """What a parent or mention is: a constant, an event, a time expression,
        a pronoun, an implicit argument, a named entity, another entity."""
        if not is_var(x.lstrip("?")):
            return x if x in ("author", "document-creation-time", "root") else "other constant"
        found = self.node(x)
        if not found:
            return "unknown"
        node = found[1]
        if node["type"] in ("event", "abstract_event"):
            return "event"
        if node["type"] in ("date", "quantity") or node["concept"] in ("temporal-quantity",):
            return "time expression"
        if "refer-person" in node["attrs"]:
            return "pronoun"
        if node["concept"] == "implicit-argument":
            return "implicit argument"
        if node["type"] == "named_entity":
            return "named entity"
        return "entity"

    def node_state(self, x):
        """For a gold node: does the prediction have it; for a ? node: gold does not."""
        if x.startswith("?"):
            return "a predicted node that matches nothing in gold"
        if is_var(x) and x not in self.g2p:
            return "the prediction has no node for it (its sentence graph lacks it)"
        return ""


def dependency(check, doc, spec):
    """Temporal or modal dependency, one unit per child node: its parent(s) and
    relation(s) in gold and in the prediction."""
    section = check["section"]
    gold, pred, origin = {}, {}, {}
    for r in doc.gold:
        if r["section"] == section:
            gold.setdefault(r["child"], set()).add((r["parent"], r["relation"]))
            origin.setdefault(r["child"], r["sent"])
    for r in doc.pred:
        if r["section"] == section:
            pred.setdefault(r["child"], set()).add((r["parent"], r["relation"]))
            origin.setdefault(r["child"], r["sent"])
            if r["from"] != "document level":
                origin[(r["child"], r["parent"], r["relation"])] = r["from"]

    def rels(child, pairs):
        out = []
        for parent, relation in sorted(pairs):
            note = origin.get((child, parent, relation))
            out.append("%s :%s %s%s" % (doc.show(parent), relation, doc.show(child),
                                        " [from the %s]" % note if note else ""))
        return "; ".join(out)

    units = []
    for child in sorted(set(gold) | set(pred), key=lambda c: (sent_of(c, 0), c)):
        g, p = gold.get(child, set()), pred.get(child, set())
        unit = doc.show(child)
        gs, ps = rels(child, g) or None, rels(child, p) or None
        if g == p:
            u = mk(unit, gs, ps, "correct")
        elif g and p:
            if g & p:
                u = mk(unit, gs, ps, "partial", "agrees on part of the relations",
                       credit=len(g & p) / len(g | p))
            elif {a for a, _ in g} == {a for a, _ in p}:
                u = mk(unit, gs, ps, "wrong", "right parent, wrong relation")
            elif {r for _, r in g} == {r for _, r in p}:
                u = mk(unit, gs, ps, "wrong", "right relation, wrong parent")
            else:
                u = mk(unit, gs, ps, "wrong", "wrong parent and relation")
        elif g:
            u = mk(unit, gs, None, "missing",
                   doc.node_state(child) or "the prediction gives this node no %s parent" % section)
        else:
            u = mk(unit, None, ps, "extra",
                   doc.node_state(child) or "gold gives this node no %s parent" % section)
        u["sent"] = sent_of(child, origin.get(child, 0))
        u["pvar"] = doc.pred_var(child)
        u["gold_label"] = "/".join(sorted(r for _, r in g)) or "-"
        u["pred_label"] = "/".join(sorted(r for _, r in p)) or "-"
        u["parent_kind"] = "/".join(sorted({doc.kind_of(a) for a, _ in (g or p)}))
        u["pred_parent_kind"] = "/".join(sorted({doc.kind_of(a) for a, _ in p})) or "-"
        u["error"] = u["detail"].split(" (")[0] if u["verdict"] != "correct" else "correct"
        u["by"] = "+".join(sorted({origin.get((child, a, r), "document level") for a, r in p})) or "-"
        units.append(u)
    return units


def chains(pairs):
    """Equivalence classes of the linked pairs: {node: the set of its chain}."""
    chain_of = {}
    for a, b in pairs:
        ca, cb = chain_of.get(a, {a}), chain_of.get(b, {b})
        if ca is not cb:
            merged = ca | cb
            for x in merged:
                chain_of[x] = merged
    return chain_of


def coref_chain(check, doc, spec):
    """Identity coreference as chains, one unit per mention: is it linked to the
    same other mentions as in gold."""
    relations = set(check["relations"])
    gold = chains([(r["parent"], r["child"]) for r in doc.gold
                   if r["section"] == "coref" and r["relation"] in relations])
    pred = chains([(r["parent"], r["child"]) for r in doc.pred
                   if r["section"] == "coref" and r["relation"] in relations])

    units = []
    for x in sorted(set(gold) | set(pred), key=lambda c: (sent_of(c, 0), c)):
        g = gold.get(x, {x}) - {x}
        p = pred.get(x, {x}) - {x}
        here = sent_of(x, 0)

        def names(xs):
            """The mentions nearest to x (by sentence) first; a long chain is cut at 6."""
            xs = sorted(xs, key=lambda c: (abs(sent_of(c, 0) - here), sent_of(c, 0), c))
            shown = "; ".join(doc.show(c) for c in xs[:6])
            return shown + (" ... (%d mentions in all)" % len(xs) if len(xs) > 6 else "")

        unit = doc.show(x)
        gs, ps = names(g) or None, names(p) or None
        if g == p:
            u = mk(unit, gs, ps, "correct")
        elif g and p:
            both = g & p
            if both:
                detail = []
                if g - p:
                    detail.append("not linked to: " + names(g - p))
                if p - g:
                    detail.append("wrongly linked to: " + names(p - g))
                u = mk(unit, gs, ps, "partial", "; ".join(detail), credit=len(both) / len(g | p))
            else:
                u = mk(unit, gs, ps, "wrong", "linked to another chain than gold's")
        elif g:
            u = mk(unit, gs, None, "missing", doc.node_state(x) or "the prediction links it to nothing")
        else:
            u = mk(unit, None, ps, "extra", doc.node_state(x) or "gold links it to nothing")
        u["sent"] = here
        u["pvar"] = doc.pred_var(x)
        u["mention_kind"] = doc.kind_of(x)
        earlier = [here - sent_of(c, here) for c in (g or p) if sent_of(c, here) < here]
        nearest = min(earlier) if earlier else None
        window = check.get("window", 5)
        u["distance"] = ("first mention" if nearest is None else "same sentence" if nearest == 0
                         else "1-%d sentences back" % window if nearest <= window
                         else "more than %d back" % window)
        u["error"] = u["detail"].split(":")[0] if u["verdict"] != "correct" else "correct"
        units.append(u)
    return units


def relation_set(check, doc, spec):
    """Relations of the given section and names, compared one by one (e.g. subset-of)."""
    relations = set(check["relations"])

    def triples(rels):
        return {(r["parent"], r["relation"], r["child"]): r["sent"] for r in rels
                if r["section"] == check["section"] and r["relation"] in relations}

    gold, pred = triples(doc.gold), triples(doc.pred)
    units = []
    for t in sorted(set(gold) | set(pred), key=lambda t: (sent_of(t[2], 0), t)):
        text = "%s :%s %s" % (doc.show(t[0]), t[1], doc.show(t[2]))
        if t in gold and t in pred:
            u = mk(text, text, text, "correct")
        elif t in gold:
            u = mk(text, text, None, "missing", doc.node_state(t[0]) or doc.node_state(t[2]) or "")
        else:
            u = mk(text, None, text, "extra", doc.node_state(t[0]) or doc.node_state(t[2]) or "")
        u["sent"] = sent_of(t[2], gold.get(t, pred.get(t, 0)))
        units.append(u)
    return units


def doc_format(check, doc, spec):
    """Is each predicted document-level relation well formed, whatever gold
    says: both ends resolve to a node of some sentence graph or a known
    constant, no end is from a later sentence, the label belongs to its
    section, a node is not related to itself, a temporal child has one parent;
    and every sentence has (root :modal author). Units are correct or wrong."""
    labels, constants = check["labels"], set(check["constants"])
    units = []
    parents = {}
    for r in doc.pred:
        problems = []
        for x in (r["pred_parent"], r["pred_child"]):
            if re.match(r"^\d+:", x):
                problems.append("unresolved tree-node reference %s" % x)
            elif is_var(x):
                found = doc.nodes["pred"].get(x)
                if not found:
                    problems.append("%s is in no sentence graph" % x)
                elif found[0] > r["sent"]:
                    problems.append("%s is from a later sentence" % x)
            elif x not in constants:
                problems.append("unknown constant %s" % x)
        if r["relation"] not in labels.get(r["section"], []):
            problems.append(":%s is not a %s label" % (r["relation"], r["section"]))
        if r["pred_parent"] == r["pred_child"]:
            problems.append("relates a node to itself")
        if r["section"] == "temporal":
            parents.setdefault(r["pred_child"], []).append(r)
        text = "%s: %s :%s %s" % (r["section"], doc.show(r["parent"]), r["relation"], doc.show(r["child"]))
        u = mk(text, None, text, "wrong" if problems else "correct", "; ".join(problems),
               problem=problems[0].split(" ")[0] if problems else "none")
        u["sent"], u["pvar"] = r["sent"], doc.pred_var(r["child"]) if is_var(r["child"].lstrip("?")) else None
        units.append(u)
    for child, rs in parents.items():
        if len(rs) > 1:
            u = mk("temporal parents of %s" % child, None, "%d parents" % len(rs), "wrong",
                   "a temporal child has %d parents" % len(rs), problem="several")
            u["sent"], u["pvar"] = rs[0]["sent"], child
            units.append(u)
    for n in sorted(doc.files["pred"]):
        has = any(r["sent"] == n and r["section"] == "modal" and r["parent"] == "root" for r in doc.pred)
        u = mk("snt%d (root :modal author)" % n, None, "present" if has else None,
               "correct" if has else "wrong", "" if has else "no (root :modal author)",
               problem="none" if has else "root")
        u["sent"], u["pvar"] = n, None
        units.append(u)
    return units


DOC_MODULES = ("h", "i", "j", "k")

DOC_KINDS = {
    "doc_format": doc_format,
    "dependency": dependency,
    "coref_chain": coref_chain,
    "relation_set": relation_set,
}


def run_doc_checks(doc, spec):
    units = []
    for check in spec["checks"]:
        if check.get("level") != "document":
            continue
        if check["kind"] not in DOC_KINDS:
            raise ValueError("check %s: unknown kind %s" % (check["id"], check["kind"]))
        for u in DOC_KINDS[check["kind"]](check, doc, spec):
            u["check"], u["module"] = check["id"], check["module"]
            units.append(u)
    return units


# ------------------------------------------------------------------ scoring

def credit_of(unit, spec):
    """The unit's own credit if the check gave one, else the yaml table's."""
    if "credit" in unit:
        return unit["credit"]
    return spec["scoring"]["credit"][unit["verdict"]]


def score(units, spec):
    """Per check: counts, recall (gold side), precision (prediction side), F1.

    recall    = credit of the gold-side units / how many there are
    precision = credit of the prediction-side units / how many there are
    Both sides are listed in the yaml. A check with nothing to judge has None.
    """
    gold_side = spec["scoring"]["gold_side"]
    pred_side = spec["scoring"]["pred_side"]
    out = {}
    for check in spec["checks"]:
        mine = [u for u in units if u["check"] == check["id"]]
        counts = {v: sum(1 for u in mine if u["verdict"] == v)
                  for v in ("correct", "partial", "wrong", "missing", "extra")}
        g = [u for u in mine if u["verdict"] in gold_side]
        p = [u for u in mine if u["verdict"] in pred_side]
        recall = sum(credit_of(u, spec) for u in g) / len(g) if g else None
        precision = sum(credit_of(u, spec) for u in p) / len(p) if p else None
        if recall is None and precision is None:
            f1 = None
        elif recall is None or precision is None:      # a check with one side only
            f1 = precision if recall is None else recall
        elif not recall or not precision:
            f1 = 0.0
        else:
            f1 = 2 * recall * precision / (recall + precision)
        row = {"module": check["module"], "kind": check["kind"], "units": len(mine),
               "recall": recall, "precision": precision, "score": f1, **counts}
        diffs = [u["diff"] for u in mine if "diff" in u]
        if diffs:
            row["mean_argument_diff"] = sum(diffs) / len(diffs)
        out[check["id"]] = row
    return out


# ------------------------------------------------------------------ driver

def judge_file(pred_path, gold_path, spec):
    """Judge one pair of files: sentence by sentence (matched by sentence
    number), then the document-level relations through the same matching."""
    move = spec.get("cleanup", {}).get("move_modal_strength", False)
    pred, gold = read_umr(pred_path, move), read_umr(gold_path, move)
    doc = os.path.splitext(os.path.basename(gold_path))[0]
    units, sentences, matches = [], [], {}
    for index in sorted(gold):
        g = gold[index]
        p = pred.get(index, {"words": "", "graph": ""})
        m = match_sentences(p["graph"], g["graph"], p["words"], g["words"], index, spec)
        if m["error"]:
            sentences.append({"doc": doc, "sent": index, "status": m["error"]})
            continue
        m["words"] = {"gold": g["words"], "pred": p.get("words", "")}
        m["align"] = {"gold": g.get("alignment", {}), "pred": p.get("alignment", {})}
        matches[index] = m
        status = "prediction missing or unparsable" if m.get("pred_invalid") else "judged"
        sentences.append({"doc": doc, "sent": index, "status": status, **m["ancast"]})
        for u in run_checks(m, spec):
            u["doc"], u["sent"] = doc, index
            units.append(u)
    for u in run_doc_checks(DocView(pred, gold, matches), spec):
        u["doc"] = doc
        units.append(u)
    add_skills(units, pred_path, gold_path)
    return {"doc": doc, "units": units, "sentences": sentences}


def add_skills(units, pred_path, gold_path):
    """Which skill made the predicted node of each unit, when the run's
    <doc>.worktree.json sits next to the prediction: the skill whose call
    wrote that node (output_handler.provenance). A document-level relation is
    the document skill's, except a modal relation whose parent is the author:
    that is the predicate's modstr. A unit with no predicted node gets "(no predicted node)",
    a node no skill call wrote (the top `and` of several roots) "(output handler)"."""
    worktree_path = pred_path[:-4] + ".worktree.json"
    txt = gold_path[:-4] + ".txt"
    if not (os.path.exists(worktree_path) and os.path.exists(txt)):
        return
    sys.path.insert(0, os.path.join(os.path.dirname(HERE), "src"))
    from input_handler.umrinputhandler import UMRInputHandler
    from output_handler import umroutputhandler, umrrefineoutputhandler
    lang = "zh" if os.path.basename(gold_path).startswith("chinese") else "en"
    with open(worktree_path, encoding="utf-8") as f:
        worktree = json.load(f)
    refine = "final" in worktree        # umr-refine: a chain of whole graphs, not a tree of pieces
    provenance = (umrrefineoutputhandler if refine else umroutputhandler).provenance
    prov = provenance(UMRInputHandler(lang=lang).read(txt), worktree)
    for u in units:
        if u.get("module") in DOC_MODULES:
            # the author's strength of an event is the predicate's modstr (umr-refine: the
            # sentence graph's :modal-strength, from the chain step that last set it; the
            # output handler writes it); every other document-level relation is the document skill's
            author = u.get("pred_parent_kind", "-") == "author" or (
                u.get("pred_parent_kind", "-") == "-" and u.get("parent_kind") == "author")
            if u.get("module") == "i" and author:
                found = prov.get(int(u.get("sent", 0)), {}).get(u.get("pvar") or "")
                u["skill"] = (found or {}).get("modal", "generate") if refine else "predicate"
            else:
                u["skill"] = "document"
            continue
        if not u.get("pvar"):
            u["skill"] = "(no predicted node)"
            continue
        found = prov.get(int(u.get("sent", 0)), {}).get(u["pvar"])
        u["skill"] = found["skill"] if found else "(output handler)"     # e.g. the top `and` it adds


def judge_paths(pred, gold, spec):
    """Files, or two directories whose .umr files share names."""
    if os.path.isdir(gold):
        pairs = [(os.path.join(pred, name), os.path.join(gold, name))
                 for name in sorted(os.listdir(gold)) if name.endswith(".umr")]
    else:
        pairs = [(pred, gold)]
    units, sentences = [], []
    for pred_path, gold_path in pairs:
        if not os.path.exists(pred_path):
            print("no prediction for %s, skipped" % os.path.basename(gold_path), file=sys.stderr)
            continue
        result = judge_file(pred_path, gold_path, spec)
        units += result["units"]
        sentences += result["sentences"]
    docs = sorted({u["doc"] for u in units})
    summary = {"ALL": score(units, spec)}
    for doc in docs:
        summary[doc] = score([u for u in units if u["doc"] == doc], spec)
    return {"units": units, "sentences": sentences, "summary": summary}


class UMRJudge:
    """The Runner's judge: compare its output with the document's gold .umr: by
    default where src/gold.py finds it (newdata/, else olddata/gold/<lang>/), or
    <gold_dir>/<lang>/<doc_id>.umr when a gold_dir is given.

        judge = UMRJudge()
        judge(pred_path, annotation) -> {"doc", "units", "sentences", "summary"}, or None without gold
    """

    def __init__(self, gold_dir=None, spec_path=DEFAULT_SPEC):
        self.gold_dir = gold_dir
        self.spec = load_spec(spec_path)

    def __call__(self, pred_path, annotation):
        if self.gold_dir:
            gold = os.path.join(self.gold_dir, annotation.lang, annotation.doc_id + ".umr")
        else:
            import gold as where
            gold = where.path(annotation.doc_id, annotation.lang, ".umr")
        if not os.path.isfile(gold):
            return None
        result = judge_file(pred_path, gold, self.spec)
        result["summary"] = score(result["units"], self.spec)
        return result


# ------------------------------------------------------------------ output

UNIT_COLUMNS = ["doc", "sent", "module", "check", "unit", "verdict", "credit",
                "gold", "pred", "detail", "q", "pvar", "skill"]
SUMMARY_COLUMNS = ["scope", "module", "check", "kind", "units", "correct", "partial", "wrong",
                   "missing", "extra", "recall", "precision", "score", "mean_argument_diff"]


def write_csv(path, columns, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if v is None else v) for k, v in row.items()})


def write_results(result, spec, out):
    os.makedirs(out, exist_ok=True)
    for u in result["units"]:
        u["credit"] = credit_of(u, spec)
    write_csv(os.path.join(out, "units.csv"), UNIT_COLUMNS, result["units"])
    rows = [{"scope": scope, "check": check, **row}
            for scope, checks in result["summary"].items() for check, row in checks.items()]
    write_csv(os.path.join(out, "summary.csv"), SUMMARY_COLUMNS, rows)
    write_csv(os.path.join(out, "sentences.csv"),
              ["doc", "sent", "status", "smatch", "concept_f", "labeled_f", "unlabeled_f",
               "weighted_labeled_f"], result["sentences"])
    with open(os.path.join(out, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(result["summary"], f, ensure_ascii=False, indent=2)
    details = breakdowns(result["units"], spec)
    with open(os.path.join(out, "details.json"), "w", encoding="utf-8") as f:
        json.dump(details, f, ensure_ascii=False, indent=2)
    with open(os.path.join(out, "details.md"), "w", encoding="utf-8") as f:
        f.write(details_md(details))
    if any("skill" in u for u in result["units"]):
        write_csv(os.path.join(out, "by_skill.csv"), BY_SKILL_COLUMNS, by_skill(result["units"], spec))


def breakdowns(units, spec):
    """For each check with `breakdown: [field, ...]` in the yaml: its units
    grouped by each field, every group scored like a check. The check's own
    score is unchanged; this only says where it comes from. `confusion: true`
    adds gold label x predicted label counts."""
    out = {}
    for check in spec["checks"]:
        fields = check.get("breakdown")
        if not fields:
            continue
        mine = [u for u in units if u["check"] == check["id"]]
        one = {"id": check["id"], "module": check["module"], "kind": check["kind"]}
        out[check["id"]] = entry = {}
        for field in fields:
            groups = {}
            for u in mine:
                groups.setdefault(str(u.get(field, "-")), []).append(u)
            entry[field] = {k: score(v, {**spec, "checks": [one]})[check["id"]] for k, v in sorted(groups.items())}
        if check.get("confusion"):
            pairs = {}
            for u in mine:
                if u.get("gold_label", "-") != "-" and u.get("pred_label", "-") != "-":
                    key = "%s -> %s" % (u["gold_label"], u["pred_label"])
                    pairs[key] = pairs.get(key, 0) + 1
            entry["confusion"] = dict(sorted(pairs.items(), key=lambda kv: -kv[1]))
    return out


def details_md(details):
    lines = ["# umrjudge: where each score comes from", "",
             "Each check has one score (summary.csv); here its units are grouped. units = how many,",
             "recall / precision / score as for the check, over that group only.", ""]
    for check, entry in details.items():
        lines += ["## " + check, ""]
        for field, groups in entry.items():
            if field == "confusion":
                lines += ["gold label -> predicted label (both present):", ""]
                lines += ["- %s: %d" % (k, v) for k, v in groups.items()]
                lines.append("")
                continue
            lines += ["by %s:" % field, "", "| %s | units | correct | partial | wrong | missing | extra | recall | precision | score |" % field,
                      "|---|---|---|---|---|---|---|---|---|---|"]
            for k, r in groups.items():
                def f(x):
                    return "-" if x is None else "%.3f" % x
                lines.append("| %s | %d | %d | %d | %d | %d | %d | %s | %s | %s |" % (
                    k, r["units"], r["correct"], r["partial"], r["wrong"], r["missing"], r["extra"],
                    f(r["recall"]), f(r["precision"]), f(r["score"])))
            lines.append("")
    return "\n".join(lines) + "\n"


BY_SKILL_COLUMNS = ["skill", "check", "units", "correct", "partial", "wrong", "missing", "extra", "lost"]


def by_skill(units, spec):
    """Per skill and check: the units about nodes or relations that skill
    wrote, and `lost` = the credit they did not get (1 - credit each): where
    the points go. Units with no predicted node are "(no predicted node)"."""
    rows = {}
    for u in units:
        key = (u.get("skill", "-"), u["check"])
        r = rows.setdefault(key, {"skill": key[0], "check": key[1], "units": 0, "correct": 0, "partial": 0,
                                  "wrong": 0, "missing": 0, "extra": 0, "lost": 0.0})
        r["units"] += 1
        r[u["verdict"]] += 1
        r["lost"] += 1 - credit_of(u, spec)
    total = {}
    for (skill, _), r in rows.items():
        t = total.setdefault(skill, {"skill": skill, "check": "ALL", "units": 0, "correct": 0, "partial": 0,
                                     "wrong": 0, "missing": 0, "extra": 0, "lost": 0.0})
        for k in ("units", "correct", "partial", "wrong", "missing", "extra", "lost"):
            t[k] += r[k]
    out = sorted(total.values(), key=lambda r: -r["lost"]) + sorted(rows.values(), key=lambda r: (r["skill"], r["check"]))
    for r in out:
        r["lost"] = round(r["lost"], 2)
    return out


def print_summary(summary):
    print("%-22s %6s %7s %7s %7s" % ("check", "units", "recall", "prec.", "score"))
    for check, row in summary["ALL"].items():
        def fmt(x):
            return "   -  " if x is None else "%6.3f" % x
        extra = "" if "mean_argument_diff" not in row else "   mean diff %.2f" % row["mean_argument_diff"]
        print("%-22s %6d %s %s %s%s" % (check, row["units"], fmt(row["recall"]),
                                        fmt(row["precision"]), fmt(row["score"]), extra))


def main():
    parser = argparse.ArgumentParser(description="Fine-grained comparison of a .umr file with a gold one.")
    parser.add_argument("--pred", required=True, help="predicted .umr file, or a directory of them")
    parser.add_argument("--gold", required=True, help="gold .umr file, or a directory of them")
    parser.add_argument("--spec", default=DEFAULT_SPEC, help="the scoring yaml")
    parser.add_argument("--out", default="umrjudge_out", help="where to write the csv and json files")
    args = parser.parse_args()
    spec = load_spec(args.spec)
    result = judge_paths(args.pred, args.gold, spec)
    write_results(result, spec, args.out)
    print_summary(result["summary"])
    print("\nwrote %s/{units,summary,sentences}.csv and summary.json" % args.out)


if __name__ == "__main__":
    main()

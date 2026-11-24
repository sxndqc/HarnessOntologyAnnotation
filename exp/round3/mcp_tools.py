"""A small MCP server (stdio, JSON-RPC, one message per line) with the two lookup tools of this round.

    python3 mcp_tools.py --tools search_guidelines,propbank_lookup --log calls.jsonl

search_guidelines searches the revised full guidelines (review-round2/resources/guidelines-revised), propbank_lookup
the PropBank frame files (review-round2/resources/propbank); the code is review-round2/tools. Every call is
appended to --log.
"""
import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
R2 = os.path.join(os.path.dirname(HERE), "review-round2")
os.environ.setdefault("SP_RESOURCES", os.path.join(R2, "resources"))
sys.path.insert(0, R2)
from tools import propbank, search  # noqa: E402

TOOLS = {
    "search_guidelines": {
        "description": "Search the full UMR guidelines. Returns the passages that contain the keywords, with their "
                       "headings; passages with more of the keywords come first. Use the terms the guidelines "
                       "would use, e.g. \"aspect\", \"modal strength\", \"have-rel-role-92\", \":quant\".",
        "inputSchema": {"type": "object", "properties": {
            "keywords": {"type": "array", "items": {"type": "string"}, "description": "terms to look for"},
            "max_results": {"type": "integer", "description": "how many passages to return, 1-10 (default 3)"}},
            "required": ["keywords"]},
        "run": lambda a: json.dumps(search.search_guidelines(a.get("keywords"), a.get("max_results", 3)), ensure_ascii=False)},
    "propbank_lookup": {
        "description": "Look up lemmas in PropBank (at most 20 per call). Returns every roleset of each lemma with its "
                       "id, its numbered roles and its examples. language is \"zh\" or \"en\".",
        "inputSchema": {"type": "object", "properties": {
            "lemmas": {"type": "array", "items": {"type": "string"}, "description": "the lemmas to look up"},
            "language": {"type": "string", "enum": ["zh", "en"]}},
            "required": ["lemmas", "language"]},
        "run": lambda a: propbank.propbank_lookup(a.get("lemmas") or [], a.get("language", ""))},
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tools", required=True)
    ap.add_argument("--log", default="")
    a = ap.parse_args()
    names = [t for t in a.tools.split(",") if t in TOOLS]
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        method, mid = msg.get("method"), msg.get("id")
        if mid is None:                     # a notification
            continue
        if method == "initialize":
            result = {"protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                      "capabilities": {"tools": {}}, "serverInfo": {"name": "umr", "version": "1"}}
        elif method == "tools/list":
            result = {"tools": [{"name": n, "description": TOOLS[n]["description"], "inputSchema": TOOLS[n]["inputSchema"]}
                                for n in names]}
        elif method == "tools/call":
            p = msg.get("params", {})
            name, args = p.get("name"), p.get("arguments") or {}
            err = False
            try:
                if name not in names:
                    raise ValueError("no tool named %s" % name)
                text = TOOLS[name]["run"](args)
            except Exception as e:
                text, err = "%s failed: %s" % (name, str(e)[:300]), True
            if a.log:
                with open(a.log, "a", encoding="utf-8") as f:
                    f.write(json.dumps({"t": round(time.time(), 1), "tool": name, "args": args, "chars": len(text),
                                        "error": err}, ensure_ascii=False) + "\n")
            result = {"content": [{"type": "text", "text": text}], "isError": err}
        elif method == "ping":
            result = {}
        else:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": "no such method"}}) + "\n")
            sys.stdout.flush()
            continue
        sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": mid, "result": result}, ensure_ascii=False) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

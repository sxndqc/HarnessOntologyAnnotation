"""The tools a skill can name in its registry entry (`tools: [...]`): function and JSON schema.

    search_guidelines    passages of the full UMR guidelines (search.py)
    propbank_lookup      PropBank rolesets, Chinese or English, of the web repo's propbank/zh.json, en.json
    search_annotations   gold UMR annotations of whole sentences: the shared task's training data (UMR 2.2
                         training-clean, training-dirty), never a sentence of a test document
"""
import json

from . import propbank, search

KEYWORDS = {"type": "array", "items": {"type": "string"}}
MAX = {"type": "integer", "description": "how many to return, 1-10 (default 3)"}

TOOLS = {
    "search_guidelines": {
        "function": search.search_guidelines,
        "schema": {
            "name": "search_guidelines",
            "description": (search.search_guidelines.__doc__ or "").strip(),
            "input_schema": {"type": "object", "properties": {"keywords": KEYWORDS, "max_results": MAX},
                             "required": ["keywords"]},
        },
    },
    "propbank_lookup": {
        "function": propbank.propbank_lookup,
        "schema": {
            "name": "propbank_lookup",
            "description": (propbank.propbank_lookup.__doc__ or "").strip(),
            "input_schema": {"type": "object", "properties": {
                "lemmas": KEYWORDS, "language": {"type": "string", "enum": ["zh", "en"]}},
                "required": ["lemmas", "language"]},
        },
    },
    "search_annotations": {
        "function": search.search_annotations,
        "schema": {
            "name": "search_annotations",
            "description": (search.search_annotations.__doc__ or "").strip(),
            "input_schema": {"type": "object", "properties": {
                "language": {"type": "string", "enum": ["zh", "en"]}, "keywords": KEYWORDS, "max_results": MAX},
                "required": ["language", "keywords"]},
        },
    },
}


def schemas(names):
    return [dict(TOOLS[n]["schema"], eager_input_streaming=True) for n in names]


def call(name, args):
    """(text of the result, is_error)."""
    if name not in TOOLS:
        return "no tool named %s" % name, True
    if not isinstance(args, dict):
        return "the tool input must be a JSON object", True
    schema = TOOLS[name]["schema"]["input_schema"]
    missing = [k for k in schema["required"] if k not in args]
    if missing:
        return "missing argument(s): %s" % ", ".join(missing), True
    args = {k: v for k, v in args.items() if k in schema["properties"]}
    try:
        out = TOOLS[name]["function"](**args)
    except Exception as e:
        return "%s failed: %s" % (name, str(e)[:300]), True
    return (out if isinstance(out, str) else json.dumps(out, ensure_ascii=False)), False

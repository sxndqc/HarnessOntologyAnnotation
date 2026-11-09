"""One skill call through the Anthropic Messages API, with its tool loop.

    answer(model, system, user, tool_names, effort, cache_dir) -> {"text", "turns", "tool_calls", "usage",
                                                                  "stop_reason", "model"}

- The key is $UMR_MODEL_KEY (as in SkillParseUMR; not ANTHROPIC_API_KEY, which Claude Code reads itself),
  sent to https://api.anthropic.com (or $UMR_API_BASE).
- Streaming (a whole document is a long answer), adaptive thinking, the given effort.
- The system prompt (skill.md before "## Input": instructions and guideline) is the same for every document
  and carries a cache breakpoint; the tool loop is covered by automatic caching (top-level cache_control).
- No server-side refusal fallback by default, so every answer comes from the model asked for (a refusal is
  recorded as stop_reason "refusal"). UMR_FALLBACKS=default turns it on (fallbacks "default"); if the API
  refuses the parameter the call is made once more without it.
- Every response is kept under cache_dir, keyed by the whole request, so a rerun asks only what changed.
"""
import hashlib
import json
import os
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import tools as T  # noqa: E402

MAX_TURNS = 40
MAX_TOKENS = 128000
_client = None
_lock = threading.Lock()
_no_fallbacks = {"set": os.environ.get("UMR_FALLBACKS", "off") != "default"}


def client():
    global _client
    with _lock:
        if _client is None:
            import anthropic
            key = os.environ.get("UMR_MODEL_KEY")
            if not key:
                raise SystemExit("UMR_MODEL_KEY is not set")
            _client = anthropic.Anthropic(api_key=key, base_url=os.environ.get("UMR_API_BASE", "https://api.anthropic.com"),
                                          max_retries=6, timeout=3600)
    return _client


def _request(model, system, messages, tool_names, effort):
    req = {
        "model": model,
        "max_tokens": MAX_TOKENS,
        "system": [{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        "messages": messages,
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": effort},
        "cache_control": {"type": "ephemeral"},
    }
    if tool_names:
        req["tools"] = T.schemas(tool_names)
    return req


def _send(req):
    import anthropic
    c = client()
    if not _no_fallbacks["set"]:
        try:
            with c.beta.messages.stream(**req, betas=["server-side-fallback-2026-07-01"], fallbacks="default") as s:
                return s.get_final_message()
        except anthropic.BadRequestError as e:
            if "fallback" not in str(e).lower():
                raise
            _no_fallbacks["set"] = True
    with c.beta.messages.stream(**req) as s:
        return s.get_final_message()


def _cached(req, cache_dir):
    key = hashlib.sha256(json.dumps(req, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    path = os.path.join(cache_dir, key[:2], key + ".json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f), True
    msg = _send(req)
    out = {"content": [b.model_dump(exclude_none=True, mode="json") for b in msg.content],
           "stop_reason": msg.stop_reason, "model": msg.model,
           "usage": msg.usage.model_dump(exclude_none=True, mode="json") if msg.usage else {}}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp%d" % threading.get_ident()
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    os.replace(tmp, path)
    return out, False


def answer(model, system, user, tool_names=(), effort="high", cache_dir=".cache/answers"):
    messages = [{"role": "user", "content": user}]
    calls, usage, cached = [], {}, 0
    out = None
    for turn in range(1, MAX_TURNS + 1):
        req = _request(model, system, messages, list(tool_names), effort)
        out, hit = _cached(req, cache_dir)
        cached += hit
        for k, v in out["usage"].items():
            if isinstance(v, int):
                usage[k] = usage.get(k, 0) + v
        if out["stop_reason"] == "refusal":
            break
        uses = [b for b in out["content"] if b.get("type") == "tool_use"]
        if out["stop_reason"] != "tool_use" or not uses:
            break
        messages.append({"role": "assistant", "content": out["content"]})
        results = []
        for b in uses:
            text, err = T.call(b["name"], b.get("input"))
            calls.append({"turn": turn, "name": b["name"], "input": b.get("input"), "chars": len(text), "error": err})
            results.append({"type": "tool_result", "tool_use_id": b["id"], "content": text, "is_error": err})
        messages.append({"role": "user", "content": results})
    text = "\n".join(b.get("text", "") for b in out["content"] if b.get("type") == "text")
    return {"text": text, "turns": turn, "tool_calls": calls, "usage": usage, "stop_reason": out["stop_reason"],
            "model": out["model"], "cached_turns": cached}

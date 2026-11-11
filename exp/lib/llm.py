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
- At most MAX_TURNS requests per answer; the last one may not call a tool (tool_choice none), so the
  model writes its answer then.
- Every response is kept under cache_dir, keyed by the whole request, so a rerun asks only what changed.
- An OpenAI model (gpt-*, o1/o3/o4*) goes through the OpenAI Responses API instead, key
  $OPENAI_API_KEY, with the same prompt (system as instructions), tools and loop, reasoning effort =
  effort; the answer is turned into the same content blocks (text, tool_use) and stop reasons, and its
  own output items (reasoning, function calls) are kept and sent back on the next turn.
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


def is_openai(model):
    return model.startswith(("gpt-", "o1", "o3", "o4"))


def _request(model, system, messages, tool_names, effort):
    if is_openai(model):
        req = {"provider": "openai", "model": model, "system": system, "messages": messages,
               "reasoning_effort": effort}
        if tool_names:
            req["tools"] = T.schemas(tool_names)
        return req
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


_openai = None


def _send_openai(req):
    """One OpenAI Responses API request for a request in this module's (Anthropic) form; the answer comes
    back in the same form: {"content": [text, tool_use blocks, and an "openai_items" block holding the
    response's own output items (reasoning, function calls) to send back on the next turn], "stop_reason",
    "model", "usage"}."""
    global _openai
    with _lock:
        if _openai is None:
            from openai import OpenAI
            _openai = OpenAI(max_retries=6, timeout=3600)
    items = []
    for m in req["messages"]:
        if isinstance(m["content"], str):
            items.append({"role": m["role"], "content": m["content"]})
        elif m["role"] == "assistant":
            items += next(b["items"] for b in m["content"] if b.get("type") == "openai_items")
        else:
            items += [{"type": "function_call_output", "call_id": b["tool_use_id"], "output": b["content"]}
                      for b in m["content"]]
    kw = {"model": req["model"], "instructions": req["system"], "input": items,
          "reasoning": {"effort": req["reasoning_effort"]}}
    if req.get("tools"):
        kw["tools"] = [{"type": "function", "name": t["name"], "description": t["description"],
                        "parameters": t["input_schema"]} for t in req["tools"]]
        if (req.get("tool_choice") or {}).get("type") == "none":
            kw["tool_choice"] = "none"
    r = _openai.responses.create(**kw)
    out_items = [o.model_dump(exclude_none=True, mode="json") for o in r.output]
    content = []
    for o in out_items:
        if o.get("type") == "message":
            text = "".join(c.get("text", "") for c in o.get("content") or [] if c.get("type") == "output_text")
            if text:
                content.append({"type": "text", "text": text})
        elif o.get("type") == "function_call":
            try:
                args = json.loads(o.get("arguments") or "{}")
            except ValueError:
                args = {"_unparsed": o.get("arguments")}
            content.append({"type": "tool_use", "id": o["call_id"], "name": o["name"], "input": args})
    content.append({"type": "openai_items", "items": out_items})
    reason = (r.incomplete_details.reason if r.incomplete_details else None)
    stop = ("tool_use" if any(b["type"] == "tool_use" for b in content) else
            "max_tokens" if reason == "max_output_tokens" else "refusal" if reason == "content_filter" else
            "end_turn" if r.status == "completed" else r.status)
    u = r.usage.model_dump(exclude_none=True) if r.usage else {}
    cached = (u.get("input_tokens_details") or {}).get("cached_tokens", 0)
    usage = {"input_tokens": u.get("input_tokens", 0) - cached, "cache_read_input_tokens": cached,
             "output_tokens": u.get("output_tokens", 0),
             "reasoning_tokens": (u.get("output_tokens_details") or {}).get("reasoning_tokens", 0),
             "openai_usage": u}
    return {"content": content, "stop_reason": stop, "model": r.model, "usage": usage, "id": r.id}


class NotCached(Exception):
    pass


def _cached(req, cache_dir, cache_only=False):
    key = hashlib.sha256(json.dumps(req, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    path = os.path.join(cache_dir, key[:2], key + ".json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f), True
    if cache_only:
        raise NotCached(key)
    if req.get("provider") == "openai":
        out = _send_openai(req)
    else:
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


def answer(model, system, user, tool_names=(), effort="high", cache_dir=".cache/answers", cache_only=False):
    """The answer, and the whole conversation: "messages" (every request's messages, each answer and tool
    result in order, the last answer included) and "responses" (stop reason, model and usage of each)."""
    messages = [{"role": "user", "content": user}]
    calls, usage, cached, responses = [], {}, 0, []
    out = None
    for turn in range(1, MAX_TURNS + 1):
        req = _request(model, system, messages, list(tool_names), effort)
        if tool_names and turn == MAX_TURNS:
            req["tool_choice"] = {"type": "none"}     # the last turn: no more lookups, write the answer
        out, hit = _cached(req, cache_dir, cache_only)
        cached += hit
        responses.append({"turn": turn, "stop_reason": out["stop_reason"], "model": out["model"], "usage": out["usage"],
                          "tool_choice": req.get("tool_choice")})
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
    if not messages or messages[-1].get("content") is not out["content"]:
        messages.append({"role": "assistant", "content": out["content"]})
    text = "\n".join(b.get("text", "") for b in out["content"] if b.get("type") == "text")
    return {"text": text, "turns": turn, "tool_calls": calls, "usage": usage, "stop_reason": out["stop_reason"],
            "model": out["model"], "cached_turns": cached, "messages": messages, "responses": responses}

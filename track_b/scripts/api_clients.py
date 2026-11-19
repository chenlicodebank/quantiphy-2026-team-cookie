#!/usr/bin/env python
"""Provider-agnostic closed-API client for the QuantiPhy Track A legs.

One call shape -- (system prompt, interleaved [text|jpeg] user content, model) --
mapped onto four transports, so a Track A leg is a `--provider/--model` pair and
nothing else in the runner changes:

  openrouter  OpenAI-compatible /chat/completions   (one key -> GPT / Gemini / Claude / Grok)
  openai      api.openai.com /v1/chat/completions   (the shape the official starter kit uses)
  gemini      generativelanguage.googleapis.com :generateContent
  anthropic   api.anthropic.com /v1/messages
  nvidia      integrate.api.nvidia.com /v1/chat/completions (build.nvidia.com API
              catalog: free developer tier, ~40 requests/minute, no credit balance)

`requests` only -- no vendor SDK, so nothing extra has to be installed on the box.

Keys resolve in this order, first hit wins:
  1. a config.yaml at the package root, `closed_api.<provider>_key`
  2. environment (OPENROUTER_API_KEY / OPENAI_API_KEY / GEMINI_API_KEY / ANTHROPIC_API_KEY /
     NVIDIA_API_KEY)

Prices are per million tokens and come from config.yaml `closed_api.prices.<model>`
(`{in:, out:, cached_in:}`) when present, else a built-in table, else
--price-in/--price-out. They only ever REPORT spend and enforce the budget cap; they
are not authoritative. Every usage record carries `cost_source`, so a stale price is
visible in the ledger instead of being silently believed.
"""
import base64
import json
import os
import random
import time

import requests

_HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_CANDIDATES = [
    # an optional config.yaml at the package root (scripts/ -> package root); else the environment
    os.path.normpath(os.path.join(_HERE, "..", "config.yaml")),
]

# USD per million tokens. VERIFY before trusting a spend number; overridable from
# config.yaml `closed_api.prices` and from --price-in/--price-out.
DEFAULT_PRICES = {
    "openai/gpt-5.1":              {"in": 1.25, "out": 10.0, "cached_in": 0.125},
    # dated ids, so a pinned reproduction of the devkit run still prices correctly
    "gpt-5.1-2025-11-13":          {"in": 1.25, "out": 10.0, "cached_in": 0.125},
    "gpt-5-2025-08-07":            {"in": 1.25, "out": 10.0, "cached_in": 0.125},
    "gpt-5-mini-2025-08-07":       {"in": 0.25, "out": 2.0,  "cached_in": 0.025},
    "openai/gpt-5":                {"in": 1.25, "out": 10.0, "cached_in": 0.125},
    "openai/gpt-5-mini":           {"in": 0.25, "out": 2.0,  "cached_in": 0.025},
    "google/gemini-3-pro":         {"in": 2.0,  "out": 12.0, "cached_in": 0.2},
    "google/gemini-2.5-pro":       {"in": 1.25, "out": 10.0, "cached_in": 0.125},
    "google/gemini-2.5-flash":     {"in": 0.30, "out": 2.5,  "cached_in": 0.03},
    "anthropic/claude-opus-4.5":   {"in": 5.0,  "out": 25.0, "cached_in": 0.5},
    "anthropic/claude-sonnet-4.5": {"in": 3.0,  "out": 15.0, "cached_in": 0.3},
}
FALLBACK_PRICE = {"in": 2.0, "out": 12.0, "cached_in": 0.2}

RETRY_STATUS = {408, 409, 429, 500, 502, 503, 504, 529}

# A 429 is normally "slow down", but these are permanent states wearing a 429:
# retrying them burns the backoff ladder on every row (~55 s each) and changes
# nothing. Seen 2026-09-14: an otherwise-valid key on an org with no credit left.
FATAL_BODY_MARKERS = ("insufficient_quota", "credit_balance_exhausted",
                      "billing_hard_limit_reached", "billing_not_active",
                      "account_deactivated")


NVIDIA_CHAT_URL = "https://integrate.api.nvidia.com/v1/chat/completions"
# GLM-5.3-Flash on NVIDIA answers a request carrying 9+ images with an in-stream
# `{"error": {"message": "Internal server error", "code": 500}}` under HTTP 200; 8 pass.
# Count, not bytes: 12 images at half size (219 kB) fail, 8 at 512 kB pass (2026-10-14).
NVIDIA_MAX_IMAGES = 8
OMITTED_IMAGE = "[earlier image not resent]"


def _last_images(messages, keep):
    """Messages with only the newest `keep` image parts; older ones become a text marker."""
    out, seen = [], 0
    for m in reversed(messages):
        c = m.get("content")
        if isinstance(c, list) and any(p.get("type") == "image_url" for p in c):
            parts = []
            for p in reversed(c):
                if p.get("type") == "image_url":
                    seen += 1
                    if seen > keep:
                        p = {"type": "text", "text": OMITTED_IMAGE}
                parts.append(p)
            m = dict(m, content=parts[::-1])
        out.append(m)
    return out[::-1]


def nvidia_body(body):
    """Rewrite an OpenRouter-shaped chat body for the NVIDIA API catalog.

    NVIDIA serves the same open weights under the same ids (`z-ai/glm-5.3-flash`) but
    rejects OpenRouter's `reasoning` block (400 "Unsupported parameter(s): `reasoning`",
    2026-10-14). It takes the flat `reasoning_effort` (GLM-5.3-Flash: low = 26 thinking
    tokens vs 198 at the default on one probe), and thinking off goes through the chat
    template, as on vLLM."""
    body = dict(body)
    body.pop("usage", None)
    body["messages"] = _last_images(body.get("messages") or [], NVIDIA_MAX_IMAGES)
    r = body.pop("reasoning", None)
    if r is not None:
        effort = r.get("effort")
        if r.get("enabled") is False or effort in ("none", "off"):
            body["chat_template_kwargs"] = dict(body.get("chat_template_kwargs") or {},
                                                enable_thinking=False)
        elif effort:
            body["reasoning_effort"] = effort
    return body


# The model lab's own endpoint for each open-weight family on OpenRouter (user ruling 2026-10-17): OpenRouter
# otherwise spreads one model over ~30 hosts at fp4 / nvfp4 / fp8, so neither the precision nor the host of a past
# answer was known. Z.AI serves GLM-5.3-Flash at fp8. A model outside this table is not pinned (served_by still
# records who answered).
OFFICIAL_PROVIDERS = {"z-ai/": "z-ai", "moonshotai/": "moonshotai", "qwen/": "alibaba"}


def openrouter_pin(body):
    """Route an OpenRouter chat body to the model lab's own endpoint only, with no fallback."""
    model = body.get("model") or ""
    for prefix, slug in OFFICIAL_PROVIDERS.items():
        if model.startswith(prefix):
            return dict(body, provider={"only": [slug], "allow_fallbacks": False})
    return body


def served_by(raw):
    """The OpenRouter provider named in a chat response (SSE stream or JSON), or None."""
    text = raw.decode(errors="replace") if isinstance(raw, bytes) else raw
    for line in text.splitlines():
        line = line[6:] if line.startswith("data: ") else line
        if '"provider"' in line:
            try:
                p = json.loads(line).get("provider")
            except ValueError:
                continue
            if p:
                return p
    return None


def chat_route(openrouter_key=None):
    """(route, url, key) for code that forwards raw /chat/completions bodies (the DSH bridges).

    QP_LLM_ROUTE picks the upstream: `openrouter` (default) or `nvidia`. On `nvidia`
    the caller passes its body through nvidia_body() and gets no per-call cost."""
    route = os.environ.get("QP_LLM_ROUTE", "openrouter").strip().lower()
    if route == "nvidia":
        return route, NVIDIA_CHAT_URL, resolve_key("nvidia")[0]
    if route != "openrouter":
        raise SystemExit("QP_LLM_ROUTE must be openrouter or nvidia, got %r" % route)
    return (route, "https://openrouter.ai/api/v1/chat/completions",
            openrouter_key or resolve_key("openrouter")[0])


def load_config():
    for p in CONFIG_CANDIDATES:
        if os.path.exists(p):
            try:
                import yaml
                with open(p, encoding="utf-8") as fh:
                    return yaml.safe_load(fh) or {}
            except Exception:
                return {}
    return {}


def resolve_key(provider, cfg=None):
    if provider == "vllm":          # a local OpenAI-compatible vLLM server (QP_VLLM_URL)
        return "EMPTY", "local vllm"
    cfg = cfg if cfg is not None else load_config()
    block = (cfg.get("closed_api") or {})
    val = block.get(provider + "_key")
    if val and not str(val).startswith("<"):
        return str(val), "config.yaml closed_api"
    env_name = {"openrouter": "OPENROUTER_API_KEY", "openai": "OPENAI_API_KEY",
                "gemini": "GEMINI_API_KEY", "anthropic": "ANTHROPIC_API_KEY",
                "nvidia": "NVIDIA_API_KEY"}[provider]
    val = os.environ.get(env_name)
    if val:
        return val, "env " + env_name
    raise SystemExit(
        "no API key for provider '%s'.\n"
        "  set config.yaml closed_api.%s_key, or export %s" % (provider, provider, env_name))


def _norm_model(model):
    """`gpt-5.1` and `openai/gpt-5.1` hit the same price row."""
    m = model.strip()
    if "/" in m:
        return m
    for pref in ("openai", "google", "anthropic", "x-ai"):
        cand = pref + "/" + m
        if cand in DEFAULT_PRICES:
            return cand
    return m


def price_for(model, cfg=None, override_in=None, override_out=None):
    if override_in is not None and override_out is not None:
        return ({"in": override_in, "out": override_out, "cached_in": override_in / 10.0},
                "--price-in/--price-out")
    cfg = cfg if cfg is not None else load_config()
    table = ((cfg.get("closed_api") or {}).get("prices") or {})
    key = _norm_model(model)
    for src, name in ((table, "config.yaml closed_api.prices"),
                      (DEFAULT_PRICES, "api_clients.DEFAULT_PRICES")):
        if model in src:
            return dict(src[model]), name
        if key in src:
            return dict(src[key]), name
    return dict(FALLBACK_PRICE), "api_clients.FALLBACK_PRICE (GUESS)"


def b64(jpeg_bytes):
    return base64.b64encode(jpeg_bytes).decode()


# ---------------------------------------------------------------------------
# content: a list of ("text", str) / ("image", jpeg_bytes) pairs, in order
# ---------------------------------------------------------------------------
def _openai_content(content, detail, cache_last_image=False):
    out = []
    for kind, val in content:
        if kind == "text":
            out.append({"type": "text", "text": val})
        else:
            img = {"url": "data:image/jpeg;base64," + b64(val)}
            if detail:
                img["detail"] = detail
            out.append({"type": "image_url", "image_url": img})
    if cache_last_image:
        # Anthropic (direct or through OpenRouter) caches nothing unless a
        # breakpoint is set; marking the LAST frame caches the whole frame prefix,
        # which is what repeats across a video's questions.
        for part in reversed(out):
            if part.get("type") == "image_url":
                part["cache_control"] = {"type": "ephemeral"}
                break
    return out


def _gemini_parts(content):
    out = []
    for kind, val in content:
        if kind == "text":
            out.append({"text": val})
        else:
            out.append({"inline_data": {"mime_type": "image/jpeg", "data": b64(val)}})
    return out


def _anthropic_content(content, cache_last_image=True):
    out = []
    for kind, val in content:
        if kind == "text":
            out.append({"type": "text", "text": val})
        else:
            out.append({"type": "image", "source": {
                "type": "base64", "media_type": "image/jpeg", "data": b64(val)}})
    if cache_last_image:
        # one breakpoint on the last frame caches the whole (system + frames)
        # prefix, which is exactly what the next question on this video re-sends
        for part in reversed(out):
            if part.get("type") == "image":
                part["cache_control"] = {"type": "ephemeral"}
                break
    return out


class _Retry(Exception):
    pass


def call_model(provider, model, system, content, key, max_tokens=100000,
               temperature=None, thinking=None, image_detail=None,
               timeout=600, max_transport_retries=5, verbose=False, extra=None):
    """One request. Returns dict(text, in_tok, out_tok, cached_in_tok, reasoning_tok,
    http_status, latency_s, error, finish_reason).

    Transport failures (429/5xx/timeout) retry with jittered backoff; a
    non-retryable error comes back as `error` rather than raising, so one bad row
    cannot kill a run whose checkpoint is the point of the exercise.
    """
    last_err = None
    for attempt in range(max_transport_retries):
        t0 = time.time()
        try:
            resp = _dispatch(provider, model, system, content, key,
                             max_tokens=max_tokens, temperature=temperature,
                             thinking=thinking, image_detail=image_detail,
                             timeout=timeout, extra=extra)
            resp["latency_s"] = round(time.time() - t0, 2)
            if resp.get("http_status") in RETRY_STATUS:
                body = str(resp.get("error") or "")
                marker = next((m for m in FATAL_BODY_MARKERS if m in body), None)
                if marker:
                    resp["error"] = "%s (not retried: %s is a permanent state)" % (
                        body[:400], marker)
                    resp["fatal"] = True
                    return resp
                last_err = "HTTP %s: %s" % (resp["http_status"], body[:300])
                raise _Retry(last_err)
            if resp.get("error") and resp.get("http_status") is None:
                last_err = str(resp["error"])[:300]
                raise _Retry(last_err)
            return resp
        except _Retry as exc:
            last_err = str(exc)
        except (requests.Timeout, requests.ConnectionError) as exc:
            last_err = "%s: %s" % (type(exc).__name__, exc)
        except Exception as exc:            # non-retryable: hand it back
            return {"text": "", "in_tok": 0, "out_tok": 0, "cached_in_tok": 0,
                    "reasoning_tok": 0, "http_status": None,
                    "latency_s": round(time.time() - t0, 2),
                    "error": "%s: %s" % (type(exc).__name__, exc)}
        if attempt < max_transport_retries - 1:
            delay = min(60.0, 3.0 * (2 ** attempt)) * (0.7 + 0.6 * random.random())
            if verbose:
                print("    transport retry %d/%d in %.1fs -- %s"
                      % (attempt + 1, max_transport_retries - 1, delay, last_err), flush=True)
            time.sleep(delay)
    return {"text": "", "in_tok": 0, "out_tok": 0, "cached_in_tok": 0,
            "reasoning_tok": 0, "http_status": None, "latency_s": 0.0,
            "error": "transport gave up after %d: %s" % (max_transport_retries, last_err)}


def _dispatch(provider, model, system, content, key, max_tokens, temperature,
              thinking, image_detail, timeout, extra=None):
    if provider in ("openrouter", "openai", "vllm", "nvidia"):
        return _call_openai_compatible(provider, model, system, content, key,
                                       max_tokens, temperature, thinking,
                                       image_detail, timeout, extra=extra)
    if provider == "gemini":
        return _call_gemini(model, system, content, key, max_tokens, temperature,
                            thinking, timeout)
    if provider == "anthropic":
        return _call_anthropic(model, system, content, key, max_tokens, temperature,
                              thinking, timeout)
    raise ValueError("unknown provider %r" % (provider,))


def _post(url, headers, payload, timeout):
    r = requests.post(url, headers=headers, data=json.dumps(payload).encode("utf-8"),
                      timeout=timeout)
    if r.status_code != 200:
        return None, {"http_status": r.status_code, "error": r.text[:2000]}
    try:
        return r.json(), None
    except Exception as exc:
        return None, {"http_status": r.status_code, "error": "bad json: %s" % exc}


def _empty(extra):
    base = {"text": "", "in_tok": 0, "out_tok": 0, "cached_in_tok": 0,
            "reasoning_tok": 0, "http_status": None, "error": None,
            "finish_reason": None}
    base.update(extra)
    return base


def _call_openai_compatible(provider, model, system, content, key, max_tokens,
                            temperature, thinking, image_detail, timeout, extra=None):
    if provider == "vllm":
        url = os.environ.get("QP_VLLM_URL", "http://127.0.0.1:8000/v1").rstrip("/") + "/chat/completions"
    elif provider == "openrouter":
        url = "https://openrouter.ai/api/v1/chat/completions"
    elif provider == "nvidia":
        url = NVIDIA_CHAT_URL
    else:
        url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    if provider == "openrouter":
        headers["HTTP-Referer"] = os.environ.get("OPENROUTER_REFERER", "https://github.com")
        headers["X-Title"] = "QuantiPhy Track A"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": _openai_content(
                content, image_detail,
                cache_last_image=model.startswith("anthropic/"))},
        ],
        # Reasoning models reject `max_tokens`; `max_completion_tokens` is the field
        # the starter kit uses and it works on both generations.
        "max_completion_tokens": max_tokens,
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if provider == "vllm":
        # vLLM's chat-template switch; the server's --reasoning-parser splits the
        # thinking into `reasoning_content`, so `content` is the answer alone
        payload["chat_template_kwargs"] = {"enable_thinking": thinking != "off"}
    elif thinking:
        # the two endpoints spell it differently: OpenRouter normalises the nested
        # `reasoning` block, api.openai.com only accepts flat `reasoning_effort`
        if provider == "openai":
            payload["reasoning_effort"] = thinking
        elif thinking == "off":
            # hybrid open models (Qwen3.x, GLM) switch their thinking mode off this way
            payload["reasoning"] = {"enabled": False}
        else:
            payload["reasoning"] = {"effort": thinking}
    if provider == "openrouter":
        payload["usage"] = {"include": True}
    if extra:
        payload.update(extra)
    if provider == "nvidia":
        payload = nvidia_body(payload)
    data, err = _post(url, headers, payload, timeout)
    if err:
        return _empty(err)
    try:
        choice = (data.get("choices") or [{}])[0]
        msg = choice.get("message") or {}
        text = msg.get("content") or ""
        if isinstance(text, list):      # some upstreams return content blocks
            text = "".join(p.get("text", "") for p in text if isinstance(p, dict))
        u = data.get("usage") or {}
        det = u.get("prompt_tokens_details") or {}
        cdet = u.get("completion_tokens_details") or {}
        return _empty({
            "text": text.strip(),
            "in_tok": int(u.get("prompt_tokens") or 0),
            "out_tok": int(u.get("completion_tokens") or 0),
            "cached_in_tok": int(det.get("cached_tokens") or 0),
            "reasoning_tok": int(cdet.get("reasoning_tokens") or 0),
            "reported_cost": u.get("cost"),
            "finish_reason": choice.get("finish_reason"),
            "http_status": 200,
        })
    except Exception as exc:
        return _empty({"http_status": 200,
                       "error": "parse: %s: %s" % (exc, str(data)[:500])})


def _call_gemini(model, system, content, key, max_tokens, temperature, thinking, timeout):
    m = model.split("/")[-1]
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           + m + ":generateContent?key=" + key)
    payload = {
        "systemInstruction": {"parts": [{"text": system}]},
        "contents": [{"role": "user", "parts": _gemini_parts(content)}],
        "generationConfig": {"maxOutputTokens": max_tokens},
    }
    if temperature is not None:
        payload["generationConfig"]["temperature"] = temperature
    if thinking:
        budget = {"minimal": 128, "low": 1024, "medium": 8192, "high": 24576}.get(thinking)
        if budget:
            payload["generationConfig"]["thinkingConfig"] = {"thinkingBudget": budget}
    data, err = _post(url, {"Content-Type": "application/json"}, payload, timeout)
    if err:
        return _empty(err)
    try:
        cands = data.get("candidates") or []
        parts = ((cands[0].get("content") or {}).get("parts") or []) if cands else []
        text = "".join(p.get("text", "") for p in parts if isinstance(p, dict))
        u = data.get("usageMetadata") or {}
        return _empty({
            "text": text.strip(),
            "in_tok": int(u.get("promptTokenCount") or 0),
            "out_tok": int(u.get("candidatesTokenCount") or 0),
            "cached_in_tok": int(u.get("cachedContentTokenCount") or 0),
            "reasoning_tok": int(u.get("thoughtsTokenCount") or 0),
            "finish_reason": cands[0].get("finishReason") if cands else None,
            "http_status": 200,
        })
    except Exception as exc:
        return _empty({"http_status": 200,
                       "error": "parse: %s: %s" % (exc, str(data)[:500])})


def _call_anthropic(model, system, content, key, max_tokens, temperature, thinking,
                    timeout):
    m = model.split("/")[-1]
    headers = {"x-api-key": key, "anthropic-version": "2023-06-01",
               "Content-Type": "application/json"}
    payload = {
        "model": m,
        "system": system,
        "messages": [{"role": "user", "content": _anthropic_content(content)}],
        "max_tokens": min(max_tokens, 32000),
    }
    if temperature is not None:
        payload["temperature"] = temperature
    if thinking:
        budget = {"minimal": 1024, "low": 2048, "medium": 8192, "high": 24576}.get(thinking)
        if budget:
            payload["thinking"] = {"type": "enabled", "budget_tokens": budget}
            payload["max_tokens"] = max(payload["max_tokens"], budget + 4096)
            payload.pop("temperature", None)     # not allowed alongside thinking
    data, err = _post("https://api.anthropic.com/v1/messages", headers, payload, timeout)
    if err:
        return _empty(err)
    try:
        blocks = data.get("content") or []
        text = "".join(b.get("text", "") for b in blocks
                       if isinstance(b, dict) and b.get("type") == "text")
        think = "".join(b.get("thinking", "") for b in blocks
                        if isinstance(b, dict) and b.get("type") == "thinking")
        u = data.get("usage") or {}
        return _empty({
            "text": text.strip(),
            "in_tok": (int(u.get("input_tokens") or 0)
                       + int(u.get("cache_read_input_tokens") or 0)
                       + int(u.get("cache_creation_input_tokens") or 0)),
            "out_tok": int(u.get("output_tokens") or 0),
            "cached_in_tok": int(u.get("cache_read_input_tokens") or 0),
            "cache_write_tok": int(u.get("cache_creation_input_tokens") or 0),
            "reasoning_tok": len(think) // 4,
            "finish_reason": data.get("stop_reason"),
            "http_status": 200,
        })
    except Exception as exc:
        return _empty({"http_status": 200,
                       "error": "parse: %s: %s" % (exc, str(data)[:500])})


def cost_of(usage, prices):
    """USD for one call. `in_tok` is normalised here to the FULL prompt count
    (cached tokens included), so the cached share bills at the cached rate and only
    the remainder at the full rate."""
    if usage.get("reported_cost") is not None:
        try:
            return float(usage["reported_cost"])
        except (TypeError, ValueError):
            pass
    cin = int(usage.get("cached_in_tok") or 0)
    cwrite = int(usage.get("cache_write_tok") or 0)
    fresh = max(0, int(usage.get("in_tok") or 0) - cin - cwrite)
    return (fresh * prices["in"]
            + cwrite * prices["in"] * 1.25          # anthropic cache-write premium
            + cin * prices.get("cached_in", prices["in"] / 10.0)
            + int(usage.get("out_tok") or 0) * prices["out"]) / 1e6


def list_models(provider, key, contains=None):
    """Discover what the account can actually reach -- model ids move faster than docs."""
    if provider == "openrouter":
        r = requests.get("https://openrouter.ai/api/v1/models",
                         headers={"Authorization": "Bearer " + key}, timeout=60)
        r.raise_for_status()
        rows = [(d["id"], (d.get("architecture") or {}).get("input_modalities"),
                 (d.get("pricing") or {}).get("prompt"),
                 (d.get("pricing") or {}).get("completion"))
                for d in r.json().get("data", [])]
    elif provider == "nvidia":
        r = requests.get(NVIDIA_CHAT_URL.rsplit("/chat/", 1)[0] + "/models",
                         headers={"Authorization": "Bearer " + key}, timeout=60)
        r.raise_for_status()
        rows = [(d["id"], None, None, None) for d in r.json().get("data", [])]
    elif provider == "openai":
        r = requests.get("https://api.openai.com/v1/models",
                         headers={"Authorization": "Bearer " + key}, timeout=60)
        r.raise_for_status()
        rows = [(d["id"], None, None, None) for d in r.json().get("data", [])]
    elif provider == "gemini":
        r = requests.get("https://generativelanguage.googleapis.com/v1beta/models?key=" + key,
                         timeout=60)
        r.raise_for_status()
        rows = [(d["name"].split("/")[-1], d.get("supportedGenerationMethods"), None, None)
                for d in r.json().get("models", [])]
    elif provider == "anthropic":
        r = requests.get("https://api.anthropic.com/v1/models",
                         headers={"x-api-key": key, "anthropic-version": "2023-06-01"},
                         timeout=60)
        r.raise_for_status()
        rows = [(d["id"], None, None, None) for d in r.json().get("data", [])]
    else:
        raise ValueError(provider)
    if contains:
        rows = [x for x in rows if contains.lower() in x[0].lower()]
    return sorted(rows)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="probe a provider: list reachable models")
    ap.add_argument("--provider", default="openrouter",
                    choices=["openrouter", "openai", "gemini", "anthropic", "nvidia"])
    ap.add_argument("--contains", default=None)
    a = ap.parse_args()
    k, src = resolve_key(a.provider)
    print("key from " + src)
    for row in list_models(a.provider, k, a.contains):
        print("  ", row)

"""Series 26 Track B (26_70+, 2026-10-20): the two-phase per-question agent on open parts only.

The Track A runner cc_agent_scene.py (Claude Code) took the Claude agent from .805 per video to .962 on its validation
videos with a question-blind scene record per video, then one fresh session per question. This is the same design on
DeepSeek Harness (MIT) driving an open-weight model through OpenRouter, reusing the dsh_coder.py bridge (sandboxed
run_python, video_frames, view_image, finish_answers, per-call cost from OpenRouter, spend caps). No Anthropic software
or model is involved at inference (method_queue 43, Decision Log 2026-10-20 "Track B harness").

Phase 1 (one session per video): the workspace holds video.mp4 and inputs.json with the video's metadata only; the
agent writes scene/ (scene.json, tracks/*.csv, notes.md, scripts/). No question, prior or depth_info is shown.
Phase 2 (one session per question, --repeats N fresh sessions each): video.mp4, a read-only copy of scene/, and
inputs.json with that question alone, its own prior, depth_info and question_fps. The answer is the median of the
repeats. Prompts are cc_agent_scene's SCENE_PROMPT / ANSWER_PROMPT with the --size-names and --real-scale conventions,
except the road-scene lane bullet (learned from a validation label; Track B code is disclosed).

    python scripts/dsh_scene.py --runtime $QP_DSH_RUNTIME --model z-ai/glm-5.3-flash --provider streamlake \
        --split val --videos simulation_0163 --out results/s26_dsh_scene_smoke --budget-usd 0.5
"""
import argparse
import json
import os
import shutil
import statistics
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from http.server import ThreadingHTTPServer
from pathlib import Path

import pandas as pd
import requests
import yaml
from deepseek_harness import DeepSeekHarness

import api_clients as A
import cc_agent_scene as S
import dsh_coder as D
import probe_lib as pl
from dsh_identity_pilot import handler
from dsh_measurement import dump, forward

ROOT = D.ROOT
LEDGER_A = ROOT / "results/s26_scene_full/ledger.csv"  # test rows (question, prior, depth_info, question_fps)

DSH_TOOLS = """Tools: video_frames shows the video (mode "sheet" with n frames, or one frame by t seconds or frame index i,
with optional crop [x0, y0, x1, y1] in pixels, scale up to 6 and a coordinate grid); run_python runs a script you write
in this folder (filename + code; numpy, scipy, opencv (cv2), PIL and av; the video is video.mp4); view_image shows an
image your script saved; finish_answers ends the session."""
DSH_RULES = """Rules: work only inside this folder; no web access; no other data. Decode frames inside your scripts as you need
them, never hold a whole high-resolution video in memory, keep scratch files small, and print summaries rather than
whole arrays."""


# --sam3-url (method_queue 54, 2026-10-22, session 432d3a13): SAM 3 segment / track as tools, served on the GH200 by
# scripts/sam3_server.py. 29_1: SAM 3's pixel speeds match Claude's own measurements on 81-91 pct of same-object pairs;
# the open agent's own colour-threshold code is where its sessions lose small or shadowed objects.
TOOLS_SAM3 = ROOT / "scripts/dsh_scene_tools.mjs"
SAM3_TOOLS = """
Segmentation tools (SAM 3, open weights): segment finds every instance of a short noun phrase on one frame and returns,
per numbered instance, its score, box, centroid and mask extents in full-resolution pixels (length_px along its main
axis, width_px across it, horiz_px, vert_px), with each mask saved as masks/*.png for your scripts and an overlay of the
numbered outlines. track follows one instance through the clip (pass the frame index i and its box from segment) and
writes tracks/*.csv per frame (frame, t_file, cx, cy, box, area, touches_border) with a linear speed and a quadratic
acceleration fit in pixels. Use these masks and tracks instead of colour thresholds you write yourself; look at the
overlay to confirm the instance is the asked object and its whole extent; when touches_border is 1 the visible-box
centre is not the object's centre. A mask holds everything SAM 3 counts as the object: if the asked dimension leaves
a part out, measure it on the mask file in your own code."""
# --depth3d (42_4, 2026-10-25, session 261cadc6; user: "if 3D is the main issue ... similar to how we use SAM ... do it"):
# Series 22's object_3d_track (dsh_depth3d.py: the 18_1 SAM 3 tracks + 19_19 Metric Video Depth Anything, rescaled by the
# object's own timed depth_info distances, lab-rig focal) as a tool of this harness, on question sessions whose lab video
# has a 3D track. With the v5r agent it won S3 on the board (c_s23s3lab_S3 +.0162 on 136 lab rows, both halves; D3 was
# noise); the DeepSeek-1017 + SAM 3 agent never had it. The paragraph is 22_6's, the track list sits in inputs.json.
TOOLS_DEPTH3D = ROOT / "scripts/dsh_scene_depth_tools.mjs"
DEPTH3D_TOOLS = """
3D tracks (lab recordings): inputs.json lists object_3d_tracks; object_3d_track(phrase, k, times) gives that tracked
object's camera-frame 3D positions from metric video depth calibrated to this question's depth_info distances, and at
the times you ask, the local 3D speed split into radial (toward or away from the camera) and transverse parts. Use it for
speeds, displacements and accelerations of objects that move in depth - a 2D pixel speed misses the radial part. First
check in a view that the track is the queried object; prefer a calibrated track (anchors present); the focal length is
a fallible lab-rig hypothesis; ignore derivatives across bounces, impacts or track jumps. Sizes and distances of static
objects still come from your own measurements."""


def _prompt(text):
    """A cc_agent_scene prompt with the DSH tool names in place of Claude Code's."""
    assert text.count(S.TOOLS) == 1 and text.count(S.RULES) == 1
    return text.replace(S.TOOLS, DSH_TOOLS).replace(S.RULES, DSH_RULES).format(
        ws="(this working directory)", video="video", py="python", tools=".")


SCENE_END = "Finish when the record is complete and checked, then reply with a one-paragraph summary of scene/notes.md.\n"
assert S.SCENE_PROMPT.count(SCENE_END) == 1
SCENE_PROMPT = _prompt(S.SCENE_PROMPT.replace(SCENE_END, (
    "Write the files with run_python. Finish when the record is complete and checked: call finish_answers with an empty "
    "answers list.\n")))

ANSWER_END = S.ANSWER_PROMPT[S.ANSWER_PROMPT.index("Finish by writing answers.json"):]
CHARACTER_NO_LANE = S.CHARACTER_NEW.split("  * A road scene's")[0]  # the lane bullet stays Track A only
assert CHARACTER_NO_LANE != S.CHARACTER_NEW and "road scene" not in CHARACTER_NO_LANE
_answer = (S.ANSWER_PROMPT.replace(S.REAL_SCALE_OLD, S.REAL_SCALE_NEW).replace(S.CHARACTER_OLD, CHARACTER_NO_LANE)
           .replace("Method:\n", S.SIZE_NAMES + S.SIZE_NAMES_FLYERS + "Method:\n", 1)
           .replace(ANSWER_END, (
               "Write notes.md with run_python (method, key measurements, the second-route check, confidence). Then call "
               "finish_answers with one answer: the question id from inputs.json, a positive number in the unit the "
               "question asks, and a short reason. Do not end your turn before finish_answers has succeeded.\n")))
ANSWER_PROMPT = _prompt(_answer)
# --physical-internet (28_6, 2026-10-22): on the dataset authors' self-filmed internet clips the reference answers sit on
# the scene's physical scale when the stated motion prior contradicts it (the Track A board read it as #196, D2 +.018 on
# 43 rows; the public VihanAggarwal repo's PHYSB probes read the same). Knowledge of how labels were made, not of any
# question's value; the threshold and standard sizes are 26_52's.
PHYSICAL_INTERNET = """- Self-filmed everyday clip (a person riding, walking or playing in a street, car park, room or court): the reference
  answers are on the scene's physical scale. Check the stated motion prior against a standard object in view (an adult
  person 1.65 m cap to soles, a basketball 24.3 cm, a table-tennis ball 4.0 cm): if the prior's scale makes that object
  more than 15 pct off its real size, take the metric scale from the standard object instead of the prior, use it for
  every length, distance and speed you report, and say so in notes.md.
"""
# --judgment-card / --self-audit (29_6, 2026-10-22, session 432d3a13): the Track A session's reading (run channel #121 /
# #123) and the 28_2 / 29_4 traces say DeepSeek loses on judgment, not tools - it picks fragile routes (hand-tuned colour
# masks that drop shadows or thin parts, deconvolving sub-10 px renders, a focal length fitted from a small far object)
# and does not check them. The card turns those choices into rules; the audit makes the first finish_answers of a
# question session return a checklist instead of saving, so the answer is checked once before it counts. Both are
# question-agnostic method guidance (our compliance rules, 2026-10-22).
JUDGMENT_CARD = """Method card (rules that hold on this benchmark's reference answers; follow them unless the video plainly rules
one out, and say so in notes.md):
- Masks: when the segment tool is available, take every object's mask from it and pick the instance on the overlay;
  hand-tune colour thresholds only if segment fails twice. A mask must hold the whole object, shadows on the object and
  thin parts (legs, tails, poles, wings, wheels) included, and nothing of the background.
- Extents: the reference answers use the full rendered extent the mask shows. Never deconvolve, shrink or sharpen edges;
  for an object under about 20 px, measure it on the frame where it is largest near the stated time.
- Motion: take positions from a track over every frame; fit a line (speed) or a parabola (acceleration) over at least 8
  frames that avoid bounces, impacts and occlusion; when the object touches the image border, use its leading or trailing
  edge, not the box centre.
- 2D scenes: one metres-per-pixel scale from the prior's object, measured the same way as the target; no focal length.
- 3D scenes: a focal length only from an object with a known size and a depth_info distance at the same time (the prior's
  object or a standard object), never from the motion of a small or far object; check it on a second reference.
- Always reproduce the prior with your own scale before measuring anything else; a scale that misses it by more than 5 pct
  is wrong.

"""
SELF_AUDIT = ("Not saved yet: check the answer once before it counts. In one short line each: (1) which object or route "
              "set the scale, and does it reproduce this question's prior within 5 pct when the prior's object is "
              "measured the same way; (2) is the measured object the one the question names, measured over its whole "
              "extent in the asked dimension; (3) is the value plausible for that kind of object at real-world scale "
              "(if not, find the error, or take the scale from a standard object and say so); (4) are times converted "
              "with question_fps; (5) recompute the final number from your measured values and units. Then call "
              "finish_answers again with the same value if every check passes, or with the corrected value.")
assert "road scene" not in ANSWER_PROMPT and "Animated characters" in ANSWER_PROMPT and "Named sizes" in ANSWER_PROMPT and "real-world" in ANSWER_PROMPT
# --readings (35_5, 2026-10-23, user: "do the context idea test"; method_queue 61, the one-session form): one session
# per question answers under every reading of the question it judges plausible and records each value, so the readings
# share one measurement and a selector can later be fitted on the labelled validation rows. Question-agnostic.
READINGS_CARD = """Readings (this run): first decide which readings of THIS question are genuinely plausible - the convention or
assumption a careful annotator could have used where the question, its prior or the video leave it open. Typical forks:
which extent a size word names (length along the body or heading vs the longest horizontal extent; 'horizontal' /
'vertical' as image axes vs the object's own axes; a box with or without attached parts such as mirrors, wings, tails,
horns or antennas); the clock (question_fps vs the file's frame rate when they differ); the scale (the prior taken
literally vs the real-world size of a standard object when the two disagree); the time window (the one-frame difference
at the asked time vs an average). Keep 1-4 readings, your default one always among them. Measure once and reuse the
measurements: compute the answer under EACH reading, then write in notes.md one fenced block

```readings
{"<short name of reading 1>": <number>, "<short name of reading 2>": <number>}
```

followed by one line `chosen: <name>` and one sentence on why; submit the chosen reading's number with finish_answers.

"""
# --readings-forks (35_6, 2026-10-23): in 35_5 the self-listed readings were mostly measurement variants (which lane
# pitch, which fit) and missed convention forks (internet_0001's file-rate clock); this card names the forks and makes
# every one that applies a recorded reading (method_queue 61's fixed menu, one session per question).
READINGS_FORKS_CARD = """Readings (this run): reuse one set of measurements and compute the answer under EVERY fork below that applies to this
question, then choose:
- clock: if inputs.json's fps and question_fps differ, the answer with times and frame steps on question_fps AND on the
  file's fps.
- scale: if an object of well-known real size is visible (an adult person, a car, a regulation ball, a door) and the
  prior's scale makes it more than 15 pct off that size, the answer at the prior's scale AND at that object's scale.
- extent (size questions): each plausible reading of the size word - along the body or heading vs the longest horizontal
  extent; 'horizontal' / 'vertical' as image axes vs the object's own axes; with vs without attached parts (mirrors,
  wings, tails, horns, antennas, handles).
- time window (a speed or acceleration at a stated time): the one-frame difference at that frame AND a smooth fit over
  about 8 frames around it.
Write in notes.md one fenced block

```readings
{"<fork>:<option>": <number>, "<fork>:<option>": <number>}
```

with one entry per option of every fork that applies (your default reading among them; if none applies, one entry
"default"), followed by one line `chosen: <key>` and one sentence on why; submit the chosen number with finish_answers.

"""


class SceneBridge(D.CoderBridge):
    """dsh_coder's bridge with the host pinned by provider.only, a finish_answers for 0 (phase 1) or 1 (phase 2)
    question, and a count of requests that ran into the output cap."""

    def _tool(self, name, a):
        if name in ("segment", "track"):
            if not self.a.sam3_url:
                raise ValueError("unknown tool")
            r = requests.post(f"{self.a.sam3_url}/{name}", json={**a, "video": str(self.ws / "video.mp4"),
                                                                  "ws": str(self.ws)}, timeout=600)
            out = r.json()
            if r.status_code != 200:
                raise ValueError(out.get("error") or r.text[:500])
            img = out.get("image")
            return {"meta": out["meta"], "images": [self.image(self.inside(img), {"file": img})] if img else []}
        if name == "object_3d_track":
            tracks = self.inputs.get("object_3d_tracks") or []
            phrase, k = a.get("phrase"), int(a.get("k", 0))
            if not any(t["phrase"] == phrase and t["k"] == k for t in tracks):
                raise ValueError("Unknown phrase/k. Available: " + json.dumps(tracks))
            import dsh_depth3d as D3
            from tools_metrology import parse_depth_info
            times = [float(t) for t in (a.get("times") or [])][:8]
            return {"meta": D3.track3d(self.inputs["split"], self.inputs["video_id"], phrase, k, self.inputs["width"],
                                       parse_depth_info(self.inputs["questions"][0].get("depth_info")), times)}
        if name != "finish_answers":
            return super()._tool(name, a)
        want = {q["id"] for q in self.inputs.get("questions", [])}
        ans = a.get("answers") or []
        if not want:
            self.final = {"answers": []}
            return {"meta": {"saved": True, "note": "scene record closed"}}
        left = self.a.max_calls - len(self.requests)
        if self.a.self_audit and not getattr(self, "audited", False) and left > self.a.finish_reserve + 3:
            self.audited = True
            self.audit_first = ans
            return {"meta": {"saved": False, "self_check": SELF_AUDIT}}
        if {x.get("id") for x in ans} != want or len(ans) != 1:
            raise ValueError(f"exactly one answer, for question id {sorted(want)}")
        v = ans[0].get("value")
        if not isinstance(v, (int, float)) or not v > 0 or v != v or v == float("inf"):
            raise ValueError("the answer must be a positive finite number")
        self.final = a
        return {"meta": {"saved": True}}

    def proxy(self, body):
        used = sum(r.get("completion_tokens") or 0 for r in self.requests)
        if len(self.requests) >= self.a.max_calls or used >= self.a.max_output:
            raise ValueError("model request/output budget exhausted")
        if self.cost >= self.a.clip_usd or D.SPEND["usd"] >= self.a.budget_usd:
            raise ValueError("spend cap reached")
        # Forced finish (2026-10-20, 26_74: 5 of 8 simulation_0060 sessions spent all 60 calls on a camera solve and
        # ended unanswered). Over the last --finish-reserve calls, a question session may only call finish_answers.
        if (self.inputs.get("questions") and self.final is None
                and (len(self.requests) >= self.a.max_calls - self.a.finish_reserve
                     or self.cost >= 0.85 * self.a.clip_usd or used >= 0.8 * self.a.max_output)):
            tools = [t for t in body.get("tools") or [] if (t.get("function") or {}).get("name") == "finish_answers"]
            if tools:
                body["tools"], body["tool_choice"] = tools, "required"
                body["_forced"] = True  # thinking low below: forced turns ran past the cap three times (26_74 q1344)
                body.setdefault("messages", []).append({"role": "user", "content": (
                    "Model calls are almost used up. Call finish_answers now with your best current estimate for the "
                    "question; give the main uncertainty in the reason.")})
        cap = min(int(body.get("max_tokens", 16384)), self.a.max_output - used)
        body.update(model=self.a.model, max_tokens=cap, temperature=self.a.temperature,
                    stream_options={"include_usage": True})
        if self.a.top_p is not None:
            body["top_p"] = self.a.top_p
        forced = body.pop("_forced", False)
        if forced:
            body["reasoning"] = {"effort": "low"}  # StreamLake: "Reasoning is mandatory ... cannot be disabled"
            body["max_tokens"] = cap = min(body["max_tokens"], 8192)
        elif self.a.reasoning != "none":
            body["reasoning"] = {"effort": self.a.reasoning}
        if self.a.provider:
            body["provider"] = {"only": self.a.provider.split(",")}  # provider.only keeps images (2026-10-18)
            if self.a.provider_ignore:  # 35_5: "deepinfra/fp8" also matched the 1.5x priority tier on 81 pct of 29_x calls
                body["provider"]["ignore"] = self.a.provider_ignore.split(",")
            if self.a.provider_order:  # 35_5: cheapest tier first, the next one only when it is rate-limited (429)
                body["provider"].update(order=self.a.provider_order.split(","), allow_fallbacks=True)
        if self.a.keep_images:  # hosts cap images per request (Crusoe 1, DeepInfra 4; 28_1, 2026-10-21)
            body["messages"] = A._last_images(body.get("messages") or [], self.a.keep_images)
        route, url, key = A.chat_route()
        t0 = time.time()
        response, retries = forward(route, url, key, body)
        rec = {"status": response.status_code, "latency_s": round(time.time() - t0, 1), "retries": retries,
               "provider": A.served_by(response.content), "max_tokens": cap}
        for line in response.content.decode(errors="replace").splitlines():
            if line.startswith("data: ") and line[6:] != "[DONE]":
                try:
                    u = json.loads(line[6:]).get("usage") or {}
                except ValueError:
                    continue
                if u:
                    rec.update({k: u.get(k) for k in ("completion_tokens", "prompt_tokens", "cost")})
                    rec["cached_tokens"] = (u.get("prompt_tokens_details") or {}).get("cached_tokens")
        rec["at_cap"] = bool(rec.get("completion_tokens") and rec["completion_tokens"] >= cap)
        c = float(rec.get("cost") or 0)
        self.cost += c
        with D.SPEND_LOCK:
            D.SPEND["usd"] += c
        self.requests.append(rec)
        return response.status_code, response.headers.get("Content-Type", "text/event-stream"), response.content


def rescue_answer(a, bridge, ws, events):
    """A question session that ended without finish_answers gets one compact request (2026-10-20, 26_74 q1344: forced
    turns inside a 190k-token conversation thought past every cap): the question, that session's own notes, its last
    tool outputs and its last reasoning, with finish_answers as the only tool. Nothing from another question."""
    q = bridge.inputs["questions"][0]
    texts = [c.get("text", "") for e in events if e.get("type") == "assistant/message"
             for c in (e["data"].get("message") or {}).get("content", []) if c.get("type") in ("reasoning", "text")]
    outs = [f"{t['tool']}: {str((t.get('meta') or {}).get('stdout') or '')[:1500]}" for t in bridge.trace[-8:]]
    notes = (ws / "notes.md").read_text(errors="replace")[:6000] if (ws / "notes.md").exists() else "(none)"
    msg = ("Your measurement session for this question ended before you submitted an answer. From your own work below, "
           "give your best estimate now by calling finish_answers (one answer, this question id, a positive number in the "
           "unit the question asks).\n\nQuestion: " + json.dumps(q, ensure_ascii=False) + "\n\nYour notes.md:\n" + notes +
           "\n\nYour last tool outputs:\n" + "\n".join(outs) + "\n\nYour last reasoning:\n" + "\n".join(texts)[-8000:])
    tool = {"type": "function", "function": {"name": "finish_answers", "description": "Submit the answer.", "parameters": {
        "type": "object", "required": ["answers"], "properties": {"answers": {"type": "array", "items": {
            "type": "object", "required": ["id", "value", "reason"], "properties": {
                "id": {"type": "integer"}, "value": {"type": "number"}, "reason": {"type": "string"}}}}}}}}
    body = {"model": a.model, "messages": [{"role": "user", "content": msg}], "tools": [tool], "tool_choice": "required",
            "max_tokens": 16000, "reasoning": {"effort": "low"}, "temperature": a.temperature}
    if a.top_p is not None:
        body["top_p"] = a.top_p
    if a.provider:
        body["provider"] = {"only": a.provider.split(",")}
        if a.provider_ignore:
            body["provider"]["ignore"] = a.provider_ignore.split(",")
        if a.provider_order:
            body["provider"].update(order=a.provider_order.split(","), allow_fallbacks=True)
    route, url, key = A.chat_route()
    r = requests.post(url, headers={"Authorization": f"Bearer {key}"}, json=body, timeout=600)
    j = r.json()
    c = float((j.get("usage") or {}).get("cost") or 0)
    bridge.cost += c
    with D.SPEND_LOCK:
        D.SPEND["usd"] += c
    bridge.requests.append({"status": r.status_code, "rescue": True, "cost": c,
                            "completion_tokens": (j.get("usage") or {}).get("completion_tokens")})
    for call in ((j.get("choices") or [{}])[0].get("message") or {}).get("tool_calls") or []:
        args = json.loads(call["function"]["arguments"])
        ans = args.get("answers") or []
        if len(ans) == 1 and int(ans[0].get("id", -1)) == int(q["id"]):
            v = ans[0].get("value")
            if isinstance(v, (int, float)) and v > 0 and v == v and v != float("inf"):
                bridge.final = args
                return True
    return False


def session(a, ws, inputs, system, prompt, rec_path):
    """One DSH session in workspace ws; the record is written to rec_path (resumable: an existing record is reused)."""
    if rec_path.exists():
        return json.loads(rec_path.read_text())
    bridge = SceneBridge(ws.name, ws, inputs, a, rec_path.parent)
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler(bridge))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_port}"
    scratch = Path(str(ws) + "_dsh")
    shutil.rmtree(scratch, ignore_errors=True)
    scratch.mkdir(parents=True)
    patch = yaml.safe_load((ROOT / "scripts/dsh_identity.patch.yml").read_text(encoding="utf-8"))
    prov = patch[-1]["insert"][0]["config"]["providers"]["qp-openrouter"]
    prov["baseURL"] = url + "/v1"
    prov["models"][0].update(id=a.model, maxTokens=max(32768, a.reply_tokens))
    depth3d = bool(a.depth3d and inputs.get("object_3d_tracks"))
    patch[-1]["insert"] += [{"id": "qp-attachments", "name": "@deepseek-ai/dsh-attachment-local"},
                            {"id": "qp-tools", "name": str((TOOLS_DEPTH3D if depth3d else TOOLS_SAM3) if a.sam3_url
                                                           else D.TOOLS_MODULE)}]
    if a.sam3_url:
        assert system.count(DSH_TOOLS) == 1
        system = system.replace(DSH_TOOLS, DSH_TOOLS + SAM3_TOOLS + (DEPTH3D_TOOLS if depth3d else ""))
    (scratch / "patch.yml").write_text(yaml.safe_dump(patch), encoding="utf-8")
    rec = {"model": a.model, "provider_pin": a.provider, "reasoning": a.reasoning}
    t0 = time.time()
    runtime = Path(a.runtime).resolve()
    try:
        with DeepSeekHarness(provider="qp-openrouter", model=a.model, max_tokens=a.reply_tokens, profile="sdk-minimal",
                             dsh_bin=str(runtime / "node_modules/.bin/dsh"), patches=(str(scratch / "patch.yml"),),
                             dsh_home=str(scratch / "home"), cwd=str(ws),
                             env={"OPENROUTER_API_KEY": "bridge-only", "DSH_SYSTEM_PROMPT": system,
                                  "QP_DSH_BRIDGE": url, "QP_DSH_TOOLS_MODULE":
                                  (runtime / "node_modules/@deepseek-ai/dsh-tools/lib/index.js").as_uri()},
                             initialize_timeout_seconds=60, request_timeout_seconds=a.timeout_min * 60) as h:
            result = h.run(prompt)
            events = list(result.events)
            for _ in range(2):
                if bridge.final is not None or len(bridge.requests) >= a.max_calls:
                    break
                result = h.run("You stopped without a successful finish_answers call. Finish what is missing in one or "
                               "two steps, then call finish_answers.", session_id=result.session_id)
                events.extend(result.events)
            rec.update(finish_reason=result.finish_reason, final_text=result.final_response,
                       events=[e for e in events if e.get("type") not in ("session/title",)])
        if bridge.final is None and getattr(bridge, "audit_first", None):  # audited, then never re-submitted
            bridge.final = {"answers": bridge.audit_first, "from_audit_first": True}
        if bridge.final is None and inputs.get("questions") and not (D.SPEND["usd"] >= a.budget_usd):
            rec["rescued"] = rescue_answer(a, bridge, ws, events)
    except Exception as exc:
        rec.update(error=str(exc), traceback=traceback.format_exc())
    finally:
        server.shutdown()
        server.server_close()
    if getattr(bridge, "audit_first", None) is not None:
        rec["audit_first"] = bridge.audit_first
    rec.update(final=bridge.final, tool_trace=bridge.trace, requests=bridge.requests, cost_usd=round(bridge.cost, 5),
               wall_s=round(time.time() - t0), images=bridge.images)
    if (ws / "notes.md").exists():
        rec["notes.md"] = (ws / "notes.md").read_text(errors="replace")[:20000]
    rec["scripts"] = {p.name: p.read_text(errors="replace")[:20000] for p in sorted(ws.glob("*.py"))}
    shutil.rmtree(scratch, ignore_errors=True)
    dump(rec_path, rec)
    return rec


def video_rows(a):
    """{video: (video path, [question rows])} for the split, each row a dict with id, question, prior, depth_info,
    question_fps, category, source, video_type."""
    out = {}
    if a.split == "val":
        packs = {p["video_id"]: p for p in json.loads((ROOT / a.packs).read_text())["videos"]}
        for v in a.videos:
            p = packs[v]
            vp = Path(p["video_path"])
            if not vp.exists():  # the packs carry the Mac's absolute path; another clone (the GH200) has the same tree
                vp = ROOT / "data/validation/validation_videos" / vp.name
            out[v] = (vp, [{
                "id": int(r["id"]), "question": r["question"].strip(), "prior": r["ground_truth_prior"].strip(),
                "depth_info": (r.get("depth_info") or "").strip() or None, "question_fps": float(r["fps"]),
                "kind": r["inference_type"], "source": r["video_source"].replace("segmentaion", "segmentation"),
                "video_type": r["video_type"]} for r in p["rows"]])
    elif a.qsource == "current":
        # The current dataset rows (CLAUDE.md, re-asks read them since 2026-10-21): all 3,289 ids (template id =
        # row_idx + 1), the full depth_info text and question_fps = the row's fps field. LEDGER_A holds only the
        # 3,012 scored ids and a depth_info flag in place of the text (28_1).
        cur = json.loads((ROOT / "data/test/test_dataset_current_20261021.json").read_text())
        for v in a.videos:
            rs = [r for r in cur if r["video_id"] == v]
            out[v] = (ROOT / "data/test" / f"{v}.mp4", [{
                "id": int(r["row_idx"]) + 1, "question": str(r["question"]).strip(), "prior": str(r["prior"]).strip(),
                "depth_info": (str(r["depth_info"]).strip() if isinstance(r["depth_info"], str) else None) or None,
                "question_fps": float(r["fps"]), "kind": r["inference_type"], "source": r["video_source"],
                "video_type": r["video_type"]} for r in rs])
    else:
        led = pd.read_csv(LEDGER_A)
        for v in a.videos:
            g = led[led.video == v]
            out[v] = (ROOT / "data/test" / f"{v}.mp4", [{
                "id": int(r.id), "question": str(r.question).strip(), "prior": str(r.prior).strip(),
                "depth_info": (str(r.depth_info).strip() if isinstance(r.depth_info, str) else None) or None,
                "question_fps": float(r.question_fps), "kind": r.kind, "source": r.source,
                "video_type": r.category} for r in g.itertuples()])
    return out


def meta(path):
    import av
    with av.open(str(path)) as c:
        s = c.streams.video[0]
        n = sum(1 for _ in c.decode(s))
        return {"fps": round(float(s.average_rate), 6), "frames": n, "width": s.width, "height": s.height}


def fresh_ws(path, src):
    shutil.rmtree(path, ignore_errors=True)
    (path / "frames").mkdir(parents=True)
    shutil.copyfile(src, path / "video.mp4")


# Fail-fast (2026-10-20, after 26_72 lost $2.7 of MiMo sessions to one repeated host error): --fail-fast sessions in a
# row that end without an answer, phase 1 or 2, stop the run; every later session is skipped, not sent.
FAIL = {"consec": 0, "stop": False, "lock": threading.Lock()}


def note_outcome(a, ok, label):
    with FAIL["lock"]:
        FAIL["consec"] = 0 if ok else FAIL["consec"] + 1
        if not ok and FAIL["consec"] >= a.fail_fast and not FAIL["stop"]:
            FAIL["stop"] = True
            print(f"FAIL-FAST: {FAIL['consec']} sessions in a row without an answer (last {label}); stopping", flush=True)


def run_video(v, src, rows, a, out):
    if FAIL["stop"]:
        return []
    m = meta(src)
    scene3d = "3" in rows[0]["video_type"][:2]
    base = {"video_source": rows[0]["source"], "scene": "3D" if scene3d else "2D", **m,
            "duration_s": round(m["frames"] / m["fps"], 4)}
    vdir = out / "videos" / v
    vdir.mkdir(parents=True, exist_ok=True)
    if not (vdir / "scene" / "scene.json").exists():
        ws = (a.workdir / v / "scene_ws").resolve()
        fresh_ws(ws, src)
        (ws / "scene").mkdir()
        (ws / "inputs.json").write_text(json.dumps(base, indent=1) + "\n")
        rec = session(a, ws, {}, SCENE_PROMPT, "Start with video_frames (a contact sheet), then build the record.",
                      vdir / "p1.json")
        note_outcome(a, rec.get("finish_reason") == "completed" and not rec.get("error"), f"{v} phase 1")
        shutil.rmtree(vdir / "scene", ignore_errors=True)
        shutil.copytree(ws / "scene", vdir / "scene", ignore=lambda d, names: [
            n for n in names if (Path(d) / n).is_file() and (Path(d) / n).stat().st_size > 2_000_000])
        print(v, "phase 1", f"${rec.get('cost_usd')}", len(rec.get("requests", [])), "calls",
              "scene.json" if (vdir / "scene/scene.json").exists() else "NO scene.json", rec.get("error", ""), flush=True)
    if a.phase == "1":  # scene records only (28_3: phase 1 of every video first, at its own parallelism)
        return []
    # Phase 2 sessions of one video are independent (each sees only its own question), so they run side by side
    # (--q-workers, 2026-10-20: serial sessions made a 5-row video take 25 min).
    def one(r, k):
        if FAIL["stop"]:
            return None
        qdir = out / "q" / f"{v}__{r['id']}"
        ws = (a.workdir / v / f"q_{r['id']}_r{k}").resolve()
        fresh_ws(ws, src)
        if (vdir / "scene").exists():
            shutil.copytree(vdir / "scene", ws / "scene")
            for p in sorted((ws / "scene").rglob("*"), reverse=True):
                p.chmod(0o444 if p.is_file() else 0o555)
        q = {"id": r["id"], "question": r["question"], "prior": r["prior"], "depth_info": r["depth_info"],
             "prior_kind_to_question_kind": r["kind"], "question_fps": r["question_fps"]}
        inputs = {**base, "video_type": r["video_type"], "question": q}
        binputs = {"questions": [q]}
        if a.depth3d:
            import dsh_depth3d as D3
            tracks = D3.available(a.split, v)
            if tracks:
                inputs["object_3d_tracks"] = tracks
                binputs.update(object_3d_tracks=tracks, split=a.split, video_id=v, width=m["width"])
        (ws / "inputs.json").write_text(json.dumps(inputs, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        prompt = ANSWER_PROMPT
        if a.judgment_card:
            prompt = prompt.replace("Method:\n", JUDGMENT_CARD + "Method:\n", 1)
            assert JUDGMENT_CARD in prompt
        if a.physical_internet and v in a.physical_internet:
            prompt = prompt.replace("Method:\n", PHYSICAL_INTERNET + "Method:\n", 1)
            assert PHYSICAL_INTERNET in prompt
        if a.readings:
            prompt = prompt.replace("Method:\n", READINGS_CARD + "Method:\n", 1)
            assert READINGS_CARD in prompt
        if a.readings_forks:
            prompt = prompt.replace("Method:\n", READINGS_FORKS_CARD + "Method:\n", 1)
            assert READINGS_FORKS_CARD in prompt
        rec = session(a, ws, binputs, prompt,
                      "inputs.json:\n" + json.dumps(inputs, indent=1, ensure_ascii=False) +
                      "\n\nRead scene/notes.md and scene/scene.json first (run_python), then measure and call "
                      "finish_answers.", qdir / f"r{k}.json")
        ans = (rec.get("final") or {}).get("answers") or []
        note_outcome(a, bool(ans), f"{v} q{r['id']}")
        reqs = rec.get("requests", [])
        for p in sorted(ws.rglob("*"), reverse=True):
            if p.exists() and not p.is_symlink():
                p.chmod(0o755 if p.is_dir() else 0o644)
        shutil.rmtree(ws, ignore_errors=True)
        return {"id": r["id"], "video": v, "category": r["video_type"][:1] + r["video_type"][1:2],
                "repeat": k, "answer": float(ans[0]["value"]) if ans else None,
                "cost": rec.get("cost_usd"), "turns": len(reqs),
                "requests_at_cap": sum(1 for x in reqs if x.get("at_cap")), "images": rec.get("images"),
                "wall_s": rec.get("wall_s"), "error": rec.get("error", "")}

    # --repeat-from (2026-10-23, 35_1): later repeats of questions already answered; an existing r<k>.json is never
    # run again, so a restart or a second launch cannot overwrite an answer.
    jobs = [(r, k) for r in rows for k in range(a.repeat_from, a.repeats + 1) if (not a.ids or int(r["id"]) in a.ids)
            and (not a.cats or r["kind"][0] + r["video_type"][1] in a.cats)
            and not (out / "q" / f"{v}__{r['id']}" / f"r{k}.json").exists()]
    with ThreadPoolExecutor(max_workers=max(1, a.q_workers)) as ex:
        rows_out = [x for x in ex.map(lambda rk: one(*rk), jobs) if x is not None]
    return rows_out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--runtime", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--provider", default="", help="OpenRouter provider.only slug(s), comma-separated")
    ap.add_argument("--provider-ignore", default="",
                    help="OpenRouter provider.ignore slug(s), e.g. deepinfra/fp8/priority,deepinfra/fp8/flex: provider.only "
                         "'deepinfra/fp8' alone billed 81 pct of the 29_x calls at the 1.5x priority tier (35_5)")
    ap.add_argument("--provider-order", default="",
                    help="OpenRouter provider.order with fallbacks, e.g. deepinfra/fp8/flex,deepinfra/fp8,deepinfra/fp8/priority "
                         "(0.8x, 1.0x, 1.5x): the standard tier alone answered 429 to 10 of 10 concurrent calls at 19:12 UTC")
    ap.add_argument("--readings-forks", action="store_true",
                    help="READINGS_FORKS_CARD: every named fork that applies (clock, scale, extent, time window) is a reading (35_6)")
    ap.add_argument("--readings", action="store_true",
                    help="READINGS_CARD in the answering prompt: answer under every plausible reading, record each (35_5)")
    ap.add_argument("--reasoning", default="medium", help="OpenRouter reasoning effort, or 'none'")
    ap.add_argument("--temperature", type=float, default=0.3)
    ap.add_argument("--top-p", type=float, default=None,
                    help="top_p sent upstream (model-card settings, 38_1); not sent when unset, as before")
    ap.add_argument("--split", choices=("val", "test"), required=True)
    ap.add_argument("--videos", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workdir", type=Path, default=D.TMP_ROOT / "dsh_scene")
    ap.add_argument("--packs", default="results/s26_val_sol_full/blind_packs.json")
    ap.add_argument("--labels", default="results/s26_val_sol_full/evaluation/scored_rows.csv")
    ap.add_argument("--repeats", type=int, default=1)
    ap.add_argument("--repeat-from", type=int, default=1,
                    help="first repeat to run: --repeat-from 2 --repeats 3 adds r2 and r3 next to an existing r1")
    ap.add_argument("--max-calls", type=int, default=60)
    ap.add_argument("--max-output", type=int, default=200000)
    ap.add_argument("--reply-tokens", type=int, default=16384,
                    help="per-reply max_tokens (42_2: MiMo-V2.6-Flash cut 40 pct of sessions at 16,384, Series 38)")
    ap.add_argument("--max-images", type=int, default=30)
    ap.add_argument("--timeout-min", type=int, default=40)
    ap.add_argument("--clip-usd", type=float, default=0.5, help="cap per session")
    ap.add_argument("--budget-usd", type=float, required=True)
    ap.add_argument("--workers", type=int, default=3)
    ap.add_argument("--ids", default="", help="comma-separated question ids to run (default: all of each video)")
    ap.add_argument("--finish-reserve", type=int, default=3, help="last calls of a question session: finish_answers only")
    ap.add_argument("--q-workers", type=int, default=6, help="phase-2 sessions of one video run in parallel")
    ap.add_argument("--fail-fast", type=int, default=3, help="stop after this many sessions in a row without an answer")
    ap.add_argument("--keep-images", type=int, default=0, help="send only the newest K images per request (0 = all)")
    ap.add_argument("--qsource", choices=("current", "ledger"), default="current",
                    help="test split: the current dataset rows (default) or the 26_30 ledger")
    ap.add_argument("--phase", choices=("1", "both"), default="both", help="1 = scene records only")
    ap.add_argument("--physical-internet", default="", help="comma-separated videos whose answering prompt carries the "
                    "self-filmed physical-scale convention (28_6)")
    ap.add_argument("--cats", default="", help="only questions of these categories (e.g. D2), comma-separated")
    ap.add_argument("--judgment-card", action="store_true", help="the method card (29_6) in the answering prompt")
    ap.add_argument("--self-audit", action="store_true", help="the first finish_answers of a question session returns "
                    "the self-check list instead of saving (29_6)")
    ap.add_argument("--sam3-url", default="", help="SAM 3 tool server (scripts/sam3_server.py), e.g. http://127.0.0.1:8790; "
                    "adds the segment / track tools and their paragraph to both prompts")
    ap.add_argument("--depth3d", action="store_true", help="object_3d_track (dsh_depth3d.py) on question sessions whose "
                    "lab video has a 3D track (42_4); needs --sam3-url")
    a = ap.parse_args()
    assert not a.depth3d or a.sam3_url, "--depth3d extends the SAM 3 tools module: pass --sam3-url"
    if os.environ.get("QP_LLM_ROUTE", "openrouter") != "openrouter":
        raise SystemExit("spend caps need OpenRouter's per-call cost; run with QP_LLM_ROUTE=openrouter")
    a.videos = a.videos.split(",")
    a.ids = {int(x) for x in a.ids.split(",") if x}
    a.physical_internet = set(x for x in a.physical_internet.split(",") if x)
    a.cats = set(x for x in a.cats.split(",") if x)
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    vids = video_rows(a)
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        res = list(ex.map(lambda v: run_video(v, *vids[v], a, out), a.videos))
    led = pd.DataFrame([x for rs in res for x in rs])
    if led.empty:
        done = sum((out / "videos" / v / "scene" / "scene.json").exists() for v in a.videos)
        print(json.dumps({"phase": a.phase, "videos": len(a.videos), "scene_json": done,
                          "spend_usd": round(D.SPEND["usd"], 4)}))
        return
    med = led.groupby("id").answer.apply(lambda s: statistics.median(s.dropna()) if s.notna().any() else None)
    led["median"] = led.id.map(med)
    if a.split == "val":
        lab = pd.read_csv(ROOT / a.labels).set_index("id")
        led["gt"] = led.id.map(lab.ground_truth_posterior)
        led["score"] = [pl.row_mra(x, g) for x, g in zip(led["median"], led["gt"])]
        led["run1_score"] = [pl.row_mra(lab.run1.get(i), g) for i, g in zip(led.id, led["gt"])]
    led.to_csv(out / "ledger.csv", index=False)
    p1 = [json.loads((out / "videos" / v / "p1.json").read_text()) for v in a.videos
          if (out / "videos" / v / "p1.json").exists()]
    summary = {"settings": {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(a).items()},
               "harness": "DeepSeek Harness (sdk-minimal) + dsh_coder_tools.mjs; no Anthropic software",
               "spend_usd": round(D.SPEND["usd"], 4),
               "phase1": [{"cost": r.get("cost_usd"), "calls": len(r.get("requests", [])), "error": r.get("error")}
                          for r in p1],
               "phase2": {"sessions": len(led), "answered": int(led.answer.notna().sum()),
                          "cost_mean": round(led.cost.mean(), 5), "turns_mean": round(led.turns.mean(), 1),
                          "requests_at_cap": int(led.requests_at_cap.sum())}}
    if a.split == "val":
        u = led.drop_duplicates("id")
        summary["mra"] = {"agent_median": round(u.score.mean(), 4), "glm_v5r_run1": round(u.run1_score.mean(), 4),
                          "rows": len(u)}
    (out / "summary.json").write_text(json.dumps(summary, indent=1, default=str) + "\n")
    print(json.dumps({k: summary[k] for k in summary if k != "settings"}, indent=1, default=str))


if __name__ == "__main__":
    main()

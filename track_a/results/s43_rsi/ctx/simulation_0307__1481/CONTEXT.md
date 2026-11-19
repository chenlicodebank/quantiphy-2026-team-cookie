# Context of question 1481 (organised record; every round adds to it)

## Question
- Text: What is the length of the plane in meters?
- Its own prior: speed of the plane = 22.16 m/s
- Its own depth_info: t = 1.0s, distance_plane_camera = 102.6664 m
t = 2.0s, distance_plane_camera = 121.8263 m
- question_fps: 24
- Video: simulation_0307.mp4 (simulation, V3SC)

## The answer currently submitted
10.7 - the Claude line's answer 10.7, unchanged.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 17.4 | 1.626 |
| C2 | Claude Opus 5.5 (Claude Code agent), 26_59 real-scale re-ask, real-scale re-ask (26_59, --real-scale, user go 2026-10-20) - stage 2 | 10.7 | 1.000 |
| C3 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_9b D3 adjudication batch 2 (DeepSeek+SAM 3 differs >25 pct) | 10.8 | 1.009 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 15.9 | 1.486 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 19.3 | 1.804 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 10.6 | 0.991 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 20.0 | 1.869 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 17.8 | 1.664 |

DeepSeek median over its 5 runs: 17.8.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v2; files in context/round1/)
- Answer: 14.8 (new, confidence medium, follows None)
- Where the answers part: nose-to-tail candidates (C2/C3/C6) ended the length at the pod rear tips; the others gave span/PCA extents
- Fault proven: a centreline tail fin lies 4.9 m aft of the pod rear tips (forcing it to the pod-tip coordinate raises its track rms from 2.5 to 15 px; it moves 5.3 pct more pixels than the adjacent pod tip, so it is nearer the camera), so pod length 10.7 misses the tail
- Closure on the prior: 1.6 pct

# Round 1 addendum: Q1481 (length of the plane)

## Established (by measurement; scripts in the round folder)
- **Scale.** A constant-velocity rigid aircraft model with |V| = 22.16 and the two origin depths gives f = 3140–3480 (depends on the origin proxy).
  - The length is insensitive to f: it varies by 0.4 % across that range.
  - Closure: the speed implied by the depths and the image rays is 22.1–22.7 m/s (within 2.4 %).
- **Rear end.** The rearmost point of the aircraft is the trailing edge of a centreline tail/ventral fin (the dark trapezoid that appears under the right body end).
  - It lies **4.9 m aft of the pod rear tips** along the body axis (4.6–5.3 in every variant).
  - Its bottom, middle and top points share one body coordinate, so the trailing edge is vertical.
  - Proof: forcing the fin bottom to the pod-tip coordinate raises its track rms from 2.5 to 15 px. Also, the fin bottom moves 5.3 % more pixels than the adjacent pod tip over frames 2–71, so it is nearer the camera.
- **Pod length.** Pod front to pod rear tip = 9.6–10.5 m. My clicks give 9.6–9.9; C3's clicks give 10.5. This agrees with C2/C3's 10.4–11.0.
- **Span.** Fin top to fin top = 18.0–18.9 m (C1's 17.4 was this span).
- **Length** (pod front to tail-fin trailing edge, along the body axis): 14.45–15.4 m. **New answer 14.8 m.** Along the flight direction it is 0.1–0.5 m more.

## Ruled out
- 10.6–10.8 (C2/C3/C6): these end at the pod tips and miss the tail fin.
- 17.4–20 (C1/C5/C7/C8): these are the span or a silhouette-PCA long axis, and the convention excludes them.
- 15.9 (C4): a PCA box fit; it is near my value only by coincidence.

## Open
- The pod-front corner has low contrast, and its automatic track slides and jumps after about frame 52. It is the main uncertainty (±0.5 m).
- Whether the reference box is aligned with the world axes: the body is 2–6° off the flight direction, which would change the answer by at most about 0.3 m.

### Round 3 (harness v3; files in context/round3/)
- Answer: 14.5 (new, confidence medium, follows None)
- Where the answers part: the rear end of the length: the pod rear tips (10.7) or the end of the central fuselage with its ventral fin, about 4.9-5.0 m further aft
- Fault proven: C2/C3/C6 ended the length at the pod tips. The fuselage end (RC) and the fin bottom (VB) triangulate 14.3-14.4 m behind the pod front, against 9.4 m for both pod tips (all rms < 2 px), and they move 5 pct more pixels than the right pod tip, so they are nearer the camera
- Closure on the prior: 0.3 pct

# Round 2 addendum: Q1481 (length of the plane)

## Established (own code: fitf.py, track.py, manual.json, tri.py, world.py, windows.py, closure_boot.py)
- **Scale.** Constant-velocity fit with |V| = 22.16 and both depths:
  - f = 3390 (hull origin) or 3240 (bbox origin).
  - Closure speed 22.22 m/s (+0.3 %) and 22.38 m/s (+1.0 %).
- **Round 1's fault is reproduced.**
  - The central fuselage rear end (RC) and the ventral-fin bottom (VB) lie on the centreline, 4.9–5.1 m aft of both pod tips (LR and RR, which are symmetric: aft 9.45 / 9.37 from the pod front).
  - This holds in every frame window (0–36, 12–48, 24–71, 0–71). Track rms is < 2 px.
  - Model-light check: from frame 2 to frame 71, RC and VB move 1155 px and the right pod tip moves 1099 px.
  - So the 10.6–10.8 answers (pod front to pod tip) miss the fuselage tail.
- **Front.** The pod front top corner (LF) is the frontmost point; the antenna is 1.5 m behind it and the fin tops 5.4 m behind.
  - The automatic LF track slides along the edge (by 9 px at frame 24), so I used 10 hand clicks (frames 2–60, rms 2.0 px).
  - A bootstrap with ±1.5 px click noise gives sd 0.18 m.
- **Length** (LF → RC along the flight direction): 14.43 at hull f, 14.67 at bbox f; the windows give 13.98–14.45. **Answer 14.5 m.**
  - Round 1's 14.8 agrees within 2 %. Its upper variants (15.4) came from C3's LF clicks, which sit 0.9 m further forward, with rms 3.05 px.
- **Other measurements.** The span across the fin tops is 18.2 m. In the level-flight frame, the pod axis is pitched 11.5° nose-up and the fuselage end sits 0.5 m above the pod front.

## Ruled out
- 10.6–10.8 (pod only).
- 17.4–20 (span or silhouette).
- 15.9 (PCA box).

## Open
- The depth of the LF corner (±0.3 m).
- How far the rounded fuselage tail cap extends beyond the RC corner (0.1–0.3 m). The sliding fin-edge point VM gives 15.0 m.
- Whether the reference box is aligned with the flight direction.

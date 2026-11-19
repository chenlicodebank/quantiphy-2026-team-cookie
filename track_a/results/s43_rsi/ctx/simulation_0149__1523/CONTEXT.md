# Context of question 1523 (organised record; every round adds to it)

## Question
- Text: What is the acceleration of the car at time 0.5s in m/s^2?
- Its own prior: diameter of the tire = 0.764m
- Its own depth_info: t=0s, distance_yellowCarRightFrontTire_camera = 14.244m
- question_fps: 24
- Video: simulation_0149.mp4 (simulation, S3MC)

## The answer currently submitted
8.81051 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 10.35 and an earlier DeepSeek median B = 7.5; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 10.35 | 1.175 |
| C2 | Claude Opus 5.5 (Claude Code agent), 26_36 second run, spread test: a second independent answer on the kept scene record (26_36) | 10.1 | 1.146 |
| C3 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 2 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 10.2 | 1.158 |
| C4 | Claude Sonnet 5.5 (Claude Code agent), 26_80 repeat, repeat run 3 of 3 (26_80, Sonnet 5.5 effort high, per-question median of three) | 7.2 | 0.817 |
| C5 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_6b S3 adjudication (DeepSeek differs >2x; Codex in the dossier) | 10.4 | 1.180 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 9.0 | 1.022 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 6.0 | 0.681 |
| C8 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 5.5 | 0.624 |
| C9 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 4.3 | 0.488 |
| C10 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 4.3 | 0.488 |
| C11 | OpenAI GPT-6 Astra (Codex agent) | 10.25 | 1.163 |

DeepSeek median over its 5 runs: 5.5.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v1; files in context/round1/)
- Answer: 10.4 (switch, confidence high, follows C5)
- Where the answers part: motion model/fit window of the wheel path around frame 12: local cubic/smoothstep on a ray-intersected straight 3D line (10.1-10.4) vs long-window constant-acceleration fits or noisy size rulers (4.3-9.0)
- Fault proven: low candidates (DeepSeek median feeding the 8.81 blend, C4) fit constant acceleration across an ease-in whose acceleration decays (my quadratic over 0-28 gives 8.3 vs cubic 10.4) or used f~1700 failing closure / noisy ECC scale
- Closure on the prior: -1.0 pct

# Round addendum, q1523 (car acceleration at t = 0.5 s, frame 12)

## Established
- The near-front rim was tracked in frames 0-30 (`rimtrack2.py`, overlay checked).
  - The hub stays at v ≈ 829 (the horizon), so the hub moves in the camera's horizontal plane.
  - Rim height is 87.2 px at f0, 99.5 at f12 and 121.9 at f20.
  - The scene record's rim heights for frames 10-16 are wrong (truncated).
- The path is a straight 3D line (1.9 cm RMS), heading 36° off the camera-ward axis. There is no yaw.
- Scale comes from depth_info (z0 = 13.357 m axial) and f ≈ 2410 (vanishing points; the prior gives 2387).
  - Closure: tyre diameter re-derived at 0.757 m against the 0.764 m prior (-1 %).
- a(12) by the convention (s12 - 2 s11 + s10)·576:
  - Cubic fits, several windows: 10.43-10.45.
  - Smoothstep fit: 10.37.
  - f from 2300 to 2500: 10.54 to 10.34.
- v(12) = 6.66 m/s. Peak speed is about 9.4 m/s.

## Ruled out
- Constant-acceleration (quadratic) fits over long windows. The motion is an ease-in whose acceleration decays,
  so these fits read low: 8.3 over frames 0-28, 9.8 over 6-18. This explains C6-C10 (4.3-9.0).
- f ≈ 1700 (C8), which fails closure.
- ECC body-scale (C4, 7.2), which is too noisy.
- The 8.81 blend, because it is pulled down by those faulty low values.

## Answer now: 10.4 m/s^2 (high confidence, about ±3 %)

## Open
- Only the frame-11 vs frame-12 centring of the convention (C2 noted 9.7 instantaneous vs 10.3 on the convention).
  The convention stated in the task, (speed(12) - speed(11))·fps, was used.

### Round 2 (harness v2; files in context/round2/)
- Answer: 10.4 (switch, confidence high, follows C5)
- Where the answers part: motion model/fit window for the second difference at frame 12 on the straight-line wheel path: local cubic/ease fit (10.1-10.6) vs long constant-acceleration fits (4.3-9.0)
- Fault proven: low candidates fit constant acceleration across an ease-in with linearly decaying acceleration: my quadratic over frames 10-28 gives 5.1 and over 0-28 gives 8.5 vs 10.5 from cubic/smoothstep (rms 2 mm); the 8.81 blend inherits the DeepSeek median 5.5
- Closure on the prior: -1.5 pct

# Round 2 addendum, q1523 (car acceleration at t = 0.5 s, frame 12)

## Verified (independent route)
- Round 1's switch to 10.4 is verified. My own value is 10.5 ± 0.15 m/s^2, so the answer is 10.4 (C5).
- **No yaw.** The heading comes from the near-front rim ellipse aspect ratio, corrected for azimuth (`traj.py`), and
  uses no size cue. It stays at 37–38.5° from the camera-ward axis in every frame 0–28. The path is a straight line
  in the hub-height horizontal plane, with the hub row at 829–831 = horizon.
- Positions come from the ray–line intersection anchored at the frame-0 point, which is set by 14.244 m and u0. The
  camera pitch (about 7°) is included.
- **Focal length.**
  - A joint fit (rim-size ratios against ray depths, plus aspect headings) gives f = 2264–2316 (±25).
  - The tyre/rim ratio of 1.515 with the prior gives about 2262.
  - The vanishing-point route (round 1 / C2) gives 2410.
- **a(12)** by the convention (s12 − 2 s11 + s10)·576:
  - Cubic: 10.60 / 10.52 / 10.32 at f = 2260 / 2300 / 2410.
  - Smoothstep: 10.58 / 10.30, with ease start i0 = 0.0, T ≈ 52–56 frames, rms 2 mm.
  - Windows and degree change the result by ≤ 0.1.
- **Closure:** the tyre comes out at 0.741–0.778 m against 0.764 at f ≈ 2290. At f = 2410 with my tyre ratio it is
  −4 to −8 %.

## Ruled out (reproduced)
- Quadratic fits: frames 10–28 give 5.1, which matches C9/C10 at 4.3. Frames 0–28 give 8.5, which matches C6 and C4.
- The 8.81 blend.

## Open
- The only point left open is the centring of the convention. The short-window instantaneous a(12) is about 9.9,
  while the backward second difference centred at frame 11 is about 10.5. The task's stated convention was followed.
- f is 2290 vs 2410, which is worth about 2 % in a.

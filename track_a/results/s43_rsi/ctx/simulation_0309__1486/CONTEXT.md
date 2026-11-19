# Context of question 1486 (organised record; every round adds to it)

## Question
- Text: What is the body length of the dragon in meters?
- Its own prior: speed of the dragon = 1.29m/s
- Its own depth_info: t = 1.0s, distance_dragon_camera = 5.2108 m
t = 2.0s, distance_dragon_camera = 6.3261 m
- question_fps: 24
- Video: simulation_0309.mp4 (simulation, V3SC)

## The answer currently submitted
1.00536 - a fixed-rule blend exp(0.7 ln A + 0.3 ln B) of the Claude line's answer A = 1.1 and an earlier DeepSeek median B = 0.815; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 1.1 | 1.094 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_9b D3 adjudication batch 2 (DeepSeek+SAM 3 differs >25 pct) | 1.05 | 1.044 |
| C3 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 0.72 | 0.716 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 0.91 | 0.905 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r3 | 1.08 | 1.074 |
| C6 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r4 | 0.6 | 0.597 |
| C7 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r5 | 0.57 | 0.567 |

DeepSeek median over its 5 runs: 0.72.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v2; files in context/round1/)
- Answer: 0.87 (new, confidence medium, follows None)
- Where the answers part: foreshortening of the head-tail axis: Claude line puts head/tail on the flight axis through a hip at root depth (closest-point construction, inflates a drooping tail), DeepSeek line ignores foreshortening (planar length)
- Fault proven: glide-phase structure-from-known-translation (rigid landmarks, rms 1-1.3 px) gives hip->tail tip 0.53 m and head->hip 0.21 m in 3D (head->tail 0.74 m at f~3550), vs C1's 0.73-0.84 tail and 0.29 head; planar answers miss a measured 0.5 m head-tail depth difference
- Closure on the prior: 0.0 pct

# Round 1 addendum (q1486, dragon body length)

## Established
- **Focal length.** A constant-velocity line fit to the hip track (|V| = 1.29 m/s, depths 5.2108 at frame 24 and 6.3261 at frame 48) gives
  f = 3440-3580 over most windows.
  - Independently, f ≈ 3550 is where the triangulated torso point in the glide sits on the root line.
  - The two-point chord route is ill-conditioned: f = 3300 to 4500 changes the chord only from 1.31 to 1.22 m, so DeepSeek's f of 3800-4500 is unsupported.
  - Flight direction in camera coordinates is about (-0.43, -0.31, 0.85), about 34° from the line of sight at t = 1.
- **Body orientation and offsets, measured directly** (`tri_glide.py`). In the glide (frames 52-71, fixed pose) each rigid
  landmark was triangulated from the known per-frame translation (rms 1-1.3 px).
  - The tail tip is 0.50 m nearer the camera than the back of the head.
  - The head→tail vector is about 15° from the flight axis.
  - 3D chords at f ≈ 3550: head(back)→tail tip 0.74 m, hip→tail 0.53, head→hip 0.21. Over the f range 3300-3800 the head→tail chord is 0.69-0.87.
- **Tail-tip hand marks** (5x crops): (1375, 570) at frame 52, (1277.6, 508.4) at 60, (1233, 479.4) at 64, (1162.4, 435.6) at 71.

## Ruled out
- **Planar, no-foreshortening lengths** (0.57-0.72). They miss the measured 0.5 m depth spread.
- **On-axis closest-point offsets in the glide** (tail 0.73-0.97, C1). They are inflated by the drooping, off-axis tail. Frames 0-8
  (C2: 0.54-0.63) agree with the triangulated 0.53.

## Answer this round
0.87 m = head→tail chord 0.74 + hidden snout about 0.10, + about 0.03 for a more extended tail. Decision "new", medium confidence.

## Open
- The hidden snout length (back of head to snout tip), assumed 0.10 ± 0.04 m. It is never visible.
- Which pose and dimension the reference used:
  - chord in the glide pose: about 0.84;
  - extent along the travel axis: about 0.81;
  - rest pose with a straight tail: possibly about 0.9.

### Round 3 (harness v3; files in context/round3/)
- Answer: 0.87 (new, confidence medium, follows round1)
- Where the answers part: 3D tilt of the head-tail axis in the glide: along the flight axis (C1/C2, ~0.9 m depth spread, ~1.0 m+snout) vs tilted ~15 deg (round 1, ~0.5 m spread, 0.74 m chord) vs planar (DeepSeek)
- Fault proven: C1's on-flight-axis geometry predicts the head-tail image vector shrinks to 205 px by frame 71; measured 223 px (rigid head-foot pair shrinks exactly at the root-depth rate 0.881), so C1's ~1.0 m head-tail chord is wrong; my triangulation gives 0.74-0.80 m, frame 0 gives ~0.77-0.83 m, +0.10 snout
- Closure on the prior: 0.3 pct

# Round 2 addendum (q1486, dragon body length)

## Verified (round 1's proposed 0.87 m holds)
- **Focal length.** My own hard-constrained constant-velocity line fit gives f ≈ 3500-3700, with glide rms 6.9 px. f = 4500 gives rms 24 px and is rejected.
  Closure: the hip chord between frames 24 and 48 is 1.285-1.294 m/s at f 3450-3550, against the prior 1.29.
- **Glide triangulation, reproduced with independent tracking.** I used my own LK tracks and my own 4x tail-tip marks; the tail-tip marks are (1373, 569) at frame 52, (1276, 507) at 60,
  (1232, 478) at 64 and (1158, 436) at 71, within about 4 px of round 1's.
  - head_spot→tail chord: 0.74 at f 3450, 0.78 at 3550, 0.76-0.87 in window 48-71.
  - The tail is 0.5 m nearer the camera than the head, and the head→tail vector is 13-15° from the flight axis.
- **New decisive check: perspective shrink over frames 52→71.**
  - A rigid head→foot pair shrinks by 0.881, equal to the root-depth ratio 0.882.
  - The head→tail vector shrinks 273 → 223 px. The along-flight-axis geometry (C1, about 1.0 m chord) predicts 205 px; the round-1 geometry predicts 221.
  - The tail's image direction is steady at 41-42°, so there is no visible tail swing.
- **Independent frame 0** (axis 43° from the line of sight): visible head front→tail is 552 px at 4.20 m, i.e. 0.82-0.83 m if the body is along the axis and about 0.77 m after droop.
  Both-at-root lower bound: 0.62 m.

## Caveat
Per-point triangulation is noisy: the hip and horn LK points land 0.6-0.9 m off in depth because the tracks slid. Use the end-to-end
shrink ratio rather than single-point depths.

## Answer
**0.87 m** = head→tail 0.74-0.80 + hidden snout about 0.10. Medium confidence.

## Open
- The hidden snout length (±0.04 m).
- Whether the reference used a rest pose with a straight tail (possibly +0.03-0.05). A value above 0.95 m would need both at their maximum.

# Context of question 1756 (organised record; every round adds to it)

## Question
- Text: What is the height of the moving bicycle (from the handlebar to the ground, including below the wheel) in meters?
- Its own prior: height of the walking person = 1.8m
- Its own depth_info: t=1s, distance_bike_camera = 16.4919m
t=2s, distance_bike_camera = 11.9277m
t=1s, distance_human_camera = 11.9259m
t=2s, distance_human_camera = 10.8165m
- question_fps: 33
- Video: simulation_0048_segmented.mp4 (segmentation, S3MX)

## The answer currently submitted
1.19336 - a fixed-rule blend exp(0.5 ln A + 0.5 ln B) of the Claude line's answer A = 1.41 and an earlier DeepSeek median B = 1.01; the rule blends every row of its population where the two differ by less than about 50 pct, so it is no judgement about this question.

## Answers so far (each from a separate session that saw only this question, its video, prior and depth_info)

| name | who | answer | x submitted |
|---|---|---|---|
| C1 | Claude Opus 5.5 (Claude Code agent), 26_30 per-question run | 1.41 | 1.182 |
| C2 | Claude Opus 5.5 (Claude Code agent), 30_x adjudication, 30_3 S3 adjudication (DeepSeek differs 25 pct to 2x) | 1.49 | 1.249 |
| C3 | Claude Opus 5.5 (Claude Code agent), 40_5 fresh per-question run | 1.55 | 1.299 |
| C4 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r1 | 1.01 | 0.846 |
| C5 | DeepSeek-V4.1-Flash-1017 (open-weight agent with SAM 3 tools), run r2 | 1.01 | 0.846 |

DeepSeek median over its 2 runs: 1.01.

Each candidate's notes.md and scripts are in context/<name>/.

## Investigation rounds

### Round 1 (harness v3; files in context/round1/)
- Answer: 0.95 (switch, confidence medium, follows C4)
- Where the answers part: scale of the bike: given bike depth 16.49 m (C1-C3, giant 2.7 m rider) vs the walker's common ground plane (C4/C5, 1.74 m rider)
- Fault proven: C1-C3 applied the given bike distance to the visible bike although the image shows rider and walker on one ground (identical size-vs-contact-row lines; one scale puts all 60 wheel contacts on the walker's plane), giving a 2.7 m seated rider that fails the adult-size hard check; C4/C5 omit the handlebar setback (+6%)
- Closure on the prior: 0.4 pct

# Round 1 addendum: q1756 (bicycle handlebar height)

**Proposed change:** switch from 1.193 (the blend) to **0.95 m**, using the common-ground reading of C4/C5. Confidence is medium.

## Established, with the measurement behind each point
- **Camera from the kiosk (`kiosk.py`, `geom3d.py`):**
  - The vertical-edge vanishing point is at (1033, 6444) and the top-face front-to-back vanishing point at (1461, 147).
  - These give f = 1181 px, a pitch of 11.0° and the horizon at row 153.
  - The walker's height from its given depths plus its bbox comes out at 1.833 / 1.782 m at t = 1 / 2 s, so the closure is 0.4%.
- **One common ground, shown by bbox height h against bottom row y1:**
  - Walker: h = 0.3805·y1 + 26.8.
  - Cyclist (head top to wheel bottom, frames 0-59): h = 0.3773·y1 + 20.8.
  - The lines are nearly identical, so both figures stand on one ground plane.
- **Ground in 3D (`ground2.py`):**
  - The walker's size-derived feet lie on a plane descending about 6-9° toward the camera, with an rms of 0.03 m.
  - Its size-derived distance is 11.89 m at t=1 (given 11.93 m) and 11.13 m at t=2 (given 10.82 m).
  - One scale puts all 60 of the cyclist's wheel contacts on that plane, with a spread of 0.008 m. That scale gives:
    - rider plus bike 1.74 m tall;
    - bike 10.6 m from the camera at t=1;
    - bike speed about 3.5 m/s.
- **The given bike depth scales with the body:** template matching shows the rider growing by 1.385-1.395 from frame 33 to frame 66, against a given depth ratio of 1.383. A rigid origin offset is ruled out. The given depth is a uniform factor of 1.55 larger than the common-ground distance, and the image alone cannot tell the two readings apart.
- **Handlebar height on the common ground (`h2_handlebar.py`):** the handlebar point sits at a horizontal setback behind the front contact.
  - Grips (v = 425.5 at t=1) with k = 0.3-0.5 m give 0.92-0.96 m.
  - Frames 20, 33, 45 and 55 give 0.98, 0.94, 0.95 and 0.93 m.
  - The image ratio to the walker's size line, with no setback correction, gives 1.005 m.

## Ruled out
- **The given-depth reading (C1-C3, about 1.41-1.55 m; my value at that scale is about 1.47):** it requires a 2.7 m seated rider (about 3 m standing) on a parallel plane 1.55 times farther from the camera. That fails the adult-size hard check.

## Open
- The only open point is the convention: whether the Blender scene really contains a scaled-up cyclist, which would make the answer about 1.47 m.
- The setback k is assumed from typical bike geometry, which leaves about ±3%.

### Round 2 (harness v3; files in context/round2/)
- Answer: 0.93 (switch, confidence medium, follows C4)
- Where the answers part: bike scale: given bike depth 16.49 m (C1-C3, 1.556x giant rider) vs common ground with the 1.8 m walker (C4/C5, round 1); secondary: handlebar setback behind the front contact (C4/C5 omit it)
- Fault proven: C1-C3's given-depth scale makes the seated rider 2.71 m (1.741 m common-ground height x 1.556), failing the adult-size hard check; C4/C5 put the handlebar directly above the front contact, so the grips, which sit 0.2-0.3 m behind it, read 5-10 pct too high
- Closure on the prior: 0.8 pct

# Round 2 addendum: q1756 (bicycle handlebar height)

**Proposed:** keep round 1's switch to the common-ground reading, with the value refined to **0.93 m** (round 1 had 0.95). Confidence is medium.

## Verified (my own code: measure.py, solve.py, setback.py, geom.py)
- **Same pixels as all earlier sessions.** At t=1 (frame 33): grips v = 425.5, stem v = 433, front-wheel bottom v = 559.5; walker rows 251-450 (overlay frames/overlay33.png).
- **Size against contact row:**
  - Walker: h = 0.3788·y1 + 28.1.
  - Cyclist: h = 0.3780·y1 + 20.9.
  - The lines are the same, so the rider plus bike is 1.741 m (SD 0.010 over frames 0-59) on the walker's ground.
  - At the given bike depth, the factor of 1.556 makes this 2.71 m seated. This reproduces round 1's fault proof for C1-C3.
- **Setback effect (image-only route):** the handlebar's ground foot is the point the front contact passed k/v earlier, with v = 3.2 m/s.
  - Grips at frame 33 with k = 0 / 0.2 / 0.3 give 1.018 / 0.948 / 0.914.
  - The stem with k = 0.2 gives 0.891.
  - Frames 20-55 agree within about 1%.
  - So C4/C5's 1.01 is the k = 0 value, and it is high.
- **Why round 1 got 0.95:**
  - Its 3D plane slopes 6-9° down toward the camera, and it measures the bbox height from the lower front contact (+k·tan(slope), about +0.04 m).
  - On level ground the value is 0.90-0.95.
  - Taking the middle of the two gives 0.93 ± 0.03.

## Open
- **Does the ground slope?** The evidence conflicts:
  - The walker's feet at its given depths are level at a pitch of about 13° (`geom.py`, camera height 3.07 / 3.09 m at t = 1 / 2).
  - The size lines of both figures extrapolate to h = 0 near row -60 rather than at the horizon (rows 110-150).
  - Effect on the answer: ±0.03 m.
- **Where the bbox top is (grips or stem) and the true setback k (0.2-0.35 m):** effect ±0.03 m.
- **The convention question remains:** the given bike depth matches the rider's apparent growth (ratio 1.383 vs 1.39), so it is image-equivalent to a 1.556x scaled cyclist. If the reference keeps that giant asset, the answer is about 1.45 m. Only the real-world-scale hard check rules it out.

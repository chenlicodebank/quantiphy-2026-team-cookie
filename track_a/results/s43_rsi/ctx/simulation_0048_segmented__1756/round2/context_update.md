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

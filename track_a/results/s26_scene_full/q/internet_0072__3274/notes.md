# q_3274 — acceleration of the credit card at 0.50 s (cm/s^2)

## Time base
- The file runs at a constant 26.846729 fps; I checked the PTS with `pts.py` and every step is 535/14363 s. The question states 30 fps.
- 26.85 fps is an unusual rate, which suggests the cut clip was re-timed from 30 fps footage, the usual rate for 4K phone or stock video. A hand moving the card is physically plausible at either rate, so physics cannot decide.
- I used **30 fps** (question_fps): t = 0.50 s → frame 15. At the file rate it would be frame 13.

## Scale (prior: card length = 8.56 cm)
- Card length = 432 px, measured from the left edge (x≈930) to the right edge (x≈1362) on the sharp rest frames 33–38. The scene record says 430–435 px, and I confirmed it on a zoomed crop of frame 37.
- Scale = 8.56 / 432 = 0.01981 cm/px.
- The blurred frames near 0.5 s show about 395 px. That reading would make the answer about 9 % higher (~81).

## Acceleration
- Track: the mask centroid in scene/tracks/card.csv (frames 8–38; ±3–5 px). The camera is static and the spotlight disc does not move.
- Raw per-frame second differences around frames 13–15 are noisy (2.6–8 px/frame²), so I smoothed them (`accel.py`):
  - local quadratic fit of x(t), y(t), centred on frame 15 with half-windows of 3–6 frames: 3.8–4.5 px/frame²
  - slope of a linear fit to the step lengths (speed) near frame 15: 3.3–4.2 px/frame²
  - quadratic fit of speed over frames 2–30, differentiated at frame 15: 4.6–4.85 px/frame²
- Adopted value: **4.2 px/frame²** (deceleration). Converted: 4.2 × 30² × 0.01981 = **74.9 cm/s²**, reported as 75.
- At the file rate (frame 13, ~4.3 px/frame² × 26.85²) the answer would be ~61 cm/s².

## Confidence
Moderate. The main uncertainties are the time base (30 vs 26.85 fps) and the noise in the second difference (about ±15 %).

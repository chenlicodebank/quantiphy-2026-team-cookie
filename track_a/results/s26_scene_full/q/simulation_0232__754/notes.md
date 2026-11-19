# Q754 – acceleration of the paper airplane at t = 1.25 s

Object: the scene record calls it an "arrow". A 4x crop at frame 30 shows it is the paper airplane seen almost
edge-on: a thin grey sliver. It is the only flying object. fps = question_fps = 24, so t = 1.25 s is frame 30.
The scene is 2D (frontal wall, motion parallel to the image), so I used one metres-per-pixel scale.

## Scale (prior: black cat speed = 0.714 m/s)
- Cat torso-centroid x from scene/tracks/cat.csv, frames 0–49. Linear-fit slope: 8.96 px/frame. Running means over
  one gait cycle (8–16 frames) give 8.93–8.99. The vertical motion is negligible.
- The cat speed is 8.96 × 24 = 215 px/s, so the scale is 0.714 / 215 = 0.00332 m/px.

## Airplane
- Per-frame points come from scene/tracks/arrow.csv: the fletching end (tail_x/y, the most reliable point) and the
  record's midpoint (ref = tail + 66 px along the shaft). The raw speed has about ±3 px/frame of noise.
- Speed rises to about 75 px/frame and holds until frame 22. After that it falls steadily: 66 at frame 24,
  about 61–64 at frame 30, 50 at frame 37. The motion is smooth (keyframed ease), with no impact.
- Fits of x(f) and y(f) for frames 20–41 (several windows), cubic and quartic (rms about 1 px), give
  speed(30) − speed(29) between −1.23 and −1.38 px/frame² (median −1.33). Quadratic fits do not fit the data
  (rms 3–11 px), so I did not use them.
- Acceleration = −1.33 px/frame² × 24² × 0.00332 m/px = **−2.54 m/s²**. The airplane is slowing down. As the
  answer must be positive, I give the magnitude: 2.54.

## Checks
- A linear fit of the raw per-frame speed against frame, over frames 24–36 or 26–34, gives −1.32 to −1.39
  px/frame², which agrees.
- Components at frame 30: vx ≈ 58 px/frame, dvx ≈ −2.0; vy ≈ 19, dvy ≈ +1.8. This gives dspeed ≈ −1.35, which
  also agrees.
- I re-tracked the airplane from scratch with background-diff masks (retrack.py). It is noisier because the pale
  nose drops out of the mask in frames 28–31. It gives −1.3 to −2.4 and only roughly supports the result. I trust
  the tail-based track more.

Confidence: moderate, about ±10%. The main risks are the 2D assumption (the cat and the airplane might be at
different depths) and the sensitivity of a single-frame speed difference to the fit choice.
Scripts: measure.py, measure2.py, measure3.py, catcheck.py, retrack.py.

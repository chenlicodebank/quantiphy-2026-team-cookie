# q_957 — body length of the phoenix (m)

Prior: acceleration of the phoenix at 2.0 s = 2 m/s^2. It's a 2D top-down video at 24 fps (file and question fps agree), so one m/px scale comes from the pixel acceleration.

## Acceleration (accel.py, accel2.py)
- Track: beak-tip x (scene/tracks/phoenix.csv ref_x) and body-template cumulative x (phoenix_body_shift.csv).
- The per-frame speed has a strong ripple at the flap period (1.04 s), so the one-frame acceleration at f48 is
  pure noise. I fit x(t) = x0 + v0 t + a t^2/2 + a flap sinusoid (period scanned; plus 2nd harmonic):
  - beak, frames 0-69: a = 378.8 px/s^2, v0 = -0.7 px/s (it starts from rest), P = 1.040 s, rms = 1.2 px
  - beak, frames 0-50 / 5-69 / 1-71: 378.8 / 378.6 / 379.3
  - body template: 370-384 (cumulative template drift makes it noisier, rms 2-4 px)
  - second route: mean speed over one flap cycle compared with the next cycle: 354-386 px/s^2
- The motion is uniform acceleration from rest with a flap-driven surge on top. The round prior (2 m/s^2) fits a
  designed constant acceleration, so a = 379 px/s^2 → scale = 2/379 = 5.277e-3 m/px.
- Alternative (not used): the local smoothed slope at f48 (~900 px/s^2, during a flap surge) would give about 1.6 m.

## Length (measure.py → extents.csv)
- Mask max|RGB-194|>12, 5x5 close, components ≥200 px. The overlay (frames/ov_24.png) covers everything from the beak to the tail tips.
- x extent (beak to tail tip, along the body axis), frames 0-68: median 716 px, range 684-750 (it changes with the tail
  pose), 707 at frame 0.
- Length = 716 px × 5.277e-3 = 3.78 m (pose range 3.61-3.96 m).

Confidence: moderate-good. The main risk is whether the reference acceleration is the constant 2 m/s^2 (assumed here), and the pose dependence of the extent is ±5 %.

# q_2515 — velocity of the red ball at 0.8 s (cm/s)

t = 0.8 s -> frame round(0.8 x 24) = 19 (file fps = question fps = 24).
Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
Ball centres: scene/tracks/red_ball.csv (cx, cy_corr), checked on a zoomed frame 19 (frames/f19.png): the ball is at
about (761, 420), with horizontal motion blur, so the pixel diameter is biased there.

## Problem
Only 4 depths are given (f5 0.8715, f10 1.166, f14 1.372, f19 1.315 m). The ball goes round a fast, roughly
elliptical conical-pendulum orbit (period about 26 frames). At f19 it is moving right AND quickly toward the camera,
so a per-frame depth estimate is needed around f19.

## Method (fit_orbit.py; plane3d.py was an exploratory plane fit)
- Per-frame depth cues: (a) the ball's pixel diameter, Z = 0.07 f / D, scaled by 1.019 to the given depths (the
  per-point ratios are 0.98-1.05); (b) a constant-height plane, Z = f·Y/(v - cy), with Y ≈ 0.116 m from the given points.
- Fit Z(t) with a 2- or 3-harmonic periodic model, pinned to the 4 given depths, which it reproduces to within 1 mm. Then
  X = (u - cx)/f·Z and Y = (v - cy)/f·Z, using the measured pixel centres.
- Speed near f19:
  - diameter cue, K=2: |p20 - p19| x 24 = 2.25 m/s, |p19 - p18| x 24 = 2.12 m/s; the mean speed over f17-21 is 2.23;
    the 5-frame mean velocity vector is 2.07 m/s, lower because it cuts across the curve.
  - diameter cue, K=3: 2.21 / 2.12 / 2.20 / 2.05 (same four quantities).
  - height-plane cue: 2.55 m/s per frame and 2.34 m/s for the 5-frame mean velocity. This is noisier, because the image y
    hardly changes at the far side of the orbit.
  - combined cue: 2.37 and 2.18 (per-frame speed and 5-frame mean velocity).
- Lateral component about 1.0 m/s and depth component about -1.8 m/s, which together give about 2.1-2.3 m/s.

## Second route
The two depth cues are independent (ball size vs height-plane geometry) and give 2.1-2.5 m/s. The diameter cue is more
reliable, and its smoothed values cluster at 2.05-2.25 m/s.

## Answer
About 2.2 m/s = **220 cm/s**. Confidence: moderate (±10-15%). The answer depends on the depth trend between the given
samples, which was estimated from the ball's apparent size.

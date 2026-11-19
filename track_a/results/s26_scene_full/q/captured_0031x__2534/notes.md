# q_2534: tennis ball velocity at t = 1.6 s (cm/s)

t = 1.6 s -> frame round(1.6*24) = 38 (question_fps = file fps = 24). Ball rolling on the table toward the camera
(it leaves the front edge at frame 42/43), so frame 38 is a clean on-table frame.

## Method (lab card)
- f = 0.5959*1280 = 763 px, principal point (640, 360).
- measure.py: yellow mask per frame (scene/track.py thresholds), least-squares circle fit to the upper/side contour
  (bottom excluded: reflection on the table) -> centre (u, v) and diameter d per frame (circ.csv; overlays frames/fit_*.png).
- velocity.py: depth per frame Z(i) = 1.19 m * d(38)/d(i) (depth_info at 1.6 s; Z ∝ 1/apparent size). d smoothed by
  its linear relation with image row (on a plane 1/Z is linear in v): d = 0.506 v - 178.1, rms 0.6 px.
  Back-projection X = (u-cx)Z/f, Y = (v-cy)Z/f. Z goes 2.01 m (rest) -> 1.19 m (f38) -> 1.09 m (f42).
- Motion is mostly along depth: at f38 velocity components ~(-18, +1, -70) cm/s.

## Results (cm/s)
- Local quadratic fit centred on f38: ±2 frames 59, ±3 frames 72, ±4 frames 76.
- 5-frame moving average then forward diff at 38: 62; backward diff: 82.
- Path-length fits: frames 16-42 linear 83 / quadratic at f38 76; 30-42 linear 79 / quad 74; 36-42 linear 61.
- Per-frame speeds are irregular (frame 35->36 step ~2x normal, 38->39 ~0.4x): uneven capture timing, so
  short windows scatter; the ball rolls at a roughly steady ~75-80 cm/s with slight deceleration.
- Route 2 (d with u-dependence): about 5% lower than route A; route C (raw diameters time-smoothed) agrees with A within 2%.

Answer: 72 cm/s (middle of the local-window estimates, slightly below the long-window steady speed).

## Caveats
- Implied ball diameter at f38 from depth_info: 1.19*50.9/763 = 7.9 cm vs prior 6.7 cm (mask/edge ~15% larger, or
  depth_info short). Scale taken from depth_info as instructed; using the prior size instead would raise Z, and the
  speed, by ~18%.
- Confidence: moderate (±15%).

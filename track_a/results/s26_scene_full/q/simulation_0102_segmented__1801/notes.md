# q_1801: initial speed of the shark (prior: shark acceleration = 1 m/s^2)

2D clip at 24 fps (question_fps is also 24, so no re-timing). The shark is at rest in frames 0-1, then swims left
with constant acceleration until its nose leaves the left edge at frame 58.

Method (fit.py): fit a quadratic x(n) to the shark's horizontal position over frames 1-58, using the scene record's
rigid template track (rms 0.27 px), the nose bbox_x0, the bbox centre and the mask centroid.
- Template: a = 0.148 px/frame^2. Velocity at motion onset (frame 1) = 7.37 px/frame; at frame 1.5 (the first
  step) = 7.44 px/frame.
- Scale-free ratio: v0 / a = v0_px[px/frame] / (24 * a_px[px/frame^2]) seconds. The scale is
  1 m/s^2 / (a_px * 576), so v0 [m/s] = v0/a [s] * 1 m/s^2.
- Template gives 2.07-2.10 s. Bbox x0, bbox centre and mask centroid give 2.01-2.10 s. The 2-40 and 10-58 windows
  agree within ±0.03.

Answer: v0 = 2.07 m/s. If the simulated value is a round 2.0 or 2.1, this is within 4%. Confidence: good.

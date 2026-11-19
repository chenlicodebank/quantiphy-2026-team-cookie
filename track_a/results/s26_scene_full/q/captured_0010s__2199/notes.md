# q_2199 — ball velocity at t = 0.3 s (frame round(0.3·24) = 7)

The file and the question both run at 24 fps. The scene is a pendulum swinging mostly toward and away from the camera. Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).

## Measurements (measure.py → ball2.csv)
- Ball centroid from the red mask, as in the scene record.
- Ball diameter: the widest horizontal chord at the half-max level of the (R−G) signal, with sub-pixel edges. The record's equiv_diam
  is inflated by vertical motion blur at mid-swing (frame 7: 31.1 px against a true width of 27.5 px). With the width, depth × width is consistent
  across all 6 depth_info points (46.8–49.5, mean 48.0 → ball ≈ 6.3 cm). With equiv_diam it was 47.5–54.

## Route 1: 3D pendulum model fit (fit_local.py, main result)
Unknowns: the ball moves on a planar circle about a pivot (pixel, depth, L, gravity pitch/roll, plane azimuth) plus a free angle θ per frame.
It is fitted to u, v (rms 0.3 / 0.15 px), to the width (k/dist) and to the depth_info distances (reproduced within ~0.01 m).
Fitted over frames 0–22: L = 0.349 m (a small-angle period of 1.19 s, about right for the observed 1.23 s at ~45° amplitude).
Speed at f7: forward difference 1.10, mean of the forward speeds over f5–f9 1.08, central 1.02 m/s.
Variants (pivot pixel fixed, frames 0–17 or 0–30, no width term) give a forward speed of 1.05–1.13 and a 5-frame mean of 1.03–1.12.
Energy check with g = 9.8 (the prior): sqrt(2gL(cosθ7 − cosθfar)) = 1.05–1.21.

## Route 2: depth from width, back-projected (route2.py)
Depth per frame = 48.0/width (smoothed with a local quadratic), giving 3D centres. The mean forward speed over f5–f9 is 1.07, and the forward
difference of the 5-frame-smoothed positions is 0.99 m/s. Noisier, but it agrees with route 1.
The image-plane part alone is 0.76 m/s, which is a lower bound.

## Answer
Using the reference convention (forward difference smoothed over about 5 frames): **1.08 m/s**.
Confidence: moderate, about ±7%.
Caveats: there seems to be a timing glitch or dropped frame between f11 and f12 (a jump in position and size), outside the f5–f9 window.
The second swing (f36–48) does not fit a single planar pendulum: the swing plane drifts.

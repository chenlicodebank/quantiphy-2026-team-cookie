# q_2417 — book velocity at t = 1.4 s (cm/s)

t = 1.4 s -> frame round(1.4*24) = 34 (file fps = question fps = 24). At f34 the book has just landed on the table
top (landed f33) and is sliding toward the camera; it stops at f37 (checked on frames 29-38, frames/seq.png).

## Method (lab card: f = 763 px, cx,cy = 640,360)
- edges.py: column-averaged (cols 520-630) gray profiles; the dark contact line under the page block gives sub-pixel
  bottom-edge rows: f33 496.0, f34 501.0, f35 504.0, f36 508.3, f37 509.3, f38 509.3 (rest).
- speed.py: the book slides on the horizontal table, so its front-bottom edge lies on the table plane at height H below
  the camera: Z = H f / (v - cy). The centre is a fixed offset from that edge (rigid translation), so the centre's
  velocity = the edge's velocity. H calibrated from depth_info: rest-frame centre distance 0.851 m (t=1.6) -> H = 0.153 m;
  or from f34 centre distance 0.857 m -> H = 0.146 m (centre depth / edge depth ratio from the cover's front/back edges).
  Lateral motion (right end fixed at x~654) adds < 0.01 m/s.
- Per-frame forward speeds (m/s): f33 0.70-0.73, f34 0.40-0.42, f35 0.54-0.57, f36 0.12-0.13, f37 0.
- Central differences at f34: 0.55-0.57 (f33-f35), 0.47-0.49 (f34-f36). A 5-frame centred mean (f32..f36, f32 still
  ~0.8 m/s at the bottom of the ramp) is ~0.52 m/s.

## Second route / checks
- Given depths alone: f29 (1.02 m) -> f34 (0.857 m) centre displacement 0.176 m in 5 frames = 0.84 m/s average coming off
  the ramp, which fits a speed that is falling from ~0.8 to ~0.5 m/s at f34.
- The prior (|a| = 2.8 m/s^2, read as friction deceleration) with a stop at f36.5-37 gives 0.30-0.35 m/s; that is lower
  than the image says (the stop looks abrupt).
- The given depths are not self-consistent: 0.857 (f34) vs 0.851 (f38), while the image shows ~5 cm of motion toward the
  camera between them (bottom edge moves 8 px, length grows 167 -> 176 px). This is the main uncertainty in the scale and in the reference.

Answer: 50 cm/s (range 41-57). Confidence: moderate.

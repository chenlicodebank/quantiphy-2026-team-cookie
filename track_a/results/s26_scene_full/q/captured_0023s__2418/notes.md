# q_2418 — length of the book (cm)

Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Scale: depth_info t=1.6 s (frame 38) book distance 0.851 m; the book is at rest on the table from f37 to the end.
(The acceleration prior is not needed for a size.)

## Main route: 3D box fit at rest (fitbox.py)
Corners read at 12x zoom on f40 (ends.py; identical to f38): cover top far-left (478,484.5), far-right (641,479.5),
near-left (478.5,498), near-right (653,492); page-block bottom near-left (480,512), near-right (653.5,505.5).
The cover quad is not symmetric (far edge 163 px, near edge 174.5 px, right end slanted, left end vertical), so the
book is yawed (~13 deg) as well as seen in perspective. Fitted a box (L, W, T, yaw, camera pitch, roll, centre pixel)
with the centre on its ray at 0.851 m Euclidean distance: L = 0.1845 m, rms 0.37 px; Monte-Carlo +-0.7 px on the
corners: sd 0.09 cm. Fixing camera pitch at 0..45 deg gives L 18.3–19.0 cm (best fit at pitch 4 deg, consistent with
the horizon near the principal row in the record).

## Checks
- Midline (average of far/near cover edges, 168.6 px) x Z (0.830 m, depth component of the 0.851 m distance) / f
  = 18.3 cm (ignores yaw).
- f29 (t=1.2 s, depth 1.02 m, Z 1.012 m) on the ramp: cover length along its 8 deg tilt ≈ 137 px (blurred) → 18.2 cm.
- f34 (t=1.4 s, depth 0.857 m, Z 0.842): ≈165 px midline → 18.2 cm.
- Naive bbox route (record's length_px 175 at rest, which is the near-edge/corner extent, x 0.851 / f) = 19.5 cm —
  overestimates because it takes the nearest edge, the yaw, and the Euclidean distance instead of Z.

Answer: 18.4 cm (confidence: good, ~±3%).
The scene record's bbox (477–652) agrees with my corner readings; no correction needed besides the interpretation.

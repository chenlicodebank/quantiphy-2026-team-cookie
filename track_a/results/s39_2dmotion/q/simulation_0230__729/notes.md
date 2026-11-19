# Q729: speed of the paper airplane at t = 1 s (m/s)

- The file is 24 fps and question_fps is 24, so t = 1 s is frame 24. Speed = |p(24) - p(23)| x 24.
- 2D scene. Scale comes from the prior, chalkboard length = 5 m.

## Chalkboard pixel length (measure.py: column-gradient edges in 4 row bands, frame 24)
- Outer wooden frame: x ≈ 320 to 1692.5. Width 1368–1376, about **1372 px**, which matches the scene record (1372).
- Green surface only: 1328–1330 px.
- SAM 3 "chalkboard" mask: box 324–1690, so 1366 px (horiz_px 1358). That is within 0.5–1 pct of my outer-frame value.
  The left edge is blurred by the sunbeam, which explains the small difference.
- The chalkboard object includes its frame, so I use 1372 px. Scale = 5/1372 = 0.003644 m/px.
  - If only the green surface counted (1329 px), the answer would be 6.27 m/s, which is +3.2 pct.

## Plane displacement, frames 23 → 24
| method | p23 | p24 | step px |
|---|---|---|---|
| scene ref (nose–tail midpoint) | (1027.9, 342.7) | (1097.1, 345.6) | 69.3 |
| my bg-diff bbox midpoint | (1028.0, 342.0) | (1097.0, 342.5) | 69.0 |
| my bg-diff centroid | (1020.2, 341.2) | (1092.0, 342.9) | 71.8 |
| SAM 3 mask centroid | (1019.1, 341.3) | (1092.7, 343.2) | 73.6 |

- The centroids are biased because the plane's pitch changes: the mass sits toward the tail, and that bias varies from frame to frame.
  The SAM mask is also shorter (134–137 px against 136–137 px for bg-diff), with ends cut differently in each frame.
  The midpoint of the plane's extent is the better stand-in for the origin.
- Second route, a smoothness check: the midpoint x-steps over frames 21–26 are 72.5, 69.5, 69.0, 68.0, 65.0, a smooth
  deceleration. The local trend at frame 23.5 is ≈69 px/frame.
- Adopted step: 69.4 px/frame, giving 1666 px/s and **6.07 m/s**.

Confidence: good on the motion (±2 pct). The main uncertainty is whether the board length includes the frame (±3 pct).

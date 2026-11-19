# q1550 — vertical (water-depth) difference between the shark and turtle centres

Answer: **2.18 m** (the shark is about 2.2 m higher than the turtle).

The file and the question both use 24 fps. 3D Blender render with a static camera; principal point taken as (960, 540).

## Focal length (from the turtle prior a = 2.639 m/s^2 and the given distances)
- The scene/ turtle core centroid is too noisy (±5–10 px, with a jump at f6) to fit an acceleration. I re-tracked the
  rigid shell with LK features (`shell_track.py`): a similarity transform per frame step, with the reference point
  starting at the f0 core centroid. The track is smooth and from rest: the image speed grows about linearly from
  0.3 px/frame.
- Model (`fit_line_scan.py`): straight-line motion with constant acceleration, P(t) = P0 + d·(v0 t + a t²/2),
  fitted to the shell track (u, v), with the given camera distances at t = 0 and 0.5 s as hard constraints.
  For each f I find where the fitted |a| equals 2.639:
  - v0 free: f ≈ 2230–2800, depending on the frame window (0–40 or 0–30) and the shell region (0.4/0.55/0.7).
  - v0 = 0 (start from rest, which the track supports): f ≈ 2440–2500, the same for every track and window.
    With a fixed at 2.639, the fitted v0 also crosses 0 at f ≈ 2450.
  - Adopted value: **f = 2480 px** (horizontal field of view ≈ 42.3°). Uncertainty is about ±8%.
- Fit residuals are 0.5–1.2 px. With this f the fitted turtle direction has a vertical component of about 0, and so
  does the shark's (separate fit on frames 0–37): both animals swim horizontally. This supports a level camera, so
  camera Y is the water-depth axis.

## Vertical positions (back-projection with the given distances, `vdiff.py`/`vdiff2.py`)
Each centre is the core centroid averaged over ±2 frames. At f = 2480:
- t = 0: shark Y = −1.274 m and turtle Y = +0.911 m (Y points down), so Δ = 2.185 m.
- t = 0.5 s: shark −1.247 and turtle +0.907, so Δ = 2.153 m.
- Shark straight-line fit, f fixed: Y = −1.261 at f0 and −1.260 at f40 (constant). The turtle fit gives Y ≈ 0.90–0.91,
  also constant. So Δ ≈ 2.17 at every time.
- Second route: the turtle track and model give the same Y independently of the core centroids (0.90 vs 0.91).
- Sensitivity: Δ scales as 1/f: 2.34 at f = 2300 and 2.02 at f = 2700.

## Confidence
Medium. The main error source is the focal length taken from the acceleration fit, about ±8%. The origin offsets
(core centroid vs rig root) add about ±0.05 m.

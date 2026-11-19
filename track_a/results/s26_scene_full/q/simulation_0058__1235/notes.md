# Q1235 – length of the white car (the white van), metres

Answer: **5.58 m**

The only white vehicle is the van crossing left to right behind the taxi (scene/notes.md and frames). The question rate
(24 fps) is the same as the file rate.

## Scale (focal length from the acceleration prior plus depth_info)
- measure.py: for a trial focal length f (principal point at the image centre), the van origin (box centre, body mid-row)
  is back-projected at frames 14 (t=0.58) and 38 (t=1.58) using the given depths 31.070 / 29.918 m. This defines its 3D
  straight motion line. Each frame's ray is then intersected with that line, which gives the path coordinate s(t). It uses
  the record's rear-edge track (row 520). I checked that track against my own background-difference edges (edges.py).
- A quadratic fit of s(t) over the clean frames 3–46 is solved for an acceleration of 4 m/s², which gives **f = 2284 px**
  (HFOV ≈ 51°). Other windows give 3–27: 2280, 20–46: 2263, 3–36: 2295. After frame 46 the rear-edge track is jumpy,
  so those frames are not used.
- Consistency: with this f the fit gives v0 ≈ 0 and rest at t ≈ 0. So the van starts from rest at a constant 4 m/s², and
  the per-frame accelerations scatter around 4.0 in frames 3–40.

## Length
- Bumper-to-bumper pixel extent at row 600 (from my own background difference, edges.py): 451–453 px in frames 36–40,
  and 464–468 px in frames 64–66, where it is larger because it is further off-axis.
- length.py models the van as a box (length L, width W ≈ 2.0 m) centred on the 3D origin and oriented along the motion
  line. It projects the box corners and solves for L so the projected extent matches the measurement. The near side is
  about 1 m closer than the origin, which is why this is about 5% below the naive value.
  - f = 2284, W = 2.0: L = 5.56 (mean of frames 36–40). Frames 64–66, a different viewing angle: 5.52–5.57. W = 1.9 / 2.1
    changes L by ±0.02.
  - f range 2263–2295 gives L = 5.55–5.62.
- Naive value (pixel length × origin depth / f, ignoring the near-side offset): 5.88 m. This is an upper bound.
- Frame 0 is not usable: the taxi hides the van's front at row 600.

## Second-route check
The second route is the far-off-axis frames 64–66. They give the same L (5.52–5.58) with the same f, which confirms f and
the box/perspective model. Sanity checks: the van height of about 170 px gives 2.2 m, and a 5.6 m length fits a
full-size van (Chevy Express-like).

Confidence: moderate-good, about ±3%. The main uncertainties are the rounded-corner silhouette compared with the box
model (which could push L up slightly) and the f window.

# q1230: width of the orange car (m) -> 2.33

The video file runs at 29.9936 fps and question_fps is 30, so t = 1 s is frame 30. The camera is static.
Inputs used: D_orange(t=0) = 19.377 m, D_orange(t=1) = 11.858 m. The acceleration prior (-2.86 m/s^2) was used only
as a consistency check.

## Width = f·W / f
1. **Pixel width.** The widest part of the car is the mirror-to-mirror span. The front body is about 0.89 of it in 3D,
   and the AABB includes the mirrors.
   - Background-difference mask (`carmask.py`), then the mirror tips per frame (`mirrors.py`), checked visually in
     `frames/mirrors_vis.png`.
   - The tips are good for f0-f30; later the detector slips onto the body.
   - Span: 193 px at f0, about 320 px at f30.
2. **Depth of the mirror plane.**
   - The car's scale change S(t) was tracked with SIFT similarity fits chained over steps of 1, 2, 3 and 5 frames
     (`sift_scale.py`).
   - Z_origin at t = 0 and t = 1 comes from the given D with the off-axis correction (small).
   - Regressing 1/span on Z_front(t) over f0-f29 (`width_fit.py`) gives f·W = 3627-3642 px·m and puts the mirror
     plane at Z = 18.8 m at f0, about 0.55 m in front of the origin. Fit rms is 0.45%.
   - Second route: the two-point solution using only the given D at t = 0 and t = 1 and the spans at f0 and f30
     gives f·W = 3560-3770 (W = 2.30-2.43 at f = 1550, for span30 = 315-327).
3. **Focal length.** The scene is not at real scale, so f comes from geometry:
   - **Vanishing point of the street direction:** (884.5, 1006.5), from about 50 road and building lines that all
     agree (`vp_split.py`).
   - **Camera roll:** about 1.4°, seen in the building and lamp verticals (`vpvert.py`).
   - **Route a, sidewalk tile joints across the street** (`vp3b.py`): their vanishing point is (18100, 600). The
     horizon through the two vanishing points slopes -1.36°, which matches the roll. Orthogonality with a
     principal point at the image centre gives **f = 1545 ± 110**. This is insensitive to cy.
   - **Route b, the hydrant's 6-bolt flange circle** (`bolts.py`, `bolts2.py`): ellipse axis ratio 0.422-0.424,
     against a predicted ratio of |g·r| → **f ≈ 1515-1540**.
   - **Route c, ground plane** (`ground.py`), assuming the hydrant and lamp origins are at their bases: the hydrant
     and the far lamp give the same camera height at **f ≈ 1720** (range 1500-2050 for ±6 px). This assumption is
     weaker.
   - Weighted combination: **f ≈ 1560 px** (horizontal FOV ≈ 67°).
4. W = 3637 / 1560 = **2.33 m** (mirror to mirror; AABB).
   - Body-only width (wheel arch / fender) ≈ 2.08 m, for reference.
   - Under the plain "wheel to wheel without mirrors" reading the answer would be ≈ 2.1 m. I answer with the AABB,
     which includes the mirrors.

## Checks and caveats
- **Acceleration prior.** The quadratic fit of 1/S(t) with a = -2.86 gives Z_front(0) ≈ 15.3-16.7 m. The D-based
  value is 15.9 m, so the two are consistent.
- **Record corrections.** The record's vanishing point (923, 1050) is off; the measured one is (884.5, 1006.5). Its
  bbox_w is not a fixed feature, because the visible side panel and perspective widen it.
- **Not used.** The man's given depths do not fit a rigid ground-plane model.
- **Confidence.** The main uncertainty is f, about ±6%. The width is about 2.33 ± 0.15 m.

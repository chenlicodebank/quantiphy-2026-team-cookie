# Q1498 – width of the central sculpture's square pedestal (m)

Answer: **1.45 m**

## Geometry
- Nadir (top-down) camera, static. The floor is parallel to the image plane, so one floor scale holds everywhere. The plinth sits at the
  image centre (960,540), directly below the camera. File fps 33.0044 vs question_fps 33 (I used frame numbers only).
- Floor scale from the prior: the person's floor point moves 3.952 px/frame (footprints at mid-stance lie on a straight line, steps
  67.4 px every ~17 frames). s_floor = 1.3/33/3.952 = 0.009968 m/px. This gives natural gait values (0.67 m steps, 1.96 steps/s).
- Plinth top face measured in code (edges.py): x 882→1038, y 462→616, so ~156 px (155–156).

## Route 1: depth_info and the floor scale (solve.py)
H = s_floor·f. Each bench seat gives d = (H−hb)·sqrt(1+(r/f)²) with r = 389 / 374 px. The left and right benches agree for every hb.
With seat height hb = 0.40–0.45: f ≈ 1039–1045, H ≈ 10.36–10.42, which puts the pedestal origin at H − 9.967 ≈ 0.39–0.45 m.
W = 156·(H − h_top)/f, giving 1.50 (top at the origin height) down to 1.44 (origin at the box centre, top ≈ 0.8 m).

## Route 2: the plinth's cast shadow (shadow_edges.py), which needs no f
The square shadow of the plinth's top face on the floor has corners at (907,431) and (1052.5,577), so it is 145.5 × 146 px. A shadow has
the true size of the top face at floor scale, so W = 145.5 × 0.009968 = **1.450 m**. The same numbers give K_top = 156/145.5 = 1.072,
so h_top ≈ 0.07·H ≈ 0.71 m. That is consistent with the origin at the box centre (≈0.40 m, so the box is ≈0.8 m tall). Plugging
h_top = 0.71 into route 1 gives 1.449 m. Both corners show the same shadow shift (+20, −36 px), and the slant of the corner-edge
shadow matches it.

## Not used
The human distances (9.24 → 9.14 m) change much less than the body's motion implies (expected about 0.4 m over 1 s). This is the case
where the animated character's origin lags the body, so I did not use them. The person's lean, taken with H ≈ 10.4, implies he is about
2.1 m tall. That is suspicious, but the answer does not depend on it: the scale comes from the speed prior and is confirmed by the
static depths (bench seat ≈ 0.4 m, a plausible value).

Confidence: about ±3% (shadow edges are soft, ±2 px).

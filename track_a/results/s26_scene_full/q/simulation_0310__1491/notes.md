# q_1491 – forklift width (wheel to wheel), simulation_0310

Question: width of the forklift from the left wheel to the right wheel (m). Prior: forklift height = 2.47 m.
depth_info: 16.7953 m at t=1 s (frame 24) and 19.0980 m at t=2 s (frame 48). File fps = question fps = 24.

**Answer: 1.47 m**

## Method (3D, static camera, the forklift only translates)
1. **Calibration** (`lsd_all.py`, `vp_ransac.py`, `calib_fit.py`). I found the vanishing points of the forklift's along,
   across and vertical edges from LSD segments in 24 frames, plus the focus of expansion of 200+ KLT tracks
   (`track_vp.py`, `vp1.py`; FOE ≈ (−2034, −806), and the strip-end paths agree at (−2145, −847)). Then a joint fit of f, pitch,
   roll and yaw with the principal point at the centre. Results: f ≈ 3546 px (lines-only fit 3445), pitch 23.2°,
   roll 0.0°, yaw ≈ 41°. Fixed-f refits (driver.py) give a fit cost of 87.6 at f = 3300, **70.8 at 3546**, 89.1 at 3830 and 126 at 4100.
   Check: the roof's orange rear strip, triangulated independently, comes out purely across the vehicle (ΔX ≈ 0, ΔZ ≈ 0.001 units).
2. **Structure from pure translation** (`sfm.py`, `tri_pts.py`, `geom.py`). I recovered the per-frame translation s(t) from the
   KLT tracks (reprojection median 1.0 px) and triangulated key points from several frames in units of the frame 0→71 translation:
   the roof strip ends (detected automatically in every frame, `strip.py`), the roof top corners, the mast top,
   the near rear and front tires (outer-sidewall bottom and hub), the far counterweight band tip, and the far rear tire silhouette (frame 71).
3. **Scale from the prior.** Height = roof top (the highest part; it is above the mast top) minus the tire bottom
   = 0.2735–0.2781 units, so 2.47 m gives 8.88–9.03 m per unit (mean 8.955).
4. **Width.** Centreline = midpoint of the roof strip ends (symmetric part). Results at f = 3546:
   - near rear tire outer-sidewall bottom: 2 × 0.0796 → 1.41 m
   - near rear tire left silhouette (frame 71, cylinder model): 2 × 0.084 → 1.49 m
   - far rear tire right silhouette, peeking past the counterweight at frame 71 (`tire_model.py`): 2 × 0.0833 → 1.48 m
   - near front (drive) tire outer bottom (`front_tire.py`): 2 × 0.0823 → 1.46 m
   - near-to-far rear tire directly, with no symmetry assumption: 1.45–1.50 m
   - for comparison: counterweight body ≈ 1.16 m and roof strip ≈ 0.93 m. The tires stick out past the body, which matches the far tire
     being visible to the right of the counterweight at frame 71.
   Mean ≈ 1.46 m with the max-roof scale, or 1.47 m with the mean-roof scale.

## Second-route checks and caveats
- Near/far symmetry about the roof centreline is best at f ≈ 3550 (near 0.084 vs far 0.083 units). At f = 3830 or 4100 the near and
  far sides disagree, and the front tire gives a very different value (`sens.py`). This supports the calibrated f.
- **Inconsistency with depth_info.** For any point on the vehicle, the reconstruction gives D48/D24 ≈ 1.11–1.125, against
  the given 1.137. The depth-based scale (about 9.5–9.8 m/unit) is ≈8% larger than the height-based one, and would make the
  forklift ≈2.69 m tall. I could not resolve this: it may be an unusual origin location, a timing offset or a lens shift.
  I used the question's own exact prior (height) for scale. With the depth scale instead, the width would be ≈1.55–1.6 m.
- Confidence: moderate. Spread between routes is ±3% at fixed f. f uncertainty adds about ±3%, and the scale conflict
  is the main risk.

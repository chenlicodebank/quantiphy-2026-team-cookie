# q_1492 — acceleration of the forklift at t = 1.0 s (simulation_0310, 3D render)

The file fps (24) and question_fps (24) are the same. t = 1.0 s is frame 24 and t = 2.0 s is frame 48.
Prior: forklift height 2.47 m. Given depths: 16.7953 m at frame 24 and 19.0980 m at frame 48.

## Method
1. **Motion vanishing point (epipole).** The forklift translates rigidly and in a straight line, so SIFT matches on the
   forklift between frame pairs (24-48, 12-36, 36-60, 0-24, 48-71, 20-52) lie on lines through one epipole.
   Result: e ≈ (-2020, -805) px; the six pairs agree within about 40 px (`epipole.py`, `epi_scan.py`).
   A projective fit of the track under constant acceleration gives the same point independently: (-1920, -815) (`fit_track.py`).
   This sets the horizon at v ≈ -805.
2. **Vertical vanishing point.** Ridge-traced trunks of the left and right pines (`trunks.py`) meet at about (1263, 9626).
   So roll ≈ 0, and the fork-carriage edges agree (they imply V ≈ 9360).
   Focal length from the two orthogonal vanishing points, with the principal point at the image centre:
   **f = sqrt(-(e-c)·(V-c)) ≈ 3678 px** (horizontal FOV about 38°), camera pitch 22.4°.
3. **Height check of f** (`check_f.py`, `mast.py`). With the camera height set by the depth at frame 24, the mast-top
   pixel (1712, 583), placed about 0.2–0.4 m ahead of and 0.5–0.9 m beside the near front-tyre contact, reconstructs to
   2.4–2.6 m. That agrees with the 2.47 m prior for f ≈ 3500–3850.
   The wheelbase reconstructed on the ground is 1.91 m in both frames, and the wheel line is parallel to the motion
   (1.6° and 0°), so the geometry holds together.
4. **Displacement 24→48.** For pure translation, p48 - e = k (p24 - e) with k = z24/z48. Measured k = 0.880 (orange
   centroid and median of SIFT points), which gives a z-ratio of 1.1368. The given depth ratio is 1.1371.
   Tz = 2.30 m (depths read as z-depths), 2.26 m (Euclidean at frame 24 only) or 2.29 m (Euclidean at frame 48 only);
   mean 2.284 m. The motion direction in camera coordinates is ((e-c)/f, 1), so D = Tz × 1.406 = **3.21 m**.
   This hardly depends on where the root pixel is.
   Caveat: reading both depths as Euclidean while keeping f = 3678 would give D = 3.63 m. That contradicts the measured
   image motion (the root would have to sit 2.4 m from the vehicle body), so I rejected it.
5. **Motion law** (`accel2.py`). Each frame's position s(t) along the motion, in metres, comes from its homothety ratio
   about e. A quadratic fit gives rms 7 mm and a = 2.07 m/s². A cubic fit gives a(1.0 s) = 2.08–2.09 and a(2.5 s) = 2.04–2.05,
   so the acceleration is constant. Sliding 24-frame windows give 1.92–2.22, which scatters around 2.07.
   The benchmark convention (one-frame differences of the fitted s) gives a(24) = 2.070 m/s² and v(1.0 s) = 2.13 m/s.
   Implied start of motion: about t = -0.05 s.

## Answer
a(1.0 s) ≈ **2.07 m/s²** (uniform acceleration).

## Second route and confidence
- Cross-checks: whole-clip quadratic, cubic, windowed fits and the benchmark difference convention all give 2.04–2.09.
  Two independent vanishing-point routes (SIFT epipole, constant-acceleration projective fit) agree.
  The height prior reproduces 2.47 m near f ≈ 3600–3850.
- Sensitivity: f ±5% changes a by about ∓2.5%; how the depths are interpreted changes it by ±2% (range 2.03–2.09 for f = 3678).
  Overall uncertainty is about ±5%. Medium-high confidence.

# q1221 – height of the streetlight (m)

3D Blender render, 1080x1080, file fps = question fps = 30. Static, level camera (principal point assumed at 540,540).
Scale: pinhole camera with depth_info; streetlight distance 8.901 m (to its origin = bbox centre, see the check below).

## Lamp pixel extent (lamp.py, frame 0)
- Top of the finial: row 121.0 (half-intensity transition). Bottom of the base: row ~894.8 → raw extent ≈ 774 px
  (the record's 777 px at y 121-898 was read by eye; 898 includes the soft contact shadow).
- The lowest image point of the base is its front-bottom edge (base half-width 36.5 px, nearer than the axis). Projected
  onto the axis plane, the extent is ≈ 774 − 356·36.5/f ≈ 766 px. Without this correction H would be 1 % larger.
- Axis u = 813.5; projected centre v ≈ 504.5.

## Focal length
1. Man (two depths, constant depth, man_f.py): pelvis u 1071 (f0) and 981 (f30), d 8.313/8.189 → f ≈ 1621 (±~30 for ±2 px),
   Z_man 7.84 → man height ≈ 1.79 m (plausible).
2. Car (geom.py/fitcar.py): rear-edge track frames 49-77 is exactly quadratic (rms 0.15 px, A = −438 px/s²); extrapolated to
   t = 0 together with d0 = 16.059 and d1 = 11.671 → f ≈ 1631, and the implied a = −2.86·(431/438) ≈ consistent with the prior
   to 1.6 %; forcing a = −2.86 exactly gives f ≈ 1653. The front-edge track of frames 21-40 (blurred nose) gives smaller
   pixel decelerations and f ≈ 1470 if constant −2.86 is enforced over 0-1 s; rejected, it does not reproduce d0 with the
   late-track model and gives an implausible 1.97 m man / 5.4 m car.
3. Static consistency: with f = 1621 and camera height from the man (1.94 m), the ground rows give distances to the
   centres of the lamp (8.906 vs 8.901 given) and the hydrant (9.21 vs 9.207 given) → origins are bbox centres.
   (The lamp+hydrant-only route is too sensitive to 1 px to fix f on its own: 1480-1620.)
Adopted f ≈ 1630.

## Result
H = 766 px · 8.901 / sqrt(f² + 273.5² + 35.5²): f 1621 → 4.15 m, f 1640 → 4.10 m, f 1655 → 4.06 m.
Uncorrected 774 px: 4.19 / 4.14. Answer 4.13 m. Confidence: moderate (±3 %), dominated by f.

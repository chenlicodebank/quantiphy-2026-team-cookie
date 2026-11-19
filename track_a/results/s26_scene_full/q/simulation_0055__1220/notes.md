# Q1220 – height of the fire hydrant (m)  → 0.97 m

The file fps (30) is the same as question_fps (30). The scene is a 3D Blender render with a static camera, 1080x1080; the principal point is taken at (540,540).

## Focal length (two routes)
1. **Man (depth_info only)**: he stays at a constant depth (his apparent size is constant). Pelvis u = 1071 (frame 0) and 981 (frame 30), v ≈ 750.
   d0²−d1² = (Z/f)²[(u0−cx)²−(u1−cx)²] gives Z/f = 0.004842 m/px. Then d1 gives Zm = 7.84 m and **f ≈ 1621 px**.
   Sanity check: the man's 370 px height → 1.79 m. Changing the pelvis row (700–800) moves f by <0.5%. (route2.py)
2. **Car + prior**: the steps of the car's rear edge in frames 49–77 are very linear: −0.486 px/frame² = −437 px/s².
   With a = −2.86 this gives s = 152.8 px/m. Combined with d1 = 11.671 at frame 30, it gives Zc ≈ 10.67 m and **f ≈ 1630 px**.
   - Equivalently, route 1 predicts 433 px/s² for −2.86 m/s², which agrees with the measured 437.
   - The early front-edge track (frames 21–48) is heavily motion-blurred (~30 px). Its acceleration is lower (−0.35 px/f²), so the car's
     deceleration is not uniform over the clip. I used the clean late window; a whole-window fit would give f ≈ 1450–1520.
   - The d0 check using the late fit extrapolated to t=0: X0²−X1² = 118 vs 121.7 given (3%).
   - I used f = 1621–1630.

## Hydrant pixel height (hydprof*.py, frame 0 and frame 75, both unoccluded)
- Top: the dome apex is at row 707.9, on the axis (a dome silhouette sits less than 0.5 px from the apex).
- Bottom: the front-most point of the base flange is at row ≈896. The flange's bottom edge is an ellipse whose ends (x≈903/987) are at ≈887.
  Its semi-minor is ≈9 px, which matches the geometry (896−540)·r_b/Z = 356·42/f = 9.2 px.
  The points at axis depth are therefore top 707.9 and bottom ≈887.1, so **H_px = 179 px**. The naive bbox is 188 px; that would give 1.01–1.02 m.
- Zh = 9.207·f/√(f²+(944−540)²+(v_o−540)²) = 8.75 m (origin at the base) to 8.83 m (origin at the centre).
- H = 179.2·Zh/f = 0.962–0.976 m. **Answer 0.97 m.**

## Confidence
Moderate to good. The two focal-length routes agree within 0.6%. The main residual uncertainty is the perspective correction (≈5%) of the base flange.
If the reference simply used the image bbox, it would be about 1.02 m (5% higher).

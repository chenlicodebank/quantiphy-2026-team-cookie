# q_1427: length of the box (simulation_0182)

The file and the question both run at 24 fps, so there is no time-base issue. The answer comes from frame 0 (t = 0), where the box is upright, at rest and seen corner-on. At that time depth_info gives a camera-to-centre distance of 9.522 m.

## Method (pinhole reconstruction of a cuboid at frame 0)
1. **Pitch check:** the blue post edge stays at x = 209.7 over rows 600–960, and the box's left and near vertical edges are vertical to within 0.0004 px/px. So pitch and roll are about 0, and the horizon is at y = 540, with the principal point at (960, 540).
2. **Vanishing points** (`measure_edges.py`, `reconstruct.py`). I fitted the box top edges with subpixel gradient lines:
   - left face top: slope −0.0529, which puts VP1 at x = −5132
   - right face top: slope 0.2717, which puts VP2 at x = 1723
   
   The two directions are perpendicular, so f² = −(x1−cx)(x2−cx), giving **f = 2156 px**. The left face is turned about 19.5° from fronto-parallel; the right face is strongly foreshortened.
3. **Independent focal length from the free fall**, frames 0–7 (`check.py`). The centroid steps are 1.8, 5.9, 10.1 … 25.7 px, matching k(2n−1). The fit gives a = 3.93 px/frame² = 2262 px/s². With the centre depth along the optical axis Z = 9.349 m and g = 9.81, this gives **f = 2156 px**, the same as the vanishing-point value. (Fitting the bottom edge instead gives 2111.)
4. **Box corners:**
   - near vertical edge at x = 607.9, top at y ≈ 236.7, bottom of the near face at y ≈ 426–428
   - left silhouette at x = 377.4, right silhouette at x = 774.5
   
   I solved for the face lengths and height with the near corner at unit depth. I then scaled so that the box centre's distance from the camera equals 9.522 m.
5. **Result:**
   - right (oblique) face = **1.571 m**, the length
   - left face = 1.057 m, the width
   - height = 0.74 m
   
   The model puts the hidden far-bottom corner at (571, 446), which matches the silhouette's lowest point (≈ 562–580, 446–447).

## Checks and sensitivity
- The length hardly depends on f: f = 2100, 2156 or 2210 gives 1.572, 1.571 or 1.570 m. It depends mainly on VP2.
- **Second route for VP2:** the silhouette bottom edge E→G is parallel to the right face. Its subpixel fit gives VP2 = 1669–1755 depending on the threshold, which means a length of 1.53–1.64 m. This brackets the top-edge value of 1723 (1.571 m). The top edge is the steeper, cleaner line (rms well under 1 px), so I used it.
- **Not used:** the prior (sliding acceleration 2.338 m/s²) and the depth at t = 0.5 s. I did not need them for the size and did not check against them. The depth at t = 0 sets the scale.
- **Reading of "length":** the longer horizontal extent, 1.57 m. The other horizontal extent (width) is 1.06 m.
- **Possible bias:** the open flaps might enlarge the bounding box slightly. Whether the origin is the centre or the base changes the scale by less than 0.5%.

Confidence: good. I expect the answer to be within about 4%.

# q_2405 – width of the table (cm)

Width means the table's shorter horizontal extent, front to back. That is the axis the ball rolls along. The file runs at 24 fps, the same as question_fps.

## Method (measure.py, check.py, prof.py)
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Table edges were fitted in code with total least squares (rms 0.3–0.5 px):
  - back edge: top silhouette, frame 0;
  - front edge: the top-surface edge, i.e. where the bright top meets the darker slab face (about 11 px thick), frame 30;
  - left and right edges: side silhouettes.
  - Corners: BL (281.2, 417.2), BR (600.2, 361.7), FR (671.6, 513.6), FL (224.7, 613.9).
- Plane orientation comes from the vanishing points of the two pairs of opposite edges:
  - normal n = (-0.044, -0.880, -0.473);
  - the two in-plane directions come out 88.8° apart, which matches a rectangle and confirms f.
- Plane offset comes from the depth_info:
  - Ball centres at frames 14, 19 and 29 (t = 0.6, 0.8, 1.2 s) were back-projected with depths 1.751, 1.687 and 1.526 m.
  - Their n·P values are -0.845, -0.846 and -0.829, a spread of about 2%. The mean is -0.840.
  - The table surface sits one ball radius (2 cm) lower, at -0.860.
- The edge pixels were back-projected onto this surface plane. The width is the in-plane perpendicular distance between the back and front edges: **58.4 cm**.
  - Both corner-based side edges (left and right) also give 58.4 cm.
  - The back and front lengths are both 71.4 cm, so the table is about 71 x 58 cm.

## Checks
- The distance along the ball's image path, from where it crosses the back edge to where it crosses the front edge, is 59.3 cm. That path is slightly oblique, about 10° off the width axis, which fits 58.4 / cos 10° ≈ 59.3.
- Alternative plane taken from the ball's 3D path direction instead of the side-edge vanishing point: 63.9 cm. I rejected it:
  - the ball path is only 7.5 + 18 cm long and the depths carry noise;
  - the midpoint sits 5.5 mm off the line;
  - in that plane the front and back lengths disagree (72.3 vs 68.9 cm), so the table would not be a rectangle.
- Ball pixel size agrees with the depths: 17–18 px predicted vs 17–18 px measured.
- Sensitivity: the 2% spread in the plane offset gives about ±1 cm.

**Answer: 58.4 cm.** Confidence: moderate to good, about ±3%.

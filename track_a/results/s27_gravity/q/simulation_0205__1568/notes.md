# Q1568 – length of the typewriter (m)

The file's fps is 24, the same as question_fps. The scene is a 3D Blender render with a static camera and the principal point assumed at the image centre (1062, 540).

## Focal length from the prior (fitf.py)
- I back-projected the magnifier origin (bbox centre from scene track) at frame 0 (depth 4.2401 m) and at frame 12 (t = 0.5 s, depth 4.4097 m) for a trial focal length f. The fall direction is P12 - P0.
- For frames 0–11 (pre-impact), I found the position along that line that reproduces the pixel v, then fitted a quadratic. I solved for f so that the acceleration is 9.8 m/s².
- Result: **f = 2635 px** (HFOV 44°). Using the mask centroid gives 2642 and the lens centre gives 2629. The fit residual is 0.3 mm. The fitted v0 of 0.02 m/s fits a release at frame 0.
- From the same fit, gravity in camera coordinates is (0.002, 0.973, 0.232), so the camera pitches down about 13°.

## Plausibility checks
- Magnifier length: 174 px × 4.38 / 2635 ≈ 0.29 m.
- Revolver: 153 px × 4.704 / 2635 ≈ 0.27 m.
- Both sizes are realistic.

## Desk plane
- Height along "up" relative to the camera: magnifier at rest −1.223 m and gun −1.225 m (both origins are a centimetre or so above the leather). I set the desk surface at −1.235 m.
- The corner depths give −1.27 to −1.30 m (corner markers are probably at the lower edge or bevel), so the plane height carries about ±0.025 m of uncertainty, which is about ±2 % in length.

## Typewriter (twlen.py, check2.py)
- Base footprint in frame 29, from a dark mask plus visual reading: back-left (853, 708), front-left (931, 756), front-right (1150, 724).
- Back-projected onto the desk plane:
  - Front edge (left–right) = **0.370 m**.
  - Side (front–back) = 0.281 m.
  - The two edges meet at 86°, and the front edge is within 3° of parallel to the desk's front edge.
- Length is the longer horizontal extent, so it is the left–right extent: about 0.37 m.
  - The back-left corner sits 1.8 cm further left, which would make the AABB up to about 0.39 m.
  - The carriage (≈0.36 m wide) lies within the base extent.
- Second route: the carriage ends back-projected at 0.10 m above the desk give a width of 0.363 m, lying 0.12–0.26 m behind the front edge, which is consistent with the base.
- Sensitivity: varying the desk height from −1.21 to −1.28 m gives 0.362–0.383 m.

**Answer: 0.375 m.** Confidence is moderate to good (about ±5 %).

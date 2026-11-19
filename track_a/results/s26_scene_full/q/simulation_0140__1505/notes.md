# Q1505: distance between the bird's flight path and the neon-sign wall

File fps = question_fps = 24, so the times line up: t=0 is frame 0 and t=0.5 is frame 12.

## Model
- The neon-sign wall is a flat backdrop facing the camera. I assume the camera axis is perpendicular to it.
- The bird flies in a plane parallel to the wall, at a constant camera z-depth.
- Answer = Z_wall - z_bird, where Z = Euclidean distance / sqrt(1 + r^2/f^2) and r is the pixel offset from the
  principal point (960, 540).

## Measurements
- **Sign centre:** (989, 311) px, the centre of the letter box from scene.json.
- **Bird centroids:** frame 0 (216, 865), which is poor because the bird is merged with its shadow, and frame 12
  (332, 712), which is good. Both are from scene/tracks/bird.csv; the bird was checked on crops.
- **Window frame width:** measured in code from a column profile (measure.py) on the central facade, row band
  420–500. The outer frame runs from about x=481 to x=600, so about 118 px (range 112–124).

## Routes (solve.py)
- **A, focal length from the prior:** 1.48 m = w x Z_wall / f, with Z_wall taken from the 34.5 m sign distance.
  - With w=118 px: f ≈ 2741 px and Z_wall = 34.38 m.
  - Bird z = 24.29 m at t=0 and 24.23 m at t=0.5. These match each other, which confirms the parallel-plane model.
  - Distance ≈ 10.12 m. Over w = 112–124 px it ranges from 10.06 to 10.20 m.
- **B, focal length from the two bird depths alone (constant bird depth):** f ≈ 2520 px, giving a bird z of
  24.11 m, a wall at 34.36 m and a distance of 10.25 m. Shifting the frame-0 centroid by ±10 px gives 10.21–10.29 m.
- The two routes agree to within about 1%.

## Answer
10.15 m. Confidence is good, at roughly ±3%. The main assumption is that the wall faces the camera head-on.

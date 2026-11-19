# q 1674 — length of the boat (m)

Time base: question_fps = 24, so t=1 s is frame 24 and t=2 s is frame 48. The file is 25 fps; I used frame indices, not the times in scene/.

## Focal length (focal.py)
- Eagle centroid: frame 24 is at (471.1, 372.2) and frame 48 at (742.1, 369.7). The given depths are 116.05 m and 108.28 m. Principal point is the image centre (480, 480).
- I solved for f so that the 3D distance between the two back-projected positions equals 11.84 m (constant speed over 1 s, nearly straight path). This gives f ≈ 3390 px (hfov ≈ 16.1°). The result is stable to ±0.3% across smoothing windows of 0–6 frames.

## Boat heading (boat3d.py, length.py)
- I back-projected the hull centre (linear fit of the track) with depths 103.157 m and 106.091 m.
- Displacement over 1 s is (-2.97, -0.03, 2.76) m, so speed is 4.05 m/s. The heading is 43° from the image plane (the boat moves left and away). Vertical drift is about 0, so the camera is nearly level.
- I assume the boat moves along its own long axis. The image agrees: you can see the side of the wheelhouse with windows and the rear face with a door, with the bow pointing left and away.

## Length
- Bow stem tip (leftmost hull pixel, centreline): x = 196 at frame 24 and 111 at frame 48.
- Hull right extreme: x = 446 and 349. The stern is rounded.
- Rudder trailing edge (centreline at the stern): x ≈ 428 and 331.
- L is the distance between the 3D points on the boat's axis line (through the origin, along the heading) whose projections hit the bow tip and the stern centreline tip.
  - Route 1 (stern tip at the rudder edge + 0–6 px): L = 10.14–10.40 m (f = 3390). Both frames agree to 0.01 m.
  - Route 2 (round stern with beam 2.5–3.5 m, fitted to the silhouette extreme): L = 10.18–10.40 m.
  - Box stern instead (L/B = 3): 9.4 m. I rejected this because the stern is visibly rounded and the rudder places the centreline tip only about 16 px inside the extreme.
- Sensitivity: f ±3% changes L by about ∓1.4%.

Answer: L ≈ 10.3 m. Confidence is moderate, about ±5%. The main assumptions are that the heading equals the motion direction and where exactly the stern tip is.

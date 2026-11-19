# q_1596: height of the wooden bench (m)

The "wooden bench" is the item the scene record calls the "side table" (slatted wooden top, splayed legs, lower shelf).
The file rate and question_fps are both 24, so t = 1.0 s is frame 24.

## Focal length (focal.py, height.py)
- I assumed the cat walks straight at a constant 0.94 m/s, so the chord from frame 0 to frame 24 is 0.94 m.
  I back-projected the torso centre (scene/tracks/cat.csv) at the given depths 4.199 m and 4.481 m, with the principal point at (960, 540).
- Raw torso centre: f = 2099 px. Torso centre smoothed with a ±4-frame linear fit (to remove gait bob): f = 2081 px.
  Mask centroid and bbox centre give 2145 to 2161 px. I used f ≈ 2090 (hfov ≈ 49°).

## Bench pixels (bench_px.py, profile.py, frame 0)
- Bench bbox (wood colour mask): x 1288-1667, y ~652-841.
- Closest (front-left) leg foot: lowest wood pixel at y = 841, x ≈ 1406.
- Slab: the top surface band is at y 655-668 and the front face at y 669-683 (column profiles).
  The top-front edge is at y ≈ 666.
- Vertical extent at the front: 841 - 666 = 175 px.

## Height
- Closest leg depth is 5.69 m. Its ray at about (1420, 770) gives Z = 5.53 m.
- Route 1 (simple pinhole): H = 175 × 5.53 / 2090 = 0.46 m.
- Route 2 (floor plane): I built the floor plane from the mirror bottom centre (pixel (1510, 815), depth 6.407 m),
  the leg foot (depth 5.69 m), and the cat's walking direction. The height of the top-front edge above the floor is
  0.459 m at f = 2099 and 0.463 m at f = 2081.
- Sanity checks: camera height 0.58 m; cat origin 0.21 m above the floor (plausible for a cat's body centre);
  the camera is just above the bench top, which matches the thin visible top surface.
- Sensitivity: f between 2081 and 2160 gives H between 0.448 and 0.465 m. Moving the top edge by ±2 px changes H by about ±0.005 m.

Answer: 0.46 m. Confidence is moderate to good (about ±5%).

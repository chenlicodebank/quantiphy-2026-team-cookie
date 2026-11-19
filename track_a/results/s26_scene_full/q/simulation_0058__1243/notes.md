# q1243 – width of the green car (parked BMW, far, front view)

The file is 24 fps, the same as question_fps, so no time conversion was needed. Frame 14 is t = 0.58 s and frame 38 is t = 1.58 s.
The green car is static. Its front faces the camera and its left side shows slightly on the image right.

## Focal length (from the prior: the white van accelerates at 4 m/s²) – m2_van.py, m3_van3d.py
- I used the van track from scene/tracks/van.csv (rear-edge track, plus the box centre). The 3D line runs through the
  back-projected van centres at frames 14 and 38, using their depths (31.07 m and 29.918 m). Every frame's ray was
  intersected with that line, and the positions along it were fitted to s0 + ½·4·((n−n0)/24)², with f fitted too.
  - Box centre: f = 2236 (frames 2–71), 2241 (2–45). Rear edge: f = 2181 (2–71), 2211 (2–45). Fit rms 3–25 mm.
  - Two-point estimate (frames 14/38 only): 2222–2377 px, depending on the assumed start time.
  - I took **f = 2210 ± 35 px**.
- Camera model: principal point at the image centre; pitch from the horizon row 422.5 (main-road vanishing point, scene/).

## Camera height – m4_ground.py
For each ground-contact reference with a given depth, I solved the camera height H so that the ground point (+ origin height) is at
that depth. At f = 2210: bike at frame 14 gives 2.81 m, bike at frame 38 gives 2.79 m, pedestrian at frame 14 (pelvis 0.9–1.0 m) gives 2.83 m.
The van gives 2.97–3.02 m, but its contact row is the near-side wheels, about 1 m in front of its origin, so it is biased and not used.

## BMW pixel width – m5_bmwedges.py (median of frames 0, 5, 10, 15, before anything covers it)
- Front tyres, outer edges at half contrast: left at x = 1030.5, right at x = 1129.1, contact row 588. That gives **98.6 px**.
- Both ground points were back-projected onto the ground plane. The front axle is at Z ≈ 37.5 m.
  The width is the 3D distance between them.
  - f = 2210: 1.662–1.687 m (bike 14, bike 38, pedestrian), mean ≈ **1.675 m**.
  - f = 2180: about 1.70 m; f = 2240: about 1.655 m.
- Check: the simple pinhole formula 98.6 px × 37.5 m / 2210 = 1.673 m agrees.

## Checks
- The camera height from the bike at two times and from the pedestrian agrees to within ±1 %.
- The 3D paths of the van and the bike come out nearly parallel (1.5° at f = 2210) and level (< 2 cm vertical change),
  which supports the camera model. Parallelism alone is a weak constraint on f (best near 2400).

## Ambiguity
- Wheel-to-wheel (the stated convention) is about 1.675 m. With the side mirrors, which reach about 8 px beyond the body
  side on each side at their depth, it would be about 1.95 m. My answer uses the wheel-to-wheel reading.

Answer: 1.675 m. Confidence: moderate; the uncertainty is about ±3 %, mostly from f.

# q1463 — speed of the car at t = 1.0 s (m/s)

Prior: the forklift accelerates at 2 m/s². depth_info gives the forklift and car camera distances at t = 1 and 2 s
(frames 24 and 48). The file and the question both use 24 fps.

## Method (fit.py, check.py)
- Pixel tracks: scene/tracks (amodal bbox centre ref_x/ref_y; I also tried the bottom-centre and the silhouette centroid).
- Pinhole camera with the principal point at the image centre and focal length f unknown.
- Forklift: I fit a 3D straight-line motion with constant acceleration a = 2 (the prior), starting from rest at t0. The
  free parameters were P0, direction, t0 and f. The fit used the pixel track over frames 0-71 and was held to the two
  given depths. Result: f = 3391 px (hfov 41°), t0 = 0.01 s, rms 1.5 px, depth residuals < 3 mm.
- Car: I used the same model with f fixed and a and t0 free, held to the car's two given depths:
  - a = 5.00-5.02 m/s² with t0 ≈ 0 (frames 10-30: rms 0.9 px; frames 0-40: 1.6 px; frames 0-71: 3 px).
  - With the bottom-centre or the centroid as reference point, a = 4.90-4.96.
- Speed by the benchmark convention (backward difference at frame 24): v = a·(24²-23²)/(2·24²) = a·47/48.
  This gives 4.92-4.94 (centre), 4.82-4.83 (bottom) and 4.89-4.90 (centroid).

## Second route (check.py)
- I back-projected frames 24 and 48 with the given depths only.
- The car/forklift displacement ratio is 2.53 at every plausible f, and it hardly depends on f. With both vehicles
  uniformly accelerating from rest, this gives car a ≈ 2 × 2.53 ≈ 5.06.
- At the fitted f, the forklift displacement is 2.98 m (expected 1.5·2 = 3.0) and the car's is 7.54 m (a = 5.03).

## Answer
- The car most likely accelerates uniformly at 5 m/s² from rest, so v(1.0 s) = 5·47/48 = 4.90 m/s (5.0 if the
  continuous a·t is used instead).
- Answer: 4.9 m/s. Confidence: high, about ±3%.

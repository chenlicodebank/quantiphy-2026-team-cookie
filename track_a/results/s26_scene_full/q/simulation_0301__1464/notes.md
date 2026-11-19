# Q1464 — speed of the car at t = 2.0 s (m/s)

File fps = question_fps = 24, so t = 2.0 s is frame 48. This is a 3D Blender scene with a static camera.
Prior: the forklift accelerates at 2 m/s². depth_info gives the forklift and car distances at frames 24 and 48.

## Method (scripts: draw.py, solve.py, solve2.py, t0.py)
- I used the image positions from scene/tracks: the amodal bbox centre (`ref`), and the amodal centroid (`cen`) as a
  second choice. I checked the boxes on frames 24 and 48 (frames/f24.png, f48.png), and they cover the right objects.
- Pinhole model with the principal point at the image centre. A 3D position = depth × unit ray(u, v, f).
- Start time: the pixel displacement from frame 0 grows as i² (car left/top edge: sqrt-displacement fit gives
  t0 = 0.00 ± 0.01 s; forklift too). So both vehicles start from rest at t = 0. Frames 0 and 1 look identical only
  because the motion over the first frame is less than a pixel.
- Focal length:
  - Route A: forklift displacement from frame 24 to 48 = 0.5·2·(2² − 1²) = 3.0 m gives f = 3329 px (ref) / 3372 (cen).
  - Route B: for each f, project every frame onto the 3D line through P24 and P48 (closest point between the ray and
    the line), then fit s = s0 + a t²/2. Forklift a = 2.00 at f ≈ 3370 (ref) / ≈ 3460 (cen). The two routes agree
    within about 3%.
- Car: same line projection and fit with t0 = 0. Car a = 5.03–5.10 (f 3330–3455) and 4.94–5.01 at f 3501.
  - The ratio of car to forklift displacement over frames 24–48 is 2.52–2.53 and hardly depends on f. With the same
    t0, the car's acceleration is ≈ 2 × 2.52 ≈ 5.05 m/s². Most likely the scene uses exactly 5 m/s².
- Speed at frame 48 by the benchmark convention (backward difference): v = a·(48² − 47²)/(2·24²)·24 = a·95/48
  = 9.90 m/s for a = 5.
- Second route: free quadratic fits of the car track (fit windows 2–71, 5–60, 21–48) give v48 = 9.55–9.87, and the
  raw per-frame step speed at frame 48 is 9.66–9.9 depending on the convention, all consistent.

## Answer
9.9 m/s. Confidence: good (about ±3%). The residual uncertainty comes from the ref point vs origin offset and the
choice of focal length.

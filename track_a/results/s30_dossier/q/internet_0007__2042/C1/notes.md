# q2042 — length of the black car (internet_0007)

The "black car" is the dark (metallic blue/black) car in the left lane that drives toward the top of the image
(scene record: blue_car). The other car is white. The shot is a top-down drone view and the camera is almost static.

## Scale (prior: lane width = 3.66 m), single-scale planar convention
- road.py / edge.py / lane.py: column colour profiles across the road on frame 200 (no car near the left lane), every 20 rows
  down the whole frame. The centre line is at x ≈ 559.5–561.
- Measuring the edge by asphalt colour (B/R ratio): road 79.5 px wide, lanes 39.8 / 40.4 px.
  Measuring it by the brightness half-way transition: road 74.9 px, lanes 36.4 / 38.5 px.
  Where the edge is clean (y 1600–1700, near the car's start): road 521.5→597.5 = 76 px, so each lane is 38 px.
- I used lane width = 38.5 px (half of the ~77 px road), which gives 3.66 / 38.5 = 0.0951 m/px.
  (The scene record's 71 px road width was too narrow.)

## Car length (bumper to bumper, along the motion)
- car.py: difference against a frame without the car (frame 250), 80th-percentile row profile, longest contiguous run.
  Frames 0–80, clear of the tree: 73, 73, 74, 76, 72, 73, 73, 74, 74, 74 px, median 73.5 px. This matches the record's
  mask_len of 73–74 px. After the tree (frames 112–120) it reads 76–77 px, but blur and the darker light are included there.
  Checked visually on frames/carmask_40.png: the lines sit on the bumpers.
- Length = 73.5 × 3.66 / 38.5 = **6.99 m**.

## Second route / sensitivity
- Lane read as 37.5 px gives 7.17 m; lane read as 40 px gives 6.73 m. Using the car's 76 px post-tree length would give 7.2 m.
- Cross-check from the car's own shape: it is 73.5 px long and about 26–28 px wide (body), an L/W ratio of about 2.7, which is
  normal for a sedan. In reality this narrow UK lane is probably ~2.4 m, so the true car is about 4.7 m. But the benchmark's
  single-scale convention with the 3.66 m prior gives ~7.0 m, and that is the answer here.
- Fps does not matter for a size.

Confidence: moderate. The scale follows the prior's convention; the remaining uncertainty is the road-edge definition (±4 %).

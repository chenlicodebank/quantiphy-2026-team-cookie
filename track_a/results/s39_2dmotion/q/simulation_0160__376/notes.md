# Q376: speed of the ball at t = 1 s (m/s)

Prior: ball diameter = 0.0757 m. This is a 2D top-down pool video, and ball 13 is the only moving ball. The file and question_fps are both 30, so t = 1 s is frame 30.

## Measurements (scripts: measure.py, diam.py)
- **Centres.** I took the centre from the difference against frame 0, using the convex-hull centroid. The x positions for frames 29 to 33 are 589.16, 556.29, 522.68, 489.08 and 455.50.
  The clean single-frame steps are 33.96 (frame 29), 32.87 (frame 30), 33.61, 33.60 and 33.58 px. Later clean steps are 33.9 (frame 36), 34.11 (frame 38) and 33.25 (frame 39).
  Frames 20–23 step about 31.5 px, and the speed rises slowly.
  The video has repeated and skipped frames (28 repeats 27, and 34 is a double step), so the raw one-frame difference is noisy.
  I used the local smooth step at frame 30, about **33.3 px/frame** (±0.3). The raw step at frame 30 alone is 32.9.
- **Diameter.**
  - The radial profile of the difference image drops at r ≈ 24 px, with a shadow/blur tail out to r ≈ 28. That gives a diameter of about 48 px.
  - Equal-area diameters are 47.2 (threshold 100), 49.4 (threshold 60) and 51 (threshold 40). The lower thresholds take in the shadow.
  - The record's ellipse major axis is 48.4. Static balls also measure about 48.
  - I used **48.2 px**.
- **SAM 3 check.**
  - Frame 30 centroid: SAM 556.0 vs mine 556.3. Frame 29: SAM 589.5 vs mine 589.2. They agree to better than 0.5 px.
  - SAM's extents at frame 30 are 47 px horizontal and 49 px vertical, with a fitted-axis length of 49.3, against my 48.2. That is within 3 pct.
  - The zoomed crop (frames/z30.png) shows the ball spanning about x 532–580 and y 479–527, so about 48 px.

## Result
- Scale: 0.0757 / 48.2 = 1.5705e-3 m/px.
- Speed: 33.3 px/frame × 30 × 1.5705e-3 = **1.57 m/s**.

## Second route
- The double steps near frame 30 are 64.94 / 2 = 32.5 (frame 27) and 66.94 / 2 = 33.5 (frame 34). Their mean is about 33.0, which gives 1.555 m/s.
- The raw frame-30 step of 32.87 gives 1.55 m/s.
- These agree with the main result within about 1.5 pct.

Confidence: good (±3 pct).

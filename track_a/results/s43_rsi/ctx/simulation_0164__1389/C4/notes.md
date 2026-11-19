# q1389 – acceleration of the bowling ball at t = 1 s (frame 24; question_fps = file fps = 24)

**Answer: 0.41 m/s²**. This is the size of the deceleration: the ball slows from about 3.9 to 3.45 m/s before it hits the pins.

## Where the candidates part ways
All four candidates used the same ball track and the same pinhole method. They differ only in **where the ball's vanishing
point (VP) sits along its image path**. That point sets how depth grows from frame to frame, so it sets the ratio a/v:
- C1 and C2 (0.41) took the VP from the lane lines, at x ≈ 5650–5680.
- C3 (0.36) averaged in a VP of 5377. That value came from fitting the apparent diameter linearly in u.
- C4 (0.32) used a lane homography and diameter-based depth, which amounts to the same short VP.

## My measurements
- `lanes.py`: I fitted the three bright cyan floor lines on frame 0 with sub-pixel column centroids.
  - Lines A and C are clean (rms 0.10 and 0.11 px) and meet at **(5643, 208.5)**.
  - The ball's straight image path (y = -0.0832x + 678.6) crosses A at x = 5669 and C at x = 5637.
  - The ball rolls at constant height, so its VP must be where its path meets the horizon. That is this point,
    whatever the camera roll, so the VP is 5643 ± ~20.
  - Line B (rms 0.74 px) is contaminated, probably by a floor reflection, and I did not use it.
- `diam.py`: The diameter route gives a VP of about 5300–5400. It depends on systematic diameter bias:
  - In the early frames the top of the ball sits against the dark gutter strip.
  - An off-axis sphere appears elongated, and motion blur also widens it.
  - A bias of a few px moves that VP estimate by hundreds of px.

  My own edge profiles were too noisy to use (VP anywhere from 6000 to 10600). I therefore rejected the diameter-based VP, which is what
  C3 and C4 relied on.
- `recon.py`: I reconstructed the ball in 3D.
  - Principal point at the image centre.
  - The line direction is the ray to the VP.
  - The line is anchored at the frame-12 ray × 9.391 m, which is depth_info at t = 0.5 s.
  - Each frame's position along the line is the closest point between its ray and the line.
  - Focal length: f = 82.1 px × 9.391 / 0.21 ≈ 3650–3670 px. With f = 3650 the predicted apparent diameters
    (88.1 → 67.7 px) match the measured ones (88.5 → 66.9) within about 1–3 %.

## Results (frames 6–37, before the pin impact at frame 37–38)
- With f = 3650 and VP 5643, the quadratic fit gives a = -0.412 m/s². The cubic fit at 1 s gives -0.409.
  A linear fit of the per-frame speeds gives -0.411. Speed at 1 s is 3.59 m/s, and the residuals are 3.3 mm rms.
- Fit windows: 6–30 → -0.42, 12–36 → -0.41, 14–34 → -0.42, 16–32 → -0.39.
- Sensitivity:
  - Changing the VP by ±50 px changes a by ±0.015.
  - f between 3500 and 3800 gives a between -0.42 and -0.40.
- The single-frame difference (speed(24) - speed(23)) × fps is far too noisy to use. The motion is uniformly
  decelerated, so the fitted constant is the acceleration at 1 s.

I agree with C1 and C2. Confidence: good, about ±7 %.

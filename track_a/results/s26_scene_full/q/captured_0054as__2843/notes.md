# q_2843: orange ball (basketball) displacement 0.5 s -> 1.0 s

File fps = question_fps = 24, so the times map to frames 12 and 24.

## Method (measure.py)
- I masked the ball by colour and fitted a circle to its contour, leaving out the part cut by the bottom image edge
  in frame 24. Overlays are in frames/fit12.png and frames/fit24.png.
  - Frame 12: centre (343.7, 606.4), diameter about 75 px.
  - Frame 24: centre (585.4, 680.7), diameter about 89 px.
  - The record's centroids agree: frame 12 (343.5, 606.8). In frame 24 the record's centroid is 2 px higher
    because it only covers the visible part of the ball.
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- I back-projected each centre with the depth_info value at that time: 2.3557 m at frame 12 and 1.8100 m at
  frame 24.
  - Method-card convention, P = ((u-cx)/f, (v-cy)/f, 1) x depth: displacement = **0.957 m**.
  - Treating the depth as a Euclidean ray length: 0.824 m.

## Check against the prior (velcheck.py)
- I interpolated the depth linearly between the two given values and differenced the per-frame 3D centres.
- Speed at frame 12, averaged over frames 10-15:
  - z (method-card) convention: 2.18 m/s, which reproduces the prior of 2.21 m/s.
  - Euclidean convention: 1.73 m/s, 22% below the prior.
- I therefore answer with the z convention.
- Caveat: the step from frame 11 to 12 is a possible dropped frame. It does not affect the two endpoints.
- The ball's apparent size is not fully consistent with the given depths. The implied diameter is 0.231 m at
  frame 12 and 0.212 m at frame 24, about 9% apart. This could come from segmentation edge effects. Only the
  centres and the given depths enter the answer.

Confidence: moderate-high. The answer is 0.957 m. If the reference used Euclidean depth, it would be 0.82 m.

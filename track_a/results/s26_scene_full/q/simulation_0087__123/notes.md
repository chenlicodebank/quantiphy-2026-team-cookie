# q_123: car acceleration at t = 1.0 s (frame 24)

The scene is 2D and seen from the top. The camera is static. fps = question_fps = 24, so no re-timing is involved.

## Scale (from the prior: bike speed = 5.07 m/s)
- The cyclist moves at a constant speed. A linear fit of the bbox-centre ref_x over frames 7-53 gives 21.10 px/frame. The front tip x1 over frames 2-53 gives 21.05 px/frame. I used 21.08 px/frame, which is 505.9 px/s.
- Scale = 5.07 / 505.9 = 0.010022 m/px.

## Car acceleration (edges.py, local.py)
- I re-measured two features on each frame to sub-pixel accuracy, using the mean profile over rows 650-730:
  - the car's front edge, where the profile crosses level 175;
  - the hood-to-windshield transition, where it crosses level 120.
- Quadratic fits around frame 24, with half-windows of 4-10 frames:
  - front edge: -0.690 to -0.697 px/frame²;
  - windshield: -0.693 to -0.702 px/frame².
- A quadratic fit over frames 2-30 gives -0.699 (front) and -0.704 (windshield), with rms residuals of only 0.05-0.08 px. The acceleration is uniform over this span.
- Local fits after frame 30 drift up to about 0.75 px/frame². This is probably motion blur growing with speed, plus some perspective: the windshield-to-front gap shrinks from 70 to 61 px as the car crosses toward the image centre. The drift does not affect frame 24.
- Value used: 0.700 px/frame² = 403.2 px/s².
- a = 403.2 × 0.010022 = **4.04 m/s²**.

## Checks
- The two features (front edge and windshield) agree within 1%.
- The scene/ record's integer x0 edges give about 0.69-0.70 over frames 2-40, which is consistent.
- Plausibility: the car starts from rest at frame 1 and reaches about 9.3 m/s by frame 53. This fits a uniform acceleration of about 4 m/s².

Confidence: good, within about 3%. The main remaining uncertainty is perspective: the bike's origin and the car's origin are at different heights, which can shift the scale by about 1%.

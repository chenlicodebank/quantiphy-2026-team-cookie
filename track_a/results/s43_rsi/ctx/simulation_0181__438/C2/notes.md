2D scene, one scale from the prior: box slide acceleration at t=0.75s measured on frames 12-29 (before crate occlusion) as 700 px/s^2 (quadratic fits to SAM3 mask centroid, min-area-rect centre and extent centre, rms 0.3-0.7 px), so scale = 2.338/700 = 0.00334 m/px. Speed at t=1.5s (frame 36) from a rigid mask-translation fit with the crate-occlusion region excluded (IoU 0.96-0.98) is a constant (32,17.5) px/frame = 881 px/s (the box reaches the belt end ~frame 29 and its acceleration falls to ~0, so a constant-acceleration extrapolation would be wrong). 881 x 0.00334 = 2.94 m/s. Second route: box top-left corner / bbox corner give 900-940 px/s, and the independent colour-mask centroid gives the same acceleration, so the answer is 2.9-3.0 m/s.

Final message:
Answered question 438 with **2.94 m/s**.

Method summary:
- **Scale from the prior**: the box's slide acceleration at t=0.75 s (frame 18) measured on the clean pre-occlusion window (frames 12–29) is ~700 px/s² (quadratic fits to the SAM 3 mask centroid, min-area-rect centre and extent centre, sub-pixel residuals). Scale = 2.338 / 700 = 0.00334 m/px.
- **Speed at t=1.5 s (frame 36)**: a rigid mask-translation fit with the crate-occlusion region excluded (IoU 0.96–0.98) shows a constant (32, 17.5) px/frame shift from frame 28 to 38 → 881 px/s. The box reaches the end of the straight belt around frame 29, so its acceleration falls to ~0; a constant-acceleration extrapolation would have overestimated the speed by ~20%.
- **Check**: the box's top-left corner and bbox corner give 900–940 px/s, and an independent colour-mask segmentation reproduces the same acceleration, so the result is 2.9–3.0 m/s.

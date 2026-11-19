# Measurement notes

- Question 1523: car acceleration at 0.5 s, in m/s^2.
- Source: simulation_0149.mp4, 1920 x 1080. Both file fps and question_fps are 24. Frame 12 is the requested frame. The reported acceleration uses the scalar-speed backward difference, equivalent to the second backward difference of distance along the straight trajectory at frames 10, 11, and 12.
- Metric references used exclusively: tire diameter 0.764 m and initial camera-to-right-front-tire distance 14.244 m.

## Measurements and geometry

The near front wheel is the right front tire. Its rim center was measured by connected-component segmentation followed by an ellipse fit to subpixel radial intensity gradients. Frames were decoded sequentially, and only small crops and tracking arrays were retained. Scripts and diagnostic overlays are included in this directory.

At frame 0 the fitted rim center is (67.50, 828.65) px, with ellipse axes 26.93 x 87.63 px. The tire's bottom edge is 898.5 px, measured from the tire-to-floor intensity transition over multiple columns. Reflecting that radius about the wheel center gives a projected tire diameter of 139.71 px. This yields a focal-length estimate of 2429.95 px from the known diameter and Euclidean distance, accounting for the wheel's offset from the image center.

An independent calibration uses the changing rim ellipse aspect ratio as the car approaches. Its aspect ratio is approximately linear in horizontal position; the resulting focal estimate is 2420.63 px, agreeing within 0.4%. This independently predicts approximately the same initial tire diameter and camera distance. Minor finite-circle projection effects, tire thickness, and the difference between the visible rim face and tire origin remain sources of small systematic error.

The rim diameter versus horizontal center position gives a motion vanishing point x = -837.24 px. Independently, ellipse aspect ratios give x = -869.48 px. The adopted value is -847.99 px, weighted toward the diameter fit. The near-constant wheel-center image height is approximately 829 px; this fixes the ground horizon and accounts for camera pitch. The changing wheel ellipse is consistent with a fixed wheel-plane direction and straight translation, so the tire and car root have the same translational acceleration.

With the adopted calibration, the initial camera-coordinate position is approximately (-4.881, 1.578, 13.288) m, whose norm is 14.244 m. The unit motion direction is approximately (0.5942, -0.0950, -0.7987). For horizontal wheel coordinate u and vanishing coordinate e, distance traveled is reconstructed as

    s = [Z0 / (-direction_z)] * (u - u0) / (u - e).

This uses perspective-corrected 3D travel, not pixel acceleration with a fixed scale. Smooth local polynomial fits to s suppress subpixel segmentation noise before taking the required backward differences.

## Independent checks and result

Five different frame windows and polynomial orders give 10.257, 10.242, 10.246, 10.188, and 10.276 m/s^2. Their median is 10.2464 m/s^2.

A separate check tracks fixed car-body features using bidirectional optical flow. Each feature's perspective travel scale is estimated against the wheel trajectory; 63 tracks pass the trajectory-residual checks. Their acceleration median is 10.325 m/s^2, with interquartile interval 10.226–10.474 m/s^2. This independently checks the temporal measurement, while sharing the metric calibration.

Final answer: 10.25 m/s^2. Confidence: moderately high; reasonable calibration and temporal-window variants differ by only a few percent. The main remaining uncertainty is locating the physical tire boundary and its origin on the dark, obliquely viewed wheel.

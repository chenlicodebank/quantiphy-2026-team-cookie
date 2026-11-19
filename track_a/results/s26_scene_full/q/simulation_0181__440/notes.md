# q_440 — height of the box (m)

Prior: box acceleration at t = 0.75 s (frame 18) = 2.338 m/s². No depth_info. fps = question_fps = 24 (no re-timing).
Scene: one cardboard box falls from rest (frames 0–7), lands on a blue ramp (~28.3° in image), and slides
down-right with constant tilt. The camera is static, and the motion is close to a plane facing the camera, so one m/px scale is used.

## Measurements (scripts in this folder)
- `track4.py`: masked-template ECC pairwise displacements (|i−j| ≤ 3), least-squares positions.
  - Free fall frames 0–7: y(t) quadratic, a = 2450 px/s² (2446–2458 across windows, residual 0.1 px),
    v(0) ≈ 0, which means it starts from rest. Saved in `freefall_ls.csv`.
  - Slide frames 13–31: direction 28.3°. The acceleration along the ramp depends on the window: 655 (13–22), 634 (13–31),
    612 (19–29), 577 (20–29), 560 (20–31) px/s². Early frames are still affected by the post-landing yaw (the long side
    shrinks 311→280 px until frame 20). Mask-centroid fits (`slidefit.py`) are noisier (530–740).
    Best estimate after the yaw settles: ≈ 592 ± 30 px/s².
- `height.py`: front face of the box at frame 0. The top edge is at y = 228.3 (strong gradient, x = 550–610) and the bottom edge
  at y = 441.4, so the height is **212.7 px** (body only; the dark region above is the open top/interior seen from above, not a raised flap).
  The silhouette height while sliding (~185 px) is not usable because the ramp's front face hides the bottom of the box.

## Scale and answer
- Route 1 (prior): 2.338 / 592 = 0.00395 m/px, so H = 212.7 × 0.00395 = 0.840 m (±5% from the slide-acceleration spread).
- Route 2 (check: Blender gravity 9.81 m/s² on the measured free fall): 9.81 / 2450 = 0.004004 m/px, so H = 0.852 m.
  This route also predicts a slide acceleration of 584 px/s², matching the prior within the measurement spread. Both the height
  and the free-fall motion are measured on the front face in the same image region, so perspective and front-face depth cancel.
- Answer: 0.845 m (mean of the two routes, which agree within 1.5%).

Confidence: medium-high (±4%). The main uncertainty is the pixel acceleration of the slide.
The scene record's slide acceleration from mask centroids (~730 px/s²) is biased high and would give 0.68 m. That value was not used.

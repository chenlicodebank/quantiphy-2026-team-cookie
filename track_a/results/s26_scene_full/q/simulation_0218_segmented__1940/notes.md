# q_1940 – height of the big robot (prior: speed = 5.924 m/s)

The video has only one object, the tracked drill robot ("big robot"). It drives right at constant speed, at constant depth, with a static camera. fps = question_fps = 24.

## Measurements (scripts: strips.py, strips3.py, pillars.py)
- Pixel speed depends on the depth of the feature (the camera is close and the perspective is visible):
  - Near-side tread outer face (template match, rows 800-880): 50.78 px/frame, residual 0.1 px.
    Upper tread (rows 700-790): 50.68.
  - Top handle centre (on the robot's centre plane, which is where the origin is): 48.78 px/frame.
    Head-box and tread silhouette centres: about 49.9.
  - Depth ratio near face / centre plane ≈ 50.78/48.78 = 1.041.
- Scale at the origin (centre plane): 5.924 / (48.78 × 24) = 0.005060 m/px.
- Vertical extent in every fully visible frame: y 270 (top of handle) to 893 (near bottom edge of the treads), about 623 px.
- Pillar edges in the background frame 49 are exactly vertical, so the camera has no pitch and the principal point is at y≈540.
  The near bottom edge is 353 px below the centre. At the centre-plane depth this becomes 353/1.041 = 339 px, so the
  bottom is at y≈879. Height at the centre-plane scale = 879 − 270 = 609 px.
- Height = 609 × 0.005060 = **3.08 m**.

## Cross-checks
- Without the depth correction: 623 px × 0.005060 = 3.15 m.
- Using the near-tread scale for everything: 623 × 5.924/(50.78×24) = 3.03 m.
- The corrected value 3.08 m lies between these two bounds, which differ by about 4%. Confidence: moderate-good (±3%).

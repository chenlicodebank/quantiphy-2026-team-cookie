# Q1893: height of the big elephant (m)

- This is a 2D side-view clip at 24 fps (file rate = question_fps). The background is white and the camera is static. Both elephants walk right on a ground line at y ≈ 691–695 px.
- Prior: the big elephant's speed is 2.313 m/s. That gives one m/px scale from its pixel speed.
- `measure.py` re-measured every frame. Mask: min RGB channel more than 25 below white. The big elephant is the blob to the right of the widest empty column gap.
  - Pixel speed:
    - Linear fit of the centroid x: 7.008 px/frame.
    - Mean |centroid step|: 7.056 px/frame.
    - Front-edge fit: 7.061 px/frame.
    - The record's bbox centre: 7.08 px/frame.
    - The rear-edge fit (6.36) is biased by the tail swinging, so I discarded it.
  - Taking ≈7.04 px/frame = 169 px/s gives a scale of ≈0.01369 m/px.
  - Height (feet to top of back/head): median 229 px, range 220–233 over the gait. This agrees with the record's 228.
- Height = 229 × 0.0137 ≈ 3.13 m. Across the speed estimates it is 3.11–3.15 m.
- Second route: the scene record's own numbers (228 px, 7.06 px/frame) give 3.11 m. It is consistent.
- It is a plausible adult elephant height. Confidence: good (about ±3%).

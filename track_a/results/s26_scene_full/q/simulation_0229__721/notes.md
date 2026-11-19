# q_721: acceleration of the paper airplane at t = 1 s

- Video: a 2D Blender render at 24 fps. question_fps is also 24, so no re-timing. t = 1 s is frame 24. The camera is static.
- Scale: prior "chalkboard length = 5 m". The board's bounding box including its wooden frame is 1372 px wide
  (x 320–1692; I checked this on frame 24). That gives 5/1372 = 3.644e-3 m/px. If only the green surface (1327 px)
  were used, the result would be 3.4% higher.
- Acceleration = the change of scalar speed (convention). Per-frame speeds are noisy at the ±3 px/frame level, so I
  took the slope of the speed around frame 24 from local fits:
  - `accel.py` uses the scene/ ref track (nose–tail midpoint) and the bbox centre. It fits position polynomials
    (degree 2–4, windows ±4–8 frames) and also fits the speed curve directly. The results range from −2.05 to
    −3.3 m/s², with most between −2.6 and −3.0.
  - `track2.py` / `accel2.py` are an independent re-measurement: background difference, then a weighted centroid,
    the bbox centre and the nose tip, each at 3 thresholds. Linear speed fits over ±3–6 frames and cubic position
    fits give: bbox centre −2.6 to −3.2, nose −2.5 to −3.1, weighted centroid −2.2 to −2.7 m/s².
- Speed near t = 1 s is about 6.05 m/s (≈69–70 px/frame). The plane is slowing: it falls from about 76 px/frame at
  frame 19 to about 55 px/frame at frame 35.
- Answer: magnitude 2.8 m/s². The plane is decelerating, so the signed value is −2.8.
- Confidence: moderate, about ±15%. The spread comes from noise in the per-frame positions and from the choice of
  board extent.

# q_729 — speed of the paper airplane at t = 1 s (m/s)

- 2D Blender scene, static camera, fps = question_fps = 24, so t = 1 s is frame 24. Speed = one-frame backward difference from frame 23 to 24.
- Scale from the prior, chalkboard length = 5 m. measure.py found the board's edges on frame 0 from intensity profiles:
  outer frame x 320–1692 (1372 px), green surface x 342–1670 (1328 px). That gives 3.644 mm/px (whole object, frame included)
  or 3.765 mm/px (green surface only).
- Plane displacement from frame 23 to 24, measured three ways:
  - nose/tail midpoint from the scene record: (1027.9, 342.7) → (1097.1, 345.6), 69.3 px
  - my own mask: bbox mid-x step 69.0 px, centroid step 70.6 px
  - neighbouring steps: 70.0 (frames 22→23) and 67.5 (frames 24→25), so the plane is slowing smoothly and 69.3 px/frame is consistent.
- Speed = 69.3 px × 24 = 1663 px/s, which is 6.06 m/s on the outer-frame scale and 6.26 m/s on the green-surface scale.
- Answer: 6.1 m/s. I used the outer frame, since the bounding box includes it, and leaned slightly toward the other scale.
  The two scales differ by 3%. Confidence: good, about ±4%.

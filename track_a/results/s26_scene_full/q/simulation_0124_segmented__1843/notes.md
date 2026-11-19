# q_1843 — horizontal distance between the two cars at t = 1 s

- 2D top-down render, fps 24 (same as question_fps), so t = 1 s is frame 24. The camera is static and one m/px scale is used for the whole frame.
- "Horizontal distance" in a top-down view means the in-plane (ground-plane) centre-to-centre distance.
- Scale: the black car moves at a constant pixel speed. Mean step over frames 2–48 (template-fit ref points) is 27.16 px/frame; over the clean frames 4–45 it is 27.13; my own mask-centroid steps over frames 5–30 give 27.21 ± 0.6. I took 27.15 px/frame = 651.6 px/s.
  scale = 26.085 / 651.6 = 0.04003 m/px. Car lengths then come out at about 4.6 m and 5.0 m, which is plausible.
- Distance at frame 24:
  - Route 1, scene ref points: dark (736.06, 542.24), silver (733.91, 437.0), 105.29 px.
  - Route 2, my own check (check24.py): the cars' masks touch, so I split them at the empty gap line and took the centroid of each part. That gives 105.03 px.
  - I used 105.2 px, which is 4.21 m.
- If the scale came from the single-frame step at frame 24 (26.87 px) instead, the answer would be 4.26 m.
- Confidence: high (about 2 %).

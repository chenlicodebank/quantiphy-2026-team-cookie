# q_731: speed of the paper airplane at t = 1.25 s

- The fps (24) and question_fps (24) agree, so t = 1.25 s is frame 30. Speed is the one-frame backward difference between frames 29 and 30.
- This is a 2D scene with a static camera, so I used one metres-per-pixel scale from the prior (chalkboard length = 5 m).
  - The chalkboard's outer frame runs from x 320 to 1692, which is 1372 px. My gradient profile in `measure.py` found the same frame edges (y 297 and 736, and the inner edges at x 342 and 1670) as `scene/notes.md`.
  - I took the whole object including its wooden frame, matching the world bounding-box convention: 5/1372 = 0.003644 m/px.
- Plane position: I re-measured it in `measure.py` as the difference from frame 49 (where the plane is gone), using the largest blob. It agrees with the record.
  - Step 29→30: 61.4 px using the mask centroid, 61.9 px using the midpoint of the principal axis. The record gives 62.8 px from its nose/tail midpoint.
  - Neighbouring steps: 64.5, 62.4, 61.4, 59.2 px. The motion is smooth and slowing down, which supports about 61.6 px per frame.
- Result: 61.6 px × 24 fps × 0.003644 m/px = **5.39 m/s**.
- Uncertainty:
  - If the green surface only (1328 px) were taken as the board, the answer would be 5.57 m/s (+3%).
  - The plane flies a little in front of the wall, so some perspective effect is possible, but it is ignored under the 2D convention.
- Confidence: good (within about 5%).

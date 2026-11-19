# q_730: paper airplane acceleration at t = 1 s

- The scene is 2D (the plane flies parallel to the blackboard and its length stays at 136–143 px). fps = question_fps = 24, so t = 1 s is frame 24.
  Convention: acc = speed(24) − speed(23), where each speed is a one-frame backward difference.
- **Scale:** prior chalkboard length = 5 m. I checked the board edges in code (`board.py`):
  - the green surface runs from x 342 to 1670 (1328 px);
  - the outer frame runs from about 321 to 1691 (1370 px).
  - I don't know which one the "length" refers to, so I used the middle value, 1350 px, giving 0.003704 m/px. Either end changes the answer by at most ±1.6 %.
- **Track:** I re-tracked the plane myself (`track2.py`): median background, difference mask (overlay `frames/ov2.png`, clean in frames 16–32), and three reference points: weighted centroid, mask centroid, and the nose/tail midpoint.
  - The scene record's track (`ref_x/ref_y`) agrees with mine to within about 1 px.
- **Speeds** (midpoint, px/frame): 21: 74.5, 22: 72.2, 23: 69.8, 24: 69.5, 25: 67.6, 26: 66.2, 27: 65.2. The plane is slowing down steadily through the apex (frame 23).
- **Acceleration in px/frame²** (`fit2.py`). I used two routes, applied to all three reference points:
  - Route 1, a line or quadratic fitted to speed in windows 18–30 and 20–28: −1.29 to −1.57.
  - Route 2, polynomials fitted to positions, then s24 − s23 computed on the fit: −1.15 to −1.63.
  - Taking −1.45 px/f² as representative: 1.45 × 576 × 0.003704 ≈ 3.09 m/s², slowing down. I report the magnitude, 3.1.
- **Confidence:** moderate, about ±12 %. The acceleration is a small second difference: about 1.4 px/frame² of change against roughly ±1 px of tracking noise.

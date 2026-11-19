# q1666: fire hydrant height (m)

Prior: the person's height is 1.87 m. Depths: man 13.882 m (t=0) and 13.768 m (t=1, frame 30 at question_fps 30);
hydrant 12.565 m. The file is 29 fps and the question is 30 fps; I used frame numbers.

## Measurements (measure.py, hydrant.py)
- **Man:** I differenced each frame against the median image and took the mask's vertical extent.
  - Walking height is 213-224 px. The maximum is 224 at frame 0 (D 13.882) and 223 at frame 30 (D 13.768).
  - I used about 224 px as the standing (rest) height.
- **Hydrant:** on frame 88, with the man far away, the cap top is at y=754 and the base bottom at y≈890.5, so the
  height is 137 px.
  - The scene record's 135 px came from the median image with threshold 215, which misses the pale cap top.

## Scale
I used a pinhole model with the principal point at (540, 540), and converted depth to Z = D·cosθ.
- f from the man at frame 0: 224·13.882·0.957/1.87 ≈ 1591 px.
- f from the man at frame 30: 223·13.768·0.964/1.87 ≈ 1583 px.
- Hydrant: H = 137·12.565·0.954/f ≈ 1.03-1.04 m.
- Ratio route (the cos factors nearly cancel): 1.87·(137/224)·(12.565/13.882)·(0.954/0.957) = 1.032 m.

## Check and confidence
- The two frames (t=0 and t=1) agree within 0.5%.
- If the rest height is 1% taller than the walking maximum, the answer drops to about 1.025.
- **Answer: 1.03 m.** Confidence is good (±3%).

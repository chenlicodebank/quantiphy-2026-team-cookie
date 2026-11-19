# q_231 – speed of the swim ring at 1.0 s

This is a 2D top-down render with a static camera, so a single metres-per-pixel scale comes from the prior (outer diameter of the ring = 1 m).

## Measurements (measure.py)
- I segmented the ring myself: saturated pink/violet pixels, largest component, filled. The overlay is in frames/ov24.png, and the outline hugs the outer edge.
- Motion: the ring moves in a straight line at constant velocity. The linear fit over all 120 frames gives vx = 0.2841 and vy = 0.2851 px/frame, so 0.4025 px/frame. This matches the scene record (0.4023).
  - The raw steps around frame 24 average 0.404 px/frame (frames 20–28). There is no acceleration.
- Diameter estimates:
  - Ellipse fit (record): 73.9 × 71.1 px.
  - Bounding box: 74 px.
  - Area-equivalent diameter of my mask: 74.9 px.
  - I used D = 74 px, which gives 0.01351 m/px.
- Time base: question_fps is 24 and the file is 24.0048 fps, a negligible difference (<0.02 %). Frame 24 corresponds to t = 1.0 s.

## Answer
Speed = 0.4025 × 24 / 74 = **0.1305 m/s**.

## Check
- The scale choice is the main uncertainty. D between 73 and 75 px gives 0.129–0.132 m/s (±1.5 %).
- The speed itself was checked two ways: the raw step mean and the linear fit agree within 0.5 %.

Confidence: high (about ±3 %).

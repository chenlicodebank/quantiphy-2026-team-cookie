# q_3101 – width of the floor lines (cm)

Prior: ball velocity at 0.5 s = 2.94 m/s. Internet video, planar, one scale. fps = question_fps = 30, so t = 0.5 s is frame 15.

**Scale.** Ball pixel speed comes from scene/tracks/basketball.csv. The record's centres were checked as consistent: smooth steps, rms fit is low.
- Forward difference at frame 15: 79.0 px/frame raw, 78.7 stabilised.
- Mean over frames 13–17: 78.2 px/frame.
- I used ≈78.5 px/frame = 2355 px/s, giving a scale of 2.94 / 2355 = 1.248 mm/px (range 1.241–1.253).
- The camera drift is ≤1.3 px/frame, which is negligible.

**Line width** (`measure_lines.py`). I took half-level edge crossings of the L-channel profile in frame 29, where the ball is gone, and measured perpendicular to each line.
- Horizontal maroon line, the one the ball rolls along: 44.6 px median, 44.1–46.9 px along its length.
- Left vertical line: 45.8 px.
- Right vertical line: 48.7 px. It is wider because of mild keystone / nearer the camera.
- Answer from the horizontal line, which is at the ball's position: 44.6 px × 1.248 mm/px = 5.57 cm.
- Using the other lines instead gives 5.5–6.1 cm.

**Check.**
- Using the raw speed at frame 15 alone (79.0 px/frame) gives 5.53 cm.
- With the same scale the ball diameter (225 px) comes out at 28 cm. The real line-to-ball ratio, 44.6/225 times a 24 cm ball, gives 4.8 cm, and real court lines are 5 cm. So the prior-based scale is ~15 % larger than the real-world one, but the convention is to use the prior.

**Answer: 5.6 cm.** Confidence: moderate-high under the prior-scale convention.

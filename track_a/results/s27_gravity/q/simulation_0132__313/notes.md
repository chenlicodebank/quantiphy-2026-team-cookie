# Q313: horizontal speed of the apple in the air (m/s)

The video is a 2D Blender render at 120 fps, and question_fps is also 120. The prior is g = 9.8 m/s². There is no depth_info.

## Method (fit.py, fit2.py)
- I used the record's apple track (scene/tracks/apple.csv). The apple leaves the counter at frame 141 and hits the floor at frame 192, so the free flight is frames 142–191.
- On each fitting window I fitted y(frame) with a quadratic (acceleration in px/frame²) and x(frame) with a straight line (vx in px/frame).
- The scale comes from gravity: m/px = 9.8 / (a_px × 120²). The speed is then |vx| × 120 × m/px = |vx| × 9.8 / (a_px × 120).

## Results
- Circle-fit centre (ref_x, ref_y), frames 146–190: a = 0.4425 px/f², vx = −3.604 px/f, which gives **0.665 m/s**.
- Other windows (142–191, 144–190, 150–190) give 0.665 to 0.666. The split halves give 0.648 (144–170) and 0.652 (165–190), but those are noisier.
- Second route, the raw mask centroid (mask_cx, mask_cy), frames 146–190: a = 0.4409, vx = −3.607, which gives **0.668 m/s**. The residuals are smaller here (about 0.3 px).
- A cubic fit leaves the acceleration unchanged (0.4425). The apple's radius is constant at 30.1 px in flight and 30.2 px on the counter, so its depth does not change and one 2D scale applies.

## Checks
- Scale check: 9.8 / (0.4425 × 14400) = 1.54 mm/px. The 61 px apple then comes out at about 9.4 cm across, which is a plausible real apple.
- Horizontal speed is nearly constant through the fall. There is a tiny drift of −0.0027 px/f², which is negligible.

## Answer
**0.666 m/s.** Confidence is high, with an error of about ±2%.

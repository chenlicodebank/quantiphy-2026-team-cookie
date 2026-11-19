# Q1504 – height of the letter neon sign (m)

Prior: each window frame is 1.48 m wide. depth_info: the sign is 34.5 m from the camera; the bird is about 25 m away.
The file rate and question_fps are both 24. The camera is static.

## Method
The sign ("BE DIFFERENT") is mounted on the central facade, so it sits at the same depth as the facade windows
around it. Facade rows show almost no perspective change in window width, so I used one px→m scale from the windows
on frame 72 (any frame works; the backdrop is static).

- **Window width** (`measure4.py`): the outer opening width, taken at 60 % of the local wall level. I measured it in
  three window rows (y≈120–190, 420–510, 650–750) and four central columns. Results: 129, 129, 125, 129, 130, 126,
  130, 130, 120, 128 px, with outliers at 106 and ~153 (edge or overlap effects). The median is about 126–128 px.
  - The inner value, from the lit frame member to the edge of the glass, is about 113–122 px.
  - I used 126 px.
- **Letter height** (`measure5.py`): the half-maximum extent of the green channel, which separates the white letter
  cores from the red glow, measured on vertical strokes of B, D, I, R/E and T. It is rows 271–351, so 80–81 px. The
  white-core bounding box (`measure.py`) is 272–351 px, which agrees. The scene record says 81 px, which also agrees.
  The glow (137 px) is excluded.

## Result
Height = 81 / 126 × 1.48 = **0.95 m**.

## Checks and sensitivity
- If the window width is 130 px, the height is 0.92 m. If it is 113 px (inner frame only), the height is 1.06 m.
- Implied focal length: 126 × 34.5 / 1.48 ≈ 2940 px, which gives a horizontal field of view of about 36°. That is
  plausible.
- Window aspect check: the windows are 164 px tall, which is 1.93 m at this scale. That is plausible for a window
  1.48 m wide.
- The second route (pinhole with the 34.5 m depth) is not independent, because the windows are at the sign's depth.

Confidence: moderate. The main uncertainty is where the window "frame" edges are (±5 %).

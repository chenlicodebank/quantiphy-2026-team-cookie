# q_317: horizontal speed of the apple when it leaves the table

Video: 2D side view, 30 fps (file and question fps are the same), static camera. Prior: g = 9.8 m/s^2. No depth_info.

## Method (fit.py)
- I used the track in scene/tracks/apple.csv. The apple leaves the counter edge at about frame 34 and is in free fall over frames 35-47. It hits the floor at frame 48.
- I fitted a parabola to the vertical position over the free-fall frames. With the centroid over frames 36-47 the vertical acceleration is 7.077 px/frame^2. The other windows I tried (37-47, 38-47, 36-46, 39-47) give 7.01-7.08 px/frame^2, whether I used the centroid, the bounding-box centre or the top edge.
- Scale: 9.8 / (7.077 x 900) = 0.001539 m/px.
- Horizontal velocity, from a linear fit of x over the same window: -14.32 px/frame. The per-frame dx is between 14.0 and 15.0 px for frames 26-47, so the horizontal speed is constant: it is the same on the counter top, at the edge and through the fall.
- v_x = 14.32 x 30 x 0.001539 = 0.661 m/s.

## Checks
- Across all the fit windows and position definitions, the answer ranges from 0.658 to 0.668 m/s.
- Plausibility: the apple's diameter is 62 px x 0.00154 = 0.095 m, which is a realistic size for an apple, so the scale holds up.

Answer: 0.662 m/s. Confidence is high, with an error of about 2%.

# q_1831 — speed of the right (last) ball at t = 2 s

- 2D Newton's-cradle-type clip, 30 fps (file fps = question_fps, so no re-timing). t = 2 s -> frame 60.
- The asked object is ball_right, the ball knocked out at about frame 28. It reaches its apex at frame 54 and is swinging back (moving down-left) at frame 60.
- measure.py re-measures the ball independently of scene/. Mask = any RGB channel < 235. I took the rightmost component, fitted a least-squares circle to its contour, and used the circle centre as the ball's position. My centres match scene/tracks/ball_right.csv to within 0.2 px.
- Per-frame centre displacement (px/frame): f57 3.03, f58 4.37, f59 5.62, **f60 6.75**, f61 8.22, f62 9.07, f63 11.10.
  The trend is smooth, and a linear fit over f57–63 gives about 6.8 at f60. I used 6.75–6.8 px/frame.
- Scale: the ball diameter (prior) is 2 m. The circle-fit radius is 83.1–83.3 px (D ≈ 166.3), the equal-area diameter is about 167, and mask_h is 165. I used D ≈ 166 px, which gives 0.01205 m/px.
- Speed = 6.78 px/frame × 30 × 0.01205 = 2.45 m/s.
- Second-route check: the scene/ track gives 6.80 px/frame at f60 by backward difference. With the scene's diameter of 165.6 px this gives 2.46 m/s, which agrees.
- Confidence: high, about ±3%. The main uncertainty is the pixel diameter (165–167 px).

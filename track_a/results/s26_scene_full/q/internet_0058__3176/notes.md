# q3176: ball velocity at t = 2.00 s (frame 60, 30 fps)

The file's fps and question_fps are both 30, so t = 2.00 s is frame 60. The ball is in free flight there: release is at
frame 22, the apex at frame 42 and the catch at frame 64. A zoomed crop of frame 60 shows the ball centre at about
(1118, 370), which matches the scene/ track (raw 1117.9, 369.6).

## Scale from the prior (g = 9.8 m/s^2)
I fitted a parabola to the ball's vertical centre over the free flight (fit.py):
- Stabilised track, frames 23-63: a = 2.223 px/frame^2, which gives a scale of 9.8 / (2.223 × 900) = 4.90 mm/px.
- The other windows give 4.85-4.93 mm/px (frames 25-61, 30-63, 23-45 and raw coordinates). The descent alone (frames
  45-63) gives 5.20 mm/px; motion blur and slight perspective are the likely causes.
- Sanity check: the ball's 50.4 px diameter becomes 0.247 m, which is basketball-sized.

## Velocity at frame 60
| Method | Speed (m/s) |
|---|---|
| Forward difference, frames 60→61, stabilised | 5.74 |
| Forward difference, raw | 5.71 |
| Parabola derivative plus horizontal drift | 5.79 (stabilised) / 5.71 (raw) |
| Backward difference | 5.54 |

Answer: 5.74 m/s (forward difference with the annotators' single scale). The independent routes agree within about 1 %.
The main uncertainty is the scale (about ±3 %), so my confidence is moderate to high.

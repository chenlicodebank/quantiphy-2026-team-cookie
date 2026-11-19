# Q3216 – person's velocity at 4.4 s (frame 132, 30 fps)

The file rate and question_fps are both 30, so frame = round(4.4 x 30) = 132.

## Scale from the prior (g = 9.8 m/s^2)
Script: `fitg.py`. I fitted a parabola to the basketball's vertical centre in the free-flight frames of `scene/tracks/ball.csv`:
- flight 1 (frames 82–112): 3536 px/s^2 raw, 3543 px/s^2 with camera drift removed
- flight 2 (frames 117–142): 3536–3546 px/s^2 raw, 3562–3570 px/s^2 with drift removed (fit residual about 0.2 px)
- The per-frame second differences are about 3.9–4.0 px/frame^2, which agrees.

I took g = 3550 px/s^2, which gives a scale of 9.8 / 3550 = 0.00276 m/px.
- Sanity check: the ball's 85 px diameter comes out at 0.235 m (a real basketball is about 0.24 m), and the person's 620 px height comes out at 1.71 m. Both are plausible.

## Person's horizontal speed at frame 132
She walks to the right. The camera drifts slightly, so the drift was removed with the scene's camera transform.
- Route 1, the scene record's `head_x_bg`: 10.9 px/frame (backward difference) and 10.7 px/frame (forward difference). Over frames 128–136 the average is 11.2 px/frame, and over 130–134 it is 11.2 px/frame.
- Route 2, my own template tracking of the head and of head plus torso (`track_head.py`): 12.1 px/frame (forward difference at 132). Averaged over frames 130–134 it is 11.5–11.7 px/frame, and over 128–136 it is 11.1–11.2 px/frame.

I used about 11.3 px/frame = 339 px/s.

v = 339 x 0.00276 ≈ 0.93 m/s.

Plausible range: 0.89–1.0 m/s, depending on the reference point and the smoothing window. Confidence is moderate to good.

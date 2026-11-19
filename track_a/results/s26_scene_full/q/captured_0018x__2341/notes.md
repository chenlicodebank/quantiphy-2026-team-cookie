# q_2341 — soccer ball velocity at 3.4 s (cm/s)

## Problem: asked time lies outside the clip
- The clip has 49 frames at 24 fps (2.04 s). question_fps = 24, so t = 3.4 s means frame 82, which does not exist.
  The question time must refer to the original, longer recording; this clip is a trimmed piece of it with an unknown offset.
- The clip runs in real time: a parabola fitted to the ball's fall (frames 30-39, with the dropped capture frame
  between 35 and 36 corrected) gives a = 8.86 m/s^2 (Z = 2.8 m, f = 0.5959*1280 = 762.8 px), close to the 9.8 prior.
  So the clip is not slowed down or subsampled, and the timestamp cannot be mapped by rescaling.

## Measurements (fit_fall.py, scene/tracks/soccer_ball.csv centroids, back-projected at Z = 2.8 m)
- Release (zero velocity) at real frame 28.5. Floor impact at frame 39 (real frame 40), when the speed is about 4.2 m/s.
- Fitted fall speed (cm/s) by frame: 30: 55, 31: 92, 32: 129, 33: 166, 34: 203, 35: 240, 36: 313, 37: 350, 38: 387, 39: 424.
- After the bounce (raw forward differences): about 250 cm/s at frame 40, falling to about 30 at frame 47 (near the apex).

## Answer choice
- Under the natural assumption that the clip is the second half of a roughly 4 s original (offset about 2 s), 3.4 s maps to
  clip frame 33-34, in mid-fall: about 166-203 cm/s. From the gravity check, v = 9.8 * (34 - 28.5)/24 = 2.25 m/s.
- The answer is 200 cm/s. This also hedges across the clip's speed range (30-424 cm/s).
- Confidence: LOW. The answer depends on an unknown time offset, not on the measurement itself.

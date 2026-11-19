# Q2323: velocity of the tennis ball at 3.4 s (cm/s)

**Problem:** the question's time can't be measured. 3.4 s at question_fps 24 is frame 82, but the clip has only
49 frames (0–48, 2.04 s). The file fps is also 24. The question's time probably refers to a longer original recording.

Tennis ball = `green_ball` in scene/ (right person's fingertips, released at f27). I checked it on the contact sheet.

## Scale (two routes, they agree)
- Gravity prior: a parabola fit to cy over f29–35 gives 3106 px/s² → 9.8/3106 = 3.15 mm/px → depth 2.41 m (f = 763 px).
- Size: a tennis ball is about 6.7 cm and measures about 22 px → depth 2.32 m.
- The near-person depth is 2.002 m, and the ball is held at her outstretched fingertips, so a depth of about 2.3–2.4 m is consistent.

## Speeds (backward difference, Z = 2.3 m, cm/s)
- Free fall f28–35: 200 → 384.
- Bounce f35/36: a frame was probably dropped here.
- Rebound f36–45: 293 → 7 at the apex.
- Falling again f46–48: 11 → 90.
- Median speed over the moving window: about 190 cm/s at Z = 2.3 m and 199 cm/s at Z = 2.41 m.

## Answer
190 cm/s. This is a hedged guess (the median speed while the ball moves), not a measurement at 3.4 s, because that frame
does not exist in this clip. Confidence is low.

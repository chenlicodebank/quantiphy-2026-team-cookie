# q_2999: ball velocity at t = 0.40 s (frame 20), prior g = 9.8 m/s^2

## Data
- Track: `scene/tracks/ball.csv`, which gives the visible ball centre. I checked the frames (the ball is a grey ball dropped in front of a door). The camera is static.
- There are dropped frames. The step into frames 7, 12, 17 and 22 is doubled (56.9 px between 24.8 and 32.4, and so on). The source was about 60 fps re-timed to 50 fps by dropping 1 frame in 6.
  - So the real time between source frames is 1/60 s.
  - On average this matches the nominal time: 6 source intervals at 1/60 s take the same time as 5 output intervals at 1/50 s.
  - I used a 50 fps time base for the question time (t = 0.40 s is frame 20). For the kinematics I used the real 1/60 s per source interval.

## Method (`fit.py`)
- I gave each output frame a source index, counting 2 intervals for each doubled step. I then fit a quadratic y(t) with t = source index / 60.
- From the fit: pixel acceleration a_px ≈ 8890 px/s^2 (frames 8–23, rms 0.56 px), so the scale is 9.8 / a_px = 1.10e-3 m/px.
  - Sanity check: the ball's 76 px diameter comes out at 8.4 cm, and the door knob at about 6.8 cm. Both are plausible.
  - With a nominal 1/50 s time base the knob would come out at about 10 cm, which is too big. This supports the 60 fps source.
- Velocity at frame 20:
  - Forward difference: (y21 − y20) = 54.06 px over 1/60 s, giving **3.58 m/s**.
  - Fitted instantaneous velocity: **3.52 m/s**.
  - Other fit windows (frames 7–23, 10–23, 13–23) give 3.50–3.68.

## Second route
- A naive quadratic fit in nominal 1/50 s time (ignoring the dropped frames) gives an instantaneous v(0.40) of 3.40 m/s. This is consistent.
- Naive per-frame second differences are dominated by the doubled steps and range from 1.5 to 4.4 m/s. They are unusable.

## Caveats
- The per-step acceleration falls from about 3.3 px/step² early on to about 2.45 px/step² late. This could be air drag on a light ball.
  - If the scale is taken from the early frames, the result is about 3.0 m/s. This is also consistent with g × 0.30 s of fall from the release near frame 5.
- Answer: 3.5 m/s. This is the real-time fit, shaded slightly toward the nominal-time fit.
- Confidence: moderate, about ±10%.

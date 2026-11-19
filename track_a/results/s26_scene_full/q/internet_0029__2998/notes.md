# q_2998: ball velocity at 0.20 s (prior: g = 9.8 m/s^2)

The question frame is t = 0.20 s, which is frame 10 at 50 fps (the file's rate and question_fps agree).
The camera is static (see scene notes). I used the ball centre track in scene/tracks/ball.csv. Frames 8-23 come from the mask centroid, accurate to about ±1 px.

## Timing
- The vertical steps are 15.5, 18.9, 21.7, 24.8, **56.9**, 32.4, ... One step in every five output frames is doubled (frames 7, 12, 17, 22 and 24). So the clip is 60 fps footage with 1 frame in 6 dropped to give 50 fps. Real time per source step is 1/60 s.
- I fitted the track with each doubled step counted as two 1/60 s intervals (fit.py). A quadratic fits frames 8-23 with an rms of only 0.2-0.56 px, which confirms this timing model.
- The 1/60 timing is also physically plausible. It gives a scale of 1.10 mm/px, so the ball is 76 px ≈ 8.4 cm and the door knob is 61 px ≈ 6.7 cm. With naive 1/50 timing the knob would be about 9 cm, which is too large.

## Measurement
- Pixel acceleration from the fit over frames 8-23: 8887 px/s^2. Scale = 9.8 / 8887 = 1.103 mm/px.
- Forward difference at frame 10: y11 - y10 = 24.76 px in one source interval (no frame is dropped between them). That is 1486 px/s, or **1.64 m/s**.
- The fitted instantaneous velocity at frame 10 is 1.56 m/s.
- Other fit windows: 8-21 gives 1.62 / 1.53, 13-23 gives 1.69 / 1.65, and 8-16 gives 1.57 / 1.47 (forward difference / instantaneous).
- **Answer: 1.6 m/s.**

## Second route and alternatives
- Local second differences inside each 4-step segment average 2.65 px/step^2, which is 9560 px/s^2 at 60 fps. This agrees with the fit (the acceleration falls slightly over the fall, perhaps from drag or perspective).
- If an annotator ignored the dropped frames, the answer would come out differently:
  - Local differences at 1/50 s: 1.83 m/s.
  - A naive global fit at 50 fps: 1.28 m/s (forward difference) or 1.45 m/s (fit).
- 1.6 m/s is the physically consistent value, and it lies within about 15% of the naive 1.45 and 1.83 readings.

## Confidence
Moderate. The measurement itself is good to about ±5%. The main uncertainty is which timing convention the reference used.

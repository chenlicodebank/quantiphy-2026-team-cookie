# Q210 – extension of the charging post at 0.5 s

2D scene, 24 fps (file fps = question_fps, no re-timing). The post/head and the phone on it rise rigidly together.

## Method (measure.py)
- Mask = |RGB - background| > 40 in strip x 700-790 (phone only); phone top row per frame.
- Tops: frames 0-1 at y=955 (rest), then exactly 24 px/frame upward (one frame 23) until frame 27 (y=332), rest after.
  Matches scene/tracks/phone.csv (23.96 px/frame) and the column shaft track.
- Scale from the prior: 0.2 m/s = 575.1 px/s -> 3.478e-4 m/px.
- t = 0.5 s -> frame 12, top y = 691. Extension = rise from rest = 955 - 691 = 264 px -> 0.0918 m.

## Check
- Second route: 11 frames of constant motion (frames 1->12) x (1/24 s) x 0.2 m/s = 0.0917 m. Agrees.
- Alternative reading: if the motion were taken to start at t = 0, 0.2 x 0.5 = 0.10 m; but the video shows
  frames 0 and 1 the same (motion starts after frame 1), so the measured 0.0918 m is the answer.

Confidence: high for the measured value; the main risk is the start-time convention (would make it 0.10).

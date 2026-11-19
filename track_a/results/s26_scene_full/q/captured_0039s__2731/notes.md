# q_2731 — white ball displacement 1.0 s → 1.5 s (cm)

Video: a lab recording at 24 fps (the file and question_fps are both 24). t=1.0 s is frame 24 and t=1.5 s is frame 36. Camera: f = 0.5959×1280 = 762.8 px, principal point (640, 360).

## Measurement (measure.py)
I re-measured the ball mask in code: it differs from frame 48, which has no ball, and it is bright and unsaturated. I then fitted a least-squares circle to the mask contour. Three centre estimates (circle fit, bbox centre and centroid) agree to within 0.5 px:
- frame 24: (542.28, 455.54), D = 25.7 px
- frame 36: (496.54, 498.47), D = 38.3 px

These match scene/tracks/ball.csv.

## Back-projection with depth_info (1.014 m at 1.0 s, 0.737 m at 1.5 s)
- Method card ((u−cx)/f, (v−cy)/f, 1) × depth, which treats the depth as z: 27.72 cm
- Depth treated as the Euclidean ray length (the unit ray × distance): 28.52 cm

The centre estimators all give the same result (28.51–28.53 cm and 27.72 cm).

Answer: **28.1 cm**. This is the midpoint of the two depth readings, within 1.5 % of each.

## Checks and caveats
- The pixel displacement is 62.6 px. The ball moves mostly toward the camera: Δz is about 0.27 m, which is the main part of the answer.
- The apparent diameter ratio (38.3/25.7 = 1.49) is larger than the depth ratio (1.014/0.737 = 1.376). The implied ball diameter is 3.4 cm at 1.0 s and 3.7 cm at 1.5 s. If the depths had been taken from the diameter instead, Δz would be larger by about 0.05 m. I used the given depth_info as the question instructs.
- The record notes a possible dropped frame at 35→36. That does not matter here, because displacement uses only the end positions.
- Confidence: good, about ±3 %.

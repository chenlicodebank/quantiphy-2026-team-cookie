# q_2203 — length of the pendulum string (cm)

The video is a lab clip: 24 fps (the file rate and question_fps are the same), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
The prior is g = 9.8 m/s². depth_info gives the ball distance at t = 0.3, 0.6, 0.9, 1.2, 1.5 and 1.8 s, which are frames 7, 14, 22, 29, 36 and 43.

## Checks on the record
- I re-detected the ball centroids myself (`measure.py`). They agree with scene/tracks/ball.csv to within about 1 px, so I used the record's centroids.
- Pivot pixel (`strline.py`): I fitted a line to the string in each of the 49 frames. The lines meet at about (638, 235), with 2.4 px rms.
  The visible top of the string is at y = 226–233. I took the pivot as (638, 229) and also tested pixels from (638, 220) to (640, 235).
- Ball diameter, from the depth and the equivalent pixel diameter: 6.8–7.7 cm, median 7.13 cm, so r ≈ 3.6 cm.

## Route 1: 3D geometry (`pivotfit.py`)
- I back-projected the ball centre at the 6 depth times with the given Euclidean distances.
- The pivot was constrained to the ray through pixel (638, 229). Fitting its distance and the radius L gives a pivot distance of 1.489 m and **L = 0.327 m** from the pivot to the ball centre.
- The residuals are ±2.4 cm. Leaving out one point at a time gives L = 0.322–0.331. Moving the pivot pixel by ±9 px changes L to 0.318–0.341.

## Route 2: period with the g prior (`period.py`)
- Far-end turning points (vertices of the cy minimum) are at frames 2.93 and 32.24, so T = 29.31 frames = 1.221 s.
  The near-end turning points (cx maximum) are at 16.25 and 45.92, which gives the same 29.7-frame spacing within noise.
- The small-angle formula gives L = gT²/4π² = 0.370 m. The swing is large: the amplitude from the 3D geometry is about 45–51°.
  The exact elliptic-integral correction (factor 1.04–1.05 on T) gives **L ≈ 0.335–0.342 m**.
- Route 1 and route 2 agree to about 3–4%. Best estimate of the pivot-to-ball-centre length: L ≈ 0.333 m.

## Answer
- The string runs from the pivot to the top of the ball, so its length is L − r ≈ 0.333 − 0.036 = 0.297 m, about 30 cm.
- If "string length" means the pendulum length (pivot to ball centre), the value is about 33.3 cm.
- I answered **30.5 cm**: the string-only reading, nudged slightly toward the other reading.
- Confidence: moderate. The measurement is about ±4%, and the bigger uncertainty is which of the two definitions is meant (about 10% apart).

# Q40 – length of the white car (m); prior: car acceleration = 4 m/s^2

This is a 2D top-down clip with a static camera, so one m/px scale applies, taken from the prior.
fps = question_fps = 24.

## Pixel acceleration (fit.py)
I fitted a quadratic to the car's centre y (scene/tracks/car.csv, origin from the front edge) over several frame windows:
- 3–71: −162.9 px/s² (rms 0.34 px)
- 6–71: −163.0
- 3–40: −162.5
- 40–71: −161.8
- 20–60: −163.2
- 5–36: −162.2

The windows agree within ±0.5 %, and a cubic term is negligible, so the acceleration is uniform. I used a = 162.8 px/s².
Scale = 4 / 162.8 = 0.02457 m/px.

## Pixel length (length2.py)
I took the row-mean profile across the car's width at frame 0 and placed each edge at half-max between road and car brightness:
front edge y ≈ 811.6, rear edge y ≈ 1046.2, so the length is 234.6 px. The scene record gives 234 px
(per-frame range 232–237), and frames 30 and 60 show the same body run, so the length is consistent along the track.

## Answer
234.6 px × 0.02457 m/px = **5.76 m**. Using the record's 234 px instead gives 5.75 m.
For a sanity check, the car's width is 87 px, which gives 2.14 m. That is van-like and plausible.

Confidence: high (about ±2 %).

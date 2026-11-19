# q165 – length of the car (prior: car acceleration = 10 m/s^2)

2D simulation, 24 fps (file fps = question_fps, no re-timing).

## Scale from the prior
`fit.py` fits a quadratic to the car's horizontal position over frames (scene/tracks/car.csv):
- mask centroid, frames 2–71: a = 0.5072 px/frame^2 (resid 0.17 px); frames 2–40: 0.5070; frames 40–71: 0.5040
- bbox left edge: 0.509; bbox centre: 0.505
- I adopted a = 0.507 px/frame^2, which is 0.507 x 576 = 292 px/s^2.
- The scale is 10 / 292 = 0.03424 m/px.

## Car pixel length (re-measured from the video in fit.py, thresholds 6/15/30)
- frame 0 (at rest, x≈1560): 172 px
- frame 24: 170 px
- frame 48 (image centre): 166 px
- frame 71 (left edge): 173 px
- Mean over the track: 169.8 px.
- The variation comes from mild perspective (end faces show towards the image edges).
- I used about 168 px (between the centre-of-image value and the mean).

## Answer
168 px x 0.03424 = 5.75 m. The range is 5.68 m (166 px) to 5.92 m (173 px), within ±3%.

Sanity check: this matches a Cybertruck-like pickup (about 5.7 m).

Second route: the length at each sampled frame (166–173 px) gives 5.68–5.92 m. The acceleration fitted on separate halves of the motion agrees within 0.6%.

Confidence: high (about ±3%).

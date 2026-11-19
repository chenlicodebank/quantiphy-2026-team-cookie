# Q171 — height of the car (m); prior: car acceleration = 10 m/s^2

2D side-view simulation, static camera, 24 fps (file fps = question_fps, so no re-timing).

## Scale from the prior (measure.py)
- Car x position = weighted mask centroid (|frame - grey bg|) per frame, frames 1-40.
- Quadratic fit x(t): a = -201.57 px/s^2 (start frame 1), -201.41 (start frame 3); rms residual 0.07 px.
- Second route: per-frame speeds go from 26.3 px/s (frames 1-2) to 341 px/s (frames 39-40), i.e. 198.8 px/s^2.
- Scale = 10 / 201.5 = 0.04963 m/px.

## Car height in pixels (profile.py)
- The scene record's ~36.5 px (35/38 integer jitter) and my first half-of-90th-percentile threshold (34.3 px) both
  cut into the roof. The roof is light, so its contrast against the grey bg is only ~60, versus ~120 for the body/wheels.
- Row-by-row contrast at frame 0: row 584 = 7, row 585 = 55 (roof apex, ~90 % covered), ..., row 622 = 58 (~50 % of the
  wheel contrast), row 623 = 15. So the top edge is at ~585.1 and the bottom at ~622.6, giving a height of 37.5 px (±0.3).
  The bottom row is 622 in every frame. The top shows as 585 or 588 in the record only because of where the threshold falls on the faint roof; the car does not move vertically.
- Height = 37.5 x 0.04963 = 1.86 m.

## Check
- Length: about 115 px at the low threshold, which is 5.7 m. That fits a Cybertruck (5.68 x 1.79 m), and the
  height/length ratio of 0.32 matches the real truck's 0.315.

Answer: 1.86 m. Confidence: good (about ±3 %).

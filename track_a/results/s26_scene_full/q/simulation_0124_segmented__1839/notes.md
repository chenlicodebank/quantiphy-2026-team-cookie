# Q1839 – length of the grey/red (silver, red-striped) car

2D top-down video, static camera, 24 fps (file and question agree). One m/px scale from the prior.

## Scale (prior: black car speed = 26.085 m/s)
- measure.py: per-frame steps of the dark car's template-fit centre (scene/tracks/car_dark.csv), frames 2–48:
  mean 27.16 px/frame, median 27.28, std 0.62 (constant speed; clean frames 5–45 only: 27.13).
- Speed = 27.15 px/frame × 24 = 651.6 px/s → scale = 26.085 / 651.6 = 0.04003 m/px.

## Silver car length
- Scene record (clean frames, 50 frames): median 126.0 px along the main axis (threshold 235, may be ~1 px large).
- Own check (check.py, min-area rect of the mask at frames 10/20/30/40/50, thresholds 235/200/150):
  122.8–128.2 px, mostly 124–126 px at the tighter thresholds.
- Taken as ≈125.5 px → 125.5 × 0.04003 = 5.02 m.

## Cross-check
- Dark car length 115.8 px → 4.64 m; silver/dark ratio and absolute values are plausible for cars.
- Range of plausible pixel lengths (124–126) gives 4.96–5.04 m (±1 %).

Answer: 5.02 m. Confidence: high (scale from a very steady speed, length well defined).

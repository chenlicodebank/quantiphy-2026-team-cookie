# Q175 – length of the car (prior: car acceleration = 10 m/s²)

2D simulation, fixed camera, 24 fps (file fps = question_fps, so no re-timing). The car (a Cybertruck-like pickup) starts at rest
at frames 0–1, then accelerates uniformly to the left.

## Scale from the prior
- I took the car's mask centroid x from scene/tracks/car.csv and fitted a quadratic over frames ≥1. The fit gives
  x = … − 0.18531 f², so a = 0.3706 px/frame² = 213.5 px/s². The residual is 0.16 px, and fitting from frame 2 or frame 5
  gives the same value.
- Second route: the slope of the per-frame backward-difference speed against time gives 214.1 px/s², which agrees.
- Scale = 10 / 213.5 = 0.04684 m/px.

## Car length in pixels (measure.py)
- I measured the car's horizontal extent every 4 frames (11 frames in total), using a mask that covers the whole car
  including the wheels.
- Integer bbox: 122–125 px with no morphological opening; the scene record gives 120–123 px with opening.
- Sub-pixel length, which counts the partly covered anti-aliased edge columns as fractions: mean 121.97 px
  (range 120.8–123.6).
- Adopted value: about 122 px.

## Answer
L = 122 px × 0.04684 m/px = **5.72 m**. The range across pixel-length readings is 5.67–5.77 m.

Sanity check: a real Cybertruck is about 5.68 m long, which is consistent. Confidence: high, about ±2%.

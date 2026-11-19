# q3147 – height of the canopy (ivy pergola), internet_0054

Prior: average speed of the scooter rider = 4.9 m/s. fps = question_fps = 30 (no re-timing issue).
Convention: one planar scale = prior world value / prior pixel value.

## Scale (speed.py)
Mean per-frame pixel speed of the rider over frames 0–93, using the scene/ track:
- camera-stabilised (measured against the background; the camera drifts ~+0.34 px/frame):
  bbox centre 496.9, front axle 497.6, torso 498.8 px/s  -> 497 px/s
- raw image coords: 486.7–488.6 px/s
Scale = 4.9 / 497 = 0.00986 m/px (the raw-coordinate track gives 0.0101 m/px, about 2 % higher).

## Canopy pixel height (canopy.py, frame 0)
- Canopy top: top edge of the green foliage mass, found with a green-pixel run detector in each column
  (x 960–2700). Median y 524, IQR about 512–534. Points checked on frames/canopy_top.png. A few sprigs stick up to ~505.
- Ground: base of the central post / path edge, read from brightness profiles: y ≈ 1087–1090.
- Canopy height ≈ 1089 − 522 ≈ 567 px (≈585 px if you include the top sprigs).

## Answer
567 px × 0.00986 m/px = 5.59 m, so the answer is **5.6 m**. Range across the choices above: 5.6 to 5.9 m.

Other reading: the canopy's thickness alone, from the foliage top (~522) to the bottom of the dark beam (~700), is
about 178 px, which gives 1.75 m. I did not choose this reading.

Sanity check: in real-world terms the prior speed looks too high. The rider is about 279 px tall, which would be
2.75 m at this scale. The scale is still taken from the prior, as the convention requires, so the canopy height
comes out above a real pergola's (about 3.3 m at a realistic scale).
Confidence: moderate. The scale is solid (to about 2 %). The main uncertainty is which points the annotator
treated as the canopy top and the ground.

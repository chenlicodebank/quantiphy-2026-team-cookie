# Q1810 – shark length (m)

2D side-view render at 24 fps (file fps = question_fps, so no re-timing). The prior says the shark's acceleration is 1 m/s².
That gives the metres-per-pixel scale.

## Pixel acceleration (fit.py)
I fitted a quadratic x(t) to the shark track (scene/tracks/shark.csv), frames 1-53 (the shark sits still from f0 to f1, then
accelerates smoothly leftward with no bounce):
- mask centroid: 85.8 px/s² (rms 0.40 px); the same value on each half (85.3 and 84.9)
- bbox centre: 85.6; tail tip: 84.8; nose: 86.4
- Adopted: **85.6 px/s²**, so scale = 1/85.6 m/px = 0.01168 m/px.

## Pixel length (len.py, re-measured on frames 10, 24, 40 and 53)
The record's nose_x sometimes misses the pale snout tip (bbox_w 272-273 at f10 and f24). With thresholds of 10, 20 and 30, the
real extent is 277-278 px in every frame checked, from the nose tip to the tail-fin tip. The shark stays horizontal and is never
clipped. Adopted: **277.5 px**.

## Answer
277.5 / 85.6 = **3.24 m**.

Second route: the scale from the tail-tip acceleration (84.8) gives 3.27 m, and the centroid (85.8) gives 3.23 m. These agree
within 1 %. A length of about 3.2 m is plausible for a shark. Confidence: high (about ±2 %).

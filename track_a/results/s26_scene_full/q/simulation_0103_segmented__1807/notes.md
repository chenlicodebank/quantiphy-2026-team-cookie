# Q1807 – initial speed of the shark (prior: shark acceleration = 1 m/s^2)

2D scene, 24 fps (file fps = question_fps). The shark moves left along a constant y at constant pixel size.
Frames 0 and 1 are identical (rest frame). Motion starts at frame 1.

Method (fit.py): quadratic fit x(t) to the shark track from scene/tracks/shark.csv, frames 1-53 (also 2-53 and 5-53),
for several reference points. Scale comes from the prior: 1 m/s^2 = |a_px|, so v0 [m/s] = v_px(start) / |a_px|.

- mask centroid: a_px = 85.84 px/s^2, v(f1) = 175.97 px/s -> v0 = 2.050 m/s (rms 0.40 px; same result for frames 2-53 and 5-53)
- bbox centre: 2.059-2.066; nose: 2.03-2.06; tail: 2.07-2.09
- Second route: linear fit of per-frame backward-difference speeds (frames 2-53): a_px = 86.1, speed at f1 = 174 px/s -> 2.02 m/s.

The fitted quadratic passes through the f1 position (rms 0.4 px), so the shark leaves f1 already moving at ~176 px/s:
it has a non-zero initial speed. It is not starting from rest.
Answer: 2.05 m/s (most likely the true value is 2 m/s; the routes agree within about ±2%). Confidence: high.

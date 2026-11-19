# q_401 — speed of the astronaut at t = 0.5 s (m/s)

Prior: astronaut height = 2.2 m. 2D video, static camera. question_fps = file fps = 24, so t = 0.5 s → frame 12.
The speed is the backward difference p(12) − p(11).

## Scale (measure.py)
- Vertical extent of the astronaut (largest bright blob) at frames 0, 6 and 12, with thresholds 20–90: 88–91 px.
  The half-max rows are 479–565 at frame 0 and 461–549 at frame 12, so the height is ≈ 89–90 px. I used **90 px**,
  which gives 2.2 / 90 = 0.02444 m/px. The figure is upright (tilted ~5°), so its vertical extent is its height.
- SAM 3 check: the frame-11 mask is 90 px tall (rows 461–550), which matches. The frame-12 mask is 87 px (rows 461–547).
  That is 3.4 % short because SAM cut off the tips of the feet; the zoomed crop (frames/f12.png) and my threshold
  (rows 459/460–549/550) show the feet go down to about y = 549–550. I kept 90 px.

## Motion
- Phase correlation of a 140x160 crop around the astronaut, consecutive frames. Steps in px/frame:
  f10 2.34, f11 2.59, f12 2.84, f13 2.92, f14 3.13. It is a smooth ease-in.
- Intensity-weighted centroid steps (noisier): f11 2.48, f12 2.69, f13 3.47, f14 2.44.
- Quadratic fit of the phase-correlation steps over f6–18, value at f12: 2.73. A cubic fit of the centroid positions
  over f4–20 gives a backward step at f12 of 2.67. The scene record's centroid gives 2.63.
- SAM centroid step f11→f12 (0.39, −4.83) is not usable because the f12 mask lost the feet.
- Adopted: 2.73 px/frame → 65.5 px/s → **1.60 m/s**.

## Second route / spread
The raw phase-correlation step at f12 (2.84) gives 1.67 m/s. The centroid cubic fit (2.67) gives 1.57 m/s.
Using 91 px as the height gives 1.58 m/s. Confidence: good, about ±4 %.

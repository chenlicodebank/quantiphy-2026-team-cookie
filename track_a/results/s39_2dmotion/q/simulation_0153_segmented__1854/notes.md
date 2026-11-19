# q1854: speed of the blue car at t = 1 s (m/s)

Prior: tyre diameter = 0.369 m. 2D scene, question_fps = 24 = file fps. t = 1 s -> frame 24; speed = backward
difference between frames 23 and 24, times 24.

## Scale (tire.py, circfit.py, SAM 3)
- Near-side front tyre, dark-pixel extents through the hub: vertical 110–111 px (frames 23–41), horizontal 112–113 px
  (frames 30–41; at frames 23–24 the far-side wheel peeks out, so the horizontal extent reads 125–129 there).
- Circle fits to the lower silhouette: 106–110 px on clean frames (28–41).
- SAM 3 "tire": frame 24 front 113 h x 108 v; frame 35 front 107 h x 109 v, rear 109 x 109.
  SAM is about 2–3 % tighter than the edge extents. On the 5x zoom of frame 35 (frames/front35.png), the tyre
  spans x≈1104–1215 and y≈837–947, about 110–111 px. SAM trims the anti-aliased edge.
- Adopted D = 110.5 px, so the scale is 0.369 / 110.5 = 3.339 mm/px.

## Motion (scene tracks + shift.py)
- Shift from frame 23 to 24 in scene/tracks/cart.csv: front hub 47.72, rear hub 47.71, marker 48.05 px.
- My own template match (shift.py), 23->24: sill and marker 47.95, front wheel 47.06, rear wheel 49.71 (the
  rotating wheel makes this one noisy).
- The seat and body patch moves only 44.8 px because it is deeper than the near side (perspective). The tyre scale
  belongs to the near side, so near-side points (hubs, sill) are the consistent motion measure.
- Neighbouring frames: 22->23 is about 46.7 px and 24->25 about 48.4 px. The car is still accelerating smoothly.
- Adopted shift: 47.8 px/frame.

## Answer
v = 47.8 x 24 x 0.003339 = 3.83 m/s.

Second route: with the SAM diameter (108.5 px) v = 3.90; with the horizontal extent (112.5) v = 3.76. The spread is
about ±2 %. Confidence: good (likely within about 3 %).

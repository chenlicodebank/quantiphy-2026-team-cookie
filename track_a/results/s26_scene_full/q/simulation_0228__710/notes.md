# Q710 — length of the black cat (with tail)

- 2D top-down render, static camera, 24 fps (file fps = question_fps, no re-timing). The "dog" in scene/ is this black cat (the only animal).
- Scale from the prior (speed 1.041 m/s): the cat walks at constant speed. A linear fit of position vs frame over all 50 frames (measure.py, V<45 mask):
  centroid 5.457 px/frame, nose end 5.462, tail end 5.518, mean per-frame step 5.479 (gait jitter makes this slightly high). I used 5.46 px/frame = 131.0 px/s
  → 0.007944 m/px.
- Length: the x-extent of the mask from tail tip to nose (the cat is axis-aligned, axis ≈ −0.3°). V<45 threshold: median 107, mean 107.2 (range 104–111).
  A half-level edge criterion (ends.py) gives median 108; the ends are sharp, so the threshold changes the result by ≤1 px. I used 107.7 px.
- Length = 107.7 × 0.007944 = 0.856 m. Over the range of gait poses (105–111 px) this gives 0.83–0.88 m.
- Second check: the speed from the nose and tail ends agrees with the centroid speed to within 1%, and scene/ independently gives a ~108 px length and 5.4 px/frame.
- Confidence: good (±3%). The main uncertainty is which pose the reference bounding box used.

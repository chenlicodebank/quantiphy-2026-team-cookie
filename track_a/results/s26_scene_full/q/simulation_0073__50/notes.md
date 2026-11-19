# Q50: distance between the white car (van) and the bicycle at 1.0 s

- This is a 2D top-down scene at 24 fps (question_fps is also 24), so t = 1.0 s is frame 24. The camera is static.
- Scale: the cyclist moves at constant velocity. A linear fit of the track centroid over frames 2–71 gives 8.916 px/frame
  (rms residual 0.45 px), which is 213.98 px/s. The prior of 5.33 m/s gives **0.024909 m/px**.
- Positions at frame 24:
  - Track centroids: van (832.7, 836.9) and cyclist (917.9, 623.1). The gap is (−85.3, 213.8) px = 230.2 px.
  - Second route: I made my own difference mask against frame 71's background (`measure.py`).
    - Van: bbox y 713–958, so its centre y is 835.5. Its mask centroid is 841, pulled down by the window colour.
    - Cyclist: bbox y 591–653, centre about 622.5. x is 917.5.
    - Local smoothed fits give 837.3 and 623.3.
  - All routes give a gap of 229.8–231 px.
- Distance = 230 px × 0.02491 m/px = **5.73 m**. The other routes give 5.72–5.75 m.
- Confidence: high, about ±2%. The main uncertainty is where the cyclist's origin sits (pelvis versus bike centre),
  which is a few px.

# q_3243 – height of the acorn (cm)

Prior: acceleration of the acorn from 2.00 s to 2.30 s is 0.77 m/s². The file and the question both give 30 fps, so 2.00–2.30 s is frames 60–69. This is an internet video, so I used one planar scale taken from the prior.

## Pixel acceleration (measure.py, using tracks/acorn.csv frames 59–72, acorn fully in frame)
- Stem-knob x is the sharpest point on the acorn. Background-stabilised (ref) and raw values:
  - Forward-difference velocities, (v(69) − v(60)) / 0.3 s: ref 3660 px/s², raw 3840 px/s².
  - Mean of the second differences over frames 60–69: ref 3771 px/s², raw 3942 px/s².
  - Quadratic fit: 3267 over frames 60–69 and 3938 over frames 59–72. The acceleration grows over time.
- The bbox centre gives higher values (4140–4850 px/s²). Motion blur makes it less reliable, so I did not use it.
- Adopted value: 3800 px/s². Scale = 0.77 / 3800 = 2.03e-4 m/px.

## Height in pixels
- Stem top to cup bottom is 418–427 px across frames 59–72 (median about 420). Height stays constant, so depth is constant.
- I checked this by eye on a zoomed crop of frame 66: stem top at y ≈ 545 and cup bottom at y ≈ 963, so about 419 px.

## Answer
420 px × 2.03e-4 m/px = 0.0851 m, so **8.5 cm**.
- Sensitivity to the choice of pixel acceleration: 8.9 cm at 3660 px/s², 8.1 cm at 4000 px/s².
- The result is plausible for a toy acorn sitting on a cup.
- Confidence: moderate. The pixel acceleration has about ±8 % spread depending on which estimator is used.

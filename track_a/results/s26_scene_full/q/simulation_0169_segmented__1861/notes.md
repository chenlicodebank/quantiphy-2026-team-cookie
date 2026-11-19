# q_1861 – acceleration of the astronaut at t = 1 s

- 2D segmentation video, 24 fps (file fps = question_fps, no re-timing); t = 1 s -> frame 24.
- Track: scene/tracks/person.csv (mask centroid as the pelvis proxy; the pose is rigid, a single figure, no occlusion). The astronaut rises smoothly: it speeds up from f3 to about f33, cruises at about 5.25 px/frame, then slows down to a stop at f78. At f24 it is still speeding up, at about 4.48 px/frame.
- Acceleration = d|v|/dt at f24, from polynomial fits of x(t) and y(t) (fit.py):
  - local fits over ±6 to ±12 frames, degree 2-4, using the centroid or the bbox centre: 0.10-0.13 px/frame²
  - second route, a global degree 5-8 fit over f2-f78: 0.1045-0.1056 px/frame²
  - adopted value: 0.108 px/frame², i.e. 0.108 x 576 = 62.2 px/s²
- Scale: the astronaut's height of 2.2 m corresponds to about 91 px (main-axis length 91.4 px on average, bbox height 90 px at the upright f0), so 0.0242 m/px.
- Answer: 62.2 x 0.0242 ≈ 1.50 m/s².
- Confidence: moderate. The fit spread is about ±7 % and the height in pixels is uncertain by about ±1 %.

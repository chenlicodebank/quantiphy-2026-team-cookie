# Q1516: rocket speed at t=1 s (frame 24, question_fps 24 = file fps)

Method (model3d.py, sens.py), using pinhole geometry with the principal point at the image centre:
- Image track: scene/tracks/missile.csv s_origin (nose/tail midpoint along the straight image flight line). I checked the
  crops at f14 and f24.
- Origin at f0 (inside the tube): nose flush with the tube mouth (s=-449), centre 72.8 px behind it. Origin at f12 = nose - 72.8 px.
- Back-projecting them with the given depths (43.064 m at t=0, 41.127 m at t=0.5) gives two 3D points. These set the 3D flight
  direction for a given focal length f. f was solved so that a 2.9 m rocket along that direction projects to 145.6 px at f13-14:
  f = 2553 px (hfov 41 deg).
- Check: the same model predicts how the apparent length grows: 144.5/162.8/177.2/206.3 px at f13/20/24/30. Measured:
  145.1/160.5/181.4/213.3 (the measured values include a little motion blur). So the 3D model is consistent.
- Position at each frame = the point on the 3D line closest to the pixel ray. A quadratic fit to s over f13-30 gives an image
  speed of 47.1 px/frame at f24, so the speed = |X24 - X23| x 24 = 18.7 m/s (cubic fit 18.66).
- Second route: raw differences f22-24 18.4, f24-26 19.3, f22-26 18.9 m/s; the nose track gives 19.5 and the tail track 17.9.
- Sensitivity: shifting the f0 origin by ±10 px or using a reference length of 140 px gives 18.3-19.9 m/s.

Answer: 18.7 m/s. Confidence: moderate-good (about ±5%).

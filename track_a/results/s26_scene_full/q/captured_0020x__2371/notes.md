# q_2371: velocity of the white jar at t = 0.60 s (cm/s)

- The file and the question both run at 24 fps, so t = 0.60 s is frame 14 (0.6 x 24 = 14.4, rounded). The jar is the
  object the record calls `white_ball` (it is actually a tumbling white cylinder or jar). The near person throws it
  and the far person catches it. Frame 14 is its last hand contact; it flies freely from f15 to f25.
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360). The depth_info gives the jar's distance only at
  f14 (1.9735 m), so I had to model how its depth changes.
- Model (joint.py, final.py): 3D ballistic trajectories with g = 9.8 m/s² (the prior). The jar (f15-25) and the
  carrot/yellow fruit (f14-23, without f18) share one gravity direction, set by camera pitch and roll. The fits use
  depth constraints of 1.9735 m (jar, f14) and 2.63 m (carrot, f14) and the record's centroids (I checked them on
  crops).
- Pitch is the main uncertainty. The ballistic fit alone pins it down poorly: the jar alone gives -11 deg
  (unphysical), the carrot alone 61 deg, both together 58 deg. But the residuals change by only ~1 px, and the
  centroid of a tumbling object carries systematic error of that size. Two independent scene cues give a lower
  pitch:
  - The vanishing point of the two people's body axes gives pitch 35.6 deg and roll 9 deg. The roll agrees with the
    ballistic roll of ~10-13 deg.
  - Putting both pelvises (3.237 m and 1.58 m) at equal height gives pitch 33-41 deg.
  - At pitch 38-40 deg, the camera height is about 2.0 m and the near person's shoe lands about 0.36 m from her
    pelvis, both plausible.
- I adopted pitch 38-40 deg. Jar speeds from the forward difference f14->f15: 3.40 m/s at 38 deg, 3.33 m/s at
  40 deg. The 5-frame mean over f12-16 is 3.36-3.43 m/s. Answer: 337 cm/s.
- Second route: the in-plane part alone is 50.4 px x 1.9735 / 763 x 24 = 3.13 m/s. The model adds a radial
  (depth-rate) part of about 1.2 m/s, which gives 3.3-3.4 m/s.
- Sensitivity: pitch 34 deg gives 354 cm/s, 45 deg gives about 314, and 58 deg (ballistic only) gives 266.
- Confidence: moderate, about ±10%, dominated by the camera pitch.

# Q81 – speed of the bike at 0.5 s

- 2D top-down simulation, 24 fps (file and question rate are the same). t = 0.5 s → frame 12; speed = |x12 − x11| × 24.
- Scale from the prior (bike length = 1.7 m): the bike's pixel length along x, front tyre tip to rear tip, is 377–378 px
  (full non-floor mask 218–595 at frame 12, stable over frames 0–16; the cyan-only mask gives 374–378 px). I used 378 px, so 1.7/378 = 0.004497 m/px.
- Motion (measure.py): bbox-centre step from frame 11 to 12 is 48 px with the cyan mask and 47.5 px in the scene record's full-mask root.
  Over frames 2–16 the motion is uniform: (880.5 − 216.5)/14 = 47.43 px/frame, and single steps alternate between 47 and 48 because of integer bbox edges.
  I used 47.5 px/frame = 1140 px/s.
- Speed = 1140 × 0.004497 = 5.13 m/s.
- Second route: the mean-centroid steps of the cyan mask average about 46.6 px/frame (they are noisier), which gives 5.03 m/s.
  The uniform-motion fit gives 47.43 px/frame, which gives 5.12 m/s. The routes agree to within about 2 %.
- Confidence: high (about ±2 %).

# q2312: height of left person (cm)
- The left person is the farther one (smaller in the image), so Z = distance_far_person_camera = 3.130 m. File fps = question fps = 24.
- measure.py: per-row background model (median of empty columns), threshold |diff|>40 inside x 330-475, every 4th frame.
  Head top y=174, shoe bottom y=577, so 404 px, the same on every frame f0-f36 (later frames pick up the dropped carton at the bottom of the ROI).
  The scene record had 405 px, which agrees.
- Method card: H = Z*px/f = 3.130*404/763 = 165.7 cm.
- Second route: the record's 405 px gives 166.1 cm. Alternative reading: if the 3.13 m is the ray distance and is converted to z-depth
  (the centre is 257 px off-axis, factor 1.055), H = 157 cm. Not used, because the method card uses the distance directly.
- Sanity check: 166 cm is a plausible height for an adult woman. Confidence: good.

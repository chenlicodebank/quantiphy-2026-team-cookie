# Q429 – displacement of the small elephant (m)

Prior: speed of the big elephant = 2.313 m/s. 2D side-view scene, static camera, fps 24 (same as question_fps), 60 frames.
Both elephants walk on the same ground line (feet y≈693–696 px), so they are at the same depth and one m/px scale applies.

Method (measure.py, uses scene/tracks which I checked on a contact sheet: the tracks follow the right animals over all frames):
- Big elephant pixel speed: linear fit of centroid_x = 6.88 px/frame = 165.2 px/s, which gives a scale of 0.01400 m/px.
  The mean per-frame 2D step, 6.99 px/frame, gives 0.01378 m/px.
- Small elephant displacement from frame 0 to 59: centroid 360.4 px (fit 361.4 px), which comes to 5.05 m.
- Other reference points (body centroid, body rear edge, body front edge): 4.95–5.06 m.
- Per-frame-speed convention for the big elephant with the small elephant's net 2D displacement: 4.97 m.

Answer: 5.02 m, the middle of the 4.95–5.06 range. Confidence: good (about ±2 %). The spread comes from gait jitter
and from how the speed is defined (fit or mean step).

# q561 - black cat length incl. tail
2D side-view walk, static camera, 24 fps (file fps = question_fps, so no re-timing). The cat walks at a steady pace.
- Pixel speed: the nose (front_x) line fit gives 427.1 px/s; the mask-centroid fit gives 428.4 px/s; the mean per-frame |dx| of the centroid is 430.7 px/s.
  The scene record's net centroid displacement gives 877/49 frames = 429.7 px/s. Used 428 px/s.
- Scale = 0.94 / 428 = 0.002196 m/px.
- Length incl. tail = horizontal bbox extent from tail to nose. The scene record (mask includes the grey nose) gives a median of 307.5 px.
  My own threshold mask (measure.py) gives a median of 301.5 px but misses part of the grey head/nose (seen on frames/ov_24.png). Used 307 px.
- Length = 307 x 0.002196 = 0.674 m.
- Second route: my mask length of 301.5 px gives 0.662 m (about 2 pct lower). It is consistent with the main value.
- Confidence: moderate-high. The main uncertainty is whether the reference AABB matches the walking-pose horizontal extent
  (the tail is raised, so the length is shorter than a stretched-out tail would give).

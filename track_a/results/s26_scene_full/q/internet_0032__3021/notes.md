# q3021 – acceleration of the boat over 0-7 s

- Prior: boat length 3.5 m. Internet video, single-scale planar convention. Camera static (shift < 0.2 px, scene record).
- Time base: question_fps 30 vs file 29.85 – a 0.5% difference with negligible effect; I used 30 (0-7 s = frames 0-210).
- Track: scene/tracks/boat.csv hull tips and centre (cx_hull). Spot-checked at frames 0 and 219 on zoomed frames: bow ≈ 760 / 420,
  stern ≈ 972 / 665, consistent with the record.
- Pixel length of the boat: 212 px (f0), 232 px (mid-clip, median), 247 px (end). Scale 3.5/232 = 0.01509 m/px (mid-clip).
- accel.py: quadratic fit x(t) of cx_hull over frames 0-210 gives a = 1.29 px/s^2, i.e. 0.0195 m/s^2 (L=232) or 0.0213 (L=212).
  Endpoint velocities (1.5 s linear fits at each end) give 0.023-0.0255 m/s^2.
- Second route (speedprof.py): 1 s window speeds rise steadily from 0.608 to 0.742 m/s (L=232) between frames 0-30 and
  180-210, so a ≈ 0.134/6 = 0.022 m/s^2. Bow and stern points bracket this (0.016-0.025) because of the perspective growth.
- Caveat: part of the apparent pixel acceleration comes from the boat approaching the camera (its length grows 16%).
  With a per-frame scale the true acceleration is about 0.010 m/s^2, but the annotators used one scale, so I follow that.
- Answer: 0.021 m/s^2 (the boat is speeding up, direction is right→left). Confidence: moderate (±15%).

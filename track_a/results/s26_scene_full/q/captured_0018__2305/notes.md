# q_2305 — velocity of the pineapple toy at 3.4 s (cm/s)

- Object: the yellow plush with green leaves, dropped by the near (right) person; the scene record calls it
  `lemon_plush`. Track checked against the contact sheet: it is the right object. Released at about frame 27, lands at about frame 36.
- **Time problem:** the clip is only 49 frames long (2.04 s at 24 fps; the file rate and question_fps are both 24).
  t = 3.4 s gives frame 82, which is not in the file. The question time must refer to a longer original recording.
- Real-time check: a quadratic fit to the plush's fall (frames 28–35, depth 2.002 m = near person, f = 763 px) gives
  g = 8.9–9.6 m/s² in clip time. So the clip plays at real speed, and the original can differ from it only by a
  time offset, not by a speed-up.
- Guess at the mapping: a gravity prior plus a velocity question points to a time during the free fall. If the clip
  is the second 49-frame block of a longer recording (an offset of 48–49 frames), 3.4 s maps to clip frame 33–34,
  which is mid-to-late in the fall.
- Speeds (3D back-projection, Z = 2.002 m): the frame-to-frame speeds at frames 31–35 are 2.5, 2.8, 3.4 and 3.4 m/s.
  The fall fit gives v(33) ≈ 3.05 m/s and v(34) ≈ 3.4 m/s. Smoothed over 5 frames, leaving out the dropped-frame
  jump between frames 35 and 36: about 3.0 m/s.
- Answer: **310 cm/s**. Confidence is LOW: the speed itself is measured well, but which frame 3.4 s refers to is a
  guess. Over the whole fall the speed runs from 0 to about 4.5 m/s.
- Script: fit.py

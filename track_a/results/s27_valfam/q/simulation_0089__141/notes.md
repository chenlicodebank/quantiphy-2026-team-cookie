# q_141 – distance big bird ↔ small bird at t = 0.3 s

- question_fps = file fps = 24 → frame round(0.3·24) = 7.
- 2D scene, static camera, single m/px scale from prior (small bird length 0.94 m).
- Small bird (B) nose-to-tail x extent re-measured in m.py (background-difference mask, thr 18):
  110, 109, 108, 108, 109 px at frames 0, 3, 5, 7, 8 (scene record: 107 with stricter mask, ~109 antialiased). Used 108 px
  → scale 0.94/108 = 0.008704 m/px.
- Frame 7: big bird A has left the frame (gone from frame 7), so its position is extrapolated at its constant
  velocity (−150.27 px/frame, RMS fit residual 0.05 px): x = 701.52 − 6·150.27 = −200.1, y 557.2.
  Small bird B ref at frame 7: (1729.4, 555.2). Distance = 1929.5 px.
- Check: the record's pair distance grows by 242.1 px/frame; frame 6 = 1687.3 → frame 7 = 1929.4 px (agrees).
- Answer: 1929.5 · 0.008704 = 16.79 m (range 16.6–16.95 for a length of 107–109 px).
- Caveat: frames 0–1 are identical (the motion starts at frame 2). If the reference indexed frames differently it
  would change the answer by about one frame of separation (~12 %). Confidence: moderate-high.

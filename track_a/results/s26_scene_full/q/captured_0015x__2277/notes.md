# q_2277 — velocity of the toy (teddy bear) at 0.6 s, cm/s

- t = 0.6 s → frame round(0.6×24) = 14 (question_fps = file fps = 24). At frame 14 the bear is still held, being
  lifted fast in toss 1 (release at frame 17).
- Scale from the prior (g = 9.8 m/s²): I fitted quadratics to the free-flight frames 17-22 and 53-58 (cy, top, bottom
  and centroid y from scene/tracks). Accelerations were 4.7-5.4 px/frame², median 5.07 → 2919 px/s² → 3.36 mm/px.
  Sanity check: bear 95 px → 32 cm, person 508 px → 1.71 m, both plausible.
- Bear position during the lift: I re-read it from 3× crops with a 10 px grid (frames/lift2.png, crops2.py). Top edge
  over frames 12-16 was 246, 216, 192, 169, 152, which matches the record. Box centres were 291, 259.5, 233, ~216, 199.
  The bear tilts in frames 12-14, so its bottom edge is uncertain. Horizontal drift is about -1.8 px/frame.
- Velocity (lab convention, smoothed over 5 frames, 12-16, linear slope):
  - top edge: 23.5 px/frame → 566 px/s → 190 cm/s
  - centre: 22.75 px/frame → 548 px/s → 184 cm/s
  - Single-frame differences of the top edge at frame 14: 193 cm/s backward, 185 cm/s forward.
- Answer: **187 cm/s**. Confidence is moderate, about ±7%. The main uncertainties are the scale from g (about ±4%) and
  the bear's centre while it is held and tilting.
- Scripts: measure.py, crops.py, crops2.py.

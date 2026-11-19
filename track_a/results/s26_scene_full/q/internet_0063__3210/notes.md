# q_3210: velocity of the water bottle at 1.70 s (prior: g = 9.8 m/s^2)

- Time base: question_fps 30 vs file fps 30.016, so t = 1.70 s falls on frame 51 at either rate. Release is at about frame 39.2, and the base hits the skirting board between frames 52 and 53. Frame 51 is late in free fall, and the forward difference (51 to 52) comes before the impact.
- The camera is rotated 90°, so gravity points along image +x. Camera drift is about 0.2 px/frame, which can be ignored.
- Track: scene/tracks/bottle.csv, cap centroid and bottle centre. I checked the frames 46–54 positions visually in frames/fall.png (view.py).
- Scale (fit.py): a quadratic fit of x over frames 41–52 gives a pixel acceleration of 11.97 px/frame² for the centre and 12.10 px/frame² for the cap. Scale = 9.8 / (a·30²) ≈ 0.00091 m/px. The per-frame second differences are 12.3 ± 1.5 px/frame², which agrees.
- Velocity, following the annotator convention (forward difference x52 − x51): 142.8 px/frame (centre) or 144.9 px/frame (cap) gives 3.90–3.92 m/s.
- Second route: the fitted velocity at frame 51 to 51.5 is 3.86–4.03 m/s. The physics check v = g·(t − t_release) = 9.8 × (51.5 − 39.2)/30 = 4.0 m/s. The result is insensitive to the scale, because it depends only on the time since release.
- Answer: 3.92 m/s. Confidence: good (about ±4%).

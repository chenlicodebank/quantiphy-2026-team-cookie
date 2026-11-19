# q_547 — length of the typewriter (m)

Prior: typewriter acceleration before 0.45 s = 9.8 m/s^2 (free fall, frames 0-10 at question_fps 24 = file fps).
No depth_info. Scale = 9.8 m/s^2 / pixel acceleration of the falling typewriter.

## Measurements (scripts in this folder)
- fit.py: quadratic fits to the scene record's bbox tracks, frames 0-9: bbox centre 6970-7330 px/s^2,
  bbox top 6820, bbox bottom 7110-7870. These are silhouette edges whose 3D points change as the view
  passes from below to above the object, so they are not reliable.
- track2.py / track3.py: frame-to-frame template matching of texture bands (sub-pixel). The second differences
  are very constant (rms < 0.3 px):
  - keyboard (front face): 7290-7360 px/s^2
  - carriage top / platen knobs (back): 6810-6980 px/s^2
  - base slab: 7380 (frames 0-7), noisy
  The roughly 5 % front/back difference is perspective (the front is closer to the camera), which puts the camera about 3.5-4 m away.
- rows.py: per-row mask widths. The widest row is the bottom base slab (y≈290 in frame 0): 291-292 px,
  matching the record's constant fall-phase bbox width of 291 px (no rotation during the fall). The front
  edge of the base slab is the widest, so it sits at about the depth of the keyboard front.

## Answer
L = 291 px × 9.8 / 7340 px/s^2 = 0.389 m (scale taken at the depth of the front face/base).
Second route: if the widest part were at the origin/centre depth (a ≈ 7130) the result is 0.400 m; at the carriage depth
(a ≈ 6940) it is 0.411 m. A real typewriter about 0.39 m wide is plausible. The answer is 0.39 m.
Confidence: about ±4 %.

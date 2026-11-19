# q_684 – acceleration of the red general at t = 0.5 s

- 2D scene, camera static, 24 fps (file rate equals question_fps). t = 0.5 s is frame 12.
- Re-measured the track myself (`measure.py`: difference to frame 44, where the piece is gone, in columns 880–1040,
  then the mask's row centroid). The results match scene/tracks to within about 1 px of constant offset (my mask
  picks up a slightly wider rim).
- Duplicated frames (9,10), (11,12), (18,19), (20,21), (28,29), (34,35): the first frame of each pair shows the next
  frame's position (8→10 = 18.9 px ≈ 9.0 + 10.2 expected steps). I left those first frames out, so frame 12 is a
  true position.
- `fit.py`: local quadratic fits of y(t) on clean frames around frame 12 give these accelerations:
  5–17: 632 px/s²; 6–16: 626; 8–17: 627; 4–20: 637; 10–15: 609.
  A global cubic fit gives 640 at t = 0.5 s. Second differences at frames 13–15 are 608, 639 and 588.
  → a ≈ 630 px/s² (±2 %).
- Scale: the general's disc diameter is 86.5 px (mask bbox 86–87 px in frames 0–39), so the scale is
  0.097 / 86.5 = 1.121e-3 m/px.
- a = 630 × 1.121e-3 ≈ 0.707 m/s².
- Second check: the speed at t = 0.5 s is 307 px/s = 0.344 m/s, and 0.344 / (0.5 − 0.055 s start) ≈ 0.77 m/s².
  That is in line with a mean acceleration that is a little higher early on. The acceleration falls slightly over
  the clip (about 560–600 px/s² late), so I used the local value.
- Confidence: about ±4 %, mostly from the scale (static pieces measure 84 px, which would give 0.73).

# q1000 – length of the plane (m)

2D video (V2SS). Prior: plane speed 22.16 m/s. question_fps = 25 (file is 24 fps; times/frames use 25 per the convention).

## Method
- Checked the scene record (scene/tracks/jet.csv) with m.py. The bbox is clean and the jet is fully visible in frames 13-55.
- Pixel speed: a linear fit of ref_x (bbox centre) over frames 13-55 gives 42.07 px/frame. The nose (x0) fit gives 42.62 and the tail (x1) fit 41.51.
  The per-frame steps are 40-43 px.
  So the speed is 42.07 x 25 = 1051.7 px/s, and the scale is 22.16 / 1051.7 = 0.02107 m/px.
- Length in pixels: the horizontal bbox width from nose to tail. It changes with perspective: 678 px at minimum (frame 26),
  696 px at mid-clip (frame 34) and 745 px at maximum (frame 55). The mean over frames 13-55 is 707 px.
- Length = 707 x 0.02107 = 14.9 m.

## Checks
- Using the nose or tail speed instead (41.5-42.6 px/frame) gives 14.7-15.1 m.
- Using the minimum or mid-clip width gives 14.3 m or 14.7 m.
- If 24 fps were used instead, the length would be 15.5 m.
- A 15 m small jet is plausible.

Confidence: moderate, about ±4%. The main uncertainty is which frame's width the reference used.

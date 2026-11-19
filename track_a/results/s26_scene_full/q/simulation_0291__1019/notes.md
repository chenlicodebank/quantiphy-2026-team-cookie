# q1019 – displacement of the fish 0.5 s -> 1.0 s

- 2D render, static camera, 24 fps (file and question agree). t=0.5 s -> frame 12, t=1.0 s -> frame 24.
- Fish swims straight along -x (y drift < 2 px), so displacement = |dx|.
- Pixel displacement, frames 12->24:
  - scene record ref_x (head-template track): 2109.99 - 1832.67 = 277.3 px
  - my own head template match (check.py, widths 150/250 px, both directions): 274.3-277.5 px -> ~277 px
  - mask centroid: 269.0 px (body bending shifts centroid relative to head)
- Scale from prior speed 0.67 m/s, taken as the fish's mean speed over the motion (frames 2-70):
  head track 22.44-22.45 px/frame (check.py: 224.6 + 1301.0 px over 68 frames) -> 0.67/(22.45*24) = 1.243e-3 m/px.
  Per-frame speed varies 22.0-23.5 px/frame (hump around frames 15-30), so the prior is treated as nominal/average.
- Displacement = 277.3 px * 1.243e-3 = 0.345 m (= 12.34 mean-speed frames).
- Second route: centroid track (269.0 px / 22.21 px/frame mean) -> 0.338 m. Naive 0.67*0.5 = 0.335 m;
  if prior matched the local speed (~23.1 px/frame) -> 0.335 m; if matched the slowest speed (22.0) -> 0.351 m.
- Answer 0.344 m; confidence: within ~3-4% unless the prior refers to a specific different frame.

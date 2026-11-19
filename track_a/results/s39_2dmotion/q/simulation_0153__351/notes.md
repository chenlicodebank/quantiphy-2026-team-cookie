# Q351 — speed of the blue car at t = 1.5 s (m/s)

Prior: tire diameter of the blue car = 0.369 m. 2D video, question_fps = file fps = 24, so t = 1.5 s is frame 36;
speed = |p(36) - p(35)| x 24.

## Scale (tire diameter in px)
- `tire_rows.py`: front tire, half-level edge crossings (tire dark vs. surroundings) on a row band through the hub
  and a column band through the centre, frames 24-41. Frames 32-41: width 111.6-113.3, height 111.4-112.7
  (frame 38 bottom spoiled by the floor). Frame 36: 112.6 x 111.6. Adopted D = 112.3 px (+-0.7).
- `circfit.py` (radial edge search + circle fit, frame 36): horizontal 112.7, vertical 113.6, R fit 57.3 (biased by
  arch shadow upper-left); consistent.
- The rear tire is partly covered (fender on top, sill/lights on the right): 108 px wide, not used.
- The scene record's 105 px wheel diameter was a visual estimate and is too small by about 7%. Corrected.
- SAM 3 "tire" frame 36, front tire: box 109.6 x 107.7, mask extents 114 x 109. `maskcheck.py` draws my circle
  (D 112.6) and the SAM outline on a 5x crop (frames/maskcheck36.png). The circle follows the tire edge. The SAM
  mask cuts about 3 px off the top and is ragged on the right. The difference is under 3% on width (114 vs 112.6),
  but the SAM box height is 3.5% less (107.7 vs 111.6). The zoom shows my edge is the right one.
- Scale = 0.369 / 112.3 = 0.003286 m/px.

## Pixel displacement, frame 35 -> 36
- `shift.py` (NCC sub-pixel template shifts of rigid patches): canopy 47.19, rear box 46.69, rear lamps 47.39,
  lower lights panel 48.05. The seat and front-body patches are spoiled by background showing through them.
- Front tire centre (edge midpoints): 1160.05 -> 1207.9 = 47.85.
- Scene record: bbox centre 942 -> 989 = 47 (rear edge 46, front 48); panel template 48.06.
- SAM 3 "blue car" box centre, frames 35/36: 944.05 -> 991.4 = 47.35. SAM front tire box centre: 1161.5 -> 1209.4 = 47.9.
- Lower features move about 0.8 px/frame faster than upper and rear ones; the car length grows about 0.5% over
  frames 33-41 (slight yaw?). The tire height stays constant, so depth is constant. Adopted 47.5 +- 0.5 px/frame
  (the mean of the routes).

## Answer
v = 47.5 px/frame x 24 x 0.003286 m/px = 3.75 m/s. Range across routes: 3.69 (46.7 px) to 3.79 (48.06 px).
Second route: front tire centre alone gives 47.85 -> 3.78 m/s; canopy gives 3.73 m/s.
Confidence: good, about +-2%.

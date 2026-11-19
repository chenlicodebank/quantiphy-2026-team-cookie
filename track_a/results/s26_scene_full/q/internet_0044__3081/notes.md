# Q3081 – distance between the white cylinder and the plastic (yellow-cap juice) bottle, cm

Prior: g = 9.8 m/s^2. Internet video, 30 fps (file and question agree; ball arcs are physically consistent at 30 fps).

## Scale from gravity (single planar scale, annotator convention)
- `fit_g.py`: quadratic fits of the ball's image y (scene track, stabilised `_f0`, arc-fill rows excluded) per arc
  between bounces. Long clean arcs (frames 41-99): 20.23, 19.80, 18.84, 19.44, 19.12, 19.09 px/frame^2 -> mean 19.42.
  Short arcs near the bowl are noisier (17.6-25).
- Second route, `reseg.py`: my own segmentation of the ball (white & differs from background frame 180) on raw frames
  42-99: 21.9, 19.7, 17.8, 18.7, 19.7, 18.7 -> mean 19.4, median 19.2.
- Adopted a = 19.4 px/frame^2 = 17460 px/s^2 -> scale = 9.8/17460 = 5.61e-4 m/px = 0.0561 cm/px.
- Sanity: ball diameter ~76 px -> 4.3 cm (real 4.0 cm; ball is a bit nearer the camera than the objects).

## Pixel distance (frame 0, `edges.py` + zoomed crop)
- White cylinder: gradient edges x = 970..1092 (rows 660-760) -> centre x = 1031 (record said 979-1095; corrected).
- Plastic bottle: x ~ 562..684 -> centre x ~ 623 (edge profiles noisy because of the transparent label; centre 615-633).
- Both stand on the desk, bases at y ~ 799 / 810. Horizontal centre separation = 408-409 px.
  Centre-to-centre including the different heights of their bbox centres (618 vs 701): 417 px.

## Answer
409 px x 0.0561 cm/px = 22.9-23.0 cm (centre-to-centre with height offset: 23.4 cm; edge gap 286 px = 16 cm, not used).
Answer: 23.0 cm. Confidence moderate (scale +-3%, centre pick +-2%, reading of "distance" adds a few %).

# q_503 — bubble speed at t = 0.8 s

2D scene, 30 fps (file and question agree), static camera. t = 0.8 s -> frame 24.

## Scale (prior: horizontal width of "skynova" text = 0.00188 m)
The brand word on the bottle is printed vertically (only "NOVA" is visible; the rest is cut off at the bottom of the frame),
so its horizontal width in the image is the letter height. `measure_text.py` thresholds the white letters in frame 24
(x 1050-1250, y 2030-2560): column extent 1106-1185 (80 px at threshold 160/175, 78 px at 190). Half-max edges of the
horizontal profile across the V's and the O both give ~78.5 px.
Scale = 0.00188 / 78.5 = 2.395e-5 m/px.

## Bubble motion
Used scene/tracks/bubble.csv (hull-centroid mask, overlays checked by the record; motion is smooth along the pipette).
Backward difference at frame 24: p24 - p23 = (-10.7, +6.8) px -> 12.68 px/frame.
Second route: chord over frames 20-28 = (87.1, 51.7) px / 8 = 12.66 px/frame; neighbours: 12.7 (f23) and 12.8 (f25).
The bubble is in its steady phase here, so the value holds up.
Speed = 12.68 x 30 = 380 px/s x 2.395e-5 = 0.00911 m/s.

## Confidence
Moderate to high. The text width is good to about ±2 px (about ±3%) and the per-frame speed to about ±2%. The main
risk is how "horizontal width" of the vertical text is read. If it meant the length of the whole word, that word is
not fully visible, and the pipette would come out about 0.5 mm wide, which is implausible.

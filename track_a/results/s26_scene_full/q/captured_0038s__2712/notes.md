# q2712 — height of the pink bottle (cm)

Lab video, 24 fps (file fps = question fps), 1280x720, f = 0.5959*1280 = 763 px.
depth_info at t=1.4 s (frame 34): pink bottle 0.9998 m, credit card 0.6867 m.

## Measurement (measure.py, profile.py; frame 34, also checked at frames 20 and 45: bottle is static)
- Vertical colour profiles at columns x=642..682: top silhouette (green -> white lid rim) at y ~329.5;
  bottom edge (pink -> dark contact line on the table) at y ~476.5. Pixel height = 147 px
  (scene record bbox 332-477 = 146 px, consistent).
- Bottom edge is almost flat across the width (y 476-477) -> camera elevation is small, so the
  ellipse overshoot of top/bottom outlines is small. Off-axis ray factor 1.002 (negligible).
- H = 0.9998 * 147 / 763 = 0.1926 m.

## Check with the prior (card.py)
- Dark credit card (lying flat, long side nearly horizontal in the image): long edge spans x 518/524 -> 618.5,
  ~97 px. 0.6867 * 97 / 763 = 8.73 cm vs prior 8.56 cm (+2%). Scale is consistent; a slight
  over-estimate of this kind suggests rounding down a little.

## Answer
19.2 cm (range 19.0-19.3). Confidence: good (~3%).

# q_719: ceiling height of the room (prior: chalkboard length = 5 m)

The view is a static, frontal shot of the classroom's front wall. Both the chalkboard and the wall's ceiling and floor
junctions lie in that wall plane, at about the same depth, so one metres-per-pixel scale is enough (2D).
fps is 24 for both the file and the question. Time does not matter for this question.

## Measurements (measure.py: mean of background frames 0, 2, 4, 46, 48; row and column gradient peaks)
- Wall/ceiling junction: y = 172.5 px, the same at every column from 900 to 1600.
- Wall/floor junction: y = 951.5 px at x = 960–1120 and x = 1800–1830 (one column gave 953.5).
- So the wall height is 779 px.
- Chalkboard with its wooden frame: x = 320.5 to 1691 px, so **1370 px** wide (the record says 1372).
- Green writing surface alone: 342 to 1671 px, so 1329 px wide.
- I checked the edges visually on CLAHE-enhanced crops (enh.py, crop.py).

## Result
- If the 5 m includes the frame (the object's bounding box): 779 × 5 / 1370 = 2.84 m.
- If the 5 m is the green surface only: 779 × 5 / 1329 = 2.93 m.
- Answer: **2.85 m**, weighted toward the frame-inclusive reading, since an object's size is its bounding box.

## Check
- The ceiling line agrees across 8 column windows and the floor line across 2 separate regions, to within 1 px.
- The board would then be about 5 × 1.62 m with its frame. That is a plausible proportion.
- A 2.8–2.9 m classroom ceiling is realistic.

Confidence: good, about ±3 %. The main uncertainty is whether "chalkboard length" includes the frame.

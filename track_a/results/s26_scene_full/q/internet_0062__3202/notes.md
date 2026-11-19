# q_3202 – shorter side of the wallet (cm)

Prior: g = 9.8 m/s^2. 2D clip (rotated 90°, gravity = image +x), static camera, 30 fps (file and question rate agree;
the fall is clean free fall, giving a plausible wallet size at 30 fps).

## Scale from gravity (measure.py)
Pouch centroid x in free fall (frames 66-80, from scene/tracks/pouch.csv, checked sharp/±1 px).
Quadratic fits: 67-80 -> 11.765 px/frame^2, 68-80 -> 11.772, 70-80 -> 11.808, 68-79 -> 11.678, 67-78 -> 11.674.
Second differences 10.6-12.6 (last one 14.6 is blur-affected). Adopted a = 11.77 px/frame^2 = 10593 px/s^2.
Scale = 9.8 / 10593 = 0.925 mm/px.

## Short side in pixels
- edges.py: half-level edge crossings on 11 intensity profiles across the short axis, held frames 5, 10, 55, 65:
  149.5-150 px each; frame 68 (early flight) 148 px.
- Min-area rectangle of V<70 mask (record + measure.py): 154.8-155.2 px (includes soft edge / shadow fringe);
  V<50 mask: 149.6-150.3 px.
- Adopted ~151 px (edges 150, threshold masks 150-155).

## Answer
151 px x 0.925 mm/px = 13.97 cm -> **14.0 cm** (range 13.9 at 150 px to 14.3 at 155 px).
Check: long side ~241-246 px -> 22-23 cm, aspect 1.6; a 14 x 23 cm zip pouch/wallet is plausible.
Confidence: good (±3%).

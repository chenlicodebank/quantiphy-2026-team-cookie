# q1320 – height of the white car (white cargo van, `white_van` in scene/)

Answer: **2.04 m** (roof top above the road; AABB vertical extent, tyres to roof).

File fps = question fps = 24; t=0.58 s -> frame 14, t=1.58 s -> frame 38.

## Camera (scale-free geometry)
- Vertical VP from 7 poles (lamp posts, traffic-light poles; `poles.py`, residuals ~0.1 px): (1078.5, 6848)
  -> principal-point x and roll confirmed (cx=1080, roll 0).
- Road VP from curbs (`curbs.py`): (810, -195); scene record says (800, -208). Horizon y ~ -203.
- f^2 = (y3 - cy)(cy - vh) -> **f = 2165 px** (2150-2172 over the vh range). Check: the cross-street curb slope is
  predicted at 0.040 and measured at 0.036.
- Checks against the given depths: the pedestrian comes out 1.74-1.78 m tall and the camera 8.17-8.20 m above the
  ground (`camheight.py`, vertical line from the pelvis at its depth down to the foot row). The cyclist with its rear-wheel
  contact re-read at row ~538 (the scene record's 516 is too high) gives 8.1-8.3 m above the road (`hc_road.py`). Use hc = 8.2 m.

## Van motion (`vhfit.py`, `features2.py`, `topedge.py`)
Four body features: roof top silhouette, rear-window top, rear-window bottom and bumper top. They are tracked over
frames 0-52 with sub-pixel accuracy, and their image distance to the VP gives the along-road motion up to scale. All
four fit a clean constant-acceleration curve (v0 ~ 0.17 m/s for a = 4). With a = 4 m/s^2 (the prior), the displacement
from frame 14 to 38 is **4.50 m** (4.48-4.53 over the vh range).

## Inconsistency found
The two van depths (21.365 -> 25.255) with f = 2165 imply only 4.09-4.17 m (a ~ 3.66 = 4 x (24/25)^2).
In that scale, with hc = 8.2 from the pedestrian and cyclist, the van's bumper bottom would sit 1.0 m above the road
and its bumper top 1.3 m above it, which is impossible. With the prior's 4.50 m, all van features have realistic heights:
- bumper bottom 0.37 m, bumper top 0.65 m, window bottom 1.43 m, window top 2.01 m, roof 2.02 m;
- rear width 1.99 m;
- an AABB-centre origin at D1 = 21.36 m implies length 5.67 m. That is a Chevrolet Express (5.69 x 2.01 x ~2.08 m).

So the prior, the pedestrian/cyclist depths and the van's absolute depth D1 (agreeing to ~1%) are mutually
consistent. Only the van's depth difference D2 - D1 is off, by ~0.3 m in D2. Under the depths-only reading the
roof would be ~2.45-2.55 m (with an impossible 1.0 m bumper), so I rejected it.

## Height
Motion parallax (`final.py`): a point at height z moving Δs along the road satisfies hc - z = Δs / Δc, where
c = (horizontal along-road distance)/(drop below camera) of its ray at frames 14 and 38.
- Roof top silhouette rows: 441.2 -> 336.8 (fit rms 0.1 px).
- Roof height: 2.02 m (f 2165, vh -203, hc 8.20). Over vh -195..-208 and hc ±0.08 m it spans 1.85-2.25, mean 2.04.

## Second route
Rear-face check: the rear body is 237 px wide (tail-light corners) at the triangulated rear-face distance, which gives
1.99 m. This matches the Express proportions (H/W ~ 1.03 -> ~2.05 m).

Answer 2.04 m. Confidence moderate: about ±5% from camera height and VP, plus the depth/prior conflict above.

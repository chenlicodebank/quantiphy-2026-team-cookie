# q_802 — width of the house (m)

Prior: speed of the horse at the back = 0.874 m/s. The horse at the back is the trailing **chestnut horse** (left).
2D simulation, static camera, fps = question_fps = 24, so no re-timing.

## Scale (prior)
Chestnut horse pixel speed, frames 0-48 (frame 48->49 is an animation-loop reset, excluded):
- linear fit of the scene track: mask centroid 3.241 px/frame, tail (bbox x0) 3.239, nose (bbox x1) 3.283
- second route, same-gait-phase matching (cycle.py): colour-mask silhouettes matched by IoU over x-shift; pairs with the
  same pose about 21 and 43 frames apart give 139/43 = 3.233, 142/44 = 3.227, 137/42 = 3.262, 136/42 = 3.238 px/frame
- endpoint centroid difference 3.154 (affected by pose change); torso template matching 2.76 (biased low by the
  static brick background inside the template, so rejected)
-> v = 3.24 px/frame = 77.8 px/s -> scale = 0.874 / 77.8 = 0.01124 m/px

## House width (eaves.py, frame 0, saturation edge versus sky)
- Full horizontal extent including the gable verge/eave tips (y around 620): x 176-903 = **728 px -> 8.18 m** (answer:
  world bounding box of the house as seen from the front, i.e. its gable-end face)
- Upper-storey timber walls: x 198-884 = 687 px -> 7.72 m
- Brick ground floor: x 250-830 = 581 px -> 6.53 m

## Depth caveat
The horses walk just in front of the house: the hooves meet the ground at y around 1045-1048 and the house's
brick/grass line is at about 1040. With a level camera (house verticals are parallel, so the horizon is near y = 960)
that means the house is at most about 3-13 % farther away, but grass hides both contact lines, so the difference is
not clear. I followed the 2D one-scale convention. If the house really is farther away, its true width would be
somewhat larger (up to about 9.2 m).

Confidence: moderate. The scale is good to about ±2 %. The main uncertainties are which extent counts as the width
(eaves versus walls, ±6 %) and depth.

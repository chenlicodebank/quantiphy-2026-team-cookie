# Q35 – width of the turning yellow car (m)

Prior: acceleration of the white car (van) = 4 m/s^2. 2D top-down scene, static camera, 24 fps (file fps = question fps).

## Scale (measure.py)
- Van front (top) edge tracked per frame with sub-pixel threshold crossings of the mean column profile (x 805-858).
- Quadratic fit of front-edge y vs frame: acceleration 0.2820 px/frame^2 in every window
  (4-71, 10-71, 4-38, 38-71, 20-60 all 0.2818-0.2820), residual rms 0.06 px -> uniform acceleration.
  (Rear edge disturbed by bumper/shadow late in the clip; not used.) Scene record ccy fit gives 0.279-0.281, consistent.
- 0.2820 x 24^2 = 162.4 px/s^2 -> scale = 4 / 162.4 = 0.02463 m/px.

## Yellow (tan) car width (sedan_width.py)
- Width = extent across the car axis, from the R-B (yellow saturation) profile at half-max:
  frame 0 (heading north, x extent): 79.5-80.1 px along the body; threshold mask 952-1031 = 80 px, no mirror protrusion.
  frame 69-71 (heading east, y extent): 79.9-81.5 px (centre 79.9).
  Scene record colour-mask cwidth median 81.1 px; diff mask 83-84 px includes soft shadow.
- Width = 80 px x 0.02463 = 1.97 m (range 1.96-2.00 for 79.5-81 px).

## Check
- Two independent orientations (start and end of the turn) give the same 80 px width.
- Sanity: van length 234.5 px -> 5.8 m, sedan length 219 px -> 5.4 m, width ~2 m: plausible vehicle sizes.

Confidence: good (scale ±1 %, width ±1.5 %).

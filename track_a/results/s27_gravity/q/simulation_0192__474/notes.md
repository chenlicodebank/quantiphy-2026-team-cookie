# q474: width of the truck (m)

Prior: the box falls with acceleration 9.8 m/s^2 before 0.6 s. There is no depth_info. File fps = question_fps = 120.
The view is frontal and the camera is static, so I used one metres-per-pixel scale from the box's fall.

## Scale (fit.py, fit2.py)
- Track: scene/tracks/cardboard_box.csv `cy_ref_px` (front-face centre, from template matching), frames 0-57,
  which is before the box touches the roof at frame 58-59.
- The box track has timing hiccups. Some frames show the simulation state one frame early (a double step), and the
  next frame is then frozen. A plain quadratic fit gives rms 2.3 px. fit2.py lets each frame show sim frame i or i+1
  and assigns this per frame iteratively. That brings the rms down to 0.09 px.
- Result: a = 2071 px/s^2, stable within 0.1 % for fit ends at frames 50, 55 and 57. Scale = 9.8/2071 = 0.004732 m/px.
- For comparison, forcing v0 = 0 gives about 2010 px/s^2, but with rms 0.5 px, so I rejected it. The best fit puts
  release near frame 1.

## Truck width (truck.py, frame 120)
- I took the outer edges of the white rear body row by row from y = 600 to 1020. The left edge is the dark outline
  at x ≈ 660. The right edge is the steepest drop at x ≈ 1228. The median width is 568 px, and it is the same in every
  row (±1 px).
- Width = 568 × 0.004732 = **2.69 m**.

## Depth / perspective check
- The tracked point is on the box's front face, so the pixel acceleration belongs to the depth of the front face.
- The box rests at the rear top edge of the truck. It hides the inner posts of the rear roof rails, and its bottom
  (y ≈ 526) sits at the roof-edge line (y ≈ 533). Its front face is therefore at about the same depth as the truck's
  rear face, possibly a little in front of it.
- From the underside of the box seen early in the fall (trapezoid ratio ≈ 0.87, about 40 px tall), the horizon is
  near y ≈ 550 and the camera is a few box-depths away.
- A depth offset of ±0.3 m between the box face and the truck's rear face would change the answer by about ±3-4 %.

## Plausibility
At this scale the truck body is 2.69 m wide and 512 px = 2.42 m tall, which is a realistic box-truck body. The box
front face is 1.33 × 0.93 m: a large box, but possible.

Confidence: moderate-good (about ±5 %). The main uncertainty is the box's depth relative to the truck's rear face.

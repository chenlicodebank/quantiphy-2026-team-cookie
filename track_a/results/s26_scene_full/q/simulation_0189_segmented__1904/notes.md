# q1904: height of the box (m). Prior: speed of the box = 0.094 m/s

The box is the brown cardboard box ("FRAGAIL", one flap up) on the roof of the catering truck's cargo body.
This is a 2D side view with a static camera. fps = question_fps = 120, so no re-timing.

## Scale from the prior (box speed)
- I tracked the box texture by template matching (measure.py, then parts.py on 5 horizontal strips from the box's top to
  its bottom). All strips move the same way, so the box is rigid. It rises at a constant 0.1599 px/frame (linear-fit
  rms 0.05 px; quadratic term ~0; every 40-frame chunk gives 0.157-0.164). That is 19.18 px/s.
- The box does NOT ride rigidly with the cargo body, which speeds up from ~0.06 to 0.24 px/frame. The constant box
  speed matches a constant-speed prior.
- Scale = 0.094 / 19.18 = 0.004900 m/px.

## Box height in pixels
- The camera is below the roof line, so the roof's front edge hides the box's bottom edge at the start and end.
  The record's box height_px (184-193 px) is therefore wrong: it measures to the roof rim, not to the box.
- In frames ~90-260 the box is up to ~8 px higher above the roof than at frame 0. Here its dark underside shows
  as a black strip below the front face (seen from below).
- The front-face bottom edge is the 50% crossing from brown to that dark strip. The top edge is the 50% crossing from
  white to brown. Both use the median of 13 columns, x 560-800 (edges.py).
- Front-face height is 190.6 ± 0.5 px, steady while the gap to the roof changes from 1 to 8 px. That steadiness
  confirms this is the box's real edge.
- The flap sticks up above the top edge by 17.9 ± 0.6 px (flap.py, 21 frames), so the height including the flap is
  ~208.5 px.

## Result
- Box body without the flap: 190.6 × 0.004900 = **0.934 m**. Width 408 px = 2.00 m.
- World bounding box including the raised flap: 208.5 × 0.004900 = **1.022 m**.
- The convention (world AABB) would include the flap if it is part of the box mesh; the nominal box height excludes it.
  I answer with the harmonic mean, **0.976 m**, which is within ~4.5% of either reading.
- Sanity check: the truck length is 1716 px = 8.4 m, which is plausible.

## Second-route check
- The top-edge track alone (chunk rises 0.148-0.178 px/frame, mean 0.157) agrees with the texture-tracked speed to within 2%.
- Front-face height measured frame by frame from 100 to 240 stays at 190.0-191.6 px.

Confidence: scale ±0.5%, height ±0.5%. The main uncertainty is whether the flap is included (±4.5%).

# Q652: width of the TV stand (m)

The TV stand is the dark low console at the top centre, x from 710 to about 1160 (the right end is under the lamp). Its width is the front-to-back depth, which is the image y extent in this top-down view.
Prior: the vacuum diameter is 0.438 m. depth_info is null. fps 24 = question_fps.

## Measurements (frame 0, scripts tvprof.py, tvprof2.py, vacprof.py)
- Console column profiles at x = 880, 1000 and 1060 all give the same edges:
  - back edge of the top: y = 168.8
  - front edge of the top: y = 282.5
  - lighter band (the front face) down to y = 292.5, then the carpet.
  - So the top surface is 113.7 px deep and the full outline is 123.7 px.
- Vacuum: radial edge scans from the fitted centre give a radius of 60.4 px in the tangential directions at frames 0, 40 and 77, so the diameter is 120.8 px. The side facing the image centre bulges by 2.7 px at frame 0, which is the vacuum's side wall seen in perspective.

## Perspective correction
The camera is a perspective camera above the image centre (cy = 540). You can tell because the side walls facing the centre are visible.
- The front face runs from radial distance 257.5 px (top edge) to 247.5 px (bottom edge). So (H - h_bottom)/(H - h_top) = 1.0404.
- The face is assumed to reach the floor. Then the scale at the console top is 1.0404 times the floor scale.
- The vacuum's side wall gives k = 2.7/663 = 0.004. So the vacuum's rim scale is about 1.004 times the floor scale.
- The scale ratio is s_vac/s_top = 1.004/1.0404 = 0.965.
- W = 0.438 x 113.7/120.8 x 0.965 = **0.398 m**.

## Alternative readings
- Top surface with a flat scale and no correction: 0.412 m.
- Full outline including the projected front face, flat scale: 0.449 m. This overstates the width because the front face is seen in perspective.
- If the face stops above the floor (on legs), the corrected value drops only slightly.

## Second-route check
The three columns agree to within 0.2 px. The vacuum diameter is the same at frames 0, 40 and 77 (tangential directions). Answer 0.40 m, which is also a typical TV-stand depth.

Confidence: moderate, about ±5%. The main assumption is the height at which the front face ends.

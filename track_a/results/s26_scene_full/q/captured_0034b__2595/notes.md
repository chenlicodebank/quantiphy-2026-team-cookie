# q_2595: diameter of the soccer ball (cm). Answer: 18.5 cm

Prior: tennis ball diameter = 6.7 cm. depth_info: right tennis ball 0.776 m and left tennis ball 0.706 m at t=1.2 s (frame 29), soccer ball 0.894 m, pencil bag 1.05 m.
question_fps = file fps = 24, so frame 29 is t = 1.2 s.

## Pixel measurements (frame 29; the soccer ball doesn't move, frames 0 to 48)
- Soccer ball (profile.py): the half-level saturation edge on 11 rows gives a horizontal width of 91.9 px (max 92.5). The top edge is at y = 269.75, and the centre is at about (601.5, 315.7). measure.py gives the same width on frames 0, 29 and 48. The scene record's 91.3 px agrees. The bottom edge is mixed with the ball's shadow, so I didn't use it.
- Tennis balls: the scene tracks' circle fits give left 28.1–29.1 px and right 28.8–29.9 px. The 29 px circle overlay matches both balls (frames/tennis_crops.png). I used 29.3 ± 0.7 px.

## The given depths contradict the image
- Method-card route (f = 763 with depth_info): soccer ball = 0.894 × 92 / 763 = 10.8 cm. This fails the prior check: the same route gives the tennis ball as 0.776 × 29.3 / 763 = 2.98 cm, not 6.7 cm.
- If I fit the focal length to the prior instead, the tennis balls give f_eff = 302–339 px. That would be a 117–129° field of view, which doesn't match this image. It gives a soccer ball of 24.2 cm (from the right ball) or 27.4 cm (from the left ball).
- The depths also put the soccer ball farther from the camera than the tennis balls (0.894 m against 0.71–0.78 m). In the image it is the other way round: the soccer ball sits in the middle of the table, and the tennis balls are near the far edge. The near (front) edge of the table is 415 px wide and the far (back) edge 303 px, which makes the tennis balls 9–17% farther away than the soccer ball.
- The focal length can be checked independently from the table. The tabletop's vanishing points, assuming its corners form a right angle, give f = 743 px, close to the lab value of 763. So the image matches the stated camera, and the depth_info values don't.
- Because the reference sizes were measured with a ruler on the real objects, I estimated the real size from the image geometry and didn't use the depth values.

## Main route (geom2.py)
- f = 763 and principal point (640, 360). The table-plane normal comes from the vanishing points of the table corners (camera tilted 37° below horizontal).
- Each ball centre sits one radius above the table plane, and its z-depth is 2·f·r / D_px.
- Fixing the tennis ball radius at 3.35 cm sets the scale (camera to table plane about 0.90–0.96 m). Then I solved for the soccer ball radius.
- Results for six tennis-ball samples (left ball at frames 29 and 30; right ball at frames 29, 30, 44 and 48): 17.6–18.9 cm, median 18.5.
- Monte Carlo with corners ±4 px, f ±3%, tennis D ±0.7 px and soccer D ±1 px: median 18.35 cm, 5–95% range 17.9–18.8 cm.

## Second route (simple perspective ratio)
- On a plane, 1/z is linear in the image row, and the table edges are nearly horizontal. So the table width at a row gives the depth ratio between the tennis-ball contact row and the soccer-ball contact row.
- Soccer diameter = 6.7 × (92 / D_tennis) / (z_tennis / z_soccer) = 17.8–19.1 cm, median about 18.7 cm.

## Answer and confidence
- Answer: 18.5 cm. That fits a size-3 soccer ball (18.5–19 cm). With no perspective correction at all, the raw pixel ratio would give 21.0 cm.
- Confidence: moderate. The two image-based routes agree to within about 3%. The main risk is whether the reference answer was derived from the inconsistent depth_info: the method card gives 10.8 cm and the prior-fitted focal length gives about 24–27 cm.

Scripts: measure.py, profile.py, tennis_hm.py (half-max widths; too noisy because of blur and shadow, not used), crops.py, corners.py, geom.py, geom2.py.

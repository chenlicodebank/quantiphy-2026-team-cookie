# q_671 — width of the floor mirror (m)

Prior: robot vacuum diameter = 0.438 m. depth_info: none. fps = question_fps = 24 (timing not needed; static size).

## Identification
scene/ lists no mirror. Its "glass_side_table" in the top-right corner (x≈1345–1625, y≈85–222) is really the floor
mirror: a light-wood rectangular frame with a reflective pane, leaning against the top wall. It reflects the robot
(frames 13–26), and in the top view it shows as a trapezoid. Its bottom bar stands on the floor at y≈220, and its top bar
rests on the wall near y≈90. Perspective spreads out the elevated top (camera centre x≈960, so the legs lean to the right).
I corrected the record here: that object is the floor mirror, not a table.

## Measurement (crop.py, legs.py; frame 77; overlay frames/mirror_lines.png)
- Straight lines fitted to the outer edges of both side legs (sub-pixel horizontal gradient, rows 130–213):
  left x = −0.459·y + 1449.1, right x = −0.867·y + 1699.8 (rms 1.2 / 0.5 px).
- Bottom edge of the frame (vertical gradient, columns 1370–1495): y = 219.5 (IQR 219.5–220.5).
- Outer width at floor level (y≈220): 1509.0 − 1348.1 = **161 px** (±3 px). At the top bar (y≈95) it is ≈210 px; that
  edge is raised, so perspective magnifies it, and I don't use it.
- Width = horizontal extent across the face, along x. Only the bottom edge is at floor level, the same plane as the robot.

## Scale
The robot is a disc of 117.8 px (circle fit, scene record; bbox 119 px), so 0.438/117.8 = 0.003718 m/px. The robot's
rim is only about 0.07–0.09 m above the floor. The mirror's trapezoid gives a camera height of about 7 m (top/bottom
width ratio ≈1.3 for a mirror about 1.5 m tall), so the robot is magnified by about 1% compared with the floor. The floor
scale is therefore ≈0.00375 m/px.

Width = 161 × 0.003718 = 0.599 m (no height correction), or 0.605 m with it.

## Check
Reading the bottom corners by eye on the zoomed, contrast-enhanced crop gives about 1345 and 1506, so 161 px. Measuring
the edges row by row (profile.py, y = 208–222) gives 160–168 px. Real floor mirrors are about 0.5–0.7 m wide, so this
fits.

**Answer: 0.60 m.** Confidence is moderate to high (about ±3%). The main uncertainty is where exactly the bottom corners
of the legs are.

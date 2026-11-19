# q_667 — length of the TV stand (m)

Prior: vacuum diameter = 0.438 m. No depth_info. fps 24 = question_fps (static size question, timing irrelevant).
Scene: overhead Blender render, static camera; frame 77 used (robot stationary).

## Measurements (scripts: prof.py, prof2.py, robot.py, persp.py)
- Robot vacuum diameter at frame 77: threshold bbox 119 x 118 px; gradient-edge circle fit 120.4 px; scene record
  circle fit 117.8 px. Used ~119 px -> floor-level scale 0.438/119 = 0.00368 m/px.
- TV console (dark grey media console on the top wall): left end x = 710.5 px (median gradient edge over rows 175-285),
  front edge y = 292.5. The right end is hidden under the lamp shade (Ø~145 px, centre 1192). Bounds: the console is
  visible up to x≈1152 at y=290 and there is carpet right of the shade, so the end lies between 1156 and 1228.
  The TV on the console has its legs at x = 842 and 1062 (centre 952); its top edge runs 803-1101 (centre 952). If the TV
  is centred on the console, the right end is 2*952 - 710.5 = 1193.5 (matching the lamp centre 1192), so the length is
  about 483 px. The scene record had 490 px (710-1200).
- Planar (single-scale) value: 483 x 0.00368 = 1.78 m.

## Perspective correction (second route; clear perspective is visible)
- The TV's front face shows up as a trapezoid: top edge y≈221.5, width ≈298 px; bottom edge y≈241.5, width ≈275 px.
  Scale ratio between the top and bottom edges is 1.067 (from y) and 1.082 (from width). A 16:9 screen
  (h = 0.5625 W) then gives f ≈ 2100-2600 px, and camera height above the robot's top ≈ 0.438 f/119 ≈ 7.7-9.5 m.
- The console top is ~0.5 m above the floor while the robot outline is at ~0.09 m, so the console top is magnified by
  ~4-6% compared with the robot's scale. Corrected length: 1.778 - 483*0.41/f ≈ 1.68-1.70 m.

## Answer
1.70 m (planar value 1.78 m without the perspective correction; corrected 1.68-1.70 m).
Confidence: moderate. The main uncertainties are where the hidden right end lies (the TV-centred assumption) and the
perspective correction (16:9 TV, console height ~0.5 m assumed).

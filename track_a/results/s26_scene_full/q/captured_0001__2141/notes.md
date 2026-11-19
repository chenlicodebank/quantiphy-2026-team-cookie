# q_2141 – size (diameter) of the ball, cm

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 763 px.

## Main route (t = 0, ball at rest, sharp)
- Depth to ball at t=0: 1.1075 m (depth_info).
- Pixel diameter, frame 0 (and frames 5-27, ball still at rest):
  - scene/ HSV mask: bbox 45x44, equiv. diameter 44.8, PCA extents 45.2/44.4.
  - measure.py: saturation profiles along 12 directions through the centre, half-max edges:
    medians 43.4 (f0), 43.9 (f5), 44.0 (f10), 43.6 (f20), 44.9 (f27).
  - Adopted 44.3 ± 0.5 px.
- Diameter = 1.1075 x 44.3 / 763 = 0.0643 m = 6.43 cm.

## Second route (t = 1.5 s, frame 36, depth 0.912 m)
- Ball is motion-blurred. Mask width across blur 51.9 px -> 0.912 x 51.9 / 763 = 6.20 cm;
  saturation half-max 48.1 px (blur lowers contrast, underestimates) -> 5.75 cm.
- Depth-ratio check: 1.1075/0.912 = 1.214 -> expected 53.8 px at frame 36, vs mask 51.9-53.5: consistent
  with the t=0 value within blur error. The sharp t=0 frame is the reliable one.

Prior (acceleration 3.0 m/s^2) not needed for size.
Answer: 6.4 cm (confidence: good, ~±4 %).

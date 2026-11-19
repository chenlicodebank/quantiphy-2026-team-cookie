# q_2449: length of the slope (cm)

The file and the question both run at 24 fps. The camera is static. Focal length f = 0.5959 x 1280 = 762.8 px, with the principal point at (640, 360).

## Method
- Slope = the white board used as a ramp. I took its outline from a mask in code at frame 46 (`board.py`, overlay in
  `frames/board_vis.png`). Corners: TL (750,360), TR (860,361), BL (~608.5,467.5), BR (~705,491). These agree with the
  corners in scene/notes.md.
- Far end = midpoint of the top edge, (805, 360.5), back-projected with distance_slope_far_camera = 1.243 m.
  Near end = midpoint of the bottom edge, (656.75, 479.25), back-projected with distance_slope_near_camera = 0.990 m.
  Each point is the depth times the unit ray, since depth_info is the Euclidean camera distance (`length.py`).
- Slope length = |P_far - P_near| = **0.371 m = 37.1 cm**.

## Checks
- Same calculation along the left edge gives 36.0 cm; along the right edge it gives 38.1 cm. Their mean is 37.05 cm.
- The book's 3D path between frames 24 and 29 (book depths 1.0685 and 0.977 m) runs almost parallel to the slope
  direction: unit vectors (-0.72, 0.42, -0.55) for the book and (-0.65, 0.41, -0.64) for the slope. The book moved
  15.9 cm against the 19.4 cm that a = 2.8 m/s^2 would give from an onset at about frame 18.5. That is roughly
  consistent, given the uncertain start time and that it is a real (noisy) recording.
- The board's width cannot be checked with a single depth per edge, because the edges recede towards a vanishing
  point at about x = 180.

Confidence: moderate-good, about ±5%. The main uncertainty is exactly which end points the annotators used for the
two depths.

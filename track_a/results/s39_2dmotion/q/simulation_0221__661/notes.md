# q_661: speed of the vacuum cleaner at t = 1 s

Prior: vacuum diameter = 0.438 m. 2D top-down scene, static camera. File fps = question_fps = 24, so t = 1 s is frame 24.
Speed = |p(24) - p(23)| x 24 (one-frame backward difference).

## Measurements (scripts in this folder)
- `measure.py`: bright-disc threshold mask + iterative circle fit, frames 20-28. Centre step 23->24 = **20.31 px**
  (neighbouring steps 20.12, 20.40, so it changes smoothly). Mask centroid gives the same step.
- Scene record (`scene/tracks/robot_vacuum.csv`, rim circle fit): step 23->24 = 20.24 px.
- SAM 3 (`white disc`, box prompt) mask centroids f23 (1411.2, 379.8) -> f24 (1391.2, 379.6): step = 20.0 px.
- I used **20.28 px/frame** (between my value and the record's; SAM is 1.4% lower).
- Diameter at frame 24: `radial.py` gives the half-max edge radius from the radial brightness profile: 60.24 px averaged over all
  angles (top 59.9, bottom 60.2, right 60.1, left 61.7). Frames 20 and 28 give the same within 0.2 px. Diameter ~120.5-121.8 px;
  the record's outer-rim fit is 121.5 px; a 4x grid crop by eye shows x 1330-1452 (~122). I used **D = 121.0 px**.
  (The threshold-170 fit gives 117.6 px, but its circle sits inside the visible rim on the overlay, so I did not use it.)
- SAM extents differ from mine by more than 3%: its mask is 132 x 139 px (box 1320.8-1458.4 in x). On the zoomed frame
  (frames/f24.png) the disc edge is at about 1330-1452, so the SAM mask also takes in the soft halo/shadow around the disc.
  I trust the half-max/rim measurement for size. SAM is fine for motion (its centroid step is within 1.4%).

## Result
scale = 0.438 / 121.0 = 0.003620 m/px; speed = 20.28 x 0.003620 x 24 = **1.76 m/s**.
Second route: record diameter 121.5 with record step 20.24 gives 1.751; SAM step 20.0 gives 1.74; my own step and diameter
(20.31, 120.5) give 1.77. Spread about ±1.5%.

Confidence: high (~2%). The main uncertainty is the edge definition for the diameter (±1%).

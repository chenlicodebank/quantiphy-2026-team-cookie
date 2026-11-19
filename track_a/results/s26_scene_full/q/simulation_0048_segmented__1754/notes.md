# q_1754 – width of the telephone booth (simulation_0048_segmented)

Answer: **1.31 m** (front-face width of the booth = the "kiosk" in scene/).

## Time base
fps = question_fps = 33. No re-timing.

## What was measured
- Booth (static) top-face edges, fitted with subpixel edge lines on an average of frames 0-4 (`box_edges2.py`, saved in `lines.npy`):
  - front edge slope 0.0986, back edge 0.0817, left edge -0.678, top/side boundary -1.516.
  - Corners: FL (1101.5,387.1), FR (1420.1,418.5), BR (1465.4,349.7), BL (1189.9,327.2).
  - Vertical silhouette edges (`vp_fit.py`, rms 0.2-0.6 px): vertical vanishing point (1023, 6550).
- Camera from the booth's three orthogonal vanishing points (`box_vps.py`, `aniso_fit.py`, `aniso_test.py`): square pixels with
  f ≈ 1630 px give 89.4°/89.9°/89.2° between the three box directions. f = 1183 px gives 77°/87°/83°, so the box would not be rectangular.
  Pitch ≈ 14-15° down, from the vertical vanishing point.
- Pedestrian (prior 1.8 m) and cyclist bboxes come from scene/tracks (checked on frames).

## Conflict between depth_info and the image
With the given depths, the walker's 1.8 m height forces f ≈ 1183 px (`camera_fit.py`). That is inconsistent with the booth geometry, and the cyclist then comes out
2.7 m tall, with a non-horizontal motion and a ground plane that is not shared (`consistency.py`, `motion_check.py`).
With f ≈ 1550-1630, the 1.8 m prior and one shared ground plane (`ground_model.py`), everything is consistent:
- the cyclist's height is 1.72-1.79 m, constant over frames 0-59;
- the walker moves at 1.08 m/s and the cyclist at about 4.1 m/s;
- the booth top is a rectangle (front ≈ back, left ≈ right).

The best focal length combines cyclist-height constancy (f≈1560), walker-height constancy (≈1610) and the box vanishing points (1580-1670):
**f ≈ 1590 px**, camera ≈ 4.2 m above the ground. The metric scale comes from the prior (the depth_info values could not be reproduced and were not used for scale).

## Booth size
The booth's base is below the image, so its size scales with its unknown height H (top plane at h−H below the camera).
- Constraint: the back-right vertical edge reaches the image bottom (y=766), so H ≥ 2.33 m (f=1590) and W ≤ 1.44 m.
- W(H) at f=1590: H 2.4 → 1.39, 2.5 → 1.31, 2.6 → 1.24, 2.8 → 1.08 m. The depth (side) is about 0.97 × W.
- I took H ≈ 2.5 m, a typical booth height just above the lower bound, which gives **W ≈ 1.31 m** (front-face width). Its side depth is ≈ 1.27 m,
  so the "shorter horizontal extent" reading gives about 1.27 m.
- Sensitivity: f 1550/1630 → 1.25/1.37 at H=2.5.

## Second route / check
The top-face rectangle is reconstructed independently at each f. The front and back edges agree to 1%, and the left and right edges agree to 0.1%.
The answer interval [1.2, 1.44] follows from the H ≥ bound and plausible booth heights.

Confidence: low-moderate. The main uncertainty is the unseen booth height (±10%). If depth_info were the true scale, every length would be about 0.78× (W≈1.0 m).

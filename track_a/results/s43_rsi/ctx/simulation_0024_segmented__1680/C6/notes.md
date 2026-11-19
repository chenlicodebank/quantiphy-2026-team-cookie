Scale from prior: boat hull centroid moves 162.5 px/s (linear fit 162.9, rms <1 px) at 90.27 m depth with 4 m/s -> f = 162.5*90.27/3.99 = 3670 px (hfov 14.9 deg); check gives boat 9.7 m long, 4.6 m tall (plausible). Rock horizontal extent measured 625 px (SAM mask 623, independent grey threshold 627, stable over the clip, fully inside frame). Rock taken at the boat's depth (only scale given): L = 625*90.27/3677 = 15.3 m; planar route 4/162.5 m/px gives 15.38 m, agreeing within 0.6%.

Final message:
**Answer: 15.35 m** (question 1680, length of the rock).

Method summary:
- **Scale**: the boat's red-hull centroid moves 162.5 px/s (linear fit 162.9 px/s, residual rms <1 px → constant velocity) at a depth of 90.27 m with a prior speed of 4 m/s, giving f ≈ 3670 px (hfov 14.9°). Cross-check: the boat then measures 9.7 m long and 4.6 m tall — a plausible small trawler, confirming the real-scale scene.
- **Rock**: SAM 3 mask plus an independent grey-threshold measurement both give a horizontal extent of 623–627 px (625 px used), stable across the clip and fully inside the frame.
- **Result**: 625 px × 90.27 m / 3677 px = 15.3 m; the single planar scale route (4/162.5 m/px) gives 15.38 m, agreeing within 0.6 %. The main residual uncertainty is the rock's own depth, which is not given, so it is taken at the boat's depth (the only scale available).

# Q1394 – width of the police car (VW-T5-style police van), simulation_0168

Prior: bike speed 5.52 m/s. depth_info: bike 28.219 m at t=0 (frame 0), 25.554 m at t=0.5 s (frame 12).
question_fps = file fps = 24.

## Camera (static, level)
* Focal length from two orthogonal building-facade vanishing points (LSD segments, `vp.py`):
  front-face VP (-3454, 543), side-face VP (2645, 536) -> f = 2727 px (bootstrap 2683-2768). Horizon ~ y 540,
  verticals vertical -> no pitch/roll; principal point at the image centre.
* Check with the bike (`camh.py`, `f_from_vp.py`): the bike rides parallel to the road/side facade (VP u≈2645; the
  van's own image track also points to u≈2658). Constant 5.52 m/s along that direction from the given frame-0
  depth reproduces the frame-12 depth (25.548 vs 25.554 m) and the bike's image path over all 80 frames
  (±10 px pedalling sway). The depth-rate/angle condition alone gives f ≈ 2690. Used f = 2727 (±2 %).
* Camera height 1.165 m: from the bike's wheel ground contacts (bbox bottom) against the modelled depths over all frames.

## Van geometry (top view on the ground plane; a = lateral coordinate, s = coordinate along the heading)
* Wheel contacts (scene keyframes 40-79): FR/RR lateral a = -5.90 ± 0.04 (constant, so the van drives straight along the
  road), wheelbase 3.00 m (2.90-3.12), along-track speed 0.2858 m/frame. FL about -7.46 (noisy, partly occluded).
* Fixed features triangulated over many frames from the van's known straight-line motion (`motion_stereo.py`,
  `ms2.py`, `silh_left.py`, `mirror.py`):
  - licence plate (centreline): a = -6.745 (plate height 0.46 m, consistent in every frame)
  - left body silhouette, bumper rows (background difference, frames 0-26): a = -7.62 .. -7.65
  - right/rear body silhouette (frames 60-79): a = -5.93 (rear corner, s ≈ FR + 3.8)
  - right mirror tip (hand-read in frames 50/60/70/79, residuals ≤ 2.4 px): a = -5.61, s = FR + 0.59, height 1.35 m
  - left mirror silhouette (mirror rows, frames 0-26): a = -7.85 .. -7.92
  - the mirror midpoint (-6.74) matches the plate centreline (-6.745), which supports the result.

## Width
* Body only (side to side, without mirrors): 7.63 - 5.93 = 1.70 m (1.63-1.77 depending on which side is
  mirrored about the centreline).
* Including the side mirrors (the extent of a world-space axis-aligned bounding box over the whole mesh):
  7.87 - 5.61 = 2.26 m (2.24-2.31). With f ±2 % the range is about ±0.05 m.
* Answer: 2.2 m. This is the full model's bounding-box width, mirrors included, since the benchmark uses the mesh's
  axis-aligned bounding box. It is shaded slightly toward the body-only reading (1.70 m) because the mirror
  convention is uncertain.

Confidence: the geometry is well conditioned (f from two routes, a consistent centreline, wheelbase 3.0 m like a
real T5). The main uncertainty is whether the reference includes the mirrors: 2.26 m with them, 1.70 m without.

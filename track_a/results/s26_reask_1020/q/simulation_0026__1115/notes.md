# Q1115 – speed of the person at t = 1.0 s (simulation_0026)

Time base: question_fps = 24, so t = 1.0 s is frame 24. The file is labelled 25 fps. Per-frame displacements are
multiplied by 24.

## Scale
- Prior: the person is 1.75 m tall. Their apparent height (sub-pixel half-max edges, head top to lowest foot, measured
  against the clean background plate; `height_track.py`) is 53.4 px on average. The standing-like plateau
  (frames 10-23) is 54.2 px. I used 54.0 px, so 0.0324 m/px at the person (implied f ≈ 3540 px at 114.83 m).
- Horizon / camera check (`mast_check.py` and the boat track): as the boat recedes, its mast top moves down and its
  hull bottom moves up. So the horizon is at y ≈ 445-475. The camera is about level, sits about 4 m above the sand,
  and has no roll.

## Person motion (image, around frame 24)
- Pelvis x (hip-band centroid, torso centroid, and the record's pelvis_x all agree): -0.54 to -0.56 px/frame over
  frames 8-40 and 12-36 (-0.52 over the whole clip). I used -0.545.
- The head top and the feet both move down by the same amount: 0.11-0.15 px/frame overall, 0.115 near frame 24. The
  whole figure translates down; it does not grow.
- Apparent size: three independent tests show no approach.
  - Linear fit of height: -0.006 px/frame.
  - Same gait phase one stride apart (36 frames): -0.7 ± 0.3 px.
  - ECC similarity alignment of same-phase silhouettes (`ecc_scale.py`): scale 0.997-1.000 over 36 frames.
  Walking toward the camera at 1 m/s would give +1.3 % (+0.7 px) per stride, which is excluded. The depth rate is
  0 to 0.3 m/s (receding), consistent with zero.
- depth_info: the person's distance changes by only 3.7 mm between t = 1 and t = 2. If the origin follows the body,
  the measured lateral and vertical motion at constant depth predicts -5 mm. So the given distances agree with a
  body that moves nearly perpendicular to the line of sight.

## Answer
v = 24 × 0.0324 × sqrt(0.545² + 0.115²) = **0.43 m/s**. This is mostly lateral (0.42 m/s), with a small downward part
(0.09 m/s).

## Caveats
- This is below the 0.9 m/s plausibility bound for walking. The scale comes from the person's own size, though, so
  the lateral part is robust.
- Only motion in depth could raise the speed, and both the size tests and depth_info argue against it. If the body
  were receding at the upper bound of the size estimate (~0.3 m/s), the speed would be about 0.52 m/s.
- The gait looks slow (stride about 36 frames). A fast in-depth walk at about 1 m/s was considered and rejected
  because the apparent size does not change.
- Confidence: moderate.

# Q61: speed of the bicycle at 1.0 s

- 2D top-down render, 24 fps (question_fps matches the file, so no re-timing). t=1.0 s → frame 24.
- Prior object: the white car is the white van on the vertical road. Its body length is 236 px (y 811–1047 at f0 and 81–317 at f71,
  read on a zoomed grid crop; scene/vehicle_sizes.json thr25 gives the same). Scale = 6 m / 236 px = 0.02542 m/px.
- Bicycle = `pedestrian_road` track (the dark rider at x≈917, riding straight up). measure.py:
  - linear fit of ref_y over f2–71: 8.886 px/frame; centroid fit: 8.919; local fit f14–34: 8.865. The motion is constant-velocity.
  - The raw one-frame step at f24 is 9.5 px, which is ±1 px mask jitter around the constant 8.9.
- Speed = 8.89 px/frame × 24 × 0.02542 = 5.42 m/s. The raw-step route gives 5.80 m/s, but that difference is jitter.
  Window fits agree to within 0.6 %.
- Confidence: high. The main uncertainty is the van length (±3 px, about 1 %).

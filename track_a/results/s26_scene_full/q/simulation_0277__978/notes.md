# Q978: raccoon speed at 1.0 s (frame 24, 24 fps)

The video is a 2D side view with a fixed camera. fps = question_fps = 24, so no re-timing is needed.

## Scale
- Prior: the raccoon's length with the tail is 1.51 m.
- The scene record's `bbox_w` (median 300) **underestimates** the length because the faint grey snout drops out of the mask. For example, at frame 38 about 30 px of snout is missing. See `frames/box_*.png` from `view.py`.
- I re-measured nose to tail tip on gridded 2x crops at frames 0, 8, 16, 24, 29, 38, 46 and 55. The lengths are 328, 318, 326, 317, 331.5, 312, 322.5 and 315 px, with a mean of 321.25 px.
- Scale = 1.51 / 321.25 = 0.00470 m/px.

## Speed
- The raccoon moves at essentially constant speed (`speed.py`):
  - Linear fit of `cx` over frames 2–71: 22.51 px/frame.
  - Same fit for `bbox_cx`: 22.50 px/frame; for the tail-tip `x0`: 22.50 px/frame.
  - Slope of my manually measured nose/tail midpoints: 22.54 px/frame.
  - Quadratic fit, slope at frame 24: 22.5–22.8 px/frame. The curvature is negligible.
  - One gallop period centred on frame 24 (frames 16–32): 22.4–23.1 px/frame.
- The raw per-frame difference of the centroid at frames 23→24 is 22 px. That value is noisy from gait and mask jitter, but it agrees.
- Speed = 22.5 px/frame × 24 = 540 px/s, × 0.00470 m/px = **2.54 m/s**.

## Check and confidence
- Using the maximum measured length (331.5 px) instead of the mean gives 2.46 m/s. Local window speeds give up to 2.60 m/s.
- Expected error is about ±4%, and the main source is which pose defines the 1.51 m length.

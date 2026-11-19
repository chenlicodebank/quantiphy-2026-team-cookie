# q_1830 — speed of the left (first) ball at t = 1 s

- 2D Newton's-cradle-style scene, fps 30 (file and question agree), t = 1 s -> frame 30.
- Scale from prior: ball diameter 2 m = 164 px (scene record medians; my free circle fits give r = 81.6–82.0 px)
  -> 0.01220 m/px.
- At frame 30 the left ball has already hit the middle ball (contact between f27 and f28) and is drifting slowly
  back to the left at about 1 px/frame.
- Measurement (fit.py): for frames 20–45 I re-fitted the left ball's circle on its own outline contour, with robust
  fits on the full outline, the outline without the contact side, and the top/bottom arcs only. Backward difference
  at f30: 1.03–1.27 px/frame across the variants (1.18 full outline).
- Second route (smooth.py): a quadratic fit of x(frame) over frames 29–45 in several windows gives a velocity at
  frame 29.5 of 0.88–1.04 px/frame (mean ~0.97). The f29 and f30 raw differences (0.76 and 1.18) average to 0.97.
  The motion is slow and steady, so I take ~1.0 px/frame as the true per-frame displacement. The single-frame
  difference carries about ±0.2 px of segmentation noise.
- Speed = 1.0 px/frame x 30 x 0.01220 m/px = 0.37 m/s. Range 0.35–0.44.
- Confidence: moderate. The value is small, so a few tenths of a pixel of edge noise make up a large share of it.

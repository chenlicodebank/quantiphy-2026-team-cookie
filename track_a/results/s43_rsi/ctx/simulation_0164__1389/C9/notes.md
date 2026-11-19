Re-measured the ball from scratch (the scene/ lane-unit scale is not metric and was discarded). Sub-pixel circle fits give the ball radius 47.5->34.4 px over frames 6-36; with f=3773 px (from the 0.21 m diameter at the given 9.391 m depth at t=0.5 s) and the camera height h=1.085 m obtained from the contact-line/centre-line slope ratio, a full pinhole fit of the straight constant-height track gives v(t=1)=3.74 m/s and a=-0.25 m/s^2 (profile likelihood +-0.15). An independent plane reconstruction (no per-frame diameter) gives a_along=-0.18+-0.04. Both routes agree on a deceleration of about 0.2 m/s^2; magnitude reported.

Final message:
I measured the ball's acceleration at t = 1 s as **0.25 m/s²** (decelerating).

**Method summary:**
- Discarded the `scene/` lane-unit scale — its homography is not metrically valid (|h₁| ≠ |h₂| after K⁻¹, and its ball-diameter-in-lane-units drifts 20 % across the clip).
- Measured the ball's silhouette with a sub-pixel gradient edge finder + circle fit (residuals 0.2–0.9 px), cross-checked with the vertical diameter (same 1.38 size ratio).
- Calibrated the camera: f = 3773 px from the 0.21 m diameter at the given 9.391 m depth at t = 0.5 s; camera height h = 1.085 m from the ratio of the contact-line and centre-line slopes; pitch 4.5°, yaw −48° (lane vanishing point at (5243, 245)).
- Fitted a straight, constant-height track with constant acceleration to all 31 centroids plus the depth/diameter/lane-edge constraints: v(t=1) = 3.74 m/s, a = −0.25 m/s² (profile likelihood ±0.15).
- Second route (plane reconstruction from the lane geometry, no per-frame diameter): a = −0.18 ± 0.04 — consistent.

Sanity checks: ball speed 3.7 m/s and head-pin height 0.32 m (vs 0.381 m regulation, 15 % low) are both plausible, so the scale was accepted. Notes written to `notes.md`.

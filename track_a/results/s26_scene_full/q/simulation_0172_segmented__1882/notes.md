# Q1882 — speed of the astronaut at t = 0.5 s (m/s)

Rate: file fps = question_fps = 24, so t = 0.5 s is frame 12 and the speed is |p12 − p11| × 24 (centred at frame 11.5).

## Method (fixed camera, pinhole, 3D)
- Mask: pixels where 255 − min(RGB) > 18, closed with a 5×5 kernel. I re-measured it myself, and the scene track agrees (bbox_h matches exactly).
- Focal length: f = h_px(f24) × 18.147 / (2.2 × k). Here h_px(f24) = 380 and k = the walking-pose height divided by the rest height, taken as 0.95 to 1.0, which gives f ≈ 3130 to 3300 px (HFOV ≈ 39°). The lateral speed changes by only ±2% across k. The depth rate does not depend on f.
- Depth per frame: Z = 18.147 × S24 / S(i), where S is the apparent scale (normalised bbox height, helmet width, sqrt of the upper-body area). Z ≈ 20.3 m for f0–9. The figure then starts to grow at about f9–10, so it is approaching the camera: Z ≈ 19.96 m at f12 and 18.15 m at f24.
- Position: the scene track's pelvis estimate (x, y) is back-projected with Z. Velocity at 11.5 comes from quadratic fits over windows of 6 to 10 frames, because the astronaut is speeding up (push-off).
- Components at frame 11.5 (k = 0.97): vX ≈ 1.86, vY ≈ 0.49, vZ ≈ −2.0 to −3.1 m/s, depending on the scale measure (bbox_h −2.05, helmet −3.1, sqrt upper area −2.8). The torso width gives a smaller rate (−1.0 to −1.5) and the whole-mask area gives the opposite sign. Both are affected by body rotation and leg closing, so I discarded them.
- Speed: the combined scale gives 3.05 to 3.8 m/s across fit windows (3.28 with the 7–16 window). Using the per-measure depth rates gives 2.8 to 3.55.

## Checks
- Pelvis track and mask centroid agree (3.28 vs 3.36).
- 4-frame difference f10→f14 gives 3.31.
- The raw f11→f12 difference is 4.8, which is noisy and not used.
- Context: in f0–9 the size is constant and the speed is about 1.8 m/s. After that the figure speeds up during push-off, the pelvis rises on screen from f16 to f35 (a hop-like lunar lope) and the speed peaks at about 6 m/s near f20. The camera is assumed fixed (simulation convention). Camera motion cannot be checked because the background is white.

## Answer
≈ 3.2 m/s. Confidence: moderate. The depth rate at f12 is the main uncertainty (±15%). If the camera were actually moving and the walk had a constant speed, the answer would be about 1.8 m/s.

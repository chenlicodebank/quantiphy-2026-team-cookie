# q_1523: acceleration of the car at t=0.5 s (frame 12, fps 24 = question_fps)

Method
- The car moves mostly toward the camera at this time, so acceleration is dominated by the depth change.
- Per-frame scale change of the car front: cv2.findTransformECC (affine) between consecutive frames over the car body.
  The vertical scale sy gives Z(i-1)/Z(i). Z(0) = 14.244 m from depth_info (the tire-camera distance).
- Lateral position comes from the tracked front hub with f ~ 2600 px, which is only weakly constrained.
  - Prior: tire diameter 0.764 m, about 130-147 px at frame 0 (tire ~1.56 x rim height). That gives f of 2500-2750.
  - Lateral motion is about 1 m/s against about 6 m/s of depth motion, so f barely matters (f 2400-2800 changes the result by <0.5 m/s^2).
- Raw per-frame sy is noisy: the raw acceleration jumps between -30 and +35. So log-scale is smoothed with a polynomial
  (deg 2-4, frames 0-20) before the backward-difference speeds, and acceleration = (speed12 - speed11) x 24.

Results
- Smoothed speeds are about 6 m/s at frame 12. Acceleration at frame 12 is 6.5-8.2 m/s^2 over poly variants.
- Second route (different body regions for ECC): upper 5.5-7.2, lower 9.5-10.2, wide 6.0-6.9.
- Answer 7.2 m/s^2. Confidence is modest (about +-25%) because of ECC noise and the unknown origin offset (yaw).

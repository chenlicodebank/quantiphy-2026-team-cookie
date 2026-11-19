# Q1407: speed of the astronaut at t = 0.5 s (m/s)

- **Time base.** fps = question_fps = 24, so t = 0.5 s is frame 12. Speed is the backward difference from frame 11 to frame 12, times 24.
- **Scene.** This is a 3D render with a static camera. At frame 12 the astronaut is in the air, descending at the end of hop 1. Over the clip the astronaut moves right and also toward the camera: the ground-contact rows go from 1024 to about 1060, and the rigid backpack grows by 18%.

## Relative depth: backpack length
`backpack.py` and `backpack_len.py` measure L, the length of the backpack (PLSS) left silhouette edge against the sky. It is a rigid vertical length, so it does not depend on which way the body is facing, and L ∝ 1/Z.

- L grows smoothly over frames 0-57: 162.2 (f0), 166.4 (f12), 176.3 (f24), 192.4 (f57).
- From frame 58 on, the readings are unreliable because the pose and the bottom edge change.
- Depth at frame 24: depth_info gives 18.147 m Euclidean, which is Z ≈ 18.12 m along the optical axis.
- Depth at frame 12: Z12 = 18.12 × 176.3/166.4 ≈ 19.2 m. Depth at frame 57: Z57 ≈ 16.6 m.

## Focal length
- The prior is a 2.2 m height. The most upright frames are 76-79, with a bbox height of about 438 px.
- I took Z79 ≈ 16.05 m from the backpack's top-to-bottom extent in frames 57, 64 and 79 (about 202, 205 and 209 px).
- This gives f ≈ 438 × 16.05 / 2.2 ≈ 3200, and I used f ≈ 3220, allowing that walking height is slightly below rest height.
- This is the weakest step, uncertain by about ±5%. The two other cues I tried gave much more scattered values: the neck ring suggests about 3030 and a horizon-at-centre guess about 3390.

## Image velocity at frame 12
- Mask centroid: (10.1, 2.0) px/frame.
- Patches tracked on the waist and hip (`hip_track.py`): 9.5-11.6 px/frame in x and 2.7-3.7 px/frame in y.
- Torso top (backpack top and helmet top): about 3-3.5 px/frame downward.
- I used (10.0-10.1, 3.3) px/frame.

## Depth velocity at frame 12
I used two routes:
- **(a) Local slope of L.** dL ≈ 0.45-0.6 px/frame gives dZ ≈ -0.052 to -0.058 m/frame, and a speed of **2.0-2.14 m/s**.
  - This is probably inflated: L barely changes over frames 0-5 while the image speed is almost constant, which points to a pose or rotation contribution.
- **(b) Ratio of depth change to lateral change, by segment.** Hop 1 (f0-14) gives 0.62, the stance (f14-24) 0.63 and hop 2 (f24-57) 0.51, so the path is close to straight.
  - Using 0.62 at frame 12 gives dX = 0.064, dZ = -0.040 and dY = 0.017 m/frame.
  - The result is |d| = 0.0773 m/frame, so **1.85 m/s**.

## Answer
**1.85 m/s**, from route (b), which also sits between the extremes. Ignoring depth motion entirely would give about 1.5 m/s.

**Confidence: moderate.** The focal length (±5%) and the depth-rate share (±10% on the speed) are the main uncertainties.

- The neck-ring and helmet-circle measures were too noisy to use.
- The upper-body template scale gave values inconsistent with the backpack measure.

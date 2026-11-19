# Q1408: acceleration of the astronaut at t = 0.5 s (m/s^2)

**Answer: 0.55 m/s^2.** This is the magnitude. The scalar speed is decreasing, so the signed value is about -0.55.

## Inputs and time base
- Prior: the astronaut is 2.2 m tall. depth_info: the astronaut is 18.147 m from the camera at t = 1 s (frame 24).
- fps = question_fps = 24, so t = 0.5 s is frame 12.
- At frame 12 the astronaut is in the air and coming down. Contact is at frames 15-16, so frames 0-14 are clean. The root also jumps about 2x in image speed at frame 15, at landing, so no fit crosses frame 14.

## Method
- **Reference point.** The reference point is the pelvis (root).
  - The torso (backpack plus upper body patch, x 705-790, y 665-850 in frame 12) and the near thigh (x 768-832, y 866-914) were each tracked as rigid parts with sub-pixel ECC (`ecc_parts.py`, Euclidean and affine; `ecc_track.py`, affine against frame 12 directly).
  - The hip joint is the point that both rigid motions move identically (`hip_solve.py`). The Euclidean warps put it at about (785, 840) in frame 12, and it is stable across frame subsets. That matches the expected pelvis height, about half of the 360 px standing height below the helmet top at y = 669.
  - The torso rotates about 0.75-0.9 deg per frame, so the chosen point matters. The backpack centre gives 0.3 m/s^2 and a point lower down at y = 885 gives about 1.1 m/s^2.
- **Depth.** The affine scale of the torso patch is flat to within about 0.3% over frames 6-14, and frame 24 is within 0.5% of frame 12. So the motion near frame 12 is essentially in the image plane, and z at frame 12 is about 18.06 m.
- **Scale.**
  - The torso patch at frame 79 is 1.22x larger than at frame 12. The most upright pose, at frame 79, is about 440 px tall, so the standing height at the frame-12 depth is about 360 px. That gives 2.2 / 360 = 0.0061 m/px.
  - Equivalently, f is about 2950 px. Check: ground-contact rows (1023 at frame 17, about 1058 at frame 79) with the 1.22 depth ratio put the horizon at y ≈ 864 and the camera height at about 0.97 m, which is plausible.
- **Hip speed in px/frame,** frames 9-14:
  - Euclidean chain: 10.62, 10.33, 10.12, 9.97, 9.90, 9.94
  - Affine direct: 10.48, 9.99, 9.77, 9.75, 9.42, 9.48
- **Acceleration at frame 12** = (speed(12) - speed(11)) x 24 in m/s, which is Δspeed[px/frame] x 0.0061 x 576.
  - Euclidean: raw -0.15 px/f^2, giving -0.52 m/s^2. Polynomial fits of the track give -0.51 to -0.69.
  - Affine: the raw value is noisy (-0.02). The local linear slope over frames 9-14 is -0.19, giving -0.67, and polynomial fits give -0.74 to -1.0.
- **Second route.** The two different trackers give consistent local slopes of -0.14 to -0.19 px/f^2, which is 0.49-0.67 m/s^2. I chose 0.55.

## Confidence
Low to moderate. This is a small quantity that is sensitive to exactly where the pelvis is and to tracking noise, so the plausible range is about 0.3-1.0 m/s^2.

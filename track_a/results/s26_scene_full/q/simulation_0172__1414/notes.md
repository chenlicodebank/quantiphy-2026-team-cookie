# q1414: astronaut acceleration at t = 3 s (frame 72 at 24 fps; the file is also 24 fps)

**Answer: 1.12 m/s²** (magnitude). The astronaut is slowing down: the change of scalar speed is about -1.1 m/s².

## Scene
- A 3D render with a static camera. The astronaut hops from frame 19 to 58, lands, then walks to the right and slightly toward the camera, slowing down from frame 60 to 79.
- At frame 72 they are in the walking/decelerating phase.

## Scale
- **Prior:** the rest height is 2.2 m.
- **Rest height in pixels at frame 72:** about 440 px.
  - The upright walking bbox is 438 px at frames 76-79.
  - The trunk is 1.5 % larger there than at frame 72.
  - I assumed walking height is about 0.98 of rest height.
  - So the scale is about 0.0050 m/px at the astronaut's depth at frame 72. I tested 432-448 px; this changes the answer by less than 2 %.
- **Depth.**
  - depth_info gives 18.147 m at frame 24.
  - The relative depth comes from the height of the backpack's rear edge (rigid and not affected by yaw; `backpack2.py`, column L14). It grows smoothly from 175 px at f0 to 214 px at f79.
  - Ratio Z24/Z72 = 1.124, so Z72 is about 16.1 m and the focal length about 3230 px (hFOV about 39°).
  - The template-scale cue (`torso_rs.py`) gave a larger ratio, but it is pose-contaminated. Its in-flight values are not linear in time, so I rejected it.
- **3D direction.** During the flight phase (f30-57) the path heads about 29° toward the camera. Near frame 72 the pixels-per-metre along this path (≈197 px/m) is close to the lateral value f/Z (≈200 px/m), so the result is insensitive to this angle.

## Reference point
- The pelvis is not visible as such.
  - **Main proxy:** a pelvis point at (1830, 875) in frame 72, carried through a fine similarity-transform track of the rigid upper body (helmet, backpack and chest; `torso_fine.py`: rotation step 0.5°, scale step 0.005, sub-pixel). This removes the trunk-pitch effect that inflates the raw upper-body deceleration.
  - **Second proxy:** the whole-mask centroid from scene/tracks.
- Each proxy is placed on the 3D straight line and differenced frame by frame (`final.py`).

## Results (m/s², slope of a linear fit to the per-frame speeds, windows ±4 / ±5 / ±6 frames around f72)
| proxy | ±4 | ±5 | ±6 |
|---|---|---|---|
| pelvis p0 | -1.01 | -1.16 | -1.11 |
| pelvis p1 | -0.98 | -1.14 | -1.09 |
| centroid | -0.96 | -1.16 | -1.20 |

- **Pelvis speed** at f72 is about 0.95 m/s; it falls from about 1.4 m/s at f66 to about 0.82 m/s at f79.
- **Raw one-frame values** are noisy: -1.27 for the pelvis proxy and +2.6 for the centroid, where swinging arms jitter the centroid. I used the smoothed trend instead.
- **Upper-body-only template** (not compensated for rotation) gives about -1.5. It is biased because the torso straightens up during these frames.

## Confidence
- Moderate.
- The single-frame value in the reference depends on how the pelvis jitters within the gait cycle, which cannot be recovered exactly.
- The smoothed deceleration is consistent at 1.0-1.2 m/s² across proxies and windows.

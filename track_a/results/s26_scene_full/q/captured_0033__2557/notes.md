# q2557 — ping pong ball velocity at t = 1.5 s (cm/s)

File fps = question_fps = 24, so t = 1.5 s is frame 36. Depth_info is at frame 22 (t = 0.9, 1.457 m) and frame 34 (t = 1.4, 0.738 m).
Lab camera: f = 763 px, principal point (640, 360).

## What happens
The ball rolls toward the camera across the table and reaches the front edge at frame 35. It is falling, motion-blurred, in frames 36–37, is cut by the bottom border at frame 38, and is out of the image from frame 39.

## Measurements
- `measure.py`: masks the ball against the ball-free background (median of frames 41–48) at 3 thresholds. It gives the centroid and the extents along and across the motion.
  - Width across the motion (px), thr 20: f33 41.1, f34 40.1, f35 47.1, f36 58.5, f37 61.4.
- `plane3d.py`: builds the table-top plane from the trapezoid's vanishing point (630, 338). The plane of ball centres is fixed by the given depth at frame 34 (camera ≈ 0.144 m above it). The on-table rolling speed comes out at ≈ 1 m/s toward the camera. This also reproduces the image drift of ~6.6 px/frame downward.

## Depths used for frames 33–37
- **Frame 33:** 0.77 m (mean of the plane value 0.80 and the size value 0.74).
- **Frame 34:** 0.738 m (given). The size gives 0.76, so the 40 mm prior agrees with the given depth here.
- **Frame 35:** 0.675 m (plane 0.70, size 0.65).
- **Frames 36 and 37:** from the size (0.483 and 0.442 m along Z), checked against a free-fall model.
  - The fall starts at about frame 34.5. The vertical drop then gives Z36 ≈ 0.506 and Z37 ≈ 0.458, which matches the size values within 5%.
  - I used Z36 = 0.495 and Z37 = 0.45.

Note: the depth given at t = 0.9 (1.457 m) does not match the ball's apparent size at frame 22 (about 0.8–1.0 m). The depth sensor probably hit the person behind the ball, so I used only the frame-34 depth as the metric anchor.

## Velocity at frame 36
Forward-difference 3D speeds (m/s):

| Step | Speed |
|---|---|
| 33→34 | 0.97 |
| 34→35 | 1.57 |
| 35→36 | 3.68 (large jump in depth between frames 35 and 36, possibly a dropped camera frame) |
| 36→37 | 1.35 |
| 37→38 | ~1.68 (estimated from physics) |

- **Paper convention:** forward difference smoothed over at least 5 frames, centred on frame 36, i.e. the mean of steps 34→35 to 37→38 = 2.07 m/s.
- **Second route:** net displacement (P38 − P34)/4 frames = 1.99 m/s.
- **Instantaneous, without the 35→36 jump:** forward step 36→37 = 1.35 m/s.

Answer: 195 cm/s, the smoothed value, shaded slightly toward the instantaneous value.

## Confidence
Low to moderate. The two plausible readings (smoothed vs instantaneous) are about 1.35 and 2.0 m/s. The depths of the blurred falling ball are uncertain by about 5–10%.

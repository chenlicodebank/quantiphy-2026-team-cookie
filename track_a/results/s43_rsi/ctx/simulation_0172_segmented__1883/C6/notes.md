# q1883: acceleration of the astronaut at t = 0.5 s

- question_fps = file fps = 24, so t = 0.5 s is frame 12.
- Prior: astronaut height is 2.2 m. depth_info: at t = 1 s (f24) the camera distance is 18.147 m.

## Method
- `torso_track.py`: frame-to-frame ECC alignment of the rigid upper body (helmet, backpack, chest). It gives a
  sub-pixel reference point (cc > 0.98). The track is smooth. The image speed changes in steps: about 11 px/frame
  up to f14, then 20 → 33 px/frame from f15, then about 18 from f29. Frame 12 lies inside the first segment, so all
  fits use f4–f14 only and never cross the f14→f15 step.
- Focal length: f = bbox_h(f24) × 18.147 / 2.2 = 380 × 18.147 / 2.2 ≈ 3134 px (horizontal FOV about 40°).
- Depth per frame: Z = f × 2.2 / h, with h a linear fit of bbox_h over f0–14 (about 342 px, so Z12 ≈ 20.1 m). This
  gives an image scale of about 0.0064 m/px at f12. I back-projected to 3D points and took one-frame backward
  differences for speed. The ECC affine scale was too noisy (±5% from torso rotation) to use for depth.
- `accel.py` results (m/s²):
  - Torso point: raw (s12 − s11) × 24 = −0.45; linear fit over f4–14 = −0.49; over f8–14 = −0.35; quadratic slope
    at f12 = −0.40.
  - Torso point with depth held constant: −0.39 to −0.48 (the depth trend barely matters).
  - Second route, mask centroid from scene/: −0.12 (quadratic), −0.27 (f8–14), −0.76 (f4–14). It is noisier but
    has the same sign and size.
  - The scene's pelvis heuristic is too jittery (±3 px) for second differences, so I did not use it.
- Speed at f12 is about 1.74 m/s and slowly falling: the astronaut is decelerating. The answer is the magnitude,
  0.40 m/s².

## Confidence
Low to moderate:
- The height-to-pixel mapping (the walking pose against the 2.2 m height) adds about ±5% to the scale.
- The true origin (pelvis) may oscillate with the gait more than the torso does.
- If the reference keeps the sign, the value is −0.40.
- The camera is assumed fixed; the background is removed, so this cannot be checked.

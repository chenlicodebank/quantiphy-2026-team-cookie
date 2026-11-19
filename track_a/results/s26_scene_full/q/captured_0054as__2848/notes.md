# q_2848: soccer ball velocity at 0.5 s

- question_fps = file fps = 24, so t = 0.5 s is frame 12.
- Frame 12 (checked on a zoomed crop, frames/f12.png): the soccer ball (white with black pentagons, centre about
  (157,608)) is still held under the crouching person's left hand. It is released at about frame 22–23. At 0.5 s it
  is essentially at rest.
- Prior check (measure.py): basketball 3D track with lab intrinsics (f = 763 px, c = (640,360)). Depth comes from the
  apparent diameter and is calibrated to depth_info 2.3557 m at frame 12. Backward difference |p12 − p11|·24 gives
  2.22 m/s, against the prior of 2.21 m/s. Neighbouring frames give about 1.4 m/s. So the reference uses the
  one-frame difference into frame 12, which includes the frame 11→12 jump (likely a dropped capture frame).
- Soccer ball, same convention, depth 3.07 m (white ball depth_info at t = 1.0 s; the ball does not move between
  0.5 s and 1.0 s):
  - Route 1, phase correlation of the ball patch (shift.py): the shift from frame 11 to 12 is (−1.28, +0.12) px,
    which gives 0.124 m/s. Other frame pairs give 0.005–0.08 m/s.
  - Route 2, mask centroid from scene/tracks: the 11→12 shift is 1.06 px, which gives about 0.10 m/s.
- Answer: 0.12 m/s (essentially at rest; the value is the small hand-induced shift between frames 11 and 12).
- Confidence: low in relative terms. The true value is near zero, so the reference's click noise dominates.

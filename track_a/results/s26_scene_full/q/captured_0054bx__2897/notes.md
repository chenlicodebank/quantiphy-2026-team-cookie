# q_2897: speed of the white ball at t = 1.0 s (frame 24, at 24 fps; the file is also 24 fps)

## Identification
- The white ball is the scene record's `white_ball`, the off-white small ball flying with the yellow-green ball
  ("green ball" in depth_info). At f24 it is at about (380, 249) px. It is heavily motion-blurred, and in f22-26 it
  touches the green ball in the image (checked in frames/strip.png and frames/mask24.png).
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Anchor: the white ball is 1.235 m from the camera
  at t = 1.0, which gives Z24 = 1.235 / |ray| ≈ 1.22 m.

## Method (measure.py, fit3d.py, gravity.py)
- Centres come from the record's ref_x/ref_y (re-checked with my own HSV mask centroids, which agree to within
  about 3 px; the difference is the overlap at f23-25). u(k) and v(k) are fitted with cubics over f21-34. That
  window is before the missing-frame jump at f35→36 and the bounce at f38.
- Depth over time: Z ∝ 1/apparent diameter, with 1/d fitted linearly in frame (ballistic flight, so Z is about linear
  in t), scaled to Z24. The diameter is either the width across the blur (minAreaRect) or a stadium-model diameter
  from the area and length. I tried several frame sets (all frames, overlap frames removed, 24-34) and a 0- or 2-px
  soft-edge offset.
- The 3D velocity at f24 is the analytic derivative of ray(u,v)·Z(t). Results range from 2.05 to 2.49 m/s with a
  median of 2.17. The variants judged more reliable (stadium diameter, or overlap frames removed) give 2.05-2.19.
  The depth rate is the main uncertainty: dZ/dt ≈ 1.3-1.5 m/s. Image motion alone (no depth change) would give
  1.76 m/s.

## Second route
- gravity.py tries different depth rates and fits a quadratic 3D trajectory. The horizontal image-x acceleration
  should be about 0 if the camera has no roll, and that happens at dZ/dt ≈ 1.35-1.4 m/s, which gives |v| ≈ 2.10-2.13.
  This agrees with the diameter-based fits.
- The fitted |a| comes out at about 7 m/s² instead of 9.8. Possible causes are camera pitch (gravity partly along Z)
  or irregular frame timing. This adds some uncertainty.
- The orange-ball depth_info (2.24 m at 0.5 s → 1.81 m at 1.0 s) contradicts its shrinking apparent size (77 → 63 px),
  so the prior (2.21 m/s) could not be reproduced cleanly. I did not use it for scale. It is the same order as the answer.

## Answer
2.15 m/s. Confidence: moderate, about ±8%, dominated by the depth-rate estimate.

# q115 — speed of the car at 1.5 s (frame 36, fps 24 = question_fps)

Prior: car acceleration = 4.03 m/s^2. 2D top-down view, static camera (cyclist moves at a constant
27.2 px/frame across the whole clip, so the camera does not pan). One m/px scale comes from the prior.

## Measurement
- track2.py: shift of the car rows (590-860) from one frame to the next, found by SSD, with subpixel parabola
  refinement -> per-frame displacement v(f) in px/frame. This avoids silhouette and perspective effects at the edges.
- Speed rises linearly (constant acceleration) from about frame 0 to about 40: the linear fit over frames 3-30 has
  0.036 px rms error and a slope of 0.888 px/frame^2. After about frame 45 the acceleration changes (it rises to
  about 1.3 px/f^2, then speed levels off at about 63 px/frame from frame 66). So the constant-acceleration phase,
  which contains t = 1.5 s, is the one the prior describes.
- Scale = 4.03 / (0.888*24^2) = 0.00788 m/px. Check: car length 726 px = 5.72 m, which matches a Cybertruck
  (5.68 m).
- v(36) = 31.73 px/frame measured (31.6 from the fit) -> 31.73*24*0.00788 = 5.99 m/s (fit 5.97).

## Second route
Subpixel front-edge track (measure.py, answer.py): a = 0.878-0.886 px/f^2 and speed36 = 5.92-5.98 m/s.
Across all fit windows and both methods the result is 5.92-6.00 m/s. Also, motion starts at about t = 0, so
4.03*(35.5/24) = 5.96.

Answer: 5.97 m/s. Confidence: high (about 1-2 %), assuming the prior is the constant acceleration of the early phase.
If the prior were instead the average acceleration over the whole clip (0.957 px/f^2), the answer would be
about 5.56 m/s. I consider that less likely.

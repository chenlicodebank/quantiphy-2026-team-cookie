# q_236 — length of the football (m)

The prior is gravity = 9.8 m/s². The scene is a 2D render with a static camera, and the football falls from rest near x ≈ 1036 px. The file runs at 24.006 fps; question_fps is 24.0, and I used 24.0 for all timing (the difference is negligible).

## Scale (fit.py)
- I fit a quadratic to the per-frame track (`scene/tracks/football.csv`, frame column, frame 17 outlier excluded):
  - centroid: a = 1798.9 to 1799.7 px/s² across different start frames (0, 1, 2, 5); residual rms 0.43 px; v0 ≈ 0, so it falls from rest.
  - bbox centre: 1795 to 1800 px/s².
- Scale = 9.8 / 1799 = 0.005447 m/px.
- Sanity check: the doors (342 x 155 px) come out at 1.86 x 0.84 m, which is realistic, so the scene is at about real scale.

## Ball length in pixels (size.py, look.py)
- Minimum-area-rectangle long side of the mask on the sharp, slow frames 0 to 3: 63.0, 63.9, 63.0 and 63.0 px. While the ball tumbles the long side ranges from 57 to 65 px; the maximum (≈63-64 px at frames 0-1 and 31) is when the long axis lies in the image plane. The short side is about 39 px.
- Hand check on raw pixel profiles, frame 0, column x = 1036: the top edge is at y ≈ 195.5 (the white stripe starts at 196). The bottom is dark brown down to y ≈ 257.5, then the blue shadow begins. That gives ≈ 62 px; the anti-aliased edges and the bottom-tip shading allow 62 to 64 px.
- The stripes look curved early in the fall and almost straight near the image centre (frame 20). So the curvature comes mostly from perspective, not from the ball being strongly tilted out of the image plane.
- Proportion check: the ratio of 63 / 39 = 1.62 matches a real football (28 / 17 cm = 1.65), so the long axis is not foreshortened.
- I used L = 63 px.

## Answer
L = 63 x 0.005447 = **0.343 m** (likely range 0.338 to 0.349).
- This is about 22 % larger than a regulation NFL ball (0.28 m), which is within the 40 % plausibility limit. Per the 2D convention the scale comes from the prior, which is consistent with the realistic door sizes.
- Confidence: moderate to high. The scale is solid (±0.3 %); the pixel length is uncertain by about ±1.5 px (±2.5 %).

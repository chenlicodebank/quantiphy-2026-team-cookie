# q_2782 – distance yoga ball ↔ person at t = 1.5 s

The video file and the question both run at 24 fps, so t = 1.5 s is frame 36.

The depth_info line for t = 1.5 s says "soccer_ball". The clip has only one ball, the exercise (yoga) ball, so I treat this as the yoga-ball depth: 1.4972 m.
This is consistent with the ball's size. The depth at t = 1.0 s (2.4985 m) and the diameter at frame 24 (149.5 px) predict 1.476 m at frame 36 from its fitted diameter of 253 px. That is 1.4 % off the given value.

## Measurements (fit.py)
- At frame 36 the ball is cut off by the bottom edge of the image. I fitted a circle to its outline, leaving out the image-edge rows.
  - Result: centre (360.9, 670.3), diameter 253 px.
  - The record's track has (367.7, 659.8) with diameter 233.6, which is wrong for this frame. The visible width alone is already 253 px.
- Person: the mask centroid is (585.2, 442.7). The person is squatting and does not move.
  - Using the bbox centre (570, 445.5) instead changes the answer by only −0.008 m.

## Camera and back-projection
- Focal length f = 0.5959 × 1280 = 762.75 px; principal point (640, 360).
- Each 3D point = ((u − cx)/f, (v − cy)/f, 1) × depth, as in the method card.
- Ball: (−0.548, 0.609, 1.497) m. Person: (−0.275, 0.415, 3.830) m.
- Distance between them: **2.357 m**.

## Alternative reading
If depth_info is the Euclidean distance (normalised ray) rather than the depth along the optical axis, the result is 2.496 m.

## Check against the prior (vel.py)
- I computed the ball velocity at t = 1.0 s from the tracked centres, with depth taken as proportional to 1/diameter and anchored at 2.4985 m.
- Smoothed over 5 frames: 2.14 m/s with depth along the optical axis, 2.24 m/s with the Euclidean reading. The prior is 2.1464 m/s.
- This favours the optical-axis reading, but the per-frame speeds are noisy.

Confidence: moderate-high; within ~5 % if the depth along the optical axis is the convention used.

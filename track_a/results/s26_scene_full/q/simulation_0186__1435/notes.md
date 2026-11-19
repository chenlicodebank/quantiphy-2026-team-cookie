# Q1435: speed of the gift box at t = 1 s (frame 24 at question_fps 24; the file is also 24 fps)

Prior: the box's sliding acceleration after 1 s is 3.18 m/s² (constant along the ramp). Depth: 9.859 m at frame 0 and 9.741 m at frame 12.
Track: scene/tracks/gift_box.csv body_cx/cy. It was checked against the record: the box falls freely over frames 0-8, lands at frames 8-9, and slides along the ramp over frames 9-39.
Speed at frame 24 is the backward difference, i.e. the speed at frame 23.5 for constant acceleration.

## Route 1 (fit3d.py): 3D reconstruction with depth from apparent size
Z(t) ∝ 1/sqrt(body_area), smoothed and anchored to 9.741 m at frame 12. The positions are back-projected with focal f, and a quadratic is fitted for path length along the 3D line.
- The ratio speed/acceleration hardly depends on f: v24 = 3.18 × v/a = 3.08-3.13 for f between 1200 and 3500.
- The reconstructed acceleration equals 3.18 when f ≈ 2200 px, which gives v24 ≈ 3.10.
- A plain 2D pixel ratio (no depth component) gives 2.6-2.9. It is biased because the box moves noticeably toward the camera: its area grows by 25%.

## Route 2 (fitproj.py): image positions only
I fitted a 3D straight line with constant acceleration a = 3.18 and distance 9.741 m at frame 12 to the pixel track, with f free. Across 4 frame windows this gave f = 2185-2205 px, an RMS error of 0.14-0.24 px, and v24 = 3.11-3.14 m/s.
Fixing f at 2000 or 2600 makes the RMS error clearly worse (0.4-1.6 px).

## Independent check on f
The free-fall pixel acceleration is 3.7 px/frame² = 2131 px/s². With g = 9.81 m/s² at about 9.8 m, that gives f ≈ 2130 px, which agrees with 2200.

Answer: 3.11 m/s. Confidence: good (about ±3%).

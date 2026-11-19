# q_2629: basketball velocity at 1.6 s (cm/s)

- Time: 1.6 s × 24 fps (question_fps; the file is also 24 fps) gives frame 38. The basketball is rolling freely to the left after the collision at frames 19-20.
- depth_info: the 4th line is labelled "soccer_ball" at t = 1.6 s with 2.412 m. The soccer ball already has 3.052 m at 1.6 s, so the 4th line must be the basketball.
  Check: the ball's diameter is 69.4 px at f38 and 74.2 px at f14. The ratio 1.069 matches the depth ratio 2.412/2.270 = 1.063.
- Camera: f = 0.5959 × 1280 = 762.75 px, principal point (640, 360).
- Measurement (measure.py): orange HSV mask, centroid per frame for frames 30-48. It agrees with scene/tracks/basketball.csv to within about 1 px.
  The dark lower patch is partly left out of the mask (frames/f38.png). This offset is the same in every frame, so it does not affect velocity.
- I back-projected the centroids at depth 2.412 m. I used a constant depth near f38 because the ball's apparent diameter is flat (~69-70 px) after frame 17.
  Per-frame speeds for 36→41: 0.378, 0.355, 0.358, 0.352, 0.337 m/s. Mean 0.356; net 36→41 / 5 = 0.356; centred 37→39 = 0.356.
  The window avoids the dropped frame at 35→36.
- Depth-rate correction: the 0.142 m depth change over 61 px of image y between f14 and f38, at -1 px/frame in y, gives about 0.045 m/s along the line of sight.
  The slight diameter trend agrees. Adding it in quadrature gives sqrt(0.356² + 0.045²) ≈ 0.358 m/s.
  Using a depth estimated from each frame's size is too noisy (the diameter jitters by ±0.7 px), so I did not use it.
- Second route: a forward window 38→43 gives 0.337 m/s; the ball is slowly decelerating.
- Answer: 35.8 cm/s. Confidence: good (about ±5%).

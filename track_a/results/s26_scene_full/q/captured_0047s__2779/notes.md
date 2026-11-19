# q_2779: distance from the yoga ball to the person at 1.5 s

- Lab video, 24 fps (the file and question_fps agree), so t = 1.5 s is frame 36. f = 0.5959 x 1280 = 762.75 px, principal point (640, 360).
- depth_info: the 1.5 s entry is labelled "soccer_ball", but the only ball in the video is the yoga ball, so I treat 1.4972 m as the yoga ball's depth at frame 36. The person is at 3.83 m.
- Ball centre at frame 36 (`dist.py`): the cone-fit centre from scene/tracks is (370, 674) and the ellipse centre is (362, 683). On the frame, the visible ball spans x 228-483 with its top at y 543, so its visual centre is about (356, 676).
- Person centre at frame 36: the mask centroid is (584.6, 438.9) and the bbox centre is (570, 445.5). The person is crouched with their feet fixed.
- Each point is back-projected along its unit ray times the given depth, and the distance is taken in 3D. Across the combinations of ball and person centre, the result ranges from 2.480 to 2.505 m. **Answer: 2.49 m.**
- Check: from the ball's angular size the radius is 0.241 m (scaled from the depth at 1.0 s), and the speed near frame 24 comes out at about 1.8-2.0 m/s. The prior is 2.15 m/s, which is roughly consistent. That size-based route puts the ball at about 1.75 m depth at frame 36 rather than the given 1.497 m; using it would give about 2.27 m. I follow the given depth, which is what the reference convention uses.
- Confidence: moderate to high. The result is driven mostly by the difference between the given depths.

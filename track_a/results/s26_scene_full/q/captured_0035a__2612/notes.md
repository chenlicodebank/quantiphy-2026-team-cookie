# Q2612 – soccer ball velocity at 0.6 s (cm/s)

File fps = question_fps = 24, so t = 0.6 s is frame round(14.4) = 14.

Method (measure.py):
- f = 0.5959 x 1280 = 762.8 px, principal point (640,360). Ball centres come from scene/tracks (RANSAC circle fits, ±1.5 px).
- The depth_info gives soccer-ball distances at frames 14 (2.758 m) and 38 (3.052 m). The second "soccer" entry at 1.6 s
  (2.412 m) is the basketball: it gives a basketball diameter of 2.412 x 71.5 / 763 = 22.6 cm, which matches the
  23.2 cm prior. The basketball at 0.6 s also gives 22.1 cm, so the scale checks out.
- To get the soccer ball's depth in every frame, I took the plane of ball-centre motion: its normal is the cross
  product of the soccer and basketball 3D displacement directions (frames 14 to 38), and it passes through the two
  given soccer points. I then intersected each frame's ray with that plane. The basketball centres sit 5 cm off the
  soccer plane, against an expected ~3.6 cm (the radius difference), so the plane is consistent with the
  basketball too. The resulting depth goes from 2.86 m (frame 12) to 2.63 m (frame 17).
- Speed = forward differences of the 3D centres, averaged over 5 frames around frame 14 (frames 12 to 17): 181 cm/s.
  Other windows: 13–16 gives 182, 12–16 gives 187, 12–18 gives 191 and 14–19 gives 195. The collision is at frame 19/20.
- Frames 11 to 12 look like a dropped frame (both balls make a jump of 1.7x their normal step), so I left them out.
  If they are included, the speed rises to about 228.
- Second route: holding the depth fixed at 2.758 m gives 146 cm/s. That is too low because it ignores the ball
  moving toward the camera, which is why I used the plane model.

Answer: 185 cm/s, the middle of the 181–191 range from the windows before the collision. Confidence: moderate, about ±8%.

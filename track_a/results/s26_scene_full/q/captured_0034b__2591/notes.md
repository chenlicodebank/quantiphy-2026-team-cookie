# q_2591: velocity of the left tennis ball at t = 1.2 s (cm/s)

- t = 1.2 s at question_fps 24 -> frame 29 (the file is also 24 fps). The ball was released at frames 24-25 and rolls right, decelerating. It is unoccluded at frames 28-31.
- Centres: scene/tracks/ball_left.csv (circle fit), re-measured in `measure.py` (HSV mask centroid and bbox centre). The two agree within about 0.5 px at frames 27-32.
  Track x: 497.43 (f27), 510.11, 522.59, 534.08, 544.02, 554.41 (f32); y stays at about 280 (so motion is mostly sideways and the depth hardly changes).
- Lab method card: f = 0.5959 x 1280 = 762.8 px, Z = 0.706 m (depth_info for the left ball at 1.2 s). The scale is Z/f = 0.0926 cm/px.
- Velocity is the forward difference smoothed over 5 frames, (p32 - p27)/5 = 11.40 px/frame, which gives 25.3 cm/s.
  Second route, centred differences from my own mask: 27->31 gives 11.76 px/fr (26.1 cm/s), 28->30 gives 12.0 (26.7), 29->30 gives 11.5-12.0 (25.5-26.7), 29->32 gives 10.6-11.0 (23.6-24.4).
- Answer: 25.5 cm/s.
- Caveat: the measured depths do not match the pixel sizes when f = 763 is used. A 6.7 cm ball spans about 28.7 px, which implies Z of about 1.78 m, not 0.706 m. The soccer ball is similar: 91 px at 0.894 m gives 10.7 cm. Using the prior-diameter scale instead (6.7/28.7 cm/px) would give about 64 cm/s. I followed the stated reference convention (back-projection with the measured depth and f = 763).
  Confidence: moderate. The main risk is which scale convention the reference used.

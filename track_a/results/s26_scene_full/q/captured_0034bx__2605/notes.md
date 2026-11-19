# q 2605: velocity of the left tennis ball at 1.2 s (cm/s)

- Left tennis ball = scene track `tennis_ball_A` (starts at x≈467, rolls right after the push at frame 24).
- Time: question_fps = file fps = 24, so t = 1.2 s is frame 29. In frames 25–30 the ball is fully visible. It starts to pass behind the soccer ball at frame 31, where only a small part is hidden and x is still good.
- I checked the track at frame 29 on a zoomed crop (frames/f29.png). The ball centre is at about (522, 280), which matches the track's (522.1, 279.6).
- Scale (lab card): f = 0.5959·1280 = 762.8 px, principal point (640, 360), depth of A at 1.2 s = 0.706 m (depth_info).
  Back-projection: P = unit ray × depth.
- Velocity follows the reference convention: forward difference of the 3D centres, smoothed over 5 frames (`vel.py`).
  - Constant depth 0.706: mean of forward speeds 27..31 = 24.7; (p31−p27)/4 = 25.0; (p32−p27)/5 = 24.6; linear fit over 27–31 = 25.0; central difference at 29 = 25.1 cm/s.
  - Depth varying along the plane of ball centres (from the table vanishing point, or from the A and B depths): the depth changes by less than 0.5 cm across the window, and the speeds come out within ±0.2 cm/s of the above (24.7–25.2).
- Second route (`check.py`): my own saturated-yellow mask with the midpoint of its extent: (p31−p27)/4 → 11.27 px/frame → 25.0 cm/s; central difference over 28–30 → 25.6 cm/s.
- The ball is slowing slowly: forward speeds are 26.6, 25.7, 24.5 and 23.5 cm/s at frames 27–30.
- Answer: **25.0 cm/s**. Confidence is high, about ±1 cm/s. The prior (6.7 cm diameter, about 31 px at 0.706 m, which predicts 6.9 cm) agrees with the scale.

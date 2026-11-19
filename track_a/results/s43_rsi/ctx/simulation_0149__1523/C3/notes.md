# q_1523: acceleration of the car at t=0.5 s (frame 12, question_fps = file fps = 24)

Method
- Tracked the near front tyre rim (white face) in code (rim3/4/5.py: relative-brightness threshold, connected component). Rim centre v sits on the horizon (y~830), so the camera is at hub height. Rim height h = depth cue (h0=88 px at frame 0, 122 at frame 20).
- Scale: depth_info gives range 14.244 m to the right front tyre at frame 0. Tyre/rim ratio about 1.52, measured from the frame-0 and frame-29 tyre contacts (0.764 m tyre -> rim 0.50 m). f is about 2330 px (about 44 deg HFOV), from the range at frame 0, h0 and the horizon-to-ground-contact geometry. f barely changes the answer (2200-2450 changes it by about 1%).
- Z(t) = Z0*h0/h(t), X = (u-cx)Z/f, Y = (v-cy)Z/f. The hub moves on a straight line in 3D (perpendicular rms about 1.5 cm over frames 0-20), so there is no yaw during frames 0-24 and the hub speed equals the origin speed.
- Fit s(t) along the line with polynomials over several windows; acceleration = (speed(12) - speed(11))*24. Speed at frame 12 is about 6.5 m/s.
- Constant-acceleration fit over frames 0-17 / 0-21 / 0-25 gives 12.4 / 11.1 / 9.8 m/s^2. Polynomial fits over frames 0-24 give 9.8-10.6. Narrow windows (6-18) are noisy (5-8).

Answer: about 10.2 m/s^2. Confidence: moderate (about 10-15 % uncertainty).

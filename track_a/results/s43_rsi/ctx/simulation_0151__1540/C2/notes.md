# q_1540: acceleration of blue car (cart) at t=1 s (frame 24)

File fps = question fps = 24.
Scale: yellow tyre 184 px = 0.764 m, tyre hub at frame 12 off-centre, depth_info 11.38 m (Euclidean) -> f ~ 2640 px (hfov ~40 deg), Z_yellow ~ 10.95 m.
Camera height 1.43 m from ground-contact row (884) vs horizon (539); cart contact row 817 -> Z_cart ~ 13.6 m.
Cart tyre = 2638*0.369/13.57 = 71.7 px (checked visually: ~68-72 px) -> 0.00515 m/px at the cart's side plane.
Motion is parallel to the image plane, so side-plane displacement = origin displacement.
Cart track (scene/tracks/cart.csv ref_x, frames 10-36 re-checked) is noisy frame to frame (+-1-2 px), so a single backward
difference is unreliable. Polynomial (deg 2/3) fits over several windows: speed at frame 24 ~3.9 m/s, accel 0.9-1.4 m/s^2
(speed plateaus ~33 px/frame after frame ~26). Answer 1.2 m/s^2. Confidence moderate (~+-30%).

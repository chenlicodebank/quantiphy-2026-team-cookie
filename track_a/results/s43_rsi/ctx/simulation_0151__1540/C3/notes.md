# q_1540: acceleration of the blue car (light-blue cart) at t=1 s (frame 24)
- File fps = question_fps = 24.
- Scale: cart tire diameter 0.369 m = ~74.5 px (dark tire extents on frame 36: front 754-830 wide, y 744-818; rear 980-1054). Scale 0.004953 m/px in the cart's side plane (same plane as the tracked roof features).
  - Cross-check: yellow tire ~190 px for 0.764 m with the 11.38 m depth gives f ~2730 px (HFOV ~39 deg) and camera height ~1.4 m. The ground-row ratio then predicts a cart tire of ~73-74 px, which agrees.
- Motion: cart ref_x track (scene/tracks/cart.csv) is noisy by +-2 px per frame. Step per frame is ~30 px at frame 20 and ~33 px at frame 28; speed at frame 24 ~3.8 m/s.
- Acceleration from polynomial fits of position or linear fits of step over windows of 8-20 frames around frame 24: 0.9-1.3 m/s^2, centre ~1.15. The raw backward difference (1.0 m/s^2 jitter) is too noisy to use directly.
- Answer 1.15 m/s^2. Confidence moderate (~15%).

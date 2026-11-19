# q_1480 – whale displacement 0.5 s → 1.0 s (frames 12 → 24 at question_fps 24 = file fps)

Prior: whale speed = 1.67 m/s. Depths: 33.7307 m at t=1 s (f24), 35.1624 m at t=2 s (f48).

Method (solve.py): I used the head template track from scene/tracks/whale_head.csv as the body's translation point,
because it is smooth and rigid and moves in steady steps of about 2.2–3.7 px/frame. I back-projected it with a pinhole
camera (principal point at the image centre). I solved for the focal length so that the 3D distance between f24 and f48
equals 1.67 m (1 s at the prior speed): f ≈ 2650 px (HFOV ≈ 52°).
- Check: under constant 3D velocity, the predicted pixel position at f12 is (1108.8, 476.7); the measured
  position is (1109.3, 478.5), which agrees. Per-frame speeds under a linear depth model are 1.65–1.78 m/s, roughly constant.
- Route 1 (constant velocity, prior speed): 1.67 × 0.5 s = 0.835 m.
- Route 2 (f12 point back-projected at the depth projected from the extrapolated line): 0.845 m.

Answer: 0.835 m. Confidence high (both routes agree within about 1%).

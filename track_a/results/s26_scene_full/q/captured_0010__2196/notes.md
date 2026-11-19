# q2196 – ball (pendulum bob) acceleration at t = 0.6 s (frame 14, question_fps = file fps = 24)

Scene: an orange ball on a string held by a standing person swings as a pendulum, mostly toward and away from the
camera. Lab camera: f = 0.5959 x 1280 = 762.75 px, principal point (640, 360). The prior (g = 9.8) is used as the
gravity value in the physics route.

Checked the scene/ ball track (mask centroid and equivalent diameter) on frames 3 and 14. It is the right object and
the track is good. Frame 14 is 3 frames (0.125 s) before the near turning point (f17: image x and y are both
stationary there). The far turning points are at f3 and f32.5. The period is about 1.20–1.23 s.

Depth scale: d x D_px at the 6 given times = 47.3, 49.7, 52.1, 47.6, 49.6, 47.9 (mean 49.0, ±3.4%). The ball's
true size is therefore about 0.064 m. From this, the far turning point is at about 1.78–1.81 m and the near one at
about 1.31–1.35 m. The 3D chord between the turning points is about 0.48–0.51 m.

Routes:
1. `harmfit.py`: 3D centres = back-projected rays x size-based depth. Each coordinate is fitted with a shared ω,
   using the fundamental plus the 2nd harmonic, and the acceleration magnitude is taken analytically at f14.
   With constant K: 5.74 m/s² (T = 1.195 s). With K interpolated between the given frames: 7.57 m/s² (T = 1.216 s).
2. `physics.py`: a nonlinear pendulum (g = 9.8). L and θ0 are solved from the chord (2L sin θ0) and the period,
   then integrated 0.125 s back from the near turning point to get |a| = sqrt((g sinθ)² + (Lω²)²). With the most
   likely values (d_far ≈ 1.80, d_near ≈ 1.32–1.33, T ≈ 1.215) this gives L ≈ 0.33–0.34 m, θ0 ≈ 48–50° and
   a ≈ 6.4–6.9 m/s². Across the full plausible range it gives 5.7–7.7.
   The fitted L agrees with the fixed-pivot fit in `fit3d.py` (L = 0.328 m).
   Raw frame-by-frame second differences (`fit3d.py`) are too noisy to use, because the depth noise is about 3%.

Answer: 6.6 m/s² (the full vector acceleration magnitude: tangential about 6.2 plus centripetal). Confidence
moderate (±15%). The answer is very sensitive to the swing amplitude, which comes from the depth of the turning
points.

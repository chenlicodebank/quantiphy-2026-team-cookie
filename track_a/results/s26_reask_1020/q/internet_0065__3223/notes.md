# Q3223 – ball velocity at 0.40 s (frame 12 at 30 fps; the file is also 30 fps)

- The scene is a top-down handheld view of a basketball rolling left to right across a gym floor at nearly constant pixel speed.
  There is no fall or bounce, so the prior (g = 9.8 m/s²) describes a motion the clip never shows and gives no usable scale.
- **Scale:** I took it from a regulation basketball (size 7, diameter ≈ 0.24 m). The ball's diameter in pixels, taken as its
  vertical extent (across the motion, so free of blur), is 255 px at frame 12. I checked this on a zoomed crop: y ≈ 285–540.
  The median over frames 5–21 is 258. Scale = 0.24 / 255 = 9.41e-4 m/px.
- **Track:** I used the stabilised centre (`cx_est_stab`, `cy_est_stab`) from scene/tracks/basketball.csv. The camera drift is
  small (≈0.3 px/frame in x). Per-frame steps over frames 5–21 are 94–103 px, with no trend, so the speed is constant within
  noise.
  - Forward difference 12→13: 94.8 px/frame → 2.68 m/s.
  - Central difference over frames 10–14: 98.3 px/frame → 2.77 m/s.
  - Linear fit over frames 5–21: 98.0 px/frame → 2.77 m/s.
- **Answer:** 2.77 m/s, the smoothed value. The single forward step is noisier, at ±3–4 px per frame.
- **Confidence:** medium. The scale rests on the assumed 0.24 m ball diameter. If it is a smaller ball (size 6, 0.23 m), the
  answer would be about 4% lower.

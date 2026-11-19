# q_2478 – distance travelled by ping pong ball, 1.1 s -> 1.3 s (cm)

- question_fps = file fps = 24. t=1.1 -> frame 26 (bounce, blurred streak 390-420 px), t=1.3 -> frame 31 (near apex).
- Track: scene/tracks/ball.csv centre (checked visually on frames 24-33, frames/seq.png; streak midpoints / ball centres OK).
  f26 (738.5, 405.0), f31 (748.5, 303.5).
- Camera: f = 0.5959*1280 = 762.8 px, pp (640,360). Back-projection: unit ray x Euclidean depth_info.
  Depths: f26 1.557 m, f31 1.4115 m (given); intermediate frames linearly interpolated.
- Path length (sum of per-frame 3D steps, frames 26..31): 25.0 cm.
- Check: straight 3D displacement 26->31 = 24.4 cm (motion is nearly straight upward + toward camera, so path ≈ displacement).
  Image-plane only (no depth change) = 19.7 cm; the 14.5 cm depth decrease dominates the difference.
- Caveat: apparent-width depths (f*0.04/w) give ~1.80 m at f26, disagreeing with given 1.557 m; given depth_info used, as instructed.
- Answer 25.0 cm; confidence moderate (depends on reference per-frame depths).

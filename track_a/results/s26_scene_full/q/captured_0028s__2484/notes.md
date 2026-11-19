# q2484 – ping pong ball distance travelled 1.1 s → 1.3 s (cm)

- question_fps = file fps = 24. t=1.1 → frame 26 (bounce 1, ball just at table), t=1.3 → frame 31 (near apex, f32).
- Track: scene/tracks/ball.csv mask centroids, checked visually on 3x crops f24–33 (frames/crops.png, crops.py):
  masks cover the (motion-blurred) ball, centres sit in the middle of the blur streak.
- Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Depth: depth_info 1.557 m at f26, 1.4115 m at f31; linearly interpolated per frame in between.
  Each centre back-projected as unit ray × depth (Euclidean distance).
- Path length = sum of frame-to-frame 3D displacements f26→31 (measure.py):
  - mask centroid: steps 4.65, 7.04, 5.53, 4.65, 3.58 cm → **25.45 cm** (net displacement 24.95)
  - bbox centre (second route): **25.14 cm** (net 24.71)
- Scale check: ball width 22 px at f31/f32 with depth 1.4115 m → 4.07 cm vs prior 4.0 cm (1.7 % off): consistent.
- Answer 25.3 cm (mean of the two routes). The motion is a single monotonic rise after the bounce, so path ≈
  displacement; ~0.1 m of it is approach toward the camera from the depth change.
- Confidence: moderate-high (±5 %); main uncertainty is blur in f26–29 and the depth interpolation.

# q_2154 — displacement of the toy between t=1.0 s and t=1.2 s (cm)

- question_fps = file fps = 24. t=1.0 → frame 24; t=1.2 → frame round(28.8) = 29.
- Toy centres (scene/tracks/toy.csv, checked visually on zoomed crops frames/f24.png, frames/f29.png):
  f24 (604.6, 141.2) sharp; f29 (576.7, 228.1) motion-blurred, centre of the blur streak agrees with crop.
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Back-projection with depth_info as Euclidean camera distance to the centre (1.402 m, 1.065 m):
  P24 = (-0.062, -0.386, 1.346) m, P29 = (-0.087, -0.181, 1.046) m → |ΔP| = 36.5 cm.
- Checks: yellow-only centroid gives 36.4 cm; treating depth as Z gives 40.2 cm (not the stated
  convention); using frame 28 instead of 29 gives 34.6 cm. Apparent size grows 50→71 px
  (ratio 1.41, blur-inflated) vs depth ratio 1.32 — consistent approach toward the camera.
- The prior (g = 9.8 m/s²) is not needed for the scale; depth_info sets it.
- Answer: 36.5 cm. Confidence: moderate-good (blur at f29 adds ~±1 cm).

# q441 – acceleration of the box (crate) 0–0.3 s

2D scene, 24 fps (file fps = question_fps, no re-timing). The box is released from rest at frame 0 and falls freely until frame 7 (0.29 s); first ramp contact at 7→8, so 0–0.3 s is pure free fall.

Scale from prior: the tool box (same crate) has acceleration 1.58 m/s² at 1.25 s (frame 30), during its steady slide down the ramp (frames 22–44).
- Slide pixel acceleration = linear fit of per-frame speed (scene/tracks/crate.csv, backward difference ×24): 390 (fr 22–44), 400 (25–35), 389 (27–33), 408 (24–36), 405 (26–44) px/s² → ~397 px/s².
- Scale = 1.58 / 397 ≈ 0.00398 m/px.

Free-fall pixel acceleration:
- Track route: speed fit over frames 1–7 = 2492 px/s² (steps 2.4, 6.7, 11.1, 15.5, 19.6, 24.0, 28.4 px; ~4.33 px/frame²).
- Independent route (measure.py): top edge of crate from colour difference vs wall, frames 0–8: 237, 240, 246, 257, 273, 292, 316, 344 → steps ~3, 6, 11, 16, 19, 24, 28 px, same ~4.3 px/frame² ≈ 2490 px/s².

Answer = 2490 × 0.00398 ≈ 9.9 m/s² (range 9.6–10.4 from the slide-fit window choice); consistent with g = 9.8 m/s², a good sanity check. Confidence: high (within ~3%).

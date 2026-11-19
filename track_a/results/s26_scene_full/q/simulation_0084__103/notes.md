# Q103: width of the yellow car (m)

The scene is 2D and seen top-down at 24 fps. The file rate equals question_fps, so no re-timing is involved. The scale comes from the prior, speed = 5.07 m/s.

- **Pixel speed** (`speed.py`): I fitted lines to the bounding-box edges in tracks/yellow_car.csv.
  - Front bumper, frames 2–71: −9.835 px/frame.
  - Rear, frames 12–71: −9.974 px/frame.
  - Mean: 9.90 px/frame = 237.6 px/s. This matches the record (cx mean −9.90).
- **Scale:** 5.07 / 237.6 = 0.02134 m/px.
- **Width** (`measure.py`): I read the per-column y extents of the car mask at frames 24, 36 and 48. All three gave the same values:
  - Mirror to mirror (y 468–583): 116 px.
  - Widest body at the wheel arches, without mirrors: 100 px. Most of the body is 94 px.
- **Answer:** the world AABB includes the mirrors, so 116 × 0.02134 = **2.475 m**.
  - Body without mirrors: 100 px → 2.13 m (alternative reading).
- **Check:** the speed from the front edge alone and from the rear edge alone gives a width of 2.45–2.49 m. The length is 272 px → 5.8 m, so length/width ≈ 2.3 with mirrors, which is plausible.
- **Confidence:** moderate. The main uncertainty is whether the reference width includes the mirrors.

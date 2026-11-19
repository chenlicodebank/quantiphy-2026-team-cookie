# q_3089: distance between the kettle and the plate (cm)

- The "plate" is the white wavy bowl/dish at the left; the kettle is the red T-fal kettle. Both are static, so the
  distance is the same in every frame (checked on frame 44, which has a 100 px grid).
- Time base: 30 fps (file 30.013, question 30.0, a negligible difference).
- **Scale from the prior (107.3 cm/s cylinder velocity).** `speed.py` reads the cylinder track (stabilised centroid, frames
  4-30, where the cylinder is fully visible):
  - a linear fit gives vx = -59.35 px/frame and vy = 4.65, so the speed is **1786 px/s**;
  - the leading edge (bbox_x0) gives a second route of 1723 px/s.
  - The per-frame speed ranges from 50 to 78 px/frame (perspective: the cylinder rolls toward the camera), so the
    clip average is used.
  - Scale = 107.3 / 1786 = 0.0601 cm/px.
- **Pixel distance** (frame 44, from scene/static_objects.json, checked against the gridded frame):
  - bowl centre x = 368;
  - kettle bbox centre x = 1372 with the handle, about 1324 for the body only, so the kettle "centre" is about 1355;
  - both bases sit on the same line (y about 714-727), so the distance is horizontal: about 987 px.
- **Answer:** 987 x 0.0601 = **59.3 cm** (centre to centre).
- Other readings and cross-checks:
  - The edge-to-edge gap (kettle left x 1168 minus bowl right x 580 = 588 px) would be 35.3 cm.
  - Using the leading-edge speed gives 61.5 cm instead.
  - Sanity check: the bowl comes out about 25.5 cm wide, the kettle about 24.6 cm with its handle, and the
    cylinder's diameter about 11 cm. All are plausible.
- Confidence: moderate. The main uncertainties are which speed the annotators used, and centre-to-centre versus gap.

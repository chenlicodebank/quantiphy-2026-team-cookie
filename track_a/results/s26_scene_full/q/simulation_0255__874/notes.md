# Q874 – acceleration of the tennis ball at t = 0.5 s (frame 12)

The prior says the tennis ball's diameter is 0.17 m. There is no depth_info, and fps = question_fps = 24, so I used 24 fps everywhere.

## Scene
The video is a 2D-style render. A single ball rolls right along the floor at a constant image row (y ≈ 563), so it moves parallel to the image plane. The camera is static. There is no bounce or occlusion, and the ball slows down steadily over all 41 frames. I treated it as planar and used one m/px scale.

## Measurements (scripts in this folder)
- `measure.py`: tracks the ball with two masks, a background-difference (median) mask weighted by intensity and a chroma mask (G−B). It also measures the FWHM height and width through the ball centre on frames 16–24.
- `accel.py`: fits a quadratic to x(frame) over several frame windows for three tracks (mine and the scene record).
  - Background-difference centroid (rms 0.07–0.13 px): a = −0.2670 (frames 0–40), −0.2711 (0–24), −0.2676 (4–20), −0.2677 (6–18), −0.2657 (16–40) px/frame².
  - A linear fit of the per-frame dx gives −0.268. A cubic fit gives a(12) = −0.270, so the deceleration is very close to uniform.
  - The chroma track and the scene-record track agree, at −0.266 to −0.270.
  - Adopted: a = 0.268 px/frame² = 0.268 × 24² = 154.4 px/s².
- Diameter in pixels, measured near the image centre (frames 10–30):
  - `radial.py`: half-contrast edge points over the upper half and sides (which avoids the contact shadow), with a circle fit, give 23.5 px (median; range 22.9–24.1).
  - The vertical FWHM of the difference profile gives 24.0 px.
  - The chroma-mask equivalent diameter is about 25 px, which includes the soft edge.
  - The scene record estimated 24.5 px.
  - Adopted: 23.8 px.
- Scale: 0.17 / 23.8 = 7.14e-3 m/px.

## Answer
|a| = 154.4 × 7.14e-3 = **1.10 m/s²**. This is a deceleration and is reported as a positive magnitude.

## Checks
- The acceleration is consistent to within ±1.5 % across fit windows and trackers.
- The diameter is the main source of uncertainty: 23.5 px gives 1.117 m/s² and 24.5 px gives 1.071 m/s², which is within ±3 %.
- Confidence: good.

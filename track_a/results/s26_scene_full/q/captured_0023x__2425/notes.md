# q_2425: book velocity at t = 1.2 s (cm/s)

File fps = question_fps = 24, so t = 1.2 s is frame 29. At that frame the book is sliding down the inclined white board, near its bottom edge.

## Method (measure.py, check_prior.py)
- Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Track: scene/tracks/blue_book.csv mask centroid, with the bbox centre as an alternative reference point.
  I checked frame 29 visually: the book is at y ~406-467 with motion blur.
- Board plane: built from depth_info slope_far = 1.201 m (top edge, y = 356) and slope_near = 0.9555 m (bottom edge, y = 481),
  with the camera x-axis lying in the plane. Slope length comes out at 0.30 m. Each per-frame 3D centre is the intersection
  of the centroid's ray with this plane.
- Check against depth_info: the plane model gives a camera distance of 1.029 m at frame 29; the given value is 1.02 m (0.9 % apart).
  I rescaled by 0.991 so it matches exactly.

## Velocity at frame 29
- Raw forward difference: 77.2 cm/s. Backward difference: 74.3. Central difference: 75.8.
- Forward difference with a 5-frame moving average (reference convention): 78.7 x 0.991 = 78.0. With a 7-frame average: ~77.6.
- Quadratic fit of the along-slope distance:
  - frames 21-30: v(29) = 76.1 cm/s, a ~1.6 m/s^2;
  - frames 24-29: 76.3 cm/s.
- Second route, bbox centre instead of centroid: quadratic fit gives 77.5-78.8; central difference gives 74.0.

## Prior check
At t = 1.4 s (frame 34) the book lands on the table and decelerates. Using the given depths of 0.857 m and 0.851 m and smoothed
velocities, the magnitude of the deceleration is ~3-4 m/s^2 (5-7 frame smoothing). That is consistent with the prior's 2.8 m/s^2.

## Answer
77.5 cm/s. The routes spread from about 74 to 79 cm/s. Confidence: good (likely within ~5 %). Frame 29 is motion-blurred,
so the centroid there is only good to about ±3 px.

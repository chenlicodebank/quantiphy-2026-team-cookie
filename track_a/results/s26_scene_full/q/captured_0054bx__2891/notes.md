# q_2891: soccer ball displacement between 1.0 s and 1.4 s

Frames: question_fps = file fps = 24, so the frames are f24 and round(1.4*24) = f34.
Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Scale: depth_info gives the soccer ball distance only at t=2.0 s (f48) = 3.254 m. The distance at other frames is
3.254 * d(f48) / d(f) (apparent diameter is proportional to 1/distance).

## Measurements (measure.py -> meas.json, solve.py)
- For each frame I segment the non-black blob in the record's bbox, then compute a RANSAC+LSQ circle fit of the contour
  and an area-equivalent diameter.
- f24: the ball is still partly hidden by the removed hand (it is released at about f23-24), so its size and centre
  can't be read directly. RANSAC centre (927.4, 606.7); a quadratic extrapolation of the f25-34 track gives
  (922.7, 606.8).
- f34: fully visible dark-grey disc. Centre (885.1, 489.6), d_area 58.6 px.
- Depth: I fit 1/d linearly in time over f32-48 (one recording frame is missing between f35 and f36, so frames >= 36
  get an effective index of +1). Fitted d: f48 45.5, f34 58.4, f24 72.0 px. That gives a distance of 2.053 m at f24
  and 2.533 m at f34. The fit also matches the measured d_area in f26-28 to within about 1 px.
  The implied ball diameter is 0.194 m, which is plausible.
- 3D points: unit ray(u, v) * distance. Displacement |P34 - P24| = 0.578 m.

## Checks
- A different fit window (f29-48) gives 0.573-0.575 m.
- Using the RANSAC diameter instead of the area diameter gives 0.577-0.579 m.
- Using the RANSAC centre at f24 instead of the extrapolated one changes the result by about 0.001 m.
- Main uncertainty: the f24 depth is extrapolated because the ball is occluded there. If d(f24) were 70 px instead of
  72 px, the answer would be about 0.53 m. Confidence: moderate (about ±8%).

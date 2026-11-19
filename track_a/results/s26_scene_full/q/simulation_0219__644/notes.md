# Q644: outer diameter of the robot's tires (m)

Prior: big robot speed = 5.924 m/s. fps = question_fps = 24, so no re-timing.

Object: the big blue tracked robot. Its "tires" are taken to be the three ringed road wheels inside the
caterpillar track (the end wheels are spoked sprockets/idlers). Each has a light grey outer tyre ring, then
spokes and a hub. Small grey robot has no wheels.

## Measurements (wheels.py, prof.py)
- I scanned the wheel-centre row (y 843-849) and found the outer ring edges at a threshold of 30 grey levels
  (the background between the wheels is about 3-10 and the ring about 45-50), with sub-pixel interpolation.
  Rotation does not affect this measurement.
- Diameter on clean frames (9, 12, 17-21, middle and right wheels): 68.8-70.4 px. Frame 12, middle wheel: edges
  387.2 / 456.8, so D = 69.6 px. Vertical check: the bottom edge is at y = 879.5 and the horizontal centre row is
  at about 845, giving a radius of about 35 px. The top edge is hidden by the suspension strut. Other frames are
  noisy because of claws, the small robot or shadows, so I left them out.
- Wheel pixel speed: the middle wheel centre moves 269.9 (f9) -> 421.6 (f12) -> 878.6 (f21), which is
  50.73 px/frame. The right wheel gives 50.7. This matches the rear track plate (50.9) in the scene record. The
  body reference moves 51.8.

## Scale and answer
The scale is set by the speed, at the wheels' own depth: 5.924 / (24 x 50.73) = 0.004866 m/px.
D = 69.6 x 0.004866 = **0.338 m**.

Second route: using the record's body reference speed of 51.8 px/frame gives 0.004766 m/px, so
D = 0.332 m (2% lower). The perspective spread between parts of the tank (about ±4%) limits the accuracy.
Confidence: moderate-high on the pixel measurement. The main uncertainties are which wheels count as the
"tires" and whether the reference speed is that of the origin.

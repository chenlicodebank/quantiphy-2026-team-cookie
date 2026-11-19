# Q1537 – speed of the yellow car at t = 1 s (m/s)

File fps = question fps = 24, so t = 1 s is frame 24, and speed = |p(24) - p(23)| x 24.
The car drives right to left, parallel to the image plane, at constant depth (its size and image row stay constant), so the origin's
world speed equals the speed of its near side plane. Scale comes from the prior: yellow tyre diameter = 0.764 m.

## Pixel displacement, frame 23 -> 24
- `tyre_r.py`: fits a circle to the white rim's outer edge (steepest bright-to-dark gradient on 90 rays, sub-pixel), giving each wheel's centre.
  - Front wheel centre x: 920.0, 825.0, 728.2, 629.9, 530.3, 429.7 (frames 21-26), so the steps are 95.0, 96.8, **98.3**, 99.6, 100.6.
  - Rear wheel: 1629.7, 1534.6, 1437.8, 1339.5, 1239.8, 1139.0, so the steps are 95.1, 96.8, **98.3**, 99.7, 100.8.
  - Both wheels agree. The steps are smooth, and y stays constant to within 0.1 px.
- The scene record's template track gives 96.97 px for 23 -> 24. That track is less smooth (96.5, 97.0, 98.1, 100.7), so I used the
  rim value of 98.3 px. Using the template value instead would lower the answer by 1.4 %.

## Tyre pixel diameter (in the wheel-face plane, at the same depth as the wheel centres)
- `tyre_r.py`, `rays.py`, `enh.py` (gamma-brightened overlays with circles of r = 85, 89 and 93 px, in `frames/enh_*.png`).
- The tyre edge against the dark arch gap (top and sides), found as the steepest darkening, is at r = 88-90 px from the rim centre in
  frames 12-28, for both wheels.
- The edge against the floor (bottom) is at r ~ 93-95 px. This includes the contact shadow and the reflection on the glossy floor.
- I took r = 89.5 +- 1.5 px, so D = 179 px. The scale is 0.764 / 179 = 0.004268 m/px.

## Result
speed = 98.3 px x 0.004268 m/px x 24 = **10.07 m/s**. With D = 180 the result is 10.01. **Answer: 10.05 m/s.**

## Checks
- Second route for the displacement: the record's template track gives 96.97 px, which means 9.93 m/s (a 1.3 % difference).
- Cart tyre consistency: the blue cart's rear tyre is about 66-72 px across in frame 41. The ground-contact rows (car 884, cart 817,
  horizon 539.3) give Z_cart / Z_car = 1.24. From those, the predicted car tyre diameter is 2.57 x d_cart, about 170-185 px, which
  agrees with 179.
- depth_info (front-left tyre at 11.38 m at frame 12; the tyre is at (1657, 791) in that frame) together with D = 179 gives f ~ 2560 px,
  which is a horizontal field of view of about 41 deg. This is plausible. It is not an independent scale, since the speed depends only on
  m/px at the wheel plane.
- Confidence: about +-3 %. The main uncertainty is where the tyre edge lies (r between 88.5 and 93 px).

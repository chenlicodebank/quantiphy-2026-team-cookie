# q_1524: speed of the yellow car at t = 1 s (frame 24 at question_fps 24; the file is also 24 fps)

Answer: **9.7 m/s**

## Scale and camera
- Prior: tyre diameter is 0.764 m. depth_info: at t=0 the right-front wheel centre is 14.244 m from the camera.
- At t=0 the right-front wheel is the near wheel on the image left (x≈67, y≈829); the car's right side faces the camera
  all through the clip. Its white rim was segmented and fitted (rims.py: region moments; rims_edge.py: sub-pixel
  half-level edges). Rim height at f0 = 86.1 px (moments) / 87.1 px (edges).
- Tyre/rim diameter ratio k ≈ 1.46, measured from tyre top/bottom against the rim at frames 24 and 30
  (range 1.42-1.5). Rim diameter = 0.764/k = 0.523 m.
- Horizon at y=829 comes from the ceiling-tube vanishing point in the scene record, so the camera is pitched up about 8°.
  The principal point is taken as the image centre. f is calibrated so that the f0 wheel distance is 14.244 m:
  f ≈ 2127-2158 px (HFOV ≈ 48°).
- Sanity check: the wheelbase comes out at 2.80-2.85 m and is stable across frames. Wheelbase/tyre ≈ 3.7, which is
  plausible for this RX-7-type model.

## Motion
- Each near-side wheel centre (front 14-31, rear 22-32) was placed in 3D from its rim centre pixel and rim height
  (geom.py). Hubs sit on the horizon, so they are at camera height.
- From about frame 18 to 31 the car moves on a straight line, heading about -49° to -50° in the level camera frame.
  Its speed is nearly constant (about 0.40 m per frame), and the heading changes by less than 0.1° per frame. Because
  the car is translating without yaw, the origin speed equals the wheel speed.
- Rigid two-wheel fits over windows 21-31, 22-31, 23-29, 22-28 and 24-31 (models.py, rims2.json = edge heights):
  - Model A (free translation, heading fitted separately): 9.65-9.9 m/s.
  - Model B (motion along the heading, no sideslip): 9.45-9.65 m/s.
  - Moment-based rim heights (rigidfit.py): 9.9-10.0 m/s.
  - The tyre/rim ratio barely matters: k from 1.40 to 1.55 changes the speed by about ±1.5%.
- Second route (lag): the rear hub reaches the image position the front hub held about 7.04 frames earlier
  (rear f30 ≈ front f22.96, with matching rim heights to about 1%). Speed ≈ wheelbase/lag = 2.83/(7.04/24) ≈ 9.65 m/s.
- Per-wheel straight-line averages over frames 22-31: front 9.71 m/s, rear 10.0 m/s.

## Answer and confidence
9.7 m/s is the centre of these routes; the spread is about ±3%. The main remaining uncertainties are:
- the f0 rim height (±1 px → ±1.2% on the overall scale);
- whether the motion has a small sideslip (model A vs model B differ by about 3-4%).

## Notes on the scene record
- In car_wheels.csv the rear rim is partly hidden in frames 20-21 and unusable. The front rim at frame 32 is dark and
  unusable, and frames 14-16 are partly hidden.
- The moment-based rim heights need care; the edge-based heights in rims_edge.json are preferred.
- The record's statement that the car is broadside at frames 30-32 refers to its appearance in the image only. In 3D
  the car keeps a heading of about -49° (straight path).

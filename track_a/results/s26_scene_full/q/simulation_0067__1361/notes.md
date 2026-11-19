# Q1361 – length of the purple car (m)

The purple car is the dark-purple classic sedan (it looks like a Mercedes W123) parked facing left on the far side of the intersection. It is static,
and no depth is given for it. Prior: the white van accelerates at 4 m/s². File fps = question fps = 24.

## Camera (3D scene, static camera; principal point at the image centre and zero roll assumed)
- Horizon y ≈ -47 (from the scene record's road vanishing points (2697,-43) and (110,-47)).
- Vertical vanishing point from 6 street-lamp shafts fitted on the clean background (poles.py, vp2.py):
  (1069–1132, 2555–2721). With f² = (vy-cy)(cy-hy), f = 1088–1131. The two road VPs being orthogonal gives f ≈ 1107.
- Camera height H, route A (prior): I tracked the van's visible rear tyre ground contact in frames 15–71 (wheel.py)
  and intersected it with the road plane. The motion is a straight line with constant acceleration (rms 0.2 % of H;
  the windows 15–40 and 40–71 agree to 0.3 %). a = 4 m/s² then gives H = 7.20 m at f=1100 and 7.10 m at f=1150 (accel.py).
- Camera height H, route B (depth_info): pedestrian pelvis from the given depths at frames 14 and 38, plus the ground point
  below it from the feet (pedH.py). This gives H above the sidewalk = 7.10–7.17 m at f=1100, i.e. about 7.25–7.3 m above the road
  with a ~0.15 m curb, which agrees with route A to about 1 %. At f=1000 the two routes disagree by 3 %.
- Van depth check (vanorigin2.py): with f=1100 the given van depths need the van origin to sit about 0.9 m ahead of the rear-axle
  contact. That is plausible only if the origin is not the box centre. With f=1000 the origin would be about 1.8 m ahead, close to the
  centre. This check is weak because the origin location is unknown, so I did not use it for scale.
- Adopted: f ≈ 1120 and H ≈ 7.16 m.

## Sedan (sedan.py, sedan2.py, sedanmask.py; average of frames 0/10/20/30)
- Near-side tyre contacts: front (1329,334), rear (1411,312).
- Bumper extremes: front far corner (1253.5,301.5) = left image extreme of the mask; front near corner (1314,318);
  rear near-side bumper tip (1451,283).
- Wheelbase ≈ 2.73 m. The distance to the sedan is ≈ 25.6 m. The wheel axis is within 0.8° of the road direction.
- Length = the distance along the car axis between the front and rear bumper planes. Corners were placed either on the vertical side plane through
  the tyre contacts (this gives bumper heights of 0.42–0.45 m for front and rear alike), or on a 0.45 m horizontal plane:

| f | H | wheel axis, near corners | wheel axis, far front corner | road axis, near | road axis, far |
|---|---|---|---|---|---|
| 1100 | 7.20 | 4.61 | 4.69 | 4.71 | 4.76 |
| 1150 | 7.10 | 4.57 | 4.59 | 4.67 | 4.67 |

- The near and far front corners give the same front plane at f≈1150–1170, which supports f ≈ 1100–1150.
- Check: length / wheelbase = 1.69. The real W123 ratio is 4.725/2.795 = 1.69, so the overhangs are consistent.
- Sensitivity: a 0.15 m error in bumper height changes L by about 0.1 m. f between 1000 and 1200 gives 4.5–4.8.

## Answer
L ≈ 4.66 m (interpolated to f=1120 and averaged over the corner and axis variants). I expect it to be within about ±3 %.

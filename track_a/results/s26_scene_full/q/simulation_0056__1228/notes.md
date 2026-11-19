# q1228: height of the streetlight (simulation_0056)

Answer: **4.6 m**. The near and far lamps are the same model: near 4.58 m, far 4.62 m at f = 1600 px.

## Inputs
- The file runs at 29.9936 fps and question_fps is 30. Only frames 0 and 30 (t = 0 and 1 s) are used, so the
  difference does not matter.
- The prior (orange car acceleration -2.86 m/s²) does not constrain the focal length. The car is near the optical
  axis, and its scale is already fixed by its depths. So f has to come from the depth_info geometry.

## Camera model (cam.py, lines.py)
- LSD line fit on frame 0, using 37 road and building lines toward one vanishing point: VP = (884.5, 1008).
- All verticals lean by dx/dy = +0.022, so the camera is rolled about 1.26°. With the roll removed, the horizon is at
  y' = 1005 (principal point taken as the image centre).
- Ground plane = the sidewalk.

## Corrections to the scene/ record
- The near lamp's base is not at y = 1378; that is only where the hydrant starts hiding it. Its plinth shows to the
  right of the hydrant and reaches the ground at y ≈ 1665 (centre of the base ellipse).
- Far lamp: top 705, base 1270. Near lamp: top 239.

## Lamp origin
- With the bases on the ground, an origin at **mid-height** reproduces both lamps' depths with the same camera height
  for any f (near/far agree within 0.6%), and the two lamps come out the same height.
- An origin at the base cannot fit both lamps at any f.
- So the depth_info points to each lamp's bbox centre, and the lamps are identical.

## Focal length (the answer scales roughly as 1/f)
Each reference gives the camera height that reproduces its own depth, as a function of f (hcurves.py, man_f.py,
hyd_f.py, check2.py, lamp_height.py). Where that curve meets the lamps' curve gives f:

| Reference | f (px) |
|---|---|
| Man at t0, depth taken to his ground-level origin (between the two foot contacts) | 1582 |
| Man at t1, same convention | 1606 |
| Hydrant, origin at bbox centre, base-ellipse centre on the ground at y = 1770–1787 | 1790–1480 (1583 at y = 1780) |
| Man, if the depth were to the pelvis (pelvis over the midpoint between the feet) | 1175–1215 |
| Dark car, ratio of its ground rows at t0 and t1 (rough, wheel rows ±8 px) | about 1300–1450 |

I took **f ≈ 1600**:
- Three references with natural origins agree there: man at t0, man at t1, and the hydrant at its centre.
- At f = 1600, the man's ground positions reproduce his given depths: 4.768 vs 4.786 and 5.165 vs 5.159.
- Sanity check: at f = 1600 the camera is 2.13 m high, the man 1.92 m and the orange car about 1.85–2.0 m wide (a
  realistic scale).
- At f ≈ 1200 every size is about 1.33 times larger, and the hydrant's origin would have to sit near its top.

## Lamp height vs f (vertical pole, origin at mid-height, base on the ground)
| f (px) | Lamp height (m) |
|---|---|
| 1500 | 4.88–4.92 |
| 1550 | 4.73–4.77 |
| 1600 | 4.58–4.62 |
| 1650 | 4.45–4.48 |
| 1700 | 4.32–4.35 |

## Second route
The near and far lamps are measured independently: different depths (5.2 m and 13.2 m) and different pixel
heights (1426 px and 565 px). They give the same height within 1%.

## Confidence
Moderate. The main risk is the human depth convention: if distance_human_camera is to the pelvis, f ≈ 1200 and the
lamp is about 6.0–6.1 m. The hydrant data argue against that reading.

# q1313 – diameter of the bicycle wheel (simulation_0064)

Answer: **0.58 m**. Confidence is low to medium; the likely range is 0.53–0.62 m.

## Time base
The file and the question are both at 24 fps. The depth times are t=0.58 s → frame 14 and t=1.58 s → frame 38.
Bike distances: 33.9976 m at f14 and 28.6807 m at f38, i.e. about 0.2217 m per frame. The ground-plane check
below confirms the motion is close to constant speed, so I used d(f) = 34.00 − 0.2217·(f−14).

## Focal length (from vanishing points, scripts vvp.py, vvp2.py, hvp.py)
- Vertical vanishing point: I fitted 43 LSD segments on poles, signal heads and building edges (road-cobble
  lines excluded). Result (1080–1086, 7705–7813); bootstrap σ(y) ≈ 50 px. Its x matches the image centre, so
  the principal point is at the centre and there is no roll.
- Street vanishing point / horizon: cobble and curb lines give (1088, −117.4). The record's curb pair gives
  (1087, −121).
- Orthogonality of the two directions gives f² = (y_v − 540)(540 − y_h), so **f ≈ 2172 px** (2146–2193 over
  the variants), and pitch ≈ 16.8°.
- Sanity checks at real-world scale: pedestrian 103 px at 38.5 m → 1.83 m; van paint width 120 px at z≈38.3 m
  → 2.1 m. The van's 3D displacement f14→f38 from depth_info plus rays is 4.13 m. The prior (a = 4 m/s² from
  rest starting at f≈1–1.5) gives 4.08–4.15 m, so it is consistent.
- Ground-plane check: the camera height from the bike's contact rows at f14 and f38 is 6.65 and 6.58 m, so
  the depths are consistent.

## Wheel in pixels (scripts front.py, prof3.py, prof.py, enh.py)
The bike rides straight at the camera, so the front wheel is seen edge-on as a thin vertical stripe. Its image
extent equals D·f/d (a circle projected onto a direction in its own plane). I measured the bright rim stripe,
which is crossed by a dark blob (shoe/pedal) that does not mark its end, on ratio-to-background profiles:

| frame | stripe rows | px | d (m) | px·d/f (m) |
|---|---|---|---|---|
| 38 | 364–404 | 40 | 28.68 | 0.528 |
| 42 | 380–421 | 41 | 27.79 | 0.525 |
| 50 | 411–456 | 45 | 26.02 | 0.539 |
| 71 | 528–582 | 54–55 | 21.37 | 0.535 |

(f46 and f58 gave shorter values, 0.45–0.50, because of occlusion or the van's shadow.)
Mean of the visible rim extent ≈ 0.53 m. The black tyre is not separable from the dark ground; it adds roughly
3–4 px at each end (about 0.03–0.04 m each), giving about 0.59–0.61 m. The front wheel is probably a few tenths
of a metre closer than the bike's origin, which lowers this by about 1–2%. **Best estimate: 0.58 m.**

## Plausibility check
The handlebar/hands sit only about 0.74 m (image height) above the contact point, and the rider's head top about
1.55 m. So this bike model is smaller than a full-size 700c bike, whose wheel is about 0.68 m. A wheel of about
0.67 m would put its top at or above the hands, which is physically impossible. A wheel smaller than about 0.46 m
(taking the dark blob as the wheel top) is contradicted by the rim stripe continuing above the blob in every frame.

## Caveats
The scene record's cyclist `wheel_bottom_y_best` is wrong in the shadow-crossing frames: at f38 it says 431,
but the frame shows about 405. Its height_px_best values there are therefore too large. The main uncertainty is
whether the bright stripe is the rim only (answer about 0.60) or the whole tyre (answer about 0.53).

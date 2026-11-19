# Q1299 — width of the turning yellow car (taxi), simulation_0063

Answer: **2.0 m** (medium-low confidence, about ±7 %).

Time base: question_fps = file fps = 24. t = 0.58 s → frame 14, t = 1.58 s → frame 38.

## Camera calibration
- **Focal length from vanishing points** (`edges.py`): curb lines fitted on frame 0 with rms of 0.3 px. Two
  orthogonal ground directions give VP1 = (-113, 525.8) (island lower edge × near curb) and VP2 = (4992, 529.2)
  (island top edge × far road edge). Orthogonality gives **f = 2160 px** (= image width, so HFOV 53°). The horizon
  is at y ≈ 527.5 and the camera is nearly level.
- Check: the four tyre contacts of the taxi at f38, back-projected onto the ground, form a rectangle with corners
  of 91.5° (91.1° at f71), and the wheelbase is 3.0 m in both frames (`wheels3d.py`).
- **Camera height H ≈ 2.18 m**, found from:
  - the prior: the van's rear edge, tracked along the ground line toward VP2, gives an acceleration of 3.94 m/s²
    at H = 2.17. That equals 4 at H ≈ 2.20, and the extrapolated speed at frame 1 is ≈ 0.5 m/s, so the van
    starts from rest (`van_acc.py`);
  - the given depths, via ground contacts: man 2.13 and 2.18, cyclist 2.19, van 2.18, taxi f38 (4 wheels)
    2.20, taxi f14 2.16 (`joint.py`, `bodyfit.py`).

## Taxi geometry
- Heading: from the tyre contacts and the side sill line: f14 +16°, f38 -37°, f71 -62° (the final road
  direction, VP1, is -61°).
- Wheelbase ≈ 2.9–3.0 m. Tyre radius ≈ 0.34 m.
- Track (contact to contact, f38 with 4 wheels and f71) ≈ 1.75 / 1.69 m, mean ≈ 1.72 m.
- Length: the silhouette tangents at f14 (pure side view, depth given), f38 and f71 give 5.30–5.37 m
  (`tangentfit.py`).

## Width
The far side of the body is only seen through rounded-corner silhouettes, so the width is poorly conditioned
when fitted to silhouettes alone:
- the rounded-rectangle tangent fit gives W = 1.82 m at r = 0.33, but the range is 1.5–2.1 depending on
  heading ±1.5° (`tangentfit.py`);
- the front is strongly rounded in plan: the plate is about 1.05 m ahead of the front axle, but the corners are
  only about 0.4 m ahead. So corner-based widths are biased low (`route_f14_f71.py`, `farcorner.py`), and I
  did not use them.

Estimates I used:
1. Outer tyre-to-tyre width = track 1.72 + tyre width ~0.24 → 1.96 m. The body is at least that wide (the
   fenders cover the tyres), so W ≈ 1.96–2.05.
2. Headlight outer edges at f71 (front face seen 30° off-axis) span 1.84 m. The body is about 0.1 m wider →
   about 1.94 m. f38 gives 2.09 m (+0.1 → 2.19), but its far headlight is heavily foreshortened, so it is less
   reliable.
3. Sanity check: the proportions match a Crown Victoria taxi at about real scale (L 5.34 against 5.39 real;
   wheelbase 3.0 against 2.91), which gives W ≈ 1.97–2.05.

Combined answer: **W ≈ 2.0 m**. If the reference bounding box includes the side mirrors, the true value could be
about 2.1–2.2 m.

The record in scene/ (pixel boxes) was right for the extents I checked (taxi f14 x 160–680, f38 right edge 1000,
f71 x 860–1326). It contains no metric scale.

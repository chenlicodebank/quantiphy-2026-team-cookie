# Q1295: height of the white car (the van), in metres. Answer: 2.19 m

File fps = question fps = 24. The white car is the van (scene/ calls it "van").

## Geometry (3D, static camera)
- **Focal length from vanishing points** (`lines2.py`, using the clean background `frames/bg_full.png`): the kerb lines
  of the two perpendicular streets.
  - Direction A: right-sidewalk front kerb, near kerb, far kerb. VP_A = (-112, 525.8), from the intersection of the two
    tight fits (residuals 0.15-0.17 px).
  - Direction B: four kerb/sidewalk edges, x at the horizon 4850-5110, about 5060.
  - Taking the principal point at the image centre: f² = (cx-u_A)(u_B-cx), so **f ≈ 2165 px** (2120 with the lowest B
    line). Horizon y ≈ 525.8, and the camera is nearly level.
- The van drives along direction B. Its rear-tyre contact track (`tyre.py`, frames 28-42: (124,709.5) → (418,698.5))
  points to x ≈ 5040 on the horizon, which matches VP_B.

## Camera height h (all lengths in units of h first)
- Ground back-projection: Z = f·h/(v-525.8) and X = (u-cx)·Z/f.
- **Route 1, distances** (`depthroute.py`):
  - The near-side tyre line comes from the tyre track.
  - The rear corner is the measured `rear_x`, on a line parallel to the tyre line at offset c.
  - The front corner (frames 69-71) gives the length L ≈ 2.58h.
  - The van's origin is taken at the box centre (at half height).
  - Matching the given distances, 29.2444 m (frame 14, from the kinematic extrapolation) and 29.8093 m (frame 38),
    gives h = 2.20 (f=2165) or 2.24 (f=2120). The two frames agree with each other to within 0.5%.
- **Route 2, acceleration prior** (`kin.py`): positions along the path from `rear_x` (frames 28-71), fitted with a
  quadratic. Requiring a = 4 m/s² gives h = 2.23-2.33, which depends only weakly on f. The two routes agree best
  near f ≈ 2100-2120.
- **Route 3, check with the man**: his feet on the ground, with the same f and h, reproduce his given distances within
  1-3%, which implies h ≈ 2.19-2.23.
- Combined result: **h ≈ 2.235 m** (spread ±2.5%).

## Van height
- At frame 38, measured by column profiles (`vprof.py`): roof top at y ≈ 529.5 and tyre contact at y = 701.5, so
  172 px.
- The roof sits 3.7 px below the horizon at a depth of about 13h, so the roof is 0.021h below the camera:
  H = 0.979·h ≈ **2.19 m**.
- With the record's rounder numbers, 165-172 px × 28.6 m / 2165 px gives 2.1-2.2 m before the near-side correction,
  which agrees.
- Implied van size is about 5.8 m long, 1.8-1.9 m wide and 2.19 m tall, which is plausible.

## Confidence
Moderate to good, about ±4%. The main uncertainty is the focal length (±2.5%) and the van's width, which sets how far
its centre is beyond the visible side.
- The scene record's van `height_px` and bottom values were partly estimated. The bottom there (692 at frame 38) was
  too high: the measured tyre contact is 701.5.
- The record's horizon of 532, taken from the man's feet, is replaced here by 525.8 from the vanishing points.

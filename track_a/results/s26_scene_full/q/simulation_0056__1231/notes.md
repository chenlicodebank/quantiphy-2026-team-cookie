# Q1231: width of the green car (m). Answer: 1.97 m

The green car is the dark-green Mercedes 300SL-like coupe ("dark_car" in scene/). Width = its shorter horizontal extent
(body side to side). The question fps (30) and the file fps (29.9936) give the same frames here (f0 = t0, f30 = t1).
The prior (orange car acceleration) carries almost no information about the focal length, because the orange car stays
near the optical axis. So the scale comes from depth_info plus a calibrated camera.

## Corrections to the scene/ record
- The road vanishing point is (883.5, 1007), not (923, 1050). It comes from an LSD/RANSAC fit of 36-39 road-parallel
  segments (road edge line, dashed line, building roof and base lines) and agrees with a direct fit of the edge and
  dashed lines (888, 1009). Script: `vp3.py`, `vp2.py`.
- The camera is **rolled by about 1.1-1.4°**: all building and lamp-post verticals lean with dx/dy ≈ +0.022 (`vvp.py`).
  This tilts the horizon by about 15 px across the image, which matters a lot for any ground-plane reasoning.

## Focal length (three routes)
1. Camera fit from three orthogonal vanishing points (`calib3vp.py`, `calib3vp_robust.py`). The families are
   road-parallel lines, 9 sidewalk-slab joints perpendicular to the road (`vp_perp.py`) and verticals.
   - Result: f = 1510-1700 px depending on which verticals are used (long verticals > 200 px: f ≈ 1580;
     leave-one-out over the joints: 1560-1630).
   - Camera rotation: pitch ≈ 0.7°, yaw ≈ -5°, roll ≈ -1.2°.
2. Green car ground footprint (`greenf.py`). The car origin is taken as directly above the footprint centre (midpoint
   of the near-rear and far-front tyre contacts). The road-level camera height must come out the same at t=0
   (D=28.684 m) and t=1 (D=17.388 m).
   - h0 = h1 at f ≈ 1590-1600 (h_road ≈ 2.34 m).
   - Reconstructed car: wheelbase 2.72 m, side ⊥ axle at 85°.
3. Hydrant and far lamp, origins at their bases, on the sidewalk (`geom3.py`). Their implied camera heights agree at
   f ≈ 1500 (h_sidewalk ≈ 2.2 m, about 0.2 m below the road-level value, consistent with a curb).

Without the roll correction, the ground methods gave inconsistent values from 700 to 1600 px. With the fitted camera
they agree. Adopted f ≈ 1580 px (±~80).

## Width measurement (`width2.py`)
- Pixel readings:
  - t=0: headlight centres (1313.3, 1095) and (1410.8, 1093.3); far-fender silhouette edge x = 1420.
  - t=1: headlights (1695.6, 1173.6) and (1874.5, 1167.5), matching the code blob centroids; fender edge
    x ≈ 1893.5 (the code mask gives 1894).
- Car origin: 3D position from depth_info, placed above the wheel footprint centre.
- Heading: from the motion t0→t1 and from the wheel contacts. Both say the car drives almost exactly parallel to the
  road (psi ≈ 0-2.5°).
- Method: on the front-face plane (normal = heading, at a distance ell ahead of the origin), the half-width is the
  distance from the headlight-pair centreline to the far-fender silhouette point.
- ell is fixed by requiring the 3D headlight spacing to be equal at t0 and t1: ell ≈ 2.2-2.3 m, plausible for a car
  with a 2.7 m wheelbase.
- Results:

| f (px) | W at t0 | W at t1 |
|---|---|---|
| 1600 | 1.92-1.95 | 1.97-2.03 |
| 1550 | 1.98-2.02 | 2.03-2.10 |

- t1 is slightly high, probably from motion blur widening the fender edge, so t0 is weighted more.
- Adopted **W ≈ 1.97 m**.

## Checks
- The headlight spacing comes out consistent at t0 and t1 (1.61-1.62 m at f=1600).
- Wheelbase 2.72 m and width ≈ 1.97 m give a ratio of 0.73, the same as the real 300SL (1.79/2.40 = 0.75). That
  implies the asset is about 1.1x real size, which is plausible.
- Track from contacts is about 1.73 m. It is less reliable because the contact rows are poorly resolved at 28 m.

## Confidence
Moderate. The main uncertainty is f (±5%), which carries into W roughly as 1/f. Silhouette and blur add about ±3%.
Overall about ±7%.

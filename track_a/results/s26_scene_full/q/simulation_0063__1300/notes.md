# Q1300 — diameter of the bicycle wheel (m)

The file rate and question_fps are both 24, so frame = round(t*24): t=0.58 → f14, t=1.58 → f38.
Prior: the white car (the "van" in scene/) accelerates at 4 m/s². depth_info gives camera distances for the man, the
yellow car (the "taxi"), the white car and the bike at f14 and f38.

## Focal length (3D pinhole; principal point (1080, 532 = horizon row), camera treated as level)
1. **Van route** (`vanfit.py`, `vanvariants.py`, `vansens.py`): the van is modelled as a box moving in a straight line
   on the ground with constant acceleration A = 4 (the prior). It is fitted to its rear-edge x f28-71 (scene record,
   re-checked), its wheel-bottom y f28-57, its front x f69-71, and the given centre distances at f14 and f38.
   Result: f = 2114 px (all data). Dropping the rear-edge frames where the man hides the van's rear (f28-29, f45-50)
   brings the rear rms from 3.9 px to 1.4 px and gives **f = 2140**. The fit also gives camera height ≈ 2.0 m and van
   length ≈ 5.6 m, so the scene looks real-scale. f stays within 2086-2146 when the width/axle assumptions change or
   when the d14 / bottom / early / late data are left out.
2. **Bike route** (`bike3d.py`, `bikefscan.py`): a constant-velocity bike through its two given distances (f14, f38)
   has to reproject onto its tracked image positions f40-71. The rms is smallest, 0.56-0.61 px, at **f ≈ 2100-2150**.
   The same model also reproduces the template-scale ratio (Z ratio 1.050 vs 1.050 at f52; 1.119 vs 1.117 at f71).
   Bike speed is 5.35 m/s, heading 62° from the optical axis, the same as the van (same road).
   → f = 2130 px (about ±2-3%).

## Wheel pixel size
The wheel's vertical outer extent is measured from intensity profiles and contrast-stretched zooms (`prof.py`,
`zoomc.py`). The vertical diameter of a wheel is not foreshortened, while its width is (wheel plane at ~60° to the
line of sight).
- f52 front wheel, on clean road: outer top 632.6 (dark tread line) to outer bottom 678.0 → **45.4 px**. Width check:
  38.5 px / sin(60.7°) = 44.1 px.
- f71 front wheel: 625.6 → 669.0 → **43.4 px**. (The rear wheel's top is mixed up with a rack-like line, so I didn't
  use it. Its bottom, 671.4, is 2.4 px lower than the front's, which fits it being about 0.5 m closer.)

## Depth at those frames
From the constant-velocity bike path through the given distances: origin Z = 30.74 m (f52) and 32.74 m (f71). Add
about +0.27 m for the front wheel being ahead of the origin along the 62° heading.

## Result
- f52: 45.4 × 31.01 / 2130 = 0.661 m
- f71: 43.4 × 33.01 / 2130 = 0.673 m

**Answer: 0.665 m.** That is a plausible real bicycle wheel (26" ≈ 0.66 m), which is consistent with the real-scale
van and camera height.

## Uncertainties and caveats
- Uncertainties: f about ±2.5%, wheel pixel extent about ±1.5%, where the bike origin sits about ±0.8%. Overall about
  ±4%. Confidence: medium-high.
- Ground-plane cross-check: camera height from the man's feet comes out ~2.15 m, against 2.0 m from the van-bottom
  model. I didn't resolve this difference. It affects the camera height, not f, and the answer doesn't depend on it.

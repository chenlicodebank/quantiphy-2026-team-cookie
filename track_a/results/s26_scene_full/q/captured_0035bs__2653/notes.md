# q_2653 — basketball displacement 0.4 s -> 0.9 s (cm)

Time base: question_fps = file fps = 24 -> t=0.4 s = frame 10 (ball still at rest, kicked at frame 12), t=0.9 s = frame 22.
Camera (lab card): f = 0.5959*1280 = 763 px, principal point (640, 360).

## Measurements (scene/tracks/basketball.csv, checked with measure.py: orange-mask bbox/eq. diameter, overlay frames/bb22.png)
- Frame 10 (rest, mean of frames 0-11): centre (828.6, 280.0), diameter 52.7 px.
- Frame 22: centre (667.2, 397.0) (3-frame mean 666.7, 395.9 gives the same answer within 0.1 cm), diameter ~61.1 px (mean 21-25).
- Frame 34 (t=1.4 s): diameter ~65.2-65.4 px.

## Depths
- Given: basketball 2.7777 m at 0.9 s. The depth_info lists "soccer_ball" twice at 1.4 s (2.6020, 2.3730); the size ratio
  shows 2.6020 is the basketball (2.7777*61.1/65.4 = 2.60) -> label typo.
- Size-implied depth 763*0.232/D_px is ~4.3% larger than the given depth at both 0.9 s and 1.4 s (2.898 vs 2.778; 2.715 vs 2.602),
  i.e. a consistent offset, so the depth at 0.4 s (not given) is taken from the calibrated constant K = d*D_px = 169.9 px*m
  (from both given points): d(0.4 s) = 169.9/52.67 = 3.22 m.
- Back-projection d*r/|r| with r = ((u-640)/763, (v-360)/763, 1).

## Result
- Displacement = |P22 - P10| = 88.0-88.1 cm (ratio/calibrated depth). Answer 88.1 cm.
- Alternative (uncalibrated absolute size depth for t=0.4 s, 3.36 m): 97.1 cm — rejected because the given depths
  consistently sit 4.3% below the size-implied ones, so the reference's sensor depth at 0.4 s should too.
- Second route: raw vs smoothed frame-22 centre (88.12 / 88.02); K from 0.9 s alone (3.222 m) vs both points (3.226 m) -> <0.3 cm change.
Confidence: moderate-high (main uncertainty is the unseen 0.4 s depth, ~±3%).

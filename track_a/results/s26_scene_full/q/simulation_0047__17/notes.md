# Q17 – length of the moving bicycle (m)

Prior: walking person speed = 1.236 m/s. No depth_info. fps = question_fps = 33. The scene is a near-top-down view of a street, so it is
treated as 2D with one scale taken from the pedestrian's speed, plus a small perspective-height correction.

## Pedestrian pixel speed (scale)
- Record track (scene/tracks/pedestrian.csv): net displacement f0→f98 gives 110.0 px/s; linear fit gives 109.7; same-gait-phase f2→f88 gives 110.1.
- Independent check (ped_check.py): head/shoulder template matching chained over 17-frame steps (same gait phase), f2→f87 → 109.8 px/s
  (the record over the same frames gives 109.9). **Used: 109.9 px/s** → 0.011247 m/px at the height of the tracked point.

## Bicycle pixel length
- measure3.py: bright pixels (frame minus median background) along the bike's axis row, taking the longest run per frame, f15–98.
  Valid frames give 136–139 px. f75–98 (both ends are tyres, so they are at the same height) give 137–138 px consistently, and f15–22 give 140.
  At f50, directly below the camera, the rear end is the rack end (131–137). Checked visually on 4x zooms at f20/f50/f70/f90
  (for example f90: front tip x≈399–403, rear tyre end x≈540). **Used: 137.5 px.**
- The parked pink bicycle on the sidewalk is a different object and was not used.

## Perspective correction
The tracked pedestrian point is the head/shoulders (about 1.4–1.5 m up), while the bike's ends are at axle height (about 0.33 m). Tall things lean
radially, as the kiosk shows. The rider's head shifts relative to the front tyre tip by 33 px over 883 px of travel (f20→f90), which gives
about 0.037 px per px per ~1.2 m of height, so the camera is about 30 m up. Correction = (H−0.33)/(H−1.45) ≈ 1.04 (±0.02 for H between 20 and 40 m).

## Result
L = 137.5 px × (1.236/109.9) m/px × 1.04 ≈ **1.61 m**. Without the perspective correction it would be 1.55 m.
Real bikes are 1.6–1.8 m long, so the value is plausible.
Confidence: moderate. Pixel length ±2 px, speed ±0.5 %; the main uncertainty is the height correction (±2–3 %).

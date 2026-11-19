# q_908: height of the plant (m)

The prior says the mug falls with g = 9.8 m/s^2. I treat the clip as 2D: the camera is static and the mug falls in a plane facing the camera. Both the file and question_fps are 30 fps.

## Scale (fit_accel.py)
- I fitted a quadratic to the mug track (scene/tracks/mug.csv) over the free-fall frames 5-15 (before the 0.5 s impact at frame 16):
  - ref_y: 6.84 px/frame^2 = 6155 px/s^2 (rms 0.5 px)
  - bottom (y1_true): 6206 px/s^2
  - rim (top_y): 6080 px/s^2
- I used 6155 px/s^2. Scale = 9.8 / 6155 = 1.592 mm/px (spread between edges is about ±1%).

## Plant (measure_plant.py, profile_plant.py, frame 36)
- The plant is a succulent in a white pot on the table at x ≈ 1084-1128 px.
- Top of the leaves: the first leaf rows are at y = 808 (edge about 807.5).
- Bottom of the pot foot: the foot shows a groove at y = 866-867 and is bright at 868-870, then gets darker from 871 down. Bottom edge ≈ 870.5 ± 1.5.
- Plant height ≈ 62-63 px, so 62 px x 1.592 mm/px ≈ 0.099 m (63 px would give 0.100 m).

## Checks
- The resting mug measures about 54 px from edge to edge (814.5 to 868), which gives 0.086 m. That is a realistic mug height.
- The takeaway cup (64 px) comes out at 0.10 m, the camera bag (223 px) at 0.36 m and the table (1022 px) at 1.63 m. All are plausible, so the scale is consistent.
- The pot's base sits about 2 px lower than the mug's base, so the plant may be slightly closer to the camera than the plane the mug falls in. This effect is about 1-3%.

Confidence: good, within about 5%. **Answer: 0.099 m.**

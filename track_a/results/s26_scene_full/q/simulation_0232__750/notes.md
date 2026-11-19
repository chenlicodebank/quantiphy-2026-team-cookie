# Q750 – ceiling height of the room (simulation_0232)

Prior: black cat speed = 0.714 m/s. No depth_info. fps 24 (file) = question_fps 24.

## Measurements (frame 24 / frame 0, scripts prof.py, prof2.py, vp.py, calc.py)
- Back wall: ceiling/wall junction y = 172 px, floor/wall junction y = 951 px (row-profile edges in 4 column bands,
  same in all bands) -> wall height 779 px at the wall's depth.
- Vanishing point from 37 Hough ceiling-tile/light-panel lines: (960, 536) = image centre -> camera level, horizon y ≈ 538.
- Cat (scene/tracks/cat.csv, checked): torso-centroid x linear fit 8.96 px/frame (endpoints 9.11, nose 9.02), y flat
  -> ~215 px/s -> 0.714/215 = 0.00332 m/px at the cat's depth.
- The cat walks near the back of the desk, in front of the wall. Depth ratio from the ground-plane geometry (level camera):
  desk top front edge y = 765, desk front floor contact y ≈ 1030 -> (Hc-hd)/Hc = 227/492 = 0.461;
  cat paw contact y ≈ 741 -> Z_cat ∝ 0.461/203, wall Z ∝ 1/413 -> Z_cat/Z_wall = 0.939 (0.93–0.96 for floor contact 1020–1035).
- H = 779 px × 0.00332 m/px / 0.939 = 2.74 m (no depth correction: 2.59 m).

## Checks
- Horizon 536–540 changes the ratio by <0.1 %.
- Consistency: camera height = 413/779·H = 1.46 m, desk height = 0.539·Hc = 0.79 m (realistic desk), cat nose–rump
  186 px -> 0.62 m; ceiling 2.74 m plausible for a classroom.
- Speed-fit choice (8.96 vs 9.11 px/frame) moves the answer by ±1.5 %.

Answer: 2.74 m. Confidence moderate (±4 %), main uncertainty the cat's depth vs the wall and the root-speed definition.

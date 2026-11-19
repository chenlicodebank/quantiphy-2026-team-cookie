# Q620 – height of the TV (m)

Prior: the black cat's speed is 0.94 m/s. depth_info is null. fps = question_fps = 24, so no re-timing.

## Scale from the cat (catspeed.py, using scene/tracks/cat.csv)
- Matched upper-body track: mean per-frame step 17.74 px (net 869 px / 49 frames = 17.73 px/frame).
  Torso centroid: 17.75 px per frame. Nose edge fit over frames 0–40: 17.77. Nose read by eye: 870/49 = 17.76.
  The cat walks steadily, so I took 17.74 px/frame = 425.8 px/s.
- At the cat's depth the scale is 0.94 / 425.8 = 0.002208 m/px.

## TV pixel height (edges.py, crop.py)
- The screen's top edge is at y = 528.0–528.3 (sub-pixel edge, 4 columns). The screen's bottom edge is at y ≈ 757.5.
- The stand feet end at y ≈ 791.5 (8× crops of both feet). This is the bottom of the AABB.
- AABB height = 263.5 px. Panel without feet = 230 px.
- The screen's sides do not converge: its width is 398.7–399.2 px all the way from top to bottom. So the camera is close to level.

## Perspective (the TV is farther away than the cat)
- The TV stand legs touch the floor at y ≈ 988 at the front and ≈ 958 at the back. The front-to-back depth ratio comes from how much the leg x positions shrink toward the centre: 763/710 px gives 1.075, and the top-surface corner gives 1.066. This puts the horizon at y_h ≈ 558. A cross-check with the stand top (front edge 792, back edge 776) gives y_h ≈ 563. I used y_h ≈ 560.
- The cat's ground line is about y = 1015 (near paws 1021, far paws about 1010).
- Depth of the stand front relative to the cat: (1015 − 560) / (988 − 560) = 1.063.
- The TV feet touch near the front of the stand top (791 against a front edge of 792 and a back edge of 776). I put the TV origin about 2 % behind the stand front.
- Overall, the TV is about 1.084 times as far away as the cat (range 1.05–1.11).

## Result
- Using the cat's scale with no correction: 263.5 × 0.002208 = 0.582 m.
- With the perspective correction: 0.582 × 1.084 = **0.63 m**. Possible range 0.61–0.645.
- Sanity check: with the same scale the TV is 0.95 m wide, a normal TV size. The panel's aspect ratio is 1.73, close to 16:9.

## Confidence
Moderate. The pixel measurements are good to about 1 %. The main uncertainty is the perspective factor, which could be off by about 3 %.
If the reference used one flat 2D scale, the answer would be 0.58 m.

# q_579 — height of the floor mirror (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 (file) = question_fps 24, so no re-timing.

## Measurements (frame 48, clean view of the mirror; scripts mirror_profile.py, mirror_edges.py)
- Mirror outer frame (warm wood vs grey wall, R-B threshold): top edge v=388-389 across all columns,
  bottom front edge v≈966 (row gradient at x=1880-1895).
- Left outer edge x = 0.0454 v + 1612.5 (1630 at top, 1656 at bottom); right edge x = 0.0612 v + 1847.2
  (1871 top, 1906 bottom). Width 241 px at top and 250 px at bottom. The x-offsets from cx=960 give
  the same ratio on both sides (left 696/670, right 946/911), so the top is 1.038x farther than the bottom: the mirror leans back.
- Wall/floor line v=944 (scene record). Cat: torso and nose slopes are 17.76-17.86 px/frame, so 17.8 px/frame = 427 px/s,
  and 0.94 m/s gives 2.20 mm/px at the cat. Cat paws at v≈1020, torso centre at v≈904.

## Model (solve.py)
The scene is labelled 2D, but the mirror is clearly farther back than the cat, so I used a pitched pinhole camera.
The fit uses the mirror bottom on the floor (v=966) and the mirror top resting on the wall (whose base is at v=944, top edge at v=388).
The top/bottom depth ratio is 1.038. The cat's origin is on its lane (floor at v=1020, origin at v=904), and its pixel speed gives the metric scale.
The focal length is not set by these data, so I scanned it from 900 to 6000 px. The answer barely moves:
- f 900-2500 px (lean 0.12-0.28 m, a realistic floor-mirror lean): H = 1.416-1.442 m
- f up to 6000: 1.39 m
- r between 1.030 and 1.046: 1.37-1.45 m
The results look physically consistent: camera height about 1.1-1.2 m, the cat's origin 0.26 m above the floor, and the horizon near the image centre.

## Check
A naive single 2D scale (578 px × 2.20 mm/px) gives 1.27 m. That underestimates, because the mirror is about 12% farther than the cat lane.
Under a simple level-camera floor-ratio estimate, (1020-540)/(966-540) = 1.13, which gives 1.43 m. This agrees with the full model.

Answer: 1.43 m. Confidence moderate; the main uncertainty is the perspective/focal assumptions, about ±3%.

# q_1756: bicycle height (handlebar top to ground), metres

File fps = question_fps = 33, so t=1 s is frame 33 and t=2 s is frame 66. 3D Blender segmentation clip with a static camera.

## Measurements
- Pedestrian (prior 1.8 m): the bbox height comes from scene/tracks/pedestrian.csv, which I checked on frames: 200 px at frame 33 and 212 px at frame 66.
  The pelvis ray goes through the mask centroid. Depths are 11.9259 and 10.8165 m.
- Bicycle: I read the handlebar top (where the bar ends enter the hands, mean of the left and right ends, from 8x zooms made by zoom.py)
  and the front-wheel bottom (bbox_y1+1):
  frame 20: 373 / 497 (124 px), frame 33: 423.5 / 561 (137.5 px), frame 45: 486 / 641 (155 px), frame 55: 547.5 / 718 (170.5 px).
  The bike is fully visible only up to frame 59, so I modelled its depth between frames from 3D constant velocity
  (positions at t=1 and t=2 back-projected using the given depths). The predicted image track of the bike centre matches the observed one within 2-4 px.

## Model (model.py, model2.py)
- Pinhole camera, principal point at the image centre, pitch from the vertical vanishing point in the record (I also tested no pitch and VP at 4000 and 9000).
  For each fit I solved f so that the pedestrian's modelled height on its vertical line comes out at 1.8 m (at t=1, at t=2, or as the mean of both).
  Result: f ≈ 1150-1250 px (hfov about 77°). The pedestrian alone is 4% inconsistent between t=1 and t=2 (gait or measurement), so I used the mean.
- Off-axis correction matters (the bike is at u≈1725, about 770 px from the centre), so I used full 3D rays rather than h·D/f.
- Bike height = vertical extent between the handlebar-top and wheel-bottom rays. The depth_info origin is assumed at the bike's centre,
  so the handlebar (about 0.38 H ahead) and the front contact (about 0.51 H ahead) are closer to the camera than the origin; I modelled this along the 3D heading.

## Results
- With the forward offsets: 1.51-1.56 m for all pitch and f choices, and steady across frames 20-55 (VP 6509, mean f: 1.542 / 1.532 / 1.543 / 1.528).
- Without offsets (all features at the origin's depth): 1.60-1.69 m.
- Second route: comparing frames 20, 33, 45 and 55 at different depths gives consistent values. A naive same-frame ratio to the pedestrian
  (1.8·h_b·D_b/(h_p·D_p)) gives 1.69-1.76 before the off-axis correction.
- Answer: **1.55 m**, leaning toward the physically modelled offset case.
  Main uncertainty is where the bike's origin sits (about ±4%) and the pedestrian's walking height versus the 1.8 m rest height (about ±2%).
- Sanity note: the cyclist is a scaled-up asset (rider about 2.7 m tall), so a 1.55 m handlebar height is consistent with the given depths, not with real-world bikes.

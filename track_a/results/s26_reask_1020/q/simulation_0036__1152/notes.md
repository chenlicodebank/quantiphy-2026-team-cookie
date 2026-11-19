# q1152: average speed of the person (m/s), simulation_0036

The file's frame rate and question_fps are both 24. There are 72 frames, so the clip runs from t = 0 to 2.958 s and the camera is static.
Prior: the boat is 10 m long. Depths: boat 133.96 m at t=1 s and 131.26 m at t=2 s; person 139.1030 m at t=1 s and 139.1044 m at t=2 s.

## Person pixel motion (scene track checked, re-measured with person_sub.py)
- Hip x (mask centroid / torso centroid) moves at 1.044-1.048 px/frame, steadily, so about 25.1 px/s. The net change is +73.5 px over 71 frames.
- Vertical drift is +0.05-0.09 px/frame (the person moves slightly down the image), which is negligible.
- Apparent size is the same in both halves of the clip: the soft-mask y-std is 10.36 px in the first half and 10.38 px in the second. So the depth to the body is
  about constant and the motion is lateral (across the view).
- The given human depth is constant to 1 mm. The origin is probably static while the body walks, so the body depth is about 139.1 m.
- Walking bbox height is about 41-42.5 px (mean 41.4 sub-pixel). That puts the standing height at about 42 px.

## Scale and focal length (two routes; they disagree)
1. Boat route. Back-projecting the boat centre at t=1 and t=2 with the given depths gives the heading: about 42 deg toward the camera at f = 3260.
   I then modelled the hull as a bow point plus transom corners (10 m long, 3-3.5 m beam). Matching the 182 px hull width at frame 24
   gives f of about 2800 px (boat_f.py, boat_f2.py). But f = 2800 with the body at 139.1 m makes the person 2.04-2.09 m tall,
   which is not plausible. This route assumes the heading equals the direction of motion and assumes a hull shape. A heading error of
   about 8 deg is enough to explain the difference.
2. Person route (standard object). A stature of 1.75-1.80 m over 42 px gives 0.0417-0.0429 m/px at the person's depth.
   That corresponds to f of about 3250 px at 139.1 m. The person's speed is 25.1 px/s x 0.042 m/px = 1.05-1.08 m/s.
   This route does not depend on the person's depth or on f.
- Speed under each focal length: f = 3260 gives 1.07 m/s; f = 3075 (person 1.9 m) gives 1.135 m/s; f = 2800 gives 1.25 m/s.

## Answer
The answer is 1.10 m/s. It is weighted toward the person-height scale, as the plausibility rule requires, but nudged up because the boat suggests a
shorter focal length. Gait sway and bob would add about 1-2 % to the mean per-frame hip speed.
Confidence is moderate: the answer is likely within about 10 % of the truth.

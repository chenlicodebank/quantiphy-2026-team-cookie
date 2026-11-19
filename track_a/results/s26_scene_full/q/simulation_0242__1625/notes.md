# Q1625: length of the white (cream) horse

The file and question_fps are both 24 fps. The camera is static.

## Scale (focal length)
- Brown horse: a linear fit of torso_cx over frames 0-48 gives 5.94 px/frame and constant image y. The 48→49 step is an animation reset and is excluded.
- I back-projected its positions at frames 0 and 24 with the given depths (16.288 and 16.112 m), principal point at the image centre.
- Solving |Δp| = 0.874 m over 1 s gives **f ≈ 2605 px** (HFOV about 40°). Torso points and ground points give the same f (`f_est.py`).
- Check (`plane_check.py`): ground points of all three animals at t = 0 and t = 1 s, using the given depths, are coplanar to about 1 cm at f = 2600. The best fit is at f ≈ 2400, but the minimum is shallow and within the noise of the hoof line (±5-10 px), so it does not decide f. I kept the value from the prior.

## Cream horse pixel length
- The horse moves almost purely along camera x at z ≈ 14.9 m, so its body lies across the line of sight.
- Nose (grey head disc) to tail, read on zoomed, gridded frames:
  - frame 0: 412 px
  - frame 12: 413 px (the track's bbox missed the shaded tail, so I used 832-1245)
  - frame 24: 416 px
  - frame 36: 425 px tail-based, 452 px with the hind leg stretched back
- The track's bbox_w averages 423 px. I used 425 px as a typical full AABB extent.

## Answer
- Length = 425 × 14.9 / 2605 = **2.43 m**.
- Range: 2.36 m (nose to tail only) to 2.59 m (leg fully stretched).
- If f were 2400, the answer would be 2.64 m.

Confidence: moderate, about ±8%. The main uncertainties are f and which animation frame the AABB comes from.

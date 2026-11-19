# q_11 – boat length (prior: person height 1.75 m, no depth_info)

fps = question_fps = 24, so no re-timing issue (only sizes matter here).

## Observation: the view is oblique, not a true 2D/top view
The camera looks down at a tilt: the person's head and shoulder tops, the boat's deck, the cabin roof and its
near side wall are all visible. So vertical sizes (the person's height) are foreshortened by cos(phi),
while horizontal sizes across the image (the boat's length runs at only ~16 deg to image x) are not.
A plain pixel ratio (342 px boat / 48 px person x 1.75 m = 12.4 m) would therefore overestimate.
Perspective is weak (telephoto): the lean of the mast changes only slightly with image x (mast2.py,
f*cot(phi) ~ 4500 px), so I treat the projection as orthographic with tilt phi.

## Measurements (scripts in this folder)
- person.py: per-frame head-top / lowest-foot rows. The planted-foot plateaus are at y = 430, 455, 481, 507
  -> step = 25.6 px in image (foreshortened by sin phi), period ~17 frames. At mid-stance (end of each plateau,
  feet together) the head-to-toe extent is 38-40 px (39 px); at heel strike it is up to 47-49 px (stride spread,
  which is why a "height" of 45-49 px from the record is too large).
- shirt.py: shoulder/shirt width 14.5 px (half-max), ~15.5 px when the shaded side is counted (horizontal, so not foreshortened).
- Boat (scene record, checked on zoomed frames): bow tip to stern along the hull axis 342 px; image axis 15.8 deg
  (matches the direction of motion, tan = 0.283).

## Scale and tilt
- Horizontal scale from shoulders: 0.45 m / 15.5 px -> k ~ 0.029 m/px.
- Height at mid-stance: 39 px * k = 1.75 cos(phi) + 0.14 sin(phi) (toe ahead of head) -> phi ~ 55 deg.
- Check by the gait: step = 25.6 px * k / sin(phi) = 0.89 m, walking speed 1.25 m/s. Both are plausible. If I
  instead assume a 0.75 m step, I get phi = 60 deg and k = 0.0254. I adopted k = 0.0285 (phi = 55.5 deg).
- Boat in plan: tan(beta) = 0.283 / sin(phi) -> beta = 19 deg. The image length factor is
  sqrt(cos^2 b + sin^2 phi sin^2 b) = 0.983.
- L = 342 * 0.0285 / 0.983 = 9.9 m. Range from the alternative routes: 8.8 m (step 0.75 m) to 11.0 m (shoulder 0.46 m / 14.5 px).
- Sanity check: the wheelhouse comes out about 1.7 m long and about 2.2 m tall (its wall is 46 px vertically
  against about 37 px for the 1.75 m person), which fits a ~10 m fishing boat.

## Confidence
Moderate. The main uncertainty is the camera tilt (+-5 deg), which gives roughly +-10 % on the answer.
The naive 2D pixel ratio would give 12.4 m.

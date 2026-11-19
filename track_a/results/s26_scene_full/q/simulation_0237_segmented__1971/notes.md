# q_1971: length of the house (m). Prior: brown horse speed = 0.874 m/s

## Scene reading
- The camera looks straight down, so this is a top-down view. The "animal" in scene/ is the brown horse seen from above: wide rump on the left, and its head with a white blaze on the right. It walks to the right (+x).
- The house is seen from above as its roof:
  - Main gable roof: eaves at x 662–1361 (699 px) and y ≈95–715.5 (620.5 px). The ridge runs along y at x≈1018 (y 25–744.5).
  - A cross roof (the "band") lies on top of it: eave corners at x≈654–1377 and y 272–517, ridge at y≈379 with its points at x 618.5 and 1423.5.
- Perspective check, with the principal point at the image centre (960, 540): the main ridge ends project farther out than the eave corners by a factor k = 1.157 (top) and 1.165 (bottom). The ridge's x position also matches this: plan midpoint 1011.5 → predicted 1019.7, observed 1018. So it is a ridge roughly 14% of Z_eave closer to the camera. The cross roof gives k ≈ 1.11.
- The cross roof covers the main ridge, so it sits higher than the main ridge, and its eaves are at depth ≤ Z_ridge = Z_eave/1.16. Its true plan length is therefore ≤ 722 px × Z_ridge/f ≈ 0.89 × the main width: it only looks wider because it is closer to the camera.
- House AABB in plan: x = main eave width, 699 px at eave depth; y = 620.5 px at eave depth. Length (the longer horizontal extent) = 699 px at eave depth.

## Scale
- Horse pixel speed, from linear fits of the track (scripts in measure.py): x1 2.653, cx 2.667, brown_cx 2.680 px/frame. Mean 2.665 px/frame = 63.96 px/s.
  - This gives 0.874/63.96 = 0.01367 m/px at the depth of the horse's back.
  - Horse length 148 px ≈ 2.0 m, which is plausible.
- The eaves are higher than the horse's back, so they are closer to the camera and the scale there is smaller by the factor Z_eave/Z_horseback.
- The focal length cannot be pinned down without depth_info. Roof geometry gives f = 2520·tan(main pitch): f ≈ 1500–2700 px for pitches of 30–47°. Blender's default 50 mm lens gives 2667 px.
- I took f ≈ 2100 px, horse back height ≈ 1.3 m and eave height ≈ 3 m:
  - Z_horseback = 0.01367 × 2100 ≈ 28.7 m, so H ≈ 30 m.
  - Z_eave ≈ 27.1 m, so the factor is ≈ 0.944.
  - Over the plausible ranges (f 1500–2700 px, eave height 2.5–5 m) the factor is 0.90–0.96.

## Result
- Naive single scale: 699 × 0.01367 = 9.55 m. With the depth correction: 9.55 × 0.944 ≈ 9.0 m.
- Cross-check: the main roof's y-extent is 620.5 px → 8.0 m, so x is the longer side. The cross roof's plan length is ≤ 0.89 × 9.0 m, so it does not set the length.
- Answer: **9.0 m**.
- Confidence: moderate. The pixel measurements are good to about 1%. The main uncertainty is the unknown camera height relative to the roof, about ±5%. Reading the band as a structure at the same depth as the eaves would give up to 801 px × 0.01367 ≈ 11 m, but the occlusion evidence argues against that.

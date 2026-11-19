# q1970: width of the house (prior: brown horse speed = 0.874 m/s)

## What the scene is
The camera looks straight down. The "building" in scene/ is the house seen from above: a cross-gabled roof. The main wing's
ridge runs vertically in the image at x≈1018, and a cross wing runs horizontally with its ridge at y≈390. The "animal" is the
brown horse seen from above, with its white nose at the right. fps 24 = question_fps, so no re-timing.

## Measurements (measure.py, frame 0 mask plus scene/tracks/animal.csv)
- Horse pixel speed: linear-fit slopes are cx 2.667, x1 2.653, x0 2.615 and brown_cx 2.680 px/frame. The horse moves at
  constant speed. Frame-to-frame centroid steps are noisy because of the gait, so I use the fit: 2.65 px/frame = 63.6 px/s.
  Scale at the horse's visible back = 0.874 / 63.6 = 0.01374 m/px.
- House, main wing (image y-extent):
  - Eave corners y 98–712 at x=665 (614 px) and y 94–715 at x=1355 (621 px).
  - Ridge ends y 24–744 (720 px).
  - The gable ends are vertical, so the eave and ridge ends have the same world Y. Ridge/eave ratio about the principal point
    is 1.17, so the ridge is about 15% closer to the camera than the eaves. This confirms the top-down perspective.
  - Eave-level y-extent ≈ 617 px; the ridge value corrected by 1/1.17 gives 615 px, which agrees.
- House, cross wing (image x-extent): eaves 653–1378 (725 px), ridge 620–1423 (803 px, ratio ≈1.10, so ≈730 eave-px).
- Width is the shorter horizontal extent, so the main wing's y-extent ≈ 617 eave-level px. The length is ≈728 px.

## Scale and perspective
- Naive single 2D scale: 617 × 0.01374 = 8.48 m.
- The eaves are higher than the horse's back, so they are closer to the camera and the house's eave-level pixels are worth
  fewer metres.
- Estimate of the correction:
  - The horse is ≈2.0 m long, so the scene is near real scale.
  - Roof rise ≈2.4–3.5 m, which gives an eave depth Ze ≈ 6.9 × rise ≈ 17–24 m (hFOV about 50–70°).
  - The eaves are ≈1–1.5 m above the horse's back.
  - Depth ratio ≈ 1.04–1.09, so the corrected width is ≈7.8–8.15 m.
- Answer: 8.1 m. It sits between the corrected estimate and the naive 2D value, within 5% of 7.75–8.5.

## Second-route check
The ridge-level route (720 px / 1.17) gives the same eave-level extent as the direct eave measurement (615 vs 617 px).
The horse speed agrees within 1.5% across 4 reference points.

## Confidence
Medium. The pixel measurements are good to about 1%. The main uncertainty is the depth difference between the eaves and the
horse, which cannot be measured because no walls or ground are visible. It is worth about ±5%.

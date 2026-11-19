# Q393 – diameter of the police car's (van's) tyre

Prior: bike speed = 5.52 m/s. 2D convention (one m/px scale from the prior object), static camera, fps 24 (= question_fps).

## Scale
- Cyclist pixel speed: linear fit of scene/tracks/cyclist.csv ref_x, f6–76: 21.024 px/frame (f33–76: 21.031),
  residual std 0.44 px. Independent template cross-correlation of the helmet/upper-body band f36→f54: 378 px / 18 = 21.0 px/frame.
  (cyc.py; later xcorr frames failed when the van came close – not used.)
- m/px at the cyclist's depth = 5.52 / (21.03 × 24) = 0.010937 m/px.

## Tyre pixel diameter (wheelfit.py, prof.py)
- Radial edge search + circle fit (Kasa, outlier rejection) on the rear van tyre: f63 74.4, f66 74.2, f69 74.2, f72 73.9 px
  (54/69 edge points inliers); f60 75.5, f75 72.9. Front tyre fits contaminated by the blue chevrons/arch (75–82, not used).
- Direct row profile through the hub at f66: rear tyre x 802.5–875.3 (72.8 px), front 1077.7–1153 (75.3 px); rear tyre
  vertical 671.5–745.5 (74 px). -> **74 ± 1 px**. (The scene record's "≈68 px" was an underestimate.)

## Depth correction
- Ground-contact rows (tyre bottom edges): van 745.5, cyclist 738; horizon (main-street vanishing point) y ≈ 598.
  Flat ground → depth ∝ 1/(y − y_h): cyclist is 147.5/140 = 1.054 × farther than the van's near tyres.
- Uncorrected (pure single-scale 2D): 74 × 0.010937 = 0.809 m.
- Depth-corrected (tyre at van near-side depth): 0.809 / 1.054 = 0.768 m.

## Answer
The depth-corrected value is the physically right one, but the depth ratio rests on a 7-px contact-row difference
(±1 px → ±1 %). I answer 0.78 m, leaning toward the corrected value; it is within 5 % of both readings.
Sanity: bike wheel 66 px → 0.72 m; van wheelbase 275 px → 2.85 m (corrected); van height 188 px → 1.95 m. Plausible.
Confidence: moderate-high (±4 %).

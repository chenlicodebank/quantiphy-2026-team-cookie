# q_811 – width of the house (m)

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. fps = question_fps = 24.

## Horse / scale
- There are two horse-like animals. The brown one is "at the back": it trails behind the others (leftmost, x≈750 vs 975) and is
  also the upper/farther one. Its scale gives plausible sizes (length 144 px → 2.0 m). If the white animal were used instead, a horse would come out 1.4 m long, which is implausible.
- Speed (speed2.py): subpixel template matching of the rear/mid body at lags of 6, 12 and 24 frames gives 2.63, 2.63 and 2.61 px/frame.
  The scene centroid track gives 2.59 (net, 0→48) and 2.70 (fit slope). I used 2.62 px/frame = 62.9 px/s.
  Frame 49 is a loop reset and is excluded.
- Scale at the horse's body height: 0.874 / 62.9 = 0.01390 m/px.

## House (roof.py, gradient profiles on frame 0)
- Main block: ridge runs along y at x≈1018, with eaves at x=660.5 and 1362. The gable (rake) edges were measured on the clean right half and extrapolated:
  north side: ridge y=18.9, eave corner y=94.1. South side: ridge y=746.5, eave corner y=716.5.
- Perspective (principal point at 540): the ridge-to-eave image ratio is 1.169 (north) and 1.170 (south). This is consistent, so the camera
  is straight down and centred, and the roof top is about 15% closer to the camera than the eaves.
- The y-extent of the house in world units is the gable-to-gable distance: 622.4 px at eave-height scale (727.6 px at ridge scale).
- The x-extent is the cross wing, gable end to gable end: 811 px at wing-ridge scale, about 753 px at wing-eave scale. The wing sits higher than the main
  roof, so its world length is ≥ ~700 eave-px. That is longer than 622, so width (the shorter horizontal extent) = the main block's y-extent.

## Perspective correction
- Width = 622.4 px × (H − z_eave)/f, while 0.01390 = (H − z_horse)/f. So width = 622.4×0.01390 − 622.4×Δ/f, where Δ = eave height − horse-back height.
- Without the correction: 8.65 m. The roof perspective links f to the roof pitch: f = 2427·tan(pitch), giving f≈1700–2700 px for a pitch of 35–48°.
  With an eave ≈3 m and a horse back ≈1.4 m (Δ≈1.6 m), the correction is 0.37–0.6 m, giving 8.05–8.3 m.
- Answer: **8.25 m**. Other readings: no perspective correction gives 8.65 m. The main block's x span (702 px, the image-horizontal extent, which is not the shorter extent) gives ≈9.4–9.8 m.

## Check
- The perspective ratio is the same on both gables (1.169 vs 1.170). The ridge offset from the principal point (58 px vs 51×1.169 = 59.6 predicted)
  is consistent with the eave midpoint. Three independent speed estimates agree within 1%.
- Confidence: moderate. The main uncertainty is the eave-height correction (±4%), plus the choice of which extent counts as "width".

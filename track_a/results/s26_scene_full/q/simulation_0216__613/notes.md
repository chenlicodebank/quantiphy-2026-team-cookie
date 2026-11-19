# q_613: height of the table lamp's shade (m)

Prior: the black cat's speed is 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.

## Scale from the prior (cat depth)
- The cat walks left to right, parallel to the image plane. From scene/tracks/cat.csv (matched upper body), the
  mean step is 17.73 px/frame (869 px over 49 frames; torso centroid 863 px, nose 870 px). That is 425.6 px/s.
- Scale at the cat's depth: 0.94 / 425.6 = 0.002209 m/px.

## The lamp is farther back than the cat (perspective correction)
The video is labelled 2D, but the cat walks on the floor in front of the TV stand, and the lamp stands on the stand,
so one scale would be wrong. The camera looks horizontally at the wall:
- The top-surface side edges of the stand converge to a vanishing point near (980, 523–550), which is about the
  image centre.
- The ratios check out: top front/back edge y = 794/776 and leg feet front/back y = 985/≈952 give the same
  (h−Hs)/h ratio.

On a floor plane, 1/Z is proportional to (y − cy), with cy ≈ 535 (results change by less than 0.3 % for cy from 523
to 550). The depth ratios are:
- Cat origin: the cat's paws are planted at y ≈ 1017 (near side) and ≈ 1005 (far side), so its midline is at 1011
  (frames 6, 15, 24, 34, 43).
- Stand front, floor (leg foot) at y = 985: Z_front / Z_cat = 476/450 = 1.058.
- Lamp base: its bottom front is at y = 788.5 (column profiles) on the stand top, whose front edge is at y = 794:
  Z_basefront / Z_front = 259/253.5 = 1.022. Going from the front of the base to the lamp axis (radius ≈ 20 px)
  adds ≈ +0.7 %.
- Result: Z_lamp / Z_cat ≈ 1.089, so the scale at the lamp is 0.002406 m/px.

## Shade pixel height
Measured from vertical brightness profiles, averaging frames 0, 5 and 10 (shade_rim.py, measure_shade2.py):
- Silhouette: top 501.5, bottom 608.5–608.8 (pleat tips) at the centre column, so about 107 px.
- The bottom rim edge is almost flat, with ≈ 1.5 px of sag over its ≈ 96 px half-width. This gives a focal length
  of roughly 2700 px (very uncertain, 1800–4700).
- Silhouette extremes are the rim's front points, which are slightly closer to the camera than the lamp axis.
  Correcting them to the axis depth takes ≈ 2.6 px off the bottom and adds ≈ 0.5 px at the top. Corrected height
  ≈ 104.2 px.

## Answer
104.2 px × 0.002406 m/px ≈ **0.251 m**. Without the rim correction it would be 0.257 m; with no perspective
correction at all (the cat's scale) it would be 0.236 m.

## Checks
- With the same scale, the TV screen (399 px wide, about the lamp's depth) comes out at 0.96 m, a normal 43" TV.
- The camera height comes out at 1.05 m and the stand top at 0.446 m above the floor; both are plausible and
  consistent with each other.
- The cat's body length (nose to rump) comes out at 0.54 m, plausible.

Confidence: moderate. The main uncertainties are whether the prior's "speed" matches the mean pixel speed (±3 %),
and the depth ratio and rim correction (±3 %).

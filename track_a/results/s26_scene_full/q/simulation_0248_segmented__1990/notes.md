# q_1990: average speed of the white horse (prior: brown horse speed = 0.874 m/s)

2D side view, static camera, 24 fps (file and question rates agree). One metres-per-pixel scale for both horses: their hooves sit on the same image row.

## Which horse is which
- Left horse (scene's "red_horse"): bay/chestnut, mean RGB (77,42,39). Clearly brown, so it is the prior's **brown horse**.
- Right horse (scene's "brown_horse"): pale grey-brown, mean RGB (74,58,52), desaturated. It is the only other horse, so it is the **white horse**.
- Scale check: with brown = left, the scale is 0.0112 m/px. That makes the horses about 2.2 m and 2.6 m long and 1.9 m and 2.0 m tall, which is realistic, and the white horse walks at about 1.6 m/s, a normal pace.
  With the opposite assignment the horses would be about 1.4 m long and the speeds 0.47 to 0.87 m/s, which is less plausible.

## Measurements (measure.py; scene tracks re-checked)
- Brown (left) horse: torso template moves 156 px over frames 0 to 48, which is 3.25 px/frame. The bbox front edge also gives 3.25 and the centroid gives 3.20.
  At frame 49 the animation loops back to the start, so that frame is excluded.
  Scale = 0.874 / (3.25 × 24) = 0.01121 m/px.
- White (right) horse: the mean per-frame step is 5.937 px for the torso, 5.936 for the centroid and 5.9375 for both bbox edges. Vertical motion is negligible.
- Average speed = 5.937 / 3.25 × 0.874 = **1.597 m/s**.

## Second route
Using mask centroids for both horses: 0.874 × 5.936 / 3.197 = 1.623 m/s, which is 1.6% from the answer. The torso and bbox front edge give 3.25 for the brown horse and are more robust to pose changes, so they set the answer.

## Confidence
The measurement itself is good, about ±2%. The main risk is the colour-to-horse assignment: if the labels were reversed, the answer would be about 0.48 m/s.

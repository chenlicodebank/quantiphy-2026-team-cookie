# q_1958: length of the swimming ring (flamingo float), in metres

Prior: the black cat's speed is 1.041 m/s. depth_info is null. fps = question_fps = 24, so no re-timing is needed.

## Measurements (scripts in this folder)
- `catspeed.py`: a linear fit of the cat's centroid x over frames 0–49 gives 5.465 px/frame (bbox edges give 5.44 and
  5.46; the two halves give 5.59 and 5.34). That is 131.2 px/s at constant depth, so the scale at the cat's depth is
  1.041 / 131.2 = 0.00794 m/px.
- Float: the bbox width is 158 px in every frame (157–159). This is the ring's outer diameter, and the flamingo head
  stays inside it. The ring bottom (front ground contact) is at y = 1015, and the ring silhouette spans y ≈ 960–1015.
- `chairs.py` / `edges.py`: the static chairs show clear perspective. The floor is not 2D-flat: the back-row chairs
  span 142 px from leg to backrest top and the front-row chairs 165 px. The leg-bottom pairs are front row 900/870
  and back-left 857/834. The ground-plane relation (y − y_horizon) ∝ 1/Z, applied to these pairs, gives a horizon
  at y ≈ 578 ± 15. This also reproduces the back/front size ratio of 0.86.
- The cat walks on the ground with its feet at y ≈ 918, and the float lies on the ground with its centre's ground
  point at y ≈ 1002 (1015 minus the projected ring radius). The float is therefore nearer the camera:
  Z_cat / Z_float = (1002 − 578) / (918 − 578) ≈ 1.24. Moving the horizon between 565 and 590 changes this ratio to
  1.22–1.25.

## Answer
The scale at the float is 0.00794 / 1.24 = 0.0064 m/px, so the length is 158 × 0.0064 ≈ **1.01 m**.

Check: if the cat and float were assumed to be at equal depth (the plain 2D convention), the length would be 1.25 m.
I rejected this because the cat and float stand on a ground plane with visible perspective (rows of identical chairs
shrink by 14% over 44 px of ground height). The sizes are plausible: the cat is 0.84 m tail to nose, and a flamingo
ring of about 1 m is typical.

Confidence: moderate. The main uncertainty is the horizon line, which adds about ±3%. Choosing between perspective
and equal depth is a larger risk.

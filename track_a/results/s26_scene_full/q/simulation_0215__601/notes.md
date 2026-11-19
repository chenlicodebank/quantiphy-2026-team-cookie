# q_601 — length of the TV stand (m)

Prior: speed of the black cat = 0.94 m/s. The only moving animal is the black quadruped that the scene record
calls a "dog". It walks steadily to the right in a top-down 2D view. fps = question_fps = 24, so no re-timing.

## Scale (scale.py)
- Pixel speed from scene/tracks/dog.csv: mean per-frame speed is 11.10 (torso centroid, jittery), 11.03 (mask
  centroid) and 11.02 (nose) px/frame. All linear-fit slopes are 10.99. I use 11.0 px/frame = 264 px/s.
- Scale: 0.94 / 264 = 0.00356 m/px.

## TV stand pixel length (probe_tv.py, probe_right.py, probe_bar.py, frame 0)
- Left end: sharp grey step at x = 710 (it shows at rows 180, 230 and 280). Bottom edge at y ≈ 291, top edge at y ≈ 170.
- Right end: hidden under the round white lamp shade (circle fit: centre (1191, 224.6), r = 75.4). No console pixels
  show right of or below the lamp (floor grey ≈ 120 there), so the right end lies between x ≈ 1157 (where the lamp
  starts on the bottom edge) and ≈ 1225 (where the bottom-right corner would stick out of the lamp).
- To pin the end, I used the TV that stands on the console (a thin dark panel from x ≈ 811 to 1095, with feet at
  x ≈ 841 and 1063). Both give a TV centre of x ≈ 952.5. If the TV is centred on the stand, the right end is
  2·952.5 − 710 ≈ 1195. That falls inside the bound from the lamp occlusion.
- Length ≈ 1195 − 710 = 485 px.

## Answer
485 px × 0.00356 m/px ≈ **1.72 m** (1.67–1.83 m over the occlusion range).
Check: it fits the scene. The dog is about 191 px long (0.68 m including the tail) and the stand is a normal size
for a TV stand. The stand top is raised above the floor, so perspective may make it a few percent too large. I did
not correct for this, to keep the benchmark's single-scale 2D convention.
Confidence: moderate. The main uncertainty is the hidden right end (±15 px, about ±3%).

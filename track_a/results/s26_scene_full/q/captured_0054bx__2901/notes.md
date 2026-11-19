# q_2901: distance green ball – white ball at t = 1.0 s

- question_fps = file fps = 24, so t = 1.0 s is frame 24.
- "Green ball" = the small yellow-green (tennis-type) ball, called `yellow_ball` in scene/. The white ball is `white_ball`.
  Checked on frame 24 (frames/f24.png): the two small balls are motion-blurred and touching, yellow-green on the left, white on the right.
- Centres (scene record, colour split with the yellow rim excluded from the white mask, ref_quality good):
  green (323.86, 270.63) px, white (381.56, 248.36) px. They match the blob extents on the zoomed frame
  (green about x 290-357, white about x 352-408).
  My own quick HSV re-segmentation (measure.py, frames/mask24.png) gives green (325.7, 271.2) and white (377.7, 249.6).
  Its white mask picks up part of the yellow ball's pale rim, which pulls that centre left, so I kept the scene record's centres.
- Camera: f = 0.5959 x 1280 = 762.75 px, principal point (640, 360). depth_info is the Euclidean distance from the camera centre,
  so P = unit ray x distance, with distances green 1.331 m and white 1.235 m.
- Result: |P_green - P_white| = 0.1334 m (my own centroids give 0.1278 m; treating depth as z instead of Euclidean range gives 0.158 m, but that reading is not used).
- Sanity check: the white ball is closer (1.235 m) and appears slightly larger (48.5 vs 47.2 px blur width), which is consistent.
  The pixel separation of 62 px corresponds to about 0.10 m laterally, plus a 0.096 m range difference.
- Answer: 0.133 m. Confidence: moderate (about ±5 %). It depends on how the blurred, touching blobs are split.
  The orange-ball velocity prior is not needed for this distance.

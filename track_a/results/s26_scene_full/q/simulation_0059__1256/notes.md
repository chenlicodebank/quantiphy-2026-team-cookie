# q1256: width of the green car (m) -> 1.83

Labels: white car = white van (scene record "van"), yellow car = taxi. Green car = parked car facing the camera,
far down the main road (bbox ~1088-1172 x 728-786 at f64-71). It does not move. The file is 24 fps, the same as question_fps.

## 1. Focal length from the prior (measure_f.py)
Van track (patch_cx + constant offset to the bbox centre, v = 745.5). Each pixel is back-projected onto the near-vertical
plane through the two depth_info points (t=0.58 -> f14, d=43.812; t=1.58 -> f38, d=43.003). I took per-frame speeds, did a
linear fit of speed against time (and a quadratic fit of path length), and solved for a = 4 m/s^2:
f = 2210 px (f2-71); the windows f2-35, f36-71 and f10-60 give 2208 / 2215-2218 / 2190-2207. The given depths are reproduced
exactly by construction. The speed grows linearly (0 -> 11.8 m/s), so the acceleration really is uniform.

## 2. Distance to the green car (ground plane; ground2.py)
- Horizon y = 702. Two independent checks agree: the road-curb vanishing point (scene record) and the lamp posts left_near
  and left_mid (top/base lines meet at y = 702, the horizon at 0.55 of the post height).
- Camera height from objects with depth_info. Each object's horizontal distance comes from its back-projected origin
  (minus about 1 m to the near-side tyres for side-on vehicles), and its tyre or wheel contact row gives the angle
  below the horizon:
  van f14/f38 1.84/1.83 m, cyclist 1.80/1.80 m, taxi f14/f38 1.90/1.93 m (mean 1.85 m). The pedestrian gives 1.53 m;
  they stand on the raised sidewalk, so I left them out.
  Correction to the record: the taxi's tyre contact at f14 is y ~815 (checked on a 4x zoom), not the 803 in taxi.csv.
- Green car front tyre/shadow contact y ~786 (contacts.py, zoom). Camera-axis depth of the front: Zc = 48.8 m (distance 49.1 m).
- A free joint fit of horizon + height from the depths alone is badly conditioned (depth ratios are only 1.1-1.4). It
  drifted to a horizon of ~760, which the lamp posts and road contradict, so I did not use it.

## 3. Pixel width (green_px.py, green_width.py, averaged over f64-71)
Threshold mask: body and bumper x 1088-1171 = 84 px, mirrors about 85 px. Half-maximum edges: body 79-80 px, lower bumper
83.6 px. Used 83 px (the bbox should include the mirrors and widest part); the uncertainty is about +-2 px.

Width = 83 x 48.77 / 2210 = 1.83 m.
Spread: if the height comes only from van + cyclist, 1.80 m; only from the taxi, 1.89 m; horizon +-12 px gives 1.79-1.89 m.

## Second-route check
The taxi at f71 is front-on on the same road: 181 px wide, contact y 852. The same ground model gives a taxi width of
~2.2 m including mirrors, and a side-view taxi length of 299 px x 38.6/2210 = 5.2 m. The taxi:green width ratio is 1.2,
close to the real ratio of a Crown Victoria to a BMW (~1.18), so the green car's absolute width is plausible.
Confidence: moderate (about +-5%). The main uncertainty is the horizon and camera height.

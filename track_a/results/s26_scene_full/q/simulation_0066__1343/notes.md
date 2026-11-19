# Q1343 — length of the green car (m)

The green car is a static, parked teal coupe (BMW E24-like) on the far side of road B. It faces image-left, with its long axis along road B.
The prior (white van acceleration 4 m/s²) barely constrains the scale here because the depths already fix it. I checked it
(vanacc.py): with the given depths the van's ground-plane acceleration comes out at 3.9–4.5 m/s² for any focal length from 830 to 1800. So the scale comes from depth_info.
The file and question both run at 24 fps, and the depths are at frames 14 and 38.

## Camera (model.py)
- Vanishing points from curb lines fitted in code on scene/bg.png (curbs.py): road B far curb (its left and right parts are collinear,
  rms 0.35 px) and near-right curb give VP_B = (3128, 77). Road A right curb (rms 0.5 px) meets the horizon at VP_A = (620, 77).
- If the roads are orthogonal and the principal point is the image centre, f = 853 px (HFOV 103°, pitch 28.5°). Check: the predicted vertical vanishing point
  (1080, 2112) reproduces the visible lean of the lamp posts. Independent check (vpcal.py/pedcal.py): the pedestrian's
  3D step between f14 and f38 (from the given depths) is parallel to road B only for f ≈ 830–860.
- Camera height above the ground: from the pedestrian at f38 (pelvis (360,437), depth 21.3488 m; both feet on the contact line
  (356,482)–(391,476)): Hc = 6.886 m (±0.01 for ±4 px of pelvis error). The pelvis comes out 0.86 m above ground (plausible).
- Second route (carcheck.py): taxi f38 and van f38 wheel contacts combined with their given depths give Hc = 6.93/7.06 (taxi,
  root/centre origin) and 7.08/7.18 (van). That is 1–4 % above the pedestrian value.

## Green car (carlen.py, front.py)
Points are read in the clean background image at 6–10x zoom. Wheel contacts: front (1514.5,414), rear (1596,397.5). Near-rear corner (1626.5,372).
Near-front corner ≈ (1497,394). The far-front corner is the leftmost point, x = 1442.
- Wheel contacts on the ground plane give a wheelbase of 2.77 m, aligned with road B to within 0.5°.
- Overhangs come from solving (along-road offset, height) in the car's near-side vertical plane. Front: 0.73–0.80 m at h ≈ 0.4–0.6 m. This agrees with
  the leftmost far-front corner if the car width is about 1.55–1.6 m. Rear: 0.84–0.88 m at h ≈ 0.5–0.65 m.
- L = 2.77 + 0.75 + 0.88 ≈ 4.40 m with Hc = 6.886 m. The length scales with Hc. With the car-based Hc (6.93–7.18) L = 4.44–4.58 m.
  Corner-reading errors of ±3 px give ±0.1–0.15 m.
- If f is moved over 820–890 and Hc is re-derived for each, L = 4.31–4.56 m.

## Answer
L ≈ 4.45 m. This is the pedestrian-based 4.40 nudged toward the car-based camera height (mean Hc ≈ 6.97 m).
Confidence: moderate, about ±5 %. The main uncertainties are where the rounded front corner sits and the camera height (1–4 % spread).

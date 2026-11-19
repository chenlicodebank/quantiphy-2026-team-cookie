# q_1353 — height of the turning yellow car (taxi), simulation_0067 (3D)

Answer: **1.47 m** (world-AABB vertical extent, ground to the top of the roof sign).

Time base: file fps = question_fps = 24; depth times 0.58 s / 1.58 s -> frames 14 / 38.

## Camera
- Principal point taken at the image centre (1080,540), zero roll.
- Horizon y ≈ -45 (road vanishing points (2697,-43) and ≈(85..112,-47) from scene/).
- Vertical vanishing point fitted in code from 10 poles / lamp posts on scene/bg.png (poles.py; sub-pixel dark-centre line
  fits, rms 0.1-0.6 px): VPv ≈ (1073, 2632) -> f² = (VPv_y - cy)(cy - y_h) -> **f ≈ 1105 px** (per-pole 1089-1132).
  Independent check: orthogonal-roads VP pair gives f ≈ 1106-1125. Pitch ≈ 27.9°.

## Taxi geometry (taxi_h2.py)
- Hand-read on 4x crops and checked with drawn marks (marks.py, frames/mark_*.png): near-side wheel ground contacts
  (front + rear) and the centre of the roof sign's top face in frames 14 (left side visible), 50 and 62 (right side visible).
- Ground plane n·X = H (H = camera height). Per frame the car pose comes from the two contacts; the sign is modelled as
  R + a·x̂ + b·ŷ(far side) + c·up, (a, b, c) fitted jointly over the three frames (rms 1.4 px):
  c = 0.2127 H (sign top height), b = 0.138 H (contact line to centreline), wheelbase 0.409-0.428 H.
  c is insensitive to f (±0.5 % over 1100-1110); scanning b shows ±0.01 H in b -> ±2.3 % in c.

## Camera height H (metric scale from depth_info)
- Taxi's own depths, origin = car centre at half height: D14 -> H = 6.74 (≈6.81 with bbox centre ~0.2 m behind the
  wheelbase centre), D38 (origin below the sign top) -> H = 6.85.
- Cyclist f14 (pelvis on saddle, ground point on the wheel-contact line below it), D = 14.14: H = 6.96.
- Pedestrian (pelvis = bbox centre, feet at bbox bottom), f14/f38: H = 7.07 / 7.00 (on the sidewalk, so road H should
  be slightly larger; pelvis pixel uncertainty ±5 px).
- Adopted H ≈ 6.88 m (taxi-own routes weighted with the others) -> height = 0.2127 × 6.88 = **1.46-1.47 m**.
  Range: 1.45 (taxi depths only) to 1.49 (cyclist/pedestrian H).

## Sanity checks
- Same scale gives wheelbase ≈ 2.9 m and contact-line half width ≈ 0.95 m (a Crown-Victoria-type taxi: 2.91 m
  wheelbase), pedestrian stature ≈ 1.85 m, saddle height ≈ 0.72 m: realistic proportions.
- The van-acceleration prior (4 m/s²) route was tried (van_acc.py) but the van's bbox track is not a clean origin track
  (speed profile saturates, inconsistent with D38), so it was not used for scale.

## Ambiguity
- If the AABB excluded the roof sign, the roof height would be ~0.1-0.15 m less; the sign is part of the taxi model, so the
  full extent is reported.
Confidence: moderate-good (~±4 %).

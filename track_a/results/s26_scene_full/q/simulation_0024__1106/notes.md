# Q1106 – height of the boat (m)

Prior: boat speed 4 m/s. depth_info: 90.1103 m at t=1 s, 90.4360 m at t=2 s.
Time base: question_fps = 24 → t=1 s is frame 24, t=2 s is frame 48 (the file is 25 fps; frame indices used, not file seconds).

## Focal length (focal.py)
Boat origin ≈ hull-bbox centre (scene/tracks/boat.csv, checked on frames). Frame 24 → 48: du = −155.0 px, dv = −6.0 px
(roof centre: −155.6 px; linear fit over frames 12–60: 6.44 px/frame). Back-projecting with the two depths and requiring
|p48 − p24| = 4 m (24 frames × 4/24 m) gives f ≈ 3509 px (roof: 3525). Used f = 3510 px (hFOV ≈ 15.6°).
Check: boat length 396 px → ≈ 10.2 m, plausible for this fishing boat.

## Camera pitch (mast.py, height.py)
The mast's image slope changes with its image x across the clip (vertical lines converge to a vanishing point below
the image). Fitting the mast line in every frame (difference to a median background) and regressing slope against x:
Theil–Sen gives 1/(y_v − 400) = 8.2e-5 (CI 7.2–9.2e-5) → y_v ≈ 12,600 px → pitch ≈ 16° (14–18°). The visible deck
depth (~30 px for a ~3 m beam) agrees with ~15°.

## Height
Vertical extent mast top → hull/keel bottom (incl. rudder) measured in column profiles:
frame 24: 300.5 → ~660 px; frame 48: 297 → 653 px. A world-vertical line through the back-projected origin,
projected with pitch φ:
- φ=15°: H = 9.46 (f24), 9.41 (f48); φ=16°: 9.51 / 9.45; φ=0°: 9.22 / 9.17; φ=20°: 9.70 / 9.64.
Answer 9.45 m.

## Second route / confidence
The two frames (independent pixel extents and depths) agree to 0.6 %. Pitch uncertainty adds about ±2 %. The main risk
is a submerged part of the hull: the bottom looks visible down to a dark keel/shadow line at the waterline; if the model's
keel sits deeper under the water, the true AABB height would be larger. Medium-high confidence, about ±5 %.

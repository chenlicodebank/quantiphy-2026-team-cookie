# q 3111 — height of the gray table (internet_0049)

Prior: average speed of the scooter rider = 3.8 m/s. fps = question_fps = 30 (no re-timing; rider speed ~3.8 m/s and
height ~1.72 m with the resulting scale are plausible).

## Scale (one planar scale, internet convention)
Rider torso track (scene/tracks/rider_scooter.csv, checked: monotonic, left→right, frames 143–258 unflagged ends).
- Raw pixels: x 119.7 (f143) → 3667.8 (f258) = 3548 px / 115 frames = 30.85 px/frame = 925.5 px/s.
- Background-corrected: 31.3 px/frame (camera drifts ~0.3 px/frame; small).
- Whole crossing (scooter front at left edge f132 → rear leaves right edge ~f266): (3840+264)/134 = 30.6 px/frame.
Scale = 3.8 / 925.5 = 0.00411 m/px (range 0.00405–0.00414).
Sanity: rider cap-to-sole 420 px → 1.72 m.

## Table pixel height (measure_table.py, frame 0, column profiles + zooms)
Gray metal picnic table, front left. Top front edge of the tabletop (slat ends) starts at y≈1267; front leg bottoms
(x≈380–455) end at y≈1495–1497 → height ≈ 228 px (scene record said 220; the far edge of the top surface at y≈1252 would give 243).

## Answer
228 px × 0.00411 = 0.937 m → 0.94 m. Second route (whole-crossing speed 30.6 px/frame) → 0.944 m.
The table stands nearer the camera than the rider's path, so the true table height is probably ~0.75 m. The
annotation convention uses a single scale with no perspective correction, so I report the planar value.
Confidence: moderate (±5% from the pixel height and the averaging window).

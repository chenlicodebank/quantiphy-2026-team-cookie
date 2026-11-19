# Q2107 — tea cup diameter (mm); prior: mouse width = 57 mm

Static top-down camera; the mouse and the cup are static, so time base (16.67 vs 25 fps) is irrelevant.
Mouse and cup lie on the same desk plane, so one planar scale is used (internet convention).

## Mouse (prior object) — mouse2.py / measure.py
White mouse segmented (V>th, S<70), minAreaRect at frame 35 (same at frames 0 and 20):
width 104.5 / 103.6 / 102.5 / 101.2 px for thresholds 120/145/170/200 -> 103.6 px (mid-edge threshold).
Length 199 px. Scale = 57 / 103.6 = 0.550 mm/px.

## Tea cup — rim.py
Intensity profiles through the cup centre at frame 35 (3 rows, 3 columns):
- horizontal: outer edge of the lip at x ~1185 (left), ~1370 (right) -> ~185 px; lip highlight 1188 -> 1365 = 177 px
- vertical: outer edge y ~1022 (top), ~1204 (bottom) -> ~182 px; highlight 1026 -> 1201 = 175 px
Outer rim diameter ~183 px (saucer is ~250 px, a separate object).
Diameter = 183 x 0.550 = 100.7 mm (lip-highlight reading 176 px -> 97 mm).

## Check
Mouse aspect 199/103.6 = 1.92, close to an Apple Magic Mouse (113.5 x 57 mm, 1.99). Scaling by the length
instead gives 113.5/199 x 183 = 104 mm. A ~10 cm tea cup is plausible.

Answer: 101 mm. Confidence: moderate-good (edge reading ±3 px on cup, ±1 px on mouse -> ~±4 %).

# q_535 – length of the letter under the gun (simulation_0203)

File fps = question_fps = 24. Script: `measure.py`; crops in `frames/`.

Object: the revolver lies on a white card/letter between the alarm clock and the telephone (the scene record calls it
"scissors_inkwell_card"; the "scissors/keys" is a revolver). The card lies flat on the desk, its edges aligned with the image x axis (its
side edges converge toward the central vanishing point as expected).

Card pixels (frame 29, brightness > 120 row scans): back edge y 984, x 1192-1375 (183 px); front edge y 1001,
x 1197-1387/1388 (191 px); centre row ~992 -> ~187 px. Its depth extent is only ~17 px tall, which works out to
about half the width, so the horizontal side is the length.

Scale from the prior (magnifying glass in free fall, frames 0-10): ring-centre track 205, 212, 232, 265, 310, 369,
440, 524.5, 621, 731, 853 px. Its second differences average 12.94 px/frame^2, which is 7452 px/s^2 (a quadratic
fit gives 7380). The record's bbox-centre track gives 7488. Adopted value: 7430 +- 60 px/s^2, so 9.8/7430 = 1.319 mm/px
in the glass's fall plane.
Check: glass length 162 px -> 0.214 m and ring diameter 104 px -> 0.137 m, both plausible.

Perspective: the glass rests at the same depth it fell at (ring width 104 px both in the air and at rest). It rests
with its footprint centre at y ~1019; the card centre is at y ~992. Ground-plane scale goes as (y - y_horizon).
The card's own edges give a horizon near 595 (183 vs 191 px over 17 rows); a level camera would give 540. The
card's scale is therefore 0.936-0.944 of the glass plane's, so the card is ~6 % farther away.

Length = 187 px x 1.319e-3 / 0.94 = 0.262 m (0.261-0.264 across the horizon range). Without the depth correction it
would be 0.247 m.
Confidence: moderate-good, about +-4 %.

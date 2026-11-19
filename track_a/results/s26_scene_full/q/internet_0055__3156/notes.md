# q 3156 – width of the Bicycle sign (m)

Prior: average speed of the "person riding scooter" = 1.95 m/s. No scooter is visible in this clip; the only moving
person is the woman crossing right to left (scene/tracks/pedestrian.csv), so the prior's object is taken to be her.
Time base: file fps = question_fps = 30, so no re-timing.

## Scale (single factor, internet convention)
Pixel speed of the person over frames 0-74 (scripts: answer.py). The walk is steady, so the mean per-frame speed equals
the net speed:
bbox_cx 248.5, stab_bbox_cx 251.6, head-top 242.3 / 245.8 (stab), centroid 241.6 / 244.9 (stab) px/s -> mean 245.8 px/s
(spread ±2.5%). Scale = 1.95 / 245.8 = 0.00793 m/px.

## Sign
Yellow diamond with the bicycle symbol. "Width" = horizontal extent across its face, i.e. tip to tip (the sign is
mounted as a diamond). Measured on frame 0 on zoomed crops plus a row profile (prof.py, sign.py): outer rim from
x≈870.5 to x≈1032, so 161-162 px (scene record: 161 px). The yellow area inside the black border alone is 152 px, and
the same at frames 37 and 74 (static sign).
Width = 161.5 px × 0.00793 = **1.28 m**. (Other reading: inner yellow only, 152 px -> 1.21 m. Square side
= 161.5/√2 px -> 0.91 m.)

## Check / confidence
Other reference points give 1.25-1.30 m. Sanity check: at this scale the woman (about 290 px tall) would be about 2.3 m,
so 1.95 m/s is fast for her, and the sign also sits at a slightly different depth. Even so, the annotators' convention is
one scale from the prior, so I answer with 1.28 m. A real 30-36 in diamond has a 1.08-1.29 m diagonal, which is consistent.
Confidence is moderate, because the prior names a "scooter" rider and I am assuming it means this person.

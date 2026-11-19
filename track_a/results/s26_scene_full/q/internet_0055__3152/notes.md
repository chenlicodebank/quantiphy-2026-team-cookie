# Q3152 – height of the DO NOT ENTER sign (m)

Prior: average speed of the "person riding scooter" = 1.95 m/s. No scooter appears anywhere in the 75 frames.
The only moving person is the woman walking from right to left (scene/tracks/pedestrian.csv), so the prior must refer
to her (mislabelled). Time base: 30 fps for both the file and the question, so no re-timing.

Convention (internet video): one scale = prior world value / prior pixel value, no perspective correction.

## Prior pixel speed (measure.py)
Mean per-frame displacement of the pedestrian reference point over frames 0-74:
- bbox centre: raw 8.36, 5-frame smoothed 8.37, net 8.29 px/frame
- head top: 8.18 raw; mask centroid: 8.99 raw (noisy), 8.34 smoothed
- background-stabilised bbox centre: 8.46 px/frame (camera drift is about 1%)
Used 8.35 px/frame = 250.5 px/s -> scale = 1.95 / 250.5 = 0.00778 m/px.

## Sign pixel height (measure.py, sign_edges.py, sign_bottom.py; overlay frames/sign_mask_36.png)
The panel is rolled about 3-5 deg and seen slightly from below.
- Frame 0, at the panel centre column: top edge y≈144 (sky/panel step), bottom edge y≈285 (white border/trees step) -> about 141 px
- Frame 36: about 140 px. Panel width across its face: 148 px (rows 170-200).
- The axis-aligned bbox including the roll is about 148-150 px (the scene record gives 150).
Used 143 px, between the vertical extent at the centre and the rolled bbox.

## Answer
143 px x 0.00778 m/px = 1.11 m (range 1.10-1.17 m, depending on whether 141 or 150 px is used).
Other reading: the whole sign including the post (top y≈145 down to the post base, about 430+ px) would be about 3.4 m.
Not used, because "sign" normally means the panel.
Sanity check: real DO NOT ENTER panels are 0.76 m. The prior's 1.95 m/s is fast for a walker (a person-height scale
gives about 1.4 m/s), so every value converted with this prior comes out about 1.4x larger than real. That follows from
the prior, not from a measurement error.
Confidence: moderate. Uncertainty comes from the prior-object identity and the edge reading (±3%).

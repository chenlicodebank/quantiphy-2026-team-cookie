# q_2114 — length of the grey notebook (cm); prior: mouse width = 57 mm

Object: the dark grey closed notebook at the top right of the desk (centre ≈ (3065, 992) px, rotated ≈15° from
horizontal); the scene record calls it "dark tablet top right". It and the white mouse are static, so the time base
(16.67 vs 25 fps) does not matter. Measured on frame 35, checked on frame 0 (same values).

Scale (single 2D scale, internet convention): mouse short side (width) = 102.5 px
(minAreaRect of white mask at V thresholds 140–200: 101.2–103.8 px; half-max width profiles: median 102.25 px).
→ 57 / 102.5 = 0.556 mm/px.

Notebook long side: low-saturation run along the long axis at 7 offsets across the cover = 364–370 px
(median ≈ 369 px). Lines drawn on frames/chk.png fit the outer edges, including the light rim. The minAreaRect of the colour mask
gave 400–406 px, but that mask spills into shadow and the pen at the top left, so I rejected it. Short side ≈ 248 px.

Length = 369 × 0.556 = 205 mm → **20.5 cm** (width ≈ 13.8 cm, close to A5 at 21 × 14.8 cm, so it is plausible).

Second route: the mouse's length is 198 px. Its ratio to the width (1.93) matches a Magic Mouse's 113.5/57 = 1.99. Taking the scale from the
mouse length instead would give 21.2 cm, so the answer is stable to about 3%.
Confidence: good (±4%).

Scripts: measure.py, profile.py, drawchk.py, mouse_sweep.py.

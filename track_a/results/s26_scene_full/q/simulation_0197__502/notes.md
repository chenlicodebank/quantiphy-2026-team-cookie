# Q502 – bubble speed at t = 0.5 s

Time base: fps = question_fps = 30 → t = 0.5 s is frame 15; speed = |p15 − p14| × 30.

Scale (2D, one m/px from prior): the "SKYNOVA" text runs vertically on the bottle (only "NOVA" visible, x≈1106–1185,
y≈2040–2560). Its horizontal image extent (letter height) measured in code (`measure_text.py`, white low-saturation
pixels, per-letter column extents) = 78, 79, 78 px → 78 px. Scale = 0.00188 / 78 = 2.41e-5 m/px.
Sanity check: bottle ~1160 px → 28 mm, bubble ~103 px → 2.5 mm, pipette ~145 px → 3.5 mm — plausible proportions.

Bubble motion (`track.py`): template matching (TM_CCOEFF_NORMED, sub-pixel parabola) with templates from frames
10, 15, 20 (independent routes). Step 14→15 = 10.50 / 10.40 / 10.38 px (mean 10.43); neighbouring steps
13→14 ≈ 10.3, 15→16 ≈ 11.0 (smooth acceleration, consistent). Scene record's hull centroid gave 11.95 px (noisier, ±1–2 px).
Used 10.45 px/frame → 313.5 px/s → 0.00756 m/s.

Confidence: motion well measured (±2%); main uncertainty is the interpretation of "horizontal width" of the text
(taken as its horizontal extent in the image = 78 px, ±2 px).

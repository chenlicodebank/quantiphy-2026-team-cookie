# q498 — width of the droplet (simulation_0197)

2D close-up render, static camera, 30 fps (question_fps matches; no retiming). The drop hanging from the pipette tip
does not change over frames 0–49 (identical measurements at frames 0, 25 and 49).

Prior: horizontal width of the "skynova" text = 0.00188 m. Only "NOVA" is in frame. It is printed vertically (rotated),
so its horizontal extent is the letter height across the word. measure.py / measure2.py: white-letter mask on the amber
label, x = 1106–1186 px with a half-max threshold → **81 px** (thresholds of 0.7 and 170 give 79–80; every letter spans
76–78 px). Scale = 0.00188 / 81 = 2.32e-5 m/px.

Droplet = the teardrop of serum hanging below the tip (y ≈ 1840–2035). Its widest point is the lower bulb near
y ≈ 1975–2000. Strongest horizontal-gradient edges there are at x ≈ 201 and 308 → **107 px** (scene record: 105 px; on the
2x zoomed crop by eye: about 200–309).

Width = 107 × 2.32e-5 = **0.00248 m**.
Check: with the record's 105 px and an 80 px text width, the result is 0.00247 m; the full range across these methods
is 0.00244–0.00252 m. Confidence is moderate to high. The main risk is how "horizontal width of the text" is read; I
assumed it means the on-screen horizontal extent of the rotated word, because the word's length runs out of frame.

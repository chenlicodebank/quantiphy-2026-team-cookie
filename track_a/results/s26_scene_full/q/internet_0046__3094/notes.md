# q 3094 — displacement of the cup between 1.10 s and 1.30 s (cm)

- fps = question_fps = 30 → frames 33 and 39 (both have the mug body fully in frame). The camera is static (per scene/ record; the baseboard caps don't move in my frames).
- Scale (prior: cup height 10.5 cm): body height rim→base measured in code (background difference, central columns):
  f33 566 px, f39 577 px; scene record 570 / 581. I used ≈572 px → 0.01836 cm/px.
- Reference point = body centre (handle excluded). Record: x 862.6 → 1608.2, y 590 → 601.5 → 745.7 px.
  Check by eye on gridded frames: body edges f33 ≈628–1080, f39 ≈1352–1850 → centre shift ≈747 px.
  Single edges disagree (left ≈724–732, right ≈755–765) because motion blur widens the body at higher speed; the centre averages that out.
- Displacement = 746 px × 10.5/572 = 13.7 cm (range 13.4–14.0 depending on height frame / edge choice).
- Scripts: look.py (record + frames), edges.py (edge/height measurement).
- Confidence: moderate-high (±3 %).

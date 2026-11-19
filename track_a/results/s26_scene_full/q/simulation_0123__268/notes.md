# q_268 – diameter of the blue cup with the blue toothbrush

- Scene: top-down 2D Blender render, 24 fps (file fps = question_fps, so no re-timing).
- Prior: "speed of the cup = 0.338 m/s". The only moving object is the teal box/cup on the counter below the left
  basin (checked on a contact sheet; the round toothbrush cup is static), so the prior refers to that object.
- Pixel speed (measure.py, teal mask centroid, frames 2–71): 14.537 px/frame linear fit (per-frame steps 14.53 ± 0.22)
  -> 348.9 px/s. Scale = 0.338 / 348.9 = 9.69e-4 m/px.
- Toothbrush cup at (830, 415): colour-mask bbox 46 px in x (48 px in y because the toothbrush head sticks out at the top);
  minimum enclosing circle 46.6–47.3 px; area-equivalent 44.6–45.6 px; radial saturation profiles in 8 directions
  put the edge at r ≈ 23–24 px. Diameter taken as 46.5 px.
- Diameter = 46.5 × 9.69e-4 = 0.0450 m.
- Second-route check: the scene record gives an independent Ø of 46.5 px and the same 14.54 px/frame speed; those also give 0.045 m.
  Sanity check: a 4.5 cm cup is small but plausible for this scale (the box is 7.6 × 4.3 cm).
- Confidence: moderate-high (±3 % from the edge definition). It also assumes the prior's "cup" is the moving object,
  since nothing else moves.

# q_2250 — "What is the height of the book in cm?"  →  1.7 cm

Video: lab capture, 1280x720, 24 fps (file fps = question_fps = 24). The book is the light-blue hardcover pocket
notebook lying flat on the table, right of the white board (static the whole clip; the scene/ record's "notebook").
Height = vertical extent = its thickness (the book lies flat). Other reading (book "height" = long side of the
cover): about 14–18 cm depending on camera pitch (see below); width across ≈ 8.6 cm. I answer with the vertical-extent reading.

## Measurements
- Frames 36–48 averaged (ball gone, camera static). f = 0.5959·1280 = 763 px, principal point (640,360).
- Front face of the book (prof.py, vertical colour profiles at x = 645…670): blue top surface → dark cover edge →
  white page band → contact shadow on wood. Face from y≈429.5 to ≈435.5 at x=655 (similar at the other columns):
  **6.0 ± 0.7 px** vertical extent.
- Distance: depth_info book = 1.665 m (t=0) to the book centre.
- Converting a vertical extent needs the camera pitch (vertical lines are foreshortened by the oblique view).
  Pitch estimates:
  - table-top right angles from code-fitted front/left/right silhouette lines (table_vp.py): 27.6° (±0.6° under line noise),
    28.9° when the back edge is added; the vanishing point of the table leg lands at x≈639 ≈ cx for pitch 28°;
  - cup rim ellipse (minor/major ≈ 17/37 px) → ~29°;
  - right angles of the book's top face (pitch_rect.py) → ~30–35°;
  - a 9×14 cm pocket notebook aspect → ~40°;
  - a plane through the cookie/pen/book depth points → ~50°. This is an outlier: the cookie stands upright and
    the pen is thin and black, so their depths are poor.
  Adopted pitch: ~30° (range 28–35°).
- thickness.py (exact ray geometry: bottom edge on the table plane, top = bottom + normal·t, anchored on the book centre at
  1.665 m): pitch 28° → 1.54 cm, 30° → 1.59, 33° → 1.66, 35° → 1.71, 40° → 1.87 (±0.7 px ≈ ±0.18 cm).

## Answer
1.7 cm (centre of the 1.55–1.87 cm range, which covers the plausible pitch range). Sanity check: a pocket hardcover notebook
(about 9 × 14 × 1.5 cm) matches the measured width of 8.6 cm and a thickness of about 1.5–1.9 cm.
Confidence: moderate. The face is only ~6 px tall, and the pitch is uncertain.

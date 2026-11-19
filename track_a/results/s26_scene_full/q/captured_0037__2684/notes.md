# q_2684 — width of the tape (cm)

File fps = question_fps = 24; t = 1.0 s -> frame 24. Camera static (scene record), tape roll static.

## Method (lab method card)
- f = 0.5959 x 1280 = 762.75 px. Tape = translucent packing-tape roll lying flat on the table, centre ~(556,451).
- Width read as the roll's horizontal extent across its face (= outer diameter; a flat round roll has equal
  length/width). Measured in code (measure.py): row intensity profiles across the roll's side band, rows 440-468,
  frames 0/10/24/40/48 (identical, static). Gradient edges L=519.5-521.5, R=591.5 -> 70-72 px; half-intensity edges
  70-71 px. Rows where the jar's edge leaked into the window (~96 px) were discarded. Use 71 px.
- Size = d x px / f = 1.038 m x 71 / 762.75 = 0.0966 m -> 9.66 cm (70 px -> 9.53 cm). Answer 9.6 cm.
  (Using Z instead of range: 9.5 cm.)

## Checks
- White cup: 73 px at 0.845 m -> 8.1 cm (plausible tumbler). Glass jar: 57 px at 1.008 m -> 7.5 cm (plausible).
- Dark card (credit card?) horizontal extent 107 px at 0.679 m -> 9.5 cm vs 8.56 cm standard (card slightly rotated,
  extent includes a diagonal component) — scale consistent within ~10%.
- Ping-pong ball prior: at frame 24 the ball's vertical extent (little vertical blur at apex) is ~20-21 px, mask width
  ~24-26 px -> 2.9-3.6 cm at 1.055 m, below 4 cm. The small, blurred, low-contrast ball is a poor ruler; if it were used
  as the scale the roll would be ~12-13 cm. The method card (depth x pixels / f) is followed instead.
- Alternative reading (band width of the tape = roll height): not separable from the top-ellipse foreshortening in
  this view (total vertical extent 43.5 px); not used.

Confidence: moderate (diameter reading ~9.6 cm, ±5% from pixel edges; reading ambiguity is the main risk).

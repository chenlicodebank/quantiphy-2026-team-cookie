# q_1922 — width of the box (m)

2D clip at 120 fps (the same rate as question_fps). The scale comes from the prior: the box falls with a = 9.8 m/s² before 0.6 s.

## Method (fit.py)
- Track: scene/tracks/box.csv `front_top_y`, a sub-pixel top edge of the front face. I checked that it follows the falling box, which is released at about frame 4 and lands at about frame 60.
- The per-frame steps are irregular because of stalled frames in the baked simulation, so I fitted a parabola over a window of frames instead of using one-frame differences:
  - Quadratic fits over frames 5–60, 5–45, 10–60, 8–58 and 20–60 give 2000–2055 px/s².
  - Fits with a free release time t0 and cutoffs at frames 50–60 give 1997–2048 px/s².
  - I adopted a = 2030 px/s², which gives a scale of 9.8 / 2030 = 4.83e-3 m/px.
- Box width: the front face's horizontal extent is 280.5 px during the fall and 281.1 px at rest, constant to ±0.35 px. I used 280.8 px, which gives **1.355 m** (range 1.34–1.38 across the fits).

## Checks
- Truck rear body: 566 px → 2.73 m wide and 512 px → 2.47 m tall. Door frame: 246 px → 1.19 m. These are plausible for a box truck, so the scale is realistic.
- Second route: the free-t0 fits at different cutoffs give 1.342–1.376 m, which is consistent.
- Ambiguity: the box's depth extent cannot be seen from the front view. I took the visible horizontal extent across the face as its width.

Confidence: moderate-high on the scale (±2%). The main open risk is the width-versus-length reading.

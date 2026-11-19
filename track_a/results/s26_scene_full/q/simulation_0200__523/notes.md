# q_523 — height of the droplet (m)

2D video, 60 fps (file and question_fps agree). Scale comes from the prior: a = 9.7 m/s².

- Pixel acceleration (measure.py plus quadratic fits): from the scene centre track, frames 1–11: 104,133 px/s²; frames 2–11: 103,928;
  from my own tip-top track, frames 3–11: 103,964; from the bottom edge, frames 3–9: 103,800. Mean is ≈ 103,950 px/s².
  The per-frame second differences are about 28–31 px/frame², so the acceleration is uniform.
- Scale = 9.7 / 103,950 = 9.33e-5 m/px.
- Drop height (vertical, tip to bottom) on clean frames 0 and 3–8 is 85–86 px, both in my diff mask and in the scene record. I used 85.7 px.
- Height = 85.7 × 9.33e-5 ≈ 0.0080 m.
- Second route: four independent tracks (centre, top, bottom, different frame windows) give acceleration within ±0.2 %. Height is stable at ±1 px across frames.
- Confidence: high (about ±3 %). The main uncertainty is the mask threshold at the soft bottom edge.

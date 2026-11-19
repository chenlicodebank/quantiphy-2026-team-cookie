# Q890: height of the plant (m)

2D scene with a static camera. The file plays at 24 fps, but question_fps is 30, so all timing here uses 30 fps. At 30 fps, "before 0.5 s" means frames 0 to 15, and frame 15 is the last free-fall frame. That fits.

## Scale (prior: the pen falls at 9.8 m/s²)
- I fitted a quadratic to the pen centre cy over frames 3–15 (`scene/tracks/pen.csv`, using `measure.py`).
  - Result: 6.868 px/frame². The residuals are ≤ 0.5 px, and the curve's vertex is at frame −0.1, so the pen is released at t = 0.
  - At 30 fps that is 6181 px/s², which gives a scale of **1.586 mm/px**.
- Plausibility check with this scale:
  - LG outdoor AC unit: 506 px → 0.80 m. Real units are about 0.77–0.87 m. Good.
  - Table: 1021 px → 1.62 m. Good.
  - Pen: 65 px → 0.10 m.
- With 24 fps instead, the AC unit would be 1.25 m and the table 2.5 m, which are implausible. That supports using 30 fps.

## Plant pixel height (frame 38, intensity profile in `measure.py`)
- The plant is a white cup with a succulent, and I took the whole potted plant as "the plant".
- Top of the leaves: y ≈ 808.5.
- Bottom of the cup, where it meets the table, before the reflection on the glossy top: y ≈ 871.
  - This agrees with the pen's bottom contact at rest, y ≈ 869.6.
- Height: 62.5 px (±1.5 px).

## Answer
62.5 × 1.586 mm = **0.099 m**.

The cup alone, from rim (≈ 831) to bottom, is about 40 px, or 0.063 m. The leaves alone are about 22 px, or 0.035 m. I answered with the full potted-plant bounding box.

Confidence: medium-high on the scale. The main uncertainty is whether "plant" includes the pot.

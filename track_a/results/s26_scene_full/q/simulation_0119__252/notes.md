# Q252: diameter of the moving chess piece (m)

The video is a 2D top-down render. One metres-per-pixel scale comes from the prior (speed = 0.04 m/s).

- **Pixel speed:** from the scene circle-fit track (`circ_cy`), frames 0–35, before the stop at frame 36.
  - Linear fit: 1.398 px/frame.
  - Mean of the per-frame steps: 1.399 px/frame.
  - Net displacement / 36 frames: 1.397 px/frame.
  - The quadratic term is negligible, so the motion is uniform.
- **Speed in px/s:** 1.398 × 24.012 fps = 33.58 px/s. Using question_fps = 24 instead changes this by 0.05%.
- **Scale:** 0.04 / 33.58 = 1.191e-3 m/px.
- **Pixel diameter** (`measure.py`, rest frame 43):
  - The scene record's fixed-radius circle fit gives 34.3 px.
  - Frame 43 minus frame 0 as a difference mask: bbox 36 × 35 px at threshold 30, 37 × 35 at threshold 20.
  - Equal-area diameter: 33.5–35.5 px.
  - A zoomed visual read gives about 34.4 × 33.8 px.
  - Adopted value: 34.5 px.
- **Diameter:** 34.5 × 1.191e-3 = **0.0411 m**. The spread across pixel estimates is 0.0409–0.0417 m.
- **Check:** the board's square pitch is 33.6 px, so the piece moves exactly 1 square/s, which makes a square 0.040 m. The piece's footprint is about one square wide, which agrees with the answer.

Confidence: high (about ±3%).

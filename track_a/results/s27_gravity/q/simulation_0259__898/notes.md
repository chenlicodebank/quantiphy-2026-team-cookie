# Q898 — height of the plant (m)

Prior: the red cup falls with 9.8 m/s^2 before 0.5 s. The video is a 2D scene at 30 fps, and question_fps is also 30.

## Scale (measure.py)
I fitted quadratics to the cup track (scene/tracks/cup.csv) over the free fall, frames 0–14:
- top_y (lid edge, the cleanest point): 7.00–7.03 px/frame^2. Its second differences are all 7, with one 6/8 pair.
- cy (bbox centre): 6.91–6.96 px/frame^2. bottom_y: 6.82–6.90, lowered slightly by the shrinking underside ellipse.
- I used 6.98 px/frame^2 = 6282 px/s^2, so the scale is 9.8 / 6282 = 1.560 mm/px.

## Plant (base.py, measure.py; frame 39)
- The top of the leaf tips is at y ≈ 808, where non-blue pixels first appear above the wall.
- The bottom of the pot foot is at y ≈ 869–870. Below that is the table and the pot's reflection. The cup's contact line is at y = 871, so the cup and plant stand at about the same depth and the same scale applies.
- The plant's total height is 61–62 px (the scene record says 61). The lines drawn in frames/plant_lines.png confirm this.

## Result
Height = 62 px × 1.560 mm/px ≈ 0.097 m (0.095 m with 61 px).

## Check
With this scale the cup is 65 px ≈ 0.10 m tall and its lid is 42.5 px ≈ 0.066 m across, which is a plausible small paper coffee cup. The plant is a small succulent in a pot about 7 cm wide (47 px), which is plausible.

Confidence: good, about ±4% from the base edge and the reflection.

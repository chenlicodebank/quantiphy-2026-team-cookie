# q_899 — width (diameter) of the potted plant

2D scene, file fps = question_fps = 30. Prior: the red cup falls with a = 9.8 m/s² before 0.5 s (free fall in frames 0–14, impact at frame 15).

## Scale (measure.py)
I fit a quadratic to the cup's vertical track over frames 0–14 (scene/tracks/cup.csv):
- mask centroid_y: 6265 px/s² (resid 0.16 px); bbox cy: 6266; top_y: 6323; bottom_y: 6205.
- top_y and bottom_y are biased in opposite directions by perspective (the underside ellipse shrinks as the cup falls), so the
  centre (centroid, which is about the mean of top and bottom) is the origin: a = 6265 px/s².
- That gives a scale of 9.8 / 6265 = 1.564e-3 m/px. Check: the cup comes out 65 px = 0.10 m tall with a 42.5 px = 0.066 m rim,
  which is a realistic paper cup.

## Plant width (plantw2.py, frame 39)
The plant is a white pot with a yellow-green succulent, bbox about x 1083–1130, y 809–870. It stands on the back of the table,
at the same depth as the cup's landing point (contact line y ≈ 870 vs 871), so the same scale applies.
- Colour distance from a wall model, scored per column: the leaves span x 1085–1130 and the pot 1085–1128. The pot's left side is
  shaded, and the zoomed image shows its edge near x 1082.5. Overall width = 45–47 px, best estimate 46 px.
- Width = 46 × 1.564e-3 = 0.072 m (0.0713 m if the top_y acceleration is used instead).

Second route: the scene record's independent box gives the pot at 47 px, which is 0.0735 m. Both routes agree within 3 pct.
Confidence: moderate to high. The main uncertainty is the soft left edge of the pot (±1 px, about 2 pct).

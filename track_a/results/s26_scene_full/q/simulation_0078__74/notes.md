# Q74 – distance black-shirt (A) to white-shirt (B) person at t = 1.0 s

fps = question_fps = 24, so t = 1.0 s is frame 24. Overhead static camera, 2D: both walk along one image row, at the
same depth (equal apparent sizes), so one metres-per-pixel scale applies.

Scale from the prior: B's speed = 1.3 m/s. Distance and speed are both measured on the same kind of point (head-top
hair centroid, which lies above the pelvis), so they are in the same horizontal plane and the perspective height factor
cancels in the ratio D = gap_px / v_px × 1.3 m/s / 24.

## Measurements (measure.py → heads.json, analyze.py)
- Hair blob centroids (own segmentation, RGB≈(83,70,68)); agree with scene/ head_x within ~2 px.
- Frame 24: A head (256.6, 549.4), B head (1758.5, 560.6) → gap 1501.9 px (linear-fit gap 1515).
- B head speed: linear fit 15.41 px/frame, net over 17–71 15.56, per-gait-cycle windows 15.40–15.62.
- D = 1501.9 / 15.5 × 1.3 / 24 = 5.25 m (range 5.22–5.30 over speed choices).

## Second route
- scene/ pelvis estimates (head scaled toward image centre): gap 1412.7 px, B pelvis speed 14.66 px/frame → 5.22 m.
- Ground plane: head gap / 1.133 ≈ 1326 px, B foot-plant progression ≈ 13.5 px/frame → 5.32 m.
Routes agree within ~2 %.

Answer 5.25 m. Confidence: good (±3 %); the main uncertainty is whether the head is exactly above the pelvis
(a few cm forward lean per person would change D by ~1–2 %).

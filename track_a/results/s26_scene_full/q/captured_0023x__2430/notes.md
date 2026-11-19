# q_2430 — length of the slope (cm)

File fps 24 = question_fps 24. Lab camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

Slope = the white board leaning back on the table (its front face is the ramp the book slides down).
Measured in code (`measure.py`, white mask HSV V>190, S<40, largest component) at frame 48 (book off the board) and frame 0:
- top edge: y ≈ 357 (first full row 357/358), x 517–659 → centre u ≈ 588
- bottom edge: y ≈ 481 (last full row 480), x 494–676 → centre u ≈ 584.5
Back-projected with depth_info (slope_far = 1.201 m for the top edge centre, slope_near = 0.9555 m for the bottom edge centre):
- top P = (-0.082, -0.005, 1.198) m, bottom Q = (-0.068, 0.149, 0.941) m
- |P - Q| = 30.03 cm (29.83–30.15 cm for ±1 px edge row choices).

Check: board width from the top edge (142 px x 1.201 / f = 22.4 cm) and bottom edge (181 px x 0.9555 / f = 22.7 cm)
agree, so the far/near depths are consistent with the top/bottom edges of the same rectangular board.
Ramp angle implied ≈ 31° (horizontal 25.7 cm, vertical 15.5 cm), plausible for the observed slide at 2.8 m/s^2.

Answer: 30.0 cm. Confidence: moderately high (depends on depths referring to the edge centres).

# q2264 – width of the slope (cm)

Slope = the white rectangular board the ball rolls down (back-middle of the table). Width = its horizontal
extent across the board (left-right in the image, perpendicular to the rolling direction).
File fps = question fps = 24.

## Measurement (measure.py, frame 36, ball gone)
White mask (HSV S<40, V>200), longest white run per image row, between the board's left and right edges:
- near the far (top) edge, y 316-330: 95-97 px; top edge corner to corner (501,309)-(595,304) = 94 px
- near the near (bottom) edge, y 400-408: 102-103 px; bottom edge (508,423)-(610,408) = 103 px
The board's sides are nearly vertical in the image, so the row width is close to the true across-board extent.

## Scale (lab card, f = 0.5959*1280 = 763 px, c = (640,360))
- Far edge: depth 1.854 m along the ray -> z = 1.836 m (ray at (548,306)). Width = 94-96 px * 1.836/763 = 0.227-0.231 m
- Near edge: depth 1.701 m -> z = 1.687 m (ray at (559,416)). Width = 103 px * 1.687/763 = 0.228 m
- Plain card (distance used as z, no off-axis correction): 0.229-0.232 m (about 1% larger).

## Second check
The two edges, at different depths, give the same width (22.7-22.9 cm). Board length from back-projecting the
far and near edge centres = 29.5 cm, so the board is about 23 x 30 cm, which is a plausible size for such a board.

Answer: 22.8 cm (confidence: good, about ±3%).

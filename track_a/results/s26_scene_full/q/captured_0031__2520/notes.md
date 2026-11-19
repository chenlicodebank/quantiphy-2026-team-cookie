# q2520: diameter of the white ball (cm)

The file is 24 fps, the same as question_fps. t = 1.6 s is frame 38. f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Pixel diameters at frame 38
- From the scene record circle fit: white 24.52 px, yellow (tennis) 50.76 px.
- From my own half-max edge profiles (measure.py, rows in the upper half of each ball): white 24.74 px, yellow 49.86 px.
- Values used: white 24.6 px, yellow 50.3 px. Neighbouring frames 37-39 agree to within about 1 px.

## Problem with depth_info
- Read as given (tennis ball 1.19 m, white ball 0.994 m), the method card gives a tennis ball diameter of 1.19 x 50.3 / 763 = 7.85 cm. The prior says 6.7 cm, so this is 17% too large.
- The image also contradicts the given depths. Both balls sit on the same table top and the camera is slightly above the table. The white ball's contact point is at y ≈ 456 and the yellow ball's at y ≈ 477, so the white ball is the farther one, not the closer one (see full38.png).
- With the two depths swapped (tennis 0.994 m, white 1.19 m), everything fits:
  - The tennis ball comes out at 0.994 x 50.3 / 763 = 6.55 cm, 2% from the prior.
  - Ground-contact check: a camera height of about 0.15 m above the table, obtained from the yellow ball at 1.0 m (contact 117 px below cy), predicts the white ball's contact at 360 + 0.15 x 763 / 1.19 = 456 px. This matches the observed position.
- Conclusion: the depth labels are swapped.

## Answer
- Route 1 (method card, white ball at 1.19 m): 1.19 x 24.6 / 763 = 3.84 cm.
- Route 2 (ratio to the tennis-ball prior, swapped depths): 6.7 x (1.19 x 24.6) / (0.994 x 50.3) = 3.92 cm.
- Answer: 3.9 cm. This is consistent with a ping-pong-sized ball (4.0 cm).
- Taken literally, the unswapped depths would give 0.994 x 24.6 / 763 = 3.20 cm (card) or 2.74 cm (prior ratio). I rejected both: they are inconsistent with the prior and with the table geometry.
- I tried a table-plane fit from the yellow track (plane.py). It is ill-conditioned because the yellow ball's path is almost a straight line, so I did not use it.

Confidence: moderate-high, about ±5%.

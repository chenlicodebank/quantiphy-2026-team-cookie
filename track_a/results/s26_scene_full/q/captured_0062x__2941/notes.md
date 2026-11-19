# q_2941 – length of the blue shopping bag (cm)

File fps 24 = question_fps 24; t=1.4 s -> frame 34. Lab camera f = 0.5959*1280 = 763 px, c = (640,360).
Bag depth (depth_info, t=1.4) = 3.307 m. The bag is static (scene record: blue_tote_bag), lying flat on the floor.

## Bag outline (bag.py, frame 34)
Segmented the bag body (saturated blue + pink logo; the dark-grey handle is left out). The body is a quadrilateral:
L(774,312), T(826,296), R(893,349), B(841,369). The opening edge with the handle is T-R and the bottom edge is L-B
(~86-88 px). The sides L-T and B-R are ~55 px. Overlay in frames/bagmask.png.

## Floor plane (the bag lies flat, so foreshortening matters)
- fitplane.py: pitch/roll scan so the sliding white board (scene track quads, frames 20-40) keeps a constant
  metric size and right-angled corners -> pitch 40.5 deg, roll 6.5 deg, normal (0.113,-0.756,-0.645);
  board comes out 0.80 x 0.63 m, size CV 3 %.
- Independent: vanishing points of the bag quad itself (check.py) -> normal (0.176,-0.741,-0.648), VP angle 87.6 deg.
  The two agree.
- With the plane through the bag centre at 3.307 m, the predicted board-centre distance is 2.76 m, against the given 2.815 m (good).
  The box/toy/bin depths don't fit a single floor plane (the bin cannot be on this floor at 2.3 m), so I didn't use them.
- Speed prior check: at this plane the board speed near frame 34 is about 1.5-1.7 m/s (smoothed), against the prior 1.93.
  A lower pitch (32 deg) would reproduce 1.9 m/s but breaks the board's rectangularity and constant size, so I
  rejected it. The prior presumably carries depth-sensor noise.

## Result (size.py, corners back-projected onto the plane, anchored at the bag depth)
| normal | bottom L-B | opening T-R | sides |
|---|---|---|---|
| board fit 40.5/6.5 | 40.9 | 40.5 | 30.2 / 29.9 |
| board fit 38/8 | 41.5 | 41.5 | 32 |
| bag VPs | 39.3 | 39.3 | 31.9 |
| naive depth*px/f (method card) | 38.1 | 37.0 | 24 |

Length = the longer horizontal extent of the bag body, about 40.5 cm (the width, opening to bottom, is about 31 cm).
If the handles were included along the short direction, the extent would be larger, but the long side of the body is the
reading I used. Confidence: moderate (±2 cm from the plane choice and the edge blur of about 0.46 cm/px).

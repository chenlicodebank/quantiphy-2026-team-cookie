# Q732: acceleration of the paper airplane at t = 1.25 s (m/s^2)

- 2D simulation with a static camera. fps = question_fps = 24, so t = 1.25 s is frame 30. Acceleration is the change
  of scalar speed: speed(30) − speed(29), times fps.
- Scale comes from the prior "chalkboard length = 5 m". On frame 0, the row profiles (`acc.py`) put the outer wooden
  frame at x ≈ 319/320 → 1690/1691, which is 1371 px. The green surface alone is 1328 px. I used the whole object
  (1371 px), giving 0.003647 m/px. With the green surface instead (0.003765 m/px) the answer would be 3.5 m/s².
- The plane is flying in front of the board, so I treated it as the same plane.

## Track (`track2.py`)
- I subtracted a median background and took the mask centroid, the nose/tail midpoint and the weighted centroid.
- As an independent route, I template-matched the plane from one frame to the next with sub-pixel peaks, which gives
  a per-frame displacement directly.
- Speeds from template matching, in px/frame:

  | frame | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
  |---|---|---|---|---|---|---|---|---|---|
  | speed | 66.1 | 64.4 | 62.5 | 62.5 | 60.9 | 57.4 | 57.4 | 55.5 | 53.0 |

  The plane slows down steadily after its apex at frame 23.

## Acceleration estimates (`acc.py`)
- Linear and quadratic fits of the template-matching speed over windows within frames 22–35 give −1.49 to −1.69
  px/frame².
- Route 2: cubic and quartic polynomial fits of the positions over frames 16–33, using the three position
  definitions, give speed(30) − speed(29) = −1.47 to −1.73.
- Mean of all estimates: −1.60 px/frame².
- In metric units: 1.60 × 24² × 0.003647 = 3.36 m/s². This is a deceleration; the answer is given as its magnitude.

## Confidence
- The routes agree to about ±6%. The main remaining uncertainty is which chalkboard extent the prior means (about 3%).

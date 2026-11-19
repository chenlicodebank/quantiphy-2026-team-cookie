# q_3133 — height of the scooter (m)

Prior: the average speed of the person riding the scooter is 2.91 m/s. This is a 2D side view at 30 fps (the file rate and question_fps agree).

## Scale (from the prior)
- The rider moves right to left in a straight line at nearly constant speed. From scene/tracks/rider_scooter.csv, the average
  horizontal pixel speed over frames 0–55 is:
  - front wheel edge: 555 px/s raw (`*_orig`) and 560 px/s stabilised;
  - bbox centre: 555 / 561 px/s;
  - person centre: 548–555 px/s.
  The camera drift is only about 1%. I used 557 px/s.
- Scale = 2.91 / 557 = 0.005224 m/px.

## Scooter height in pixels (handlebar top to wheel bottom)
I measured on zoomed crops (crops.py, zoom.py → frames/):
- Frame 10: the hand's fist covers the grip (y 812–833), so the grip top is at about y 820. The wheel bottom is at y 1032. Height ≈ 212 px.
- Frame 45: the fist spans y 805–828, so the grip top is at about y 817. The wheel bottom is at y 1027. Height ≈ 210 px.
- Frame 52 (sunlit, crops.png): the stem top is at about y 820, consistent with the frames above.
- Result: about 211 px (±5 px). The grip is hidden under the hand, which is the main uncertainty.

Height = 211 × 0.005224 = **1.10 m**

## Check
The same scale gives:
- scooter length 203 px → 1.06 m;
- rider height 305 px → 1.59 m.
Both are plausible for a typical e-scooter (about 1.08 m long and 1.14 m tall) and an adult rider.

Confidence: moderate-high. The estimate is about ±5%, limited by where the handlebar top sits under the hand.

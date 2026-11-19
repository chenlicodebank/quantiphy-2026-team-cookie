# Q965: phoenix body length (m)

The video is 2D, 24 fps (same as question_fps), with a static camera. The prior gives the phoenix's acceleration at 2.0 s as 2 m/s².

## Scale from the prior (fit.py, fit2.py)
- I used the record's tracks (scene/tracks/phoenix.csv) for frames 1-71. A plain quadratic fit to head_x gives
  -0.51 px/frame², but the residual rms is 16 px. The head oscillates relative to the body with a period of about 25
  frames (two wing beats). Twelve-frame mean speeds come in pairs (6, 5.2, 18, 17.6, 30, 29.4 px/f), which matches a
  linear speed ramp with that oscillation on top.
- I fitted a quadratic plus sinusoids (free period P plus the 12.4-frame wing-beat period):
  - head_x: acc 0.4985 px/f², rms 4.6 px, P = 25.5
  - bbox_cx: acc 0.4925 px/f², rms 5.2 px (second, independent reference point)
  - bbox_x1 (tail tip): acc 0.488 px/f²; cx_green: 0.476 px/f² (noisier)
- I took 0.495 px/f², which is 0.495 × 576 = 285 px/s². The scale is 2 / 285 = 0.00702 m/px.

## Length in pixels
- Body length is the horizontal extent from beak tip to tail tip (side view, flying left). The record's bbox_w
  ranges from 550 to 634 px, median 600, and varies with the curl of the tail and the wing pose.
- I checked frame 38 by eye on a gridded crop: beak at about 1012 px and tail tip at about 1637 px, so about 625 px,
  in agreement with the bbox (1014-1637). The pale tail tips may be slightly under-segmented.
- I used 615 px, between the median and the extended-tail frames.

## Answer
615 × 0.00702 = 4.31 m, so the answer is **4.3 m**. Using the median 600 px gives 4.2 m; using the maximum 634 px
gives 4.45 m.

## Confidence
Moderate. The acceleration from the two reference points agrees within about 1%. The main uncertainty is which pose
defines "length" (about ±4%).

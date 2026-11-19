# Q2046: speedboat length (prior: sailboat length = 12 m)

This is internet footage from a static telephoto camera, so I used the benchmark convention: one scale = 12 m / the sailboat's pixel length.
The question gives the same rate as the file (30 fps). Timing doesn't affect a size question.

## Measurements (frames 262–312, where the motorboat is fully visible and not merged with the sailboat)
- **Sailboat length, bowsprit/bow rail to stern rail:** the scene record's median bbox length over unflagged frames is 105 px.
  My own column-darkness profile (`profile.py`, frames 265–305) gives 107 px (10th percentile 105).
  The solid hull alone at the waterline is 94–96 px (`profile.py`, `measure.py`). On a zoomed frame at t = 9.5 s the hull is about 92 px and the rails add about 10 px.
- **Speedboat (motorboat) length:** the record gives 36 px (opened mask, median of frames 262–312).
  In my profile, columns with at least 5 dark pixels give 35 px. Including the faint low stern and wake tail gives 40 px. The zoomed crop at t = 9.5 s shows a body of about 34–39 px.
  I take 37 px.

## Answer
- Scale from the full sailboat length: 12/104 = 0.115 m/px, so 37 px gives **4.3 m** (the record's own numbers, 36/105, give 4.1 m).
- Second route, scale from the hull only: 12/95 m/px gives 4.7 m. I didn't use it, because the annotators measure the full extent ("bumper to bumper").
- Caveat: the speedboat is nearer the camera than the sailboat, but the convention applies one planar scale with no perspective correction.
- Confidence: moderate, about ±10 %. The main uncertainties are where the speedboat ends (wake and spray) and which sailboat extent the annotators used.

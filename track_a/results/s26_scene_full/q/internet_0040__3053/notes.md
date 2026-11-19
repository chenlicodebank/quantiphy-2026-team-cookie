# q_3053 — average speed of the credit card from 0 to 0.73 s (cm/s)

Prior: card width 83.98 mm, which is the card's long horizontal side. Time base is question_fps = 30, so
0.73 s is frame round(21.9) = 22 and the interval is 22/30 = 0.733 s. The file's own rate is 24.406 fps; I used
the scene/ frame indices, not their seconds.

## Method (measure.py, speed.py)
- Red HSV mask, largest component. For each frame I took the median left-edge x over the middle rows, and the
  median right-edge x over the top and bottom rows, because the thumb covers the middle of the right edge. Top
  and bottom edges come from columns in the left half.
  The scene/ bbox_x1 includes the reddish fingers and overestimates the length (450-489 px). I checked frame 22
  on a grid: the true card edges are about 937 to 1368 px.
- Card length in sharp frames 15-27: 430 px (range 421-434). Scale = 8.398 cm / 430 px = 0.01953 cm/px.
  In frames 0-2 the card looks shorter (377 px) because it is tilted and blurred. If the annotator had measured
  those frames, the speed would be about 14% higher.
- Camera is static (scene/ spotlight check).
- Reference point = card centre ((L+R)/2, (T+B)/2): frame 0 (1490.5, 2614) -> frame 22 (1156, 2070).
  Net 638.6 px, path 641.1 px.
  Speed = 638.6 x 0.01953 / 0.7333 = 17.01 cm/s (net); 17.07 cm/s (path / mean of per-frame speeds).

## Second route
Other reference points: left-edge midpoint gives 17.39 (net) / 17.48 (path) cm/s; top-left corner gives
17.28 / 17.37 cm/s. These differ by 1-2% because the card turns slightly and its visible length changes.

Answer: 17.1 cm/s. Confidence: good to about 5%. The main uncertainty is which frame the annotator used for
the card's pixel length.

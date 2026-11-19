# q_619 — length of the TV (m)

Prior: speed of the black cat = 0.94 m/s. 2D simulation, fps 24 (question_fps 24, no re-timing). The camera is static.

## Scale from the prior
- The cat walks steadily from left to right for the whole clip (scene/tracks/cat.csv).
- Matched upper-body track: mean per-frame step 17.74 px (x only 17.73). The torso centroid gives 17.61 px/frame, net 863 px over 49 frames. The nose read by eye gives 870 px over 49 frames, about 17.76 px/frame.
- 17.73 px/frame × 24 = 425.6 px/s, so the scale is 0.94 / 425.6 = 0.002208 m/px.

## TV pixel length
I measured this in code with measure.py on frame 24. Dark screen columns (grey < 50) run from 815 to 1211/1212 on rows 540–745, about 397–398 px. The half-intensity edges are at x ≈ 814.5 and 1213.2, so the width is about 398.7 px, which matches the record's 399 px. The panel is seen face-on, so its horizontal extent on screen is its length.

## Answer
398.7 px × 0.002208 m/px = **0.880 m**

## Checks
- Speed routes: the centroid speed (17.61 px/frame) gives 0.886 m and the nose route gives 0.879 m.
- Size check: at this scale the cat's body (nose to rump, 245 px) is 0.54 m, which is plausible. A 0.88 m TV is about the size of a 40-inch set.
- Caveat: the TV stands against the wall, somewhat behind the cat's walking line. If perspective were corrected, the TV would come out a little larger. I followed the 2D one-scale convention.
- Confidence: moderate to high, about ±3% within this convention.

# q_1991: height of the white horse (m)

Prior: speed of the brown horse = 0.874 m/s. No depth_info. The clip is 2D (side view, one depth plane), fps 24 = question_fps.

## Identification (main uncertainty)
Neither horse is actually white. `probe.py` checked for a white horse hidden against the white background: at thresholds
from 254 down to 235 there are only 3 components (two horses and a hamster), so no white horse is hidden.
- Left horse: smaller, chestnut/red-brown coat → taken as the **"brown horse"** (prior).
- Middle horse: larger, lighter grey-brown/dun coat with a white face → taken as the **"white horse"** (asked).
This choice also gives physically plausible sizes (horse about 2 m to the top of the head, 2.15 m long, walking at 0.87 m/s).
The other assignment would make both horses about 1 m tall.

## Measurements (`measure.py`)
- Brown (red/left) horse speed: torso track, frames 0–48 (frame 49 is a loop reset). Mean 3.250 px/frame
  (linear fit 3.235, centroid 3.197), which is 78.0 px/s. Scale = 0.874 / 78.0 = 0.01121 m/px.
- White (large) horse pixel height, top of head to hooves, per frame: median 178 px at threshold 245 and 175 px at
  threshold 200 (mid-antialias). Range 170–187 depending on gait. Used 177 px.
- Height = 177 × 0.01121 = **1.98 m**.

## Check
Using the centroid speed (3.197 px/frame) instead gives 2.02 m. The threshold spread (175–178 px) is ±1 %.
Confidence: the measurement itself is good (±3 %). The colour-name assignment is the risk. With the other assignment
(brown = large horse, 5.92 px/frame; white = left horse, 165 px) the answer would be about 1.01 m.

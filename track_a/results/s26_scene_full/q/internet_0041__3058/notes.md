# q_3058: distance between the second-floor arch pillars (cm)

Prior: the middle duck is 66 cm long. Internet video, planar convention, so one scale is used for everything.

## Scale (middle duck, bill to tail)
- The scene/ mask lengths (116-130 px) leave out the pale tail-tip feathers.
- Read on 3x zoomed frames with an x ruler (duck.py, frames/dk_*.png):
  - frame 24: bill at x 2197, tail tip at x 2342, so 145 px
  - frame 48: bill at x 2117, tail tip at x 2256, so 139 px
- Length used: about 142 px. Scale = 66 / 142 = 0.465 cm/px.

## Upper-floor small columns (cols.py)
- Method: brightness profile along rows 430-540 of frame 0. The sunlit shaft halves sit at x 554.5, 784, 1373.5, 1599, 1824, 2179.5, 2404.5, 2990.5 and 3218.
- Within a bay the spacing is 225-229 px; I use 226 px centre to centre.
- Each shaft is about 38 px wide (x 1362-1400), so the clear gap between shafts is about 188 px.

## Answer
- Centre to centre (the answer): 226 x 0.465 = 105 cm.
- Under the other reading (clear gap between shafts): 188 x 0.465 = 87 cm.

## Checks
- The column spacing agrees across 4 bays to within 2%.
- The duck length differs by 4% between frames 24 and 48.
- Real-world sanity check: the building is behind the pond, so it sits farther away than the duck. Its true size is therefore larger than this planar figure. The benchmark convention ignores that.
- Confidence: medium. The largest uncertainty is which reading of "distance" was meant (centre to centre or clear gap).

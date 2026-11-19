# q_715: clock diameter (m)

Prior: chalkboard length = 5 m. The scene is a 2D frontal view with a static camera. The clock hangs on the same front wall as the board, so I use one metres-per-pixel scale for both.

## Board (measure.py)
I took edge profiles of the mean of frames 2 and 45 along several rows and columns.
- Outer wooden frame: left edge at x ≈ 320 (row profiles), right edge at x ≈ 1690–1692. Width ≈ **1371 px**, which matches the record's 1372.
- Green surface only: x 341–1670, about 1328 px.
- I take the chalkboard object's bounding box to include its frame, so the scale is 5 / 1371 = 3.647 mm/px.

## Clock (clock.py)
I fitted radial half-level crossings of the dark ring every 5°, then fitted a circle to them.
- Centre (1762.1, 292.6). Outer radius 56.9 px. Outer diameter 114 px horizontally and 113 px vertically, so **113.5 px**.
- Inner edge of the ring: radius 50.75 px.
- Direct row and column profiles agree: the ring runs from x ≈ 1705.5 to 1818.5 and from y ≈ 236.5 to 348.5, about 112–113 px.
- The scene record's figure of 105–110 px measured to the middle of the ring stroke. It undercounts the outer extent.

## Answer
113.5 × 5 / 1371 = **0.414 m**.

Alternative: if "chalkboard" meant only the green surface, the answer would be 113.5 × 5 / 1328 = 0.427 m, about 3% higher. Either way the result is close to 0.41–0.43 m, which is a plausible size for a wall clock.
Confidence: good. The main uncertainty is whether the frame counts as part of the chalkboard (±3%).

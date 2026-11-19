# Q2099: height of the sink (cm)

Prior: the picked bottle is 11.7 cm tall. This is an internet video, so I used the annotators' convention: one planar scale for everything.

## Bottle (scale)
- Frame 0: neck top at y≈1183, base at y≈1820, so the bottle is 637 px tall. This is the scene/ record, and I checked it on zoomed crops.
- Frame 3: the shoulder is at ≈1310 and the base at ≈1763. The body is ≈450 px, which matches the record's 453 at frame 0.
- Scale = 11.7 / 637 = 0.01837 cm/px. The base sits behind the pink bottle, so it is uncertain by about ±15 px, or ±2.4% of the scale.

## Sink (white vessel basins, left and right)
- Rim top, measured in code (`measure.py`, brightness edge per column):
  - Left basin, frame 0: y ≈ 1002–1004.
  - Right basin, frame 18: y ≈ 1000. That is about 982 in frame-0 coordinates, after the +18 px camera drift.
- The bottom of the basins is not in view. Both run off the bottom edge of the frame (y = 2160). The rounded lower corner of the right basin starts curving in at y ≈ 1960–2080, so its true bottom is only slightly below the frame edge, around 2160–2200.
- Visible height ≈ 2160 − 1000 = 1160 px. With the estimated hidden part, it is ≈ 1160–1200 px.

## Result
- 1160 px × 0.01837 = 21.3 cm (visible part only).
- 1190 px × 0.01837 = 21.9 cm (with the estimated hidden bottom).
- **Answer: 21.5 cm.**

## Checks and confidence
- The left and right basins give the same rim height, within about 20 px.
- As a sanity check, real vessel basins are about 15–22 cm tall.
- The basins are probably a little closer to the camera than the bottle, so in real-world terms the planar answer is an overestimate. The reference answers do not correct for perspective, so I did not either.
- Confidence is moderate. The bottom being out of frame and the base of the prior bottle being hidden are the main uncertainties.

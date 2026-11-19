# Q509: horizontal length of the "SKYNOVA" text on the bottle (m)

The video is 2D with a static camera. fps = question_fps = 60, so no re-timing was needed. The prior gives the droplet's acceleration as 9.7 m/s².

## Scale (from the prior)
- I fitted a quadratic to the drop centroid track (scene/tracks/drop.csv) against the render-step index. The record's
  duplicate-frame correction was used: video frame 7 duplicates frame 6, and render step 8 is missing.
  - Frames 0–10 (excluding the duplicate): a_y = 31.69 px/frame². Residuals are all below 0.4 px.
  - Frames 0–6 only, which are clean raw frames with no timing anomaly: a_y = 31.67 px/frame². This is the second route,
    and it agrees with the full fit.
  - a_x = −0.47 px/frame², which is negligible. |a| = 31.69 px/frame² = 114,090 px/s².
- Scale: 9.7 / 114,090 = 8.50e-5 m/px.

## Text length
- The word "SKYNOVA" is printed rotated 90° on the bottle, so it reads vertically in the image. I took "horizontal
  length" to mean the word's length along its reading direction, its own horizontal axis, which is vertical in the image.
- Measurement (measure.py, frame 12): I used the blue channel to separate the white text from the orange serum, then
  found the half-maximum edges of the per-row maximum. The text runs from y = 813.8 to y = 1141.9, so it is 328 px long.
  The mask (frames/textmask.png) is clean.
- The letter height across the reading direction is about 36 px (x = 1786–1822), which would be 0.0031 m.
- Answer: 328 × 8.50e-5 = 0.0279 m.

## Sanity check
At this scale the bottle is about 3.7 cm wide and 6.4 cm tall, which is plausible for a 30 ml serum bottle.

## Confidence
The pixel measurement and the scale are accurate to about 2%. The main risk is how the question is read: if it means the
image-horizontal extent, the answer would be about 0.003 m.

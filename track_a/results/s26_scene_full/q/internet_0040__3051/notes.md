# q_3051 — length of the credit card (cm)

Prior: width of credit card = 83.98 mm. No depth_info. Internet video, a single 2D pixel scale from the prior.

## Measurement (measure.py, measure2.py)
- Red card mask: R-G > midpoint threshold, closed to fill the text and chip, largest component. Measured on the sharp,
  nearly stationary frames 18-27; overlays are in frames/mask20/24/27.png.
- The bbox_x1 in the scene record (~1417, bbox_w ~488) is wrong: the mask runs into the thumb and fingers. The
  zoomed crops (frames/r24.png, l24.png) and the R-G edge profiles put the card's right edge at x≈1354 and its left
  edge at x≈930 (frame 24).
- Long side (horizontal): median row width 424-426 px. Edge profiles give about 423 px. **L ≈ 425 px**
- Short side (vertical): median column height 288-290 px. **W ≈ 289 px**
- Pixel aspect is 1.47. A real card is 1.585, so the card is slightly foreshortened, but the benchmark uses a planar
  single scale anyway.

## Answer
Naming convention: length = longer extent, width = shorter extent, so the prior's 83.98 mm goes with the 289 px
side. The scale is 83.98/289 = 0.2906 mm/px, giving length = 425 × 0.2906 = 123.5 mm = **12.35 cm**.

Other readings:
- If "width" means the horizontal extent (the long side, 425 px), the "length" would be the other side:
  83.98 × 289/425 = 57.1 mm = 5.71 cm. This reading makes 83.98 mm close to a real card's long side of 85.6 mm.
- 83.98 looks like a mix-up of the ISO card dimensions 85.60 × 53.98 mm. If the intended width was 53.98 mm, the
  pixel ratio gives 7.94 cm, and the real-world spec is 8.56 cm.

The instructions say to use the standard naming, so the answer is 12.35 cm.

Second route: the edge-profile crossings (left ≈930, right ≈1354; top ≈1919, bottom ≈2205) give 423/286 = 1.48,
which is within 1% of the mask ratio of 1.47.

Confidence: the pixel measurement is good to about 2%. Which reading the reference uses is the main uncertainty.

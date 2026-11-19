# q3266: length of a wall tile (cm)

Prior: the toilet paper's width is 10 cm. "Width" here means the roll's extent along its axis, which is horizontal.
Following the internet-video convention, I use one scale from the prior with no perspective correction.

## Measurements (`measure.py`, frame 59, roll at rest, camera static)
- **Roll:** left edge at x = 1616 and right edge at x = 2202, from the per-row max |dx| medians over rows 1100–1360. That gives **586 px**, which matches the scene record (583.5–585.2 px in frames 56–59).
  - Scale: 10 / 586 = 0.01706 cm/px.
- **Tile length** (longer horizontal extent; tiles are about 1600 x 1070 px). Distances are between vertical grout-line centres:
  - Middle row, the tile behind the roll (x 998 → 2606): **1608 px → 27.4 cm**
  - Top row: 1547 px (26.4 cm) and 1630 px (27.8 cm)
  - Bottom row, left tile: 1546 px (26.4 cm)
  - Mean of these four: 1583 px → 27.0 cm
  - Without the grout width (about 10 px), the middle tile is about 27.3 cm.
- **Tile height (for reference):** about 1073 px → 18.3 cm.

## Answer
27.4 cm, from the tile directly behind the roll, which is at the same depth, so the wall's slight turn matters least there.

## Check
- Averaging the other tiles gives 26.4–27.8 cm. Their spread comes from the wall being turned about 5% across the frame.
- Confidence: medium-high, within about 4%.

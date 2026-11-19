# q 2100 – width of the tray (cm); prior: picked bottle height = 11.7 cm

Internet footage, so I used the annotators' convention: one scale = prior cm / prior px, with no perspective correction. Time base doesn't matter here because this is a static size question.

## Bottle (prior), pixel height
- scene record, frame 0: neck top y 1183 → base y 1820 = 637 px. The base is hidden behind the pink perfume bottle.
- Lengths along the bottle during the lift (record, frames 2–8): 610–638 px.
- My check (diff2.py, difference against the bottle-free frame 18 with drift compensated): at frame 4 the base is at y ≈ 1735 and the neck top is at ≈ 1110, so about 625 px. At frame 0 (diff.py) the glass runs down to about y 1830 and the metal neck shows from about y 1150, so the upper bound is about 670 px.
- Value used: about 640 px (range 625–670).

## Tray (brass tray holding the products), pixel width
- tray.py: Sobel edges of the front face of the brass tray.
  - Frame 18 (no hand): x 1243 → 3006, which is 1763 px (rows y 2040 and 2060); 1749 px at y 2080.
  - Frame 0: 1760 / 1751 px.
- Value used: 1760 px. The black tray/board underneath, which sticks out on the left, is not included.

## Answer
11.7 × 1760 / 640 = **32.2 cm**. Using 637 px gives 32.3; using 670 px gives 30.7.

## Readings of "width"
- Used: the horizontal extent across the image (the front edge). This is what can be measured in pixels on a planar scale, and 32 cm is a plausible size for a vanity tray.
- The other reading, front-to-back depth, is heavily foreshortened (back edge at y ≈ 1667, front at about 2000, so roughly 330–410 px, or 6–7.5 cm). That is not physically plausible as a tray depth under the planar convention, so I rejected it.

## Confidence
Moderate. The main uncertainty is the bottle's pixel height, because the base is occluded and the neck is gripped, about ±5%.

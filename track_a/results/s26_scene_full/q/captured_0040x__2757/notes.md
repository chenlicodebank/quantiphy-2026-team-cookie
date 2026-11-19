# q_2757 — height of the poker tower (cm)

The object is the playing-card tent ("card_tent" in scene/), which stays still the whole clip. The file is 24 fps, the same as question_fps.
f = 0.5959 x 1280 = 763 px, principal point (640, 360).

## Pixel measurements (measure.py, card.py; average of frames 0/5/10/20)
- Tent top (ridge, against the black background): y = 416 (columns 683-695).
- Card bases on the table: front card base at y ≈ 499-500 (x ≈ 692-712). The other card's base is at y ≈ 493. The middle of the base under the ridge is at about y ≈ 496.
- Vertical extent: 84 px from the top to the lowest base pixel, and 80 px from the ridge to the middle of the base.
- Front card long edges: (674,419)-(692,500) = 83 px and (695,416)-(712,493) = 79 px, so about 81 px. The face is seen nearly edge-on, so the long axis lies almost in the image plane.
- Credit card (prior 85.6 mm, depth 0.69 m): its long edges measure 91-99 px, about 95 px. 95 x 0.69 / 763 = 8.6 cm, which matches the prior, so f and the card depth agree.

## Route A: method card, using the given tower depth 0.91 m
- 84 px x 0.91 / 763 = 10.0 cm. Using 80 px gives 9.5 cm.

## Route B: table-plane geometry (credit card plus cup)
- Back-projecting the credit card centre (564, 540) at 0.69 m puts the camera about 0.149 m above the table, with the camera level.
- The cup base (y ≈ 500) then lands at Z ≈ 0.81 m. That agrees with its given 0.842 m (Z ≈ 0.824), so the level-camera model holds.
- The tent base (y 493-500) lands at Z ≈ 0.81-0.86 m, with the ridge at about 0.83 m.
- Height ≈ 80 px x 0.833 / 763 = 8.7 cm. Measured as H - (416 - 360) x Z / f = 0.149 - 0.061, it is 8.8 cm.
- Check: at Z = 0.83 the front card's 81 px long edge is 8.8 cm, which equals a standard poker card (88.9 mm). At 0.91 m the same card would be 9.7 cm, longer than any standard card. A card tent also cannot be taller than one card length (8.9 cm).

## Answer
The given tower depth of 0.91 m conflicts with the tower's image position: its base sits at the same image row as the cup's base, yet the cup's given depth is 0.842 m. It also conflicts with the card's size. The reference was measured on the real object with a ruler, so I answer with route B: **8.8 cm**. Route A, the strict method-card reading, gives 10.0 cm.
Confidence: moderate, about ±0.5 cm.
Note: the depth for the white cup is printed as "8420m" in the inputs; I read it as 0.842 m.

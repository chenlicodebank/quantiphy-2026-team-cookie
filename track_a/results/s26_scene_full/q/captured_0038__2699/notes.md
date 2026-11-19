# Q2699 – height of the poker tower (cm)

Object: the "poker tower" is scene.json's `card_stand`, two playing cards leaned against each other in front of the pink bottle.
Credit card (prior 85.6 mm): the dark navy card near the table front edge, at x 520–619. It is the closest card, and its given depth is 0.6867 m.
File fps = question fps = 24.

## Measurement (prof.py, median of frames 3,5,8,30,34,40; the tower is static)
- Apex top edge: y ≈ 416.5–417 (gradient in columns x 676–684).
- Feet: right/front card foot y ≈ 499.5, left/back card foot y ≈ 494. The table point under the apex lies at the
  apex depth, between the two feet, so the base is at y ≈ 497.
- Pixel height ≈ 80 px (±2).
- Lab card method: f = 0.5959·1280 = 762.8 px. H = 0.9035 · 80 / 762.8 = **9.48 cm**.

## Check with the prior (credit card)
- The dark card's horizontal extent is 99.2 px (edges at x 519.5 and 618.7, row y = 544). At 0.6867 m this gives 8.93 cm,
  but the prior is 8.56 cm, so the lab scale reads +4.3 % high here (the effective f would be about 796 px).
- Applying the same correction to the tower gives 9.09 cm.
- Table-plane check: the camera height computed from the ball contact line (y 530 at 0.716 m) and from the tower base (y 497 at 0.9035 m)
  is 0.160 m and 0.162 m. These agree, so the given depths and f are geometrically consistent.
- Plausibility: standard playing cards are 88.9 mm long and lean slightly, which would make the tower about 8.5–8.9 cm. The
  card's long edge in the image is about 81 px, which is about 9.2–9.6 cm, so the cards may be slightly larger or the scale may run slightly high.

## Answer
The estimates range from 9.1 to 9.5 cm, and physical plausibility points to the low end. Answer: **9.2 cm**. Confidence is moderate (±5 %).

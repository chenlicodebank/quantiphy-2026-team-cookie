# q_2729 — diameter of the white cup's rim (cm)

File fps = question fps = 24. The cup does not move; measured on frame 48 (the ball is gone by then).

## Method (lab method card)
- f = 0.5959 x 1280 = 762.75 px, principal point ~ (640, 360).
- Cup rim (measure_cup.py): rows y = 382-387 (the rim lip, the widest rows of the cup) have a bright mask from x = 724 to 795.
  A sub-pixel edge from the partly covered edge pixels (left 159/194, right ~150/185 over an ~81 background) gives
  723.8 -> 795.2, so the width is 71.4 px (72 px by whole pixels). The body just below the rim is 71 px wide, then tapers to 55 px at the bottom.
  This matches the record (scene.json top_width_px 71).
- Diameter = 0.874 m x 71.5 px / 762.75 = 8.19 cm, so the answer is **8.2 cm**.

## Check with the prior (credit card, 85.6 mm, 0.6867 m)
- The credit card is the dark card with a yellow sticker near the front edge (measure_card.py). Its long edges measure about 93.5 px (top) and
  100 px (bottom), mean ~97 px. With f = 763 px the prediction is 85.6 x 762.75 / 686.7 = 95.1 px, about 2% off,
  which fits the card's oblique, slightly rotated pose. So the card-method focal length holds.
- If the Euclidean depth is first converted to z-depth (the cup is ~140 px off the image centre, a factor of 1.017), the result is 8.06 cm. The card method uses the distance directly: 8.19 cm.

Confidence: good (about ±3%).

# q_2734 — height of the poker tower (cm)

Object: the "poker tower" is the A-frame of two playing cards leaning on each other between the pink bottle and
the white cup (scene.json "leaning_card", x 663-713, y 416-500). It is static, so I measured it on frames 0, 10, 24
and 48, which are identical. File fps = question fps = 24.

Method (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640, 360), depth to the tower = 0.9035 m.
- Apex top edge: y = 415.5 (intensity step in the column profiles at x 675-687, measure.py).
- Lowest foot: the bottom of the front (right) card is at y ≈ 498. The flat card stack starts at y 500. The back (left)
  card's foot is at y ≈ 494.
- Pixel height from top to lowest point = 82.5 px -> 0.9035 x 82.5 / 762.8 = 9.77 cm.
- Apex to the table point directly under it (y ≈ 496, between the two feet) = 80.5 px -> 9.53 cm.

Second route (table-plane geometry): the credit card's centre (v ≈ 542, depth 0.6867) puts the table plane
0.163 m below the camera. The tower base (v ≈ 496.5, Z ≈ 0.90) gives 0.161 m, which agrees. The apex is
(415.5 - 360)/762.8 x 0.897 = 0.065 m below the camera, so the height is ≈ 0.096-0.098 m.

Scale check with the prior: the credit card is about 98 px long (parallelogram, 93-101 px) at 0.6867 m, which gives
8.8 cm against the true 8.56 cm, so this scale reads about 3 % high. Bottle (19 cm) and cup (14 cm) look plausible.

Answer: 9.5 cm, between the raw values (9.5-9.8) and the version corrected with the card check (9.3-9.5).
Confidence: moderate, about ±5 %. Note that a standard poker card is 8.9 cm long, so a tent made of them should
be shorter than that. The image says about 9.5, so either the cards are larger or the depth/scale is slightly off.

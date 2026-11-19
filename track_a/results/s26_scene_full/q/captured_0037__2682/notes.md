# Q2682: height of the poker tower (cm)

The poker tower is the card tent, two playing cards leaned together between the tape roll and the white cup. File fps = question fps = 24. I used frame 24 (t = 1.0 s), and the static frames 0 and 48 give the same mask extent (rows 416-504 in all three).

## Method (lab method card)
f = 0.5959 x 1280 = 763 px, and depth to the poker tower = 0.905 m (from depth_info).
- Top ridge edge, from half-intensity crossings in full-res column profiles (edges.py): y = 415.5-416.5, so I used ~416.
- Bottom: the front (right) card's foot is at y ≈ 499-500, just behind the far edge of the flat cards (y ≈ 501). The back (left) card's foot is at y ≈ 495-496. The table plane under the ridge (midway between the two feet) is at y ≈ 497.5.
- Pixel height: 81.5 px (ridge to the table under the ridge), or 83-84 px (ridge to the front foot). The record in scene/ gives 85 px, which includes the edge of the flat cards.
- Height = 0.905 x 81.5..84 / 763 = 9.67-9.96 cm. If I convert the range to z-depth first (centre offset (45, 96) px from the image centre, factor 0.990), I get 9.57-9.86 cm.

Answer: 9.7 cm.

## Checks
- White cup with the same method: width 73 px x 0.845 / 763 = 8.1 cm and height 13.8 cm. Both are plausible, so the depth scale looks sane.
- Front card length in the image is ~85 px, which gives ≥ 10 cm (the card also leans toward the camera, so the true length is longer still). This is larger than a standard 8.9 cm poker card, so the cards are either large or the depth runs ~10% high. If they were standard cards, the tent height would be ~8.5-9 cm.
- The ball at t = 1.0 measures ~20-22 px (vertical, unblurred), which implies 3.0 cm at 1.055 m against the 4 cm prior. That deviation goes in the opposite direction, so there is no consistent correction to apply, and I kept the method card.

Confidence: moderate (±10%).

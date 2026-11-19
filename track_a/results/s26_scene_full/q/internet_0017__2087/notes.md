# Q2087 – length of the pen (cm); prior: credit card width = 5.4 cm

Internet footage, static overhead camera, 2D planar convention: one scale = 5.4 cm / card width in px.
Static sizes, so the fps question (22.37 vs 22) does not matter.

## Card (prior object)
- The credit card is the black **Visa** card held in the left hand (the other black card on the desk is a
  "grind.co.uk blackcard" loyalty card, not a credit card).
- `measure.py`: dark mask (max channel < 60) → min-area rectangle; then the perpendicular width measured in 10-px
  strips along the long axis in the part free of fingers. Width (short side) = 193 (f0), 196 (f7), 204 (f13),
  203 (f20), 200 (f27) px; long side 354–355 px. It changes a little because the card is tilted in the hand. I used
  the mean, about 199 px.
- Scale: 5.4 / 199 = 0.0271 cm/px.

## Pen
- The pen lies on the clipboard at the left (cap end upper-left, tip lower-right). `pen.py` / `penview.py` take an
  intensity profile along the pen axis (from (509,1362) towards (887,1809)). The cap end edge is at s ≈ 11 px.
  The dark tip end reaches half contrast at s ≈ 590–595, with a faint blurred tail out to about 620. Length is
  about 583 px (±6). The scene record has 578 px.

## Answer
583 × 5.4 / 199 = **15.8 cm**.

## Checks / alternatives
- Visa card width taken per frame: 193 px → 16.3 cm and 204 px → 15.4 cm.
- Second route using the flat loyalty card on the desk (short side 216.5 px, steady in every frame, same plane
  as the pen): 14.5 cm. The Visa card is held above the desk and tilted, so it looks a little larger along its
  length and foreshortened across its width. The annotators' convention uses the named credit card's pixel width,
  so I kept the Visa-based value.
- A gel pen with its cap is typically 14–16 cm long, so the answer is plausible.

Confidence: moderate (±5–8 %, mostly because the held card is tilted).

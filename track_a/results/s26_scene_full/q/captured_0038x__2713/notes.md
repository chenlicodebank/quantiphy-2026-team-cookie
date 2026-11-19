# q_2713 – height of the poker tower (cm)

Video: lab capture, 1280x720, 24 fps (file fps = question_fps = 24). Camera static. f = 0.5959*1280 = 763 px, c = (640, 360).
Poker tower = playing-card A-frame standing on a few flat-lying cards, in front of the pink bottle (static; the
ball passes in front only in frames 29-35, so frames 2, 5, 8, 20 were averaged for measurement).

## Measurements (measure.py, card.py)
- Tower top edge: column profiles x=676-696 show the black/pink -> white transition at y ≈ 414.5-417 -> top ≈ 415.
- Tower base: the flat cards' back edge is at y ≈ 500-501 across x=688-712 (front edge ≈ 515); the standing card's
  foot merges with it at y ≈ 497-500 -> base ≈ 500 (±2).
- Pixel height ≈ 85 px (±3).

## Scale
- Method card: H = d * px / f = 0.9035 * 85 / 763 = 10.07 cm.
- Using optical-axis depth z = d*cos(off-axis angle) at the tower centre (690, 457): z = 0.894 m -> 9.96 cm.
- Check with the prior: credit card (dark card) long side measured 97-99 px; predicted with z (0.6867*0.968 = 0.665 m)
  = 0.0856*763/0.665 = 98.2 px (agrees within 1 %); with raw distance 95.1 px (4 % short). So the z-based form is
  consistent with the prior.

## Answer
≈ 10.0 cm (between 9.96 and 10.07). Confidence moderate: the base row is ±2 px (±2.5 %); a standard poker card is
8.9 cm long, so a ruler height of 9-10 cm is plausible.

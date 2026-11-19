# q2050 — How tall is the shooter (cm)? Prior: basketball diameter = 24 cm

Method (internet-video convention: one planar scale = 24 cm / ball pixel diameter, no perspective correction).
Scripts: crops.py, zoom.py, zoomb.py (zoomed crops with pixel rulers, frames/*.png). No timing involved, so the
fps question (29.66 vs 30) does not matter.

## Ball diameter at the shooter's depth (px)
- f40: ball held above head, clean against the awning: horizontal 1236 -> 1281 = ~45 px.
- f0 (in hand at dribble start): x 1259 -> 1305 (~46), y 1475 -> 1517+ (~43-45).
- f5 (dribble, slight vertical blur): ~41-44.
- scene record: full outline against sky in flight 45.1-45.9 px; f16 in hands ~45.
- Adopted: 45 px (+-1.5). Scale = 24/45 = 0.533 cm/px.

## Shooter height (px), head top (hair above the face blur) to shoe soles, upright frames before the jump
- f28: 1426 -> ~1767 = ~341
- f32: 1427 -> ~1765 = ~338 (legs straight, feet together, ball above head)
- f36: 1432 -> ~1765 = ~334 (head tilting forward)
- f16 (walking stride): ~1424 -> 1757 = ~333; f40 knees bent: ~328 (excluded)
- scene record keyframes f0-40: 331-337.
- Adopted: 338 px (+-4).

## Result
338 / 45 x 24 = 180.3 cm -> **180 cm**.
Second route: scene-record numbers (335 px standing / 45 px ball) give 179 cm; range from the uncertainties
(334-341 px, 44-46 px) is 174-186 cm. Real-world sanity: an adult man ~1.8 m is plausible.
Confidence: moderate-high (~+-4 %).

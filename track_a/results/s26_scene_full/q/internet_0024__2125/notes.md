# Q2125 – longest side of the wallet (cm); prior: earphone-case width = 45 mm

Static overhead view of a desk. Both objects are static; I measured them on frame 29, after the cup has left.
The time base doesn't matter here. Following the internet convention, a single planar scale comes from the prior.

## Earphone (AirPods) case – `air2.py`
- GrabCut segmentation (overlay `frames/air_gc.png`) follows the full outline, including the shaded lower side with the port.
- minAreaRect is 227.8 x 196.2 px at -55°. The long axis runs from the port (lower-left) to the lid (upper-right). The lid seam
  runs across the short axis, so width = 196 px. A plain white-threshold mask gives 193-197 px.
- Scale = 45 mm / 196 px = 0.2296 mm/px.

## Wallet (tan leather organiser on the grey notebook) – `wallet2.py`
- Leather colour mask (H 4-24, S>120). I fitted robust lines to its four edges, avoiding the polaroid on top and the strap
  at the bottom, and checked the corners on zoomed crops (`frames/wallet_quad.png`, `bl.png`, `br.png`).
- Long side: the top edge is 743 px and the bottom edge 765-772 px (the bottom-left corner checked by eye is ~(2950,835)).
  I used the mean, ~757 px. Short side ~530 px. The scene record had ~770 px.
- Long side = 757 x 0.2296 = 173.8 mm ≈ 17.4 cm (range 17.1-17.7 depending on which edge is used).

## Second-route check
- The case's other side is 228 px. That gives 228 x 0.2296 = 52.3 mm, close to a real AirPods case (53.5 x 44.3 mm), so
  the 196 px width is consistent.
- Scaling from the length instead (53.5 mm / 228 px) gives 17.8 cm, within 2 %.
- Confidence: moderate-high, about ±4 %.

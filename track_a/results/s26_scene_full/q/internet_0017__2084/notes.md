# Q2084 – diameter of the round container (cm); prior: credit card width = 5.4 cm

Static top-down 2D scene, so one scale is used (cm per px from the card's width). Time base doesn't matter for a size.

## Scale (measure2.py)
- Held Visa card: I fitted lines to the mask contour edges and intersected them to get the corners. Short side
  (width) in px: f0 193.6, f5 196.0, f14 204.1, f20 203.2, f27 199.9, mean ≈ 199 px. Long side ≈ 354 px. The card is
  tilted, so its aspect (1.78) isn't the flat 1.586.
- Cross-check: the second card lying flat on the desk has a short side of ≈ 201 px (scene record), consistent with 199.
- Scale = 5.4 / 199 = 0.0271 cm/px.

## Container (pin tin, top right)
- The dark outline is the union of two overlapping circles: the tin body (upper right, silver rim) and its lid
  (lower left). Circle fits on each arc give D = 378.6–379.0 px (body) and 377–381 px (lid), stable over 5 frames.
  The whole union's extent is ≈ 413 px. The scene record's 417 px is this union, not the tin itself.
- Diameter = 379 × 0.0271 = 10.3 cm. Using the desk card (201 px) instead gives 10.2 cm.
- Other reading: if the lid and body are measured together as one extent (413 px), the answer would be 11.2 cm.

Answer: 10.3 cm. Confidence moderate: the main uncertainty is which pixel width the annotators used for the tilted card.

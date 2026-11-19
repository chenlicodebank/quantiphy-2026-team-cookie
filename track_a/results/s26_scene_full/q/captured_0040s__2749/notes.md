# q_2749 – height of the poker tower (cm)

Question fps 24 = file fps 24. Static object, measured on frame 0 (also checked on a median of frames 0/10/20/40/48).

Object: the "poker tower" is the two-card tent in the centre of the table (scene record calls it `card_tent`,
bbox 660–712 x 416–500). The flat cards in front of it are a separate object (they lie in front, not under it).

## Pixel measurement (bottom.py, measure.py)
- Top of tent: green→white transition between rows 415 and 416 in columns 684–693 → top y ≈ 416.0.
- Bottom: the lowest point is the front (blue-back) card's bottom-left corner at x≈690–693. The card is bright
  down to row 499, and the flat cards begin at row 501 → bottom y ≈ 499.5 (±1). The rear card stands on the table higher in the image (~495).
- Vertical extent ≈ 83.5 px.

## Scale (lab method card)
f = 0.5959 × 1280 = 763 px. depth_info puts the tower at 0.91 m.
H = 0.91 × 83.5 / 763 = 0.0996 m = 9.96 cm.
Variant: using the optical-axis depth Z = 0.91/1.010 = 0.901 m (pixel offset ~110 px from the image centre) gives 9.86 cm.

## Checks
- Credit card (prior 85.6 mm, depth 0.69 m): the expected length is 94.7 px. Measured from the parallelogram outline,
  the back edge is ≈89 px and the front edge ≈97 px (mean ≈93 px). That agrees within about 2 %, so f and the depth scale are consistent.
- Table-plane consistency (level camera): camera height h = (v_contact − 360)·Z/f gives 0.158 m from the tape,
  0.159 m from the cup, 0.164 m from the card and 0.166 m from the tower base. So the tower depth of 0.91 m fits the table
  geometry to within ~4 %.
- Caveat: a standard poker card is 8.9 cm long, and a leaning tent should be shorter than that. The measured ~9.9 cm
  means either larger cards or a slightly overstated depth. I am following the given depth, as the method requires.

Answer: 9.9 cm (the mean of 9.96 and 9.86). Confidence: moderate, about ±5 % from the pixel measurement and depth, plus some risk from the card-size caveat.

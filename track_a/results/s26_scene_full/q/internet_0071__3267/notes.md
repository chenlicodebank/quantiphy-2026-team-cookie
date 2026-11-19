# q_3267 – height of a wall tile (cm)

Prior: the toilet paper is 10 cm wide. I read "width" as the roll's length along its axis, the width of the paper sheet; a standard roll is about 10 cm wide. The roll's axis is horizontal.

## Method
I used one planar scale, following the internet-video convention. Time does not matter for this question, because the tiles never move.

- **Roll width:** about 586 px.
  - measure.py measured the left and right edges on frame 58, with the roll at rest, along rows y 1150–1340. Median 588 px.
  - The scene record gives 583.5–585.2 px for frames 56–59.
  - I used 586 px, so the scale is 10/586 = 0.01706 cm/px.
- **Tile height:** measured as the distance between the horizontal grout lines above and below the tile behind the roll (x 998–2606).
  - measure.py (frame 58) gives the pitch between grout-line centres: 1062 px at x=900 up to 1087 px at x=2100. It grows to the right because the wall is turned slightly.
  - m2.py (frame 20) measured each grout line's edges at half depth. The pitch is 1065–1083 px for x 1100–1700. The tile face, without grout, is 14 px smaller: 1051–1069 px.
  - Near the roll's centre (x ≈ 1900) the pitch is about 1085 px and the face about 1071 px. Over the whole tile the average pitch is about 1077 px.
  - I used 1075 px, a value between the face and the pitch near the roll.
- **Result:** 1075 × 10/586 = **18.3 cm**.

## Second-route check
The roll's diameter is 698 px, which gives 11.9 cm with the same scale. That is a realistic roll diameter, so the scale is consistent.

## Range and confidence
- **Range:** the face value gives 1063/586 → 18.1 cm, and the pitch near the roll gives 1085/586 → 18.5 cm.
- **Main uncertainty:** the wall sits behind the roll, about 6–12 cm farther from the camera. The reference uses no perspective correction, so I did not apply one either.
- **Confidence:** medium-high, about ±3% within the stated convention.

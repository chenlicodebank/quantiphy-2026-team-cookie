# q3264 – diameter of the toilet paper roll (cm)

Prior: width of the toilet paper roll = 10 cm. This is the roll's length along its axis (the paper sheet width). Here the axis is horizontal.
Planar single-scale convention (internet video): scale = 10 cm / axial pixel length.

## Measurements (full-res px; `measure.py`: mean gradient profiles on Gaussian-blurred gray)
- Top and bottom edges: dy profile averaged over the left columns of the roll, which the hand does not cover.
- Left and right edges: dx profile averaged over upper rows, above the hand.

| frame | D (vertical) | L (axial) |
|---|---|---|
| 20 | 700 | 587 |
| 22 | 700 | 586 |
| 24 | 703 | 586 |
| 33 | 699 | 589 |
| 52 | 696 | 589 |
| 56 | 698 | 586 |
| 58 | 696 | 587 |
| 59 | 696 | 585 |

These agree with the scene record: at rest (frames 56–59) L = 583.5–585.2 and D = 697–699.

## Result
- Diameter ≈ 698 px; width ≈ 586 px.
- Diameter = 10 × 698 / 586 = 11.9 cm.

## Second route
- The roll was measured face-on in mid-motion (frames 20–24) and at rest (56–59). The ratio D/L is 1.19–1.20 in both windows.
- An 11.9 cm diameter for a 10 cm wide roll is realistic.
- Timing does not matter for a size question.

Confidence: high (about ±1.5 %).

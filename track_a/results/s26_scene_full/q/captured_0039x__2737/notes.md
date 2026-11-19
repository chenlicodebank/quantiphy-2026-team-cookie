# q2737: diameter of the white ball (cm)

Method (lab card): size = depth × pixel diameter / f, with f = 0.5959 × 1280 = 762.8 px. Depths given: 1.014 m at t=1 s
(frame 24) and 0.737 m at t=1.5 s (frame 36). question_fps = file fps = 24.

Pixel diameter:
- measure.py: horizontal edge-to-edge width (sub-pixel max-gradient edges, median over 7 rows through the centre),
  frames 20–40, using the centres from scene/tracks/ball.csv. I also checked it against the top edge (2×(cy − top)).
- The record's edge-circle-fit diameters (scene/tracks/ball.csv) were used as a second series.
- I checked 8× crops of frames 24 and 36 by eye: about 31–32 px wide at f24 and 43–45 px at f36.
- fit.py: quadratic fit of 1/D against frame (frames 20–40), plus local ±2-frame means.

Results (cm):
| series | f24 (Z=1.014) | f36 (Z=0.737) |
|---|---|---|
| width, fit | 4.28 (D=32.2) | 4.21 (D=43.6) |
| edge-fit, fit | 4.34 (D=32.6) | 4.24 (D=43.9) |
| local means | 4.24–4.30 | 4.22–4.29 |

Second route: the two independent depth/time pairs agree to within about 2%. Answer: 4.27 cm.

Sanity check: the blue card's horizontal extent in the record is 102 px (read by eye, ±2 px, and foreshortened) at
0.6867 m. With f = 762.8 that gives 9.2 cm, against 85.6 mm. That card reading is rough, so I kept the paper's fixed focal
length. If I used the card-implied f (about 818 px) instead, the ball would come out at about 4.0 cm.
Confidence: moderate to high (about ±4%).

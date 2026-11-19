# Q2040 – length of the white car (prior: lane width = 3.66 m)

Top-down drone shot of a straight two-lane road with no edge lines, only a dashed centre line. One scale is used, set by the lane width in pixels (internet convention).

## Lane width (road.py, road2.py; frames 20, 60, 200; bands of 120 rows, skipping the tree and the SLOW marking)
- Asphalt edges are taken from the strongest grey-level gradient, and the centre line from the brightest column.
- Right lane (the white car's lane), centre line to asphalt edge: 37.4–39.6 px, typically about 38.
- Left lane: 33–39 px. The verge vegetation blurs this edge.
- Whole road: 71–77 px, typically about 74, so half the road is about 37.
- Value used: **lane = 37.5 px**, so the scale is 3.66 / 37.5 = 0.0976 m/px.

## Car length (carlen.py; every 10th frame from 100 to 290; the frame-180 crop was checked by eye)
- The bumper-to-bumper extent is the row-brightness profile at 30% of the contrast above the road: 59.8–63.6 px, median **61.2 px**. Frame 220, which sits on the SLOW marking, was left out.
- Reading the frame-180 crop by eye gives y 823–885, about 61.7 px.
- The scene record's mask length has a median of 63 px, but its difference mask includes some blur.
- The length is about 62–63 near the top of the frame and about 60–61 lower down.

## Answer
61 px × 0.0976 m/px = **5.95 m**.
Sensitivity: a lane of 38.5 px gives 5.80 m, a car of 63 px gives 6.15 m. The likely spread is about ±4%.
This is longer than a typical real car (about 4.7 m). The likely reason is that this rural road's real lanes are narrower than 3.66 m, but the prior is treated as exact.

Second route: the local ratio at y ≈ 850 (car 61.5 px, right lane 38.5 px) gives 5.85 m, which agrees with the main answer.
Time base does not matter for a size.

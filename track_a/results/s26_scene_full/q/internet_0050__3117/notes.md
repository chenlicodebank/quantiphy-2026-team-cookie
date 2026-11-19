# q3117: height of the person riding the scooter (m)

Prior: the rider's average speed is 2.9 m/s. fps = question_fps = 30, so there is no re-timing.

## Scale
- I used the rider track in scene/tracks/rider.csv (frames 0-93) in background-stabilised coordinates.
- Average horizontal pixel speed: bbox centre 476.3 px/s, front-wheel edge 475.8 px/s, rear end 476.8 px/s. The mean of per-frame |dx| and net/93 give the same values. Raw image coordinates without stabilisation give 472.2 px/s.
- Scale = 2.9 / 476.3 = 0.006089 m/px.

## Height
- Frame 47 crop (look.py, look_47.png): cap top at y ≈ 875, soles on the deck at y ≈ 1149, wheel-ground contact at y ≈ 1172.
- Bbox heights at frames 10, 47 and 80 are 301, 298 and 297 px from cap to ground. The scene record gives a median of 299.
- Person cap-to-soles is about 275 px (±5). The person stands almost straight on the deck.
- Answer: 275 × 0.006089 = **1.674 m**.

Other reading: cap to ground, which includes the scooter deck, is 299 px = 1.82 m. I did not use it because the question asks for the person's height.

## Check
The ratio with the scooter length gives the same result: the scooter is 177 px, which is 1.08 m at this scale and plausible for an e-scooter. Using unstabilised pixel speed would change the answer by only 0.9 % (1.689 m).

Confidence: moderate-high. The main uncertainty is which points the annotator clicked for top and bottom (±3 %).

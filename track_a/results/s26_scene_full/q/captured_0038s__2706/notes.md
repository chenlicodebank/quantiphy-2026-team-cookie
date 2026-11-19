# q_2706 — height of the poker tower (cm)

The "poker tower" is the card tent: two playing cards leaning together in front of the pink bottle (scene/ "card_tent").
The tower is static. I measured it on a median of frames 0, 2, 4, 44, 46 and 48 (the ball is far from the tower in
those frames; at t = 1.4 s, frame 34, the ball passes in front of it). The file rate and question_fps are both 24.

## Measurements (measure.py, edges.py, geom.py)
- Apex: the top edge of the tower is at v = 415.5 px (from column intensity profiles at x 675-693).
- Base: both card feet end at v ≈ 498-499 px (taken as 498.5). The flat cards' far edge is right below, at v ≈ 500.
  Pixel height: 83 px.
- Focal length f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Table plane: I took its normal from the vanishing line of the four table corners. The camera is almost level
  (pitch about 0.5°) and sits about 16.6 cm above the tabletop, so vertical objects are hardly foreshortened.

## Routes
1. Method card: Z = 0.9035 / |ray| at the tower centre gives H = 83 x Z / f = **9.74 cm**. Back-projecting the apex and
   base and solving with the plane normal, then scaling so the centre matches 0.9035 m, gives 9.75 cm.
2. Independent check using the credit card: back-projecting the card's corners onto the table plane, fixed by the card
   centre at 0.6867 m, gives long edges of 8.60 and 8.49 cm (the prior is 8.56 cm, so the scale checks out). The tower's
   base placed on that plane gives H = 9.54 cm. The centre then lands at 0.884 m instead of the given 0.9035 m (2% off).

Answer: 9.7 cm, using the given tower depth as the method card says. Confidence: ±3-4%. The main uncertainty is where
the feet sit (±1.5 px), because the flat cards in front may hide the bottom edge slightly.

# q_2727: height of the poker tower (cm)

The file's frame rate and question_fps are both 24. The camera is static. The props do not move, so I measured on frame 48, where the ball is gone.

**Object:** the "poker tower" is the A-frame of two leaning playing cards in front of the pink bottle: a white/blue-grey card on the right and a pink card on the left. The record calls these the "leaning_cards". Its depth is given: distance_poker_tower_camera = 0.9035 m.

## Pixel measurement (zoom.py, frames/z_tower.png, grey-level profiles in measure.py)
- Ridge (top edge of the tent): from (675, 418) to (696, 416). Its top boundary at the middle (x ≈ 686) is at y ≈ 416.0 ± 0.7.
- Feet:
  - Front card bottom edge: (691, 500) to (712, 492.5). Midpoint y ≈ 496.8, taken from the profile edge.
  - Pink card: its bottom near corner is at (656, 494). The rest of the bottom edge is hidden but parallel to the front card's, so its midpoint is about (666.5, 490.5).
- Ground point under the ridge = midpoint of the two foot midpoints, about (684, 493.6). It sits almost directly below the ridge midpoint (x 684 vs 686), which fits a vertical segment.
- Vertical pixel height ≈ 493.6 − 416.0 = **77.6 px** (±1.5 px).

## Scale (lab method card)
- f = 0.5959 × 1280 = 762.75 px.
- H = 0.9035 × 77.6 / 762.75 = 9.19 cm.
- Foreshortening of a vertical segment: I fitted the table plane through the ball centres at t = 1 s and t = 1.5 s (with their given depths) and the credit-card centre (plane.py). The camera's optical axis is almost level (about 1° down), so the ray to the tower is about 7° below horizontal, cos = 0.992. That gives H ≈ 9.27 cm.
- Independent check of the camera height: the plane fit puts the camera about 0.18 m above the table. The ground ray at the tower's feet then gives a horizontal distance of about 0.93 m, which agrees with the given 0.9035 m.

## Second route: scale check with the prior (credit card, 85.6 mm, distance 0.6867 m)
- The card's long edges measure 92.9 px (far edge) and 100.7 px (near edge), mean about 96.8 px. Pinhole geometry predicts 95.1 px.
- So the nominal f reproduces the prior to within about 1.8%. Using the card-calibrated f (about 777 px) instead would give H ≈ 9.10 cm.
- Card-foreshortening check: the card's depth extent (about 16 px against 60 px if seen face-on) means the ray meets the table at about 15°. That matches the plane fit (1° pitch + 13.4° off-axis).

## Result
- Estimates: 9.10 to 9.27 cm. **Answer: 9.2 cm.**
- Caveat: a standard 88.9 mm poker card could not make a tent this tall. The measured card length in the tower (about 9.4 cm), and the flat card on the table, suggest these cards are larger than standard. Alternatively, the given distance is slightly long.
- Confidence: moderate, about ±4%. The main uncertainties are where exactly the ground point under the ridge lies and the given depth.

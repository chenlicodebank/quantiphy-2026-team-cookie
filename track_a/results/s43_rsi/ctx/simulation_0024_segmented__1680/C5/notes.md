Scale from the boat: red-hull centroid moves 155.96 px/s at question_fps 24 (6.498 px/frame), so with the 4 m/s prior m/px = 4/155.96 = 0.02565 at the boat's 90 m depth; independently, back-projecting the boat centroids at t=1 and t=2 with the given depths and solving |P2-P1|=4 m gives f=3506 px and m/px=90/3506=0.02567 (0.1% agreement; boat hull 390 px -> 10 m, realistic). SAM 3 rock mask (frame 37) gives horizontal/main-axis length 622 px, so length = 622 x 0.02565 = 15.95 m, rounded to 16.0 m.

Final message:
Answered: **16.0 m** for the rock's length.

Method summary:
- **Scale (two routes, agreeing to 0.1%)**: the boat's red-hull centroid moves 6.498 px/frame → 155.96 px/s at the question's 24 fps; with the 4 m/s prior that gives 0.02565 m/px at the boat's 90 m depth. Independently, back-projecting the boat centroids at t=1 s and t=2 s with the given depths and solving |P₂−P₁| = 4 m yields f = 3506 px → 90/3506 = 0.02567 m/px. Sanity check: the boat's 390 px hull → 10.0 m, a realistic fishing boat, and the derived camera pitch puts the camera ~0.7 m above the waterline.
- **Rock**: SAM 3 mask (verified on the overlay) gives a horizontal/main-axis length of 622 px, static in the image and never occluding the boat.
- **Length** = 622 px × 0.02565 m/px ≈ 15.95 m → **16.0 m**.

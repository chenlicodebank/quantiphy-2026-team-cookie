# Q1041 – height of the pier deck above the water surface

Answer: **0.40 m**

Time base: question_fps = 24, so t = 1 s is frame 24. The file runs at 22.802 fps; I used frame indices only.
The camera is static (from the scene record). The "pier" is the small jetty in front of the boathouse
(x 460-638 at frame 0); the boathouse stairs sit behind it.

## Focal length (focal.py, stem.py)
- Boat origin is taken as the centre of the full-boat box (scene ref_x = bow + 324 px): u = 1314.2 at frame 0
  and 1059.6 at frame 24, v ≈ 686-690. The given distances are 7.452 m and 6.655 m.
- If the boat's camera depth Z is the same at both frames: **f = 1000 px, Z_b = 5.854 m, f/Z_b = 170.9 px/m**.
- I checked that the depth really is constant by tracking, in code, the bow-stem post top and the stem foot (where
  the stem meets the water) in every frame. Averaged over frames 0-4 the foot is at y = 744.2; over frames 20-28 it
  is at 744.1. The stem height is about 123.5 px in both windows, so the depth changes by less than about 0.5%,
  which gives f = 1000 ± 35 px. Later the boat recedes slightly (foot at 740 and height 121 by frame 60).
  The bow-patch scale registration (scale_reg.py) was too flat to use.
- Check against the prior: at 170.9 px/m the stem rises 123.5 px = 0.72 m above the water. A 0.75 m bounding box
  then implies about 3 cm of keel below the water, which is plausible.

## Pier measurements (pier.py, frame 0, column profiles x 480-600)
- The front face bottom edge is at y = 644.5. Its reflection's top edge is at 707.0, which puts the **water line at
  the front face at y = 675.75**.
- The deck top front edge is at y ≈ 629.7: there is a seam at 629.5, and the mirror of the reflection's lower edge
  (721.5) gives 630.0. So the deck stands **46.0 px** above the water at the front face.
- Horizon: the bollards on both deck sides give vanishing lines that meet at y ≈ 531 (x ≈ 546). The camera is
  nearly level.

## Route 1: water plane through the boat
- Camera height above the water: h_c = (744 − 531) × Z_b/f = 213 / 170.9 = 1.247 m.
- Front-face depth: Z_f = f·h_c / (675.75 − 531) = 8.62 m.
- Deck height: h_d = 46.0 × Z_f / f = **0.396 m**. With the horizon at 540 instead of 531 this becomes 0.405 m.

## Route 2: given pier distance, assuming the origin is at the middle of the pier
- The pier origin is close to the image axis, so Z ≈ 11.579 / 1.003 = 11.54 m.
- The deck top recedes from y 629.7 (front) to about y 590 (far end at the grass). Since Z ∝ 1/(y − 531),
  Z_f / Z_back = 59 / 98.7.
- Setting (Z_f + Z_back) / 2 = 11.54 gives Z_f = 8.65 m and h_d = 46 × 8.65 / 1000 = **0.398 m**.
- This matches route 1's Z_f of 8.62 m, so the pier origin depth is reproduced.

## Uncertainty
- Focal length ±3.5% and horizon ±3 px give about ±4% overall.
- If the boat had no keel below the water (stem top = 0.75 m), f/Z_b would be 164.7 and the answer 0.41 m.
- Final answer: 0.40 m. Confidence is moderately high.

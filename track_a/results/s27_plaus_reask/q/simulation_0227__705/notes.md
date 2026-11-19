# q705: width of the beach chair (m)

The prior is the black cat's speed, 1.041 m/s. There is no depth_info. The question fps and the file fps are both 24, and the camera is static.

## Scale
- The cat walks steadily to the right at constant image height (body_cy 886.2 → 885.6). Its apparent height is the same at the start and the end (52.5 vs 53.6 px), so the walk is lateral, across the view.
- A linear fit of body_cx over frames 0–49 gives 5.389 px/frame = 129.35 px/s (`speed.py`; the net displacement gives 5.378).
- Scale: 1.041 / 129.35 = **0.008048 m/px** at the cat's depth (paws at y ≈ 918).

## Chair width (frame 0, zoomed crops in `crops.py` → frames/edges.png)
- The front-row loungers are seen from the foot end, so their horizontal x extent is the width.
- Front-left lounger: front frame and legs from x ≈ 765 to 947, which is **182 px**.
- Middle lounger: x ≈ 1006 to 1189, about 183 px. This agrees and is the second check.
- The right lounger (1215–1432) is turned at an angle and is not used.

## Perspective correction
- The lounger's front feet stand at y ≈ 900 and the cat's paws at y ≈ 918, so the lounger is slightly farther away.
- The horizon is at about y ≈ 560–640. This comes from the lounger's left side line on the ground: front leg at (767, 900), rear leg at (783, 872), extended to the principal-point column.
- Ground depth goes as 1/(v − v_h), so the depth ratio is 1.05–1.07.

## Result
- Width = 182 × 0.008048 × ~1.06 ≈ 1.54–1.57 m with the perspective correction, or 1.465 m with the plain single 2D scale.
- **Answer: 1.53 m.** It lies between the two readings and is within 5 percent of both.

## Plausibility
- 1.5 m is wide for a lounger. However, the lounger's own proportions in the image show it is a wide model: its width is about 4.5 times its 40 px leg/frame height.
- With the same scale, the leg height comes out at about 0.34 m, which is realistic.
- I found no error in the geometry: the cat's motion is lateral and its size is constant, so I kept the scale from the prior.

## Confidence
Moderate. The pixel measurements are good to about ±2 percent. The main uncertainties are the depth correction (about 5 percent) and the possibility that the reference answer used the plain 2D scale.

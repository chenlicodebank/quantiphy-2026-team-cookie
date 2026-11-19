# q2726 — height of the pink bottle (cm)

Lab video, 24 fps (file and question rates match), 1280x720, f = 0.5959*1280 = 762.8 px. The camera is static and the bottle doesn't move (frame differences in the bottle box come only from the ball/hand elsewhere; profiles taken at f48).

## Measurement (measure.py)
- Vertical colour profiles (R-B and brightness) at columns x = 648, 655, 662, 670 on f48:
  - top silhouette edge: y ≈ 327.5-328 (the step from grey wall to cap; bright rim at 330)
  - bottom edge: y ≈ 476.5-477 (contact shadow at 478)
  - pixel height ≈ 149 px. This agrees with the scene record (y330-479; its 149 px came from a cruder box).
- The bottle is ≈50 px wide (x≈640-689), so its radius is about 3.3 cm at this depth.

## Scale
- Method card: H = d * px / f = 0.9998 * 149 / 762.8 = 19.5 cm.
- Perspective refinement: the cap top lies above eye level (horizon y≈349) and the base lies below it, so both silhouette extremes are on the bottle's front rim. The front rim is closer than the centre by about one radius: Z ≈ 0.998 - 0.033 ≈ 0.965 m, giving H ≈ 0.965*149/762.8 = 18.9 cm.
- Answer: 19.2 cm, the midpoint of the two readings, so it is within about 2% of either one.

## Check (card.py + inline profile)
- The credit card is the dark-blue card near the table front edge (yellow sticker), with distance 0.6867 m. Its blue/dark extent is about 90-93 px, which gives 8.1-8.4 cm against the true 8.56 cm. The edges are blurry, so this check is only good to a few percent, but it confirms the focal length is consistent with the video.

Confidence: good. The result is ±3%, mostly from the depth-plane convention and ±1 px edge blur.

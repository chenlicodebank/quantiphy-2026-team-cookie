# q_614 — lampshade diameter (simulation_0216)

Prior: the black cat moves at 0.94 m/s. No depth_info is given. fps = question_fps = 24.

## Cat speed (px)
I checked scene/tracks/cat.csv `body_x_matched`. The per-frame steps are 13.9–20.0 px and the mean is 17.74 px/frame.
A linear fit to the torso centroid gives 17.87 px/frame. Using 17.74 px/frame x 24 = 425.8 px/s, the cat-plane
scale is 0.94 / 425.8 = 0.002208 m/px. As a sanity check, the cat's nose-to-rump length of 245 px comes out at 0.54 m.

## Lampshade width (px)
`shade_rows.py` reads grey-level row profiles at frame 24. The widest part is the bottom rim (y ≈ 602–604). The left
edge is at x ≈ 1238.7 and the right edge at x ≈ 1449–1451, so the width is **211 px**. The scene record gives
212 px, which agrees. The camera is static, so any frame works.

## Perspective
The cat walks in front of the TV stand: its paws touch the floor at y ≈ 1020, the stand's foot hoops at y ≈ 990,
and the wall base is at y ≈ 947. The TV's edges are exactly vertical, so I assumed a level camera with the horizon
at y ≈ 540. Depth goes as 1/(y − 540), which gives:
- stand front feet: 480/450 = 1.067 × the cat's depth;
- wall: 480/407 ≈ 1.18 × the cat's depth.

The lamp stands on the stand top, about 0.2 m behind the front feet. For any focal length from about 1400 to
4000 px, that puts it at about 1.09–1.13 × the cat's depth. I used 1.09.

## Answer
211 px × 0.002208 m/px × 1.09 ≈ **0.505 m**.

The uncorrected 2D single-scale value is 0.466 m. The correction is uncertain to about ±4% because the horizon
and the lamp's position front-to-back are unknown.

## Second route and confidence
- I checked the scale against the TV: its 399 px width gives about 0.96 m (a ~43" TV), which is plausible.
- The cat's speed is consistent across tracking methods (17.7–17.9 px/frame).
- Confidence is moderate, roughly ±7%. The main uncertainty is the depth ratio between the lamp and the cat.

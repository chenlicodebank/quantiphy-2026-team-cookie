# Q812 – length of the house (m)

Prior: speed of the horse at the back = 0.874 m/s. No depth_info. fps = question_fps = 24.

## Which horse
There are two horses, brown (upper, x≈750→874) and white (lower, ahead in x). The brown one trails the
group and is also the farther one up the image, so I took it as "the horse at the back". Check: brown at
0.874 m/s gives a body length of about 2.0 m and puts the white horse at about 2.4 m and 1.5 m/s, with the
dog about 0.5 m. Those are realistic sizes. If the white horse were the reference, both horses would be
only 1.1–1.4 m long.

## Scale from the prior (speed.py)
I tracked the brown horse body with template matching over frames 0-48 (frame 49 is a loop reset): 2.648–2.685 px/frame,
so I used 2.665 px/frame = 63.96 px/s. That gives s_b = 63.96/0.874 = 73.2 px/m at the horse's back
height (z_b ≈ 1.3 m). The scene centroid track gives 2.59–2.70 px/frame, which agrees.

## House geometry (edges.py, edges2.py, zoomed crops)
The camera looks straight down (nadir). The principal point comes out at (≈963, ≈535) from the gable perspective.
- Main block: gable roof with its ridge along y at x≈1019. Eaves at x = 660.5 and 1362.3, so the x-extent is
  701.8 px at eave depth D_e. The ridge ends sit at y = 21 / 745.5 and the eave corners at y = 95.3 / 714.7,
  so the y-extent is 619.4 px at D_e.
  Depth ratio D_e/D_ridge = 1.170 (the same from the top gable, the bottom gable and the x-offset of the ridge).
- Cross wing: ridge along x at y≈380. The gable apexes are at x≈618 and ≈1424, and the eave corners at x≈650 and ≈1380
  (ratio 1.104). The main ridge runs under the wing slopes (it ends at y=352 and y=415), so the wing ridge is higher.
  From this, D_e(main) = 1.089 × D_e(wing). In world units the wing's x-extent is 670 px·D_e/f, which is
  smaller than the main block's 701.8 px·D_e/f.
- So the house length (longest horizontal extent) is the main block's eave-to-eave x-extent, 701.8 px at depth D_e.
  The width is 619.4 px at D_e, about 0.88 × the length.

## Perspective correction
The roof is closer to the camera than the horse, so the ground scale cannot be applied to it directly:
L = 701.8·(H − h_e)/f with H = f/73.2 + z_b, which gives **L = 9.59 m − 701.8·(h_e − z_b)/f**.
The image alone does not fix f and the eave height h_e:
- The roof pitches give tanθ_main = 4.14e-4·f and tanθ_wing = 7.66e-4·f. Plausible pitches of 30–48° give f ≈ 1400–2700 px.
- Hoof versus back parallax on the brown horse (rough) gives H ≈ 30 m, so f ≈ 2100 px.
- Tile texture and shadows could not pin this down: the two roofs have different tile UV scales, and the ground
  near the house is in tree shadow.
- The animals are at real-world scale, so I assumed a realistic main eave height h_e ≈ 3 m.
  With f ≈ 2000, the main pitch is 40°, the main ridge 6.7 m, the wing eave 5.1 m and the wing ridge 7.3 m,
  and the footprint is 9.0 × 7.9 m. These are consistent house proportions.

L = 9.59 − 701.8·1.7/2000 ≈ 8.99 m. Across f = 1500–2700 and h_e = 2.5–4 m, L ranges from 8.3 to 9.3 m.
The pure ground-scale (planar 2D) value would be 9.6 m, and the upper bound with z_b = h_e is 9.59 m.

## Answer
8.9 m. Confidence is moderate: the eave height above the ground and the focal length are only constrained
by plausibility, which leaves an uncertainty of about ±6%.

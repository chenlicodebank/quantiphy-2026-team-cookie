# q1331 — width of the lane (road surface curb to curb), simulation_0066

The file and question rates are both 24 fps. Frames: t=0.58 s is f14 and t=1.58 s is f38.
Correction to the scene record: the yellow car is the **taxi** (19.65 / 16.55 m) and the white car is the **van** (23.59 / 19.99 m).

## Road geometry (lines.py, using the clean background bg.png)
- Road mask: grey pixels with low saturation. Curb edges are fitted by total least squares (rms 0.6–1.0 px).
- Road R1 runs left–right. Its far curb is a single straight line across the image (the left and right parts are collinear).
  Its near curb is the upper-left edge of the near-corner sidewalk. Vanishing point ≈ (3130, 78).
- Road R2 recedes up-left. One curb is the far-mid corner edge, which is collinear with the right corner's left edge.
  The other is the right edge of the near-corner sidewalk. Vanishing point ≈ (610, 71). The horizon is at y ≈ 75 and level.
- Both curb lines are taken at the road-side edge of the curb band.

## Camera (principal point at the image centre, no roll)
- Focal length: the roads come out perpendicular at f ≈ 850–880 px.
  - Van 3D box fit (width 2.0 m, height 2.1 m, heading along R2, origin at ground at the given depth) gives a van length of 5.1–5.4 m at f = 820–850. A larger f makes the van implausibly short (4.4 m at f = 950).
  - Purple-car wheelbase is 2.96 m at f = 850. Pedestrian walking speed is about 1.2 m/s.
  - Chosen value: f ≈ 850 (HFOV ≈ 104°, slightly wider than the stated range).
- Camera height h above the ground, two routes:
  - (a) Pedestrian: pelvis (0.54 × height) above the feet, at the given distance. h = 7.05 m over 13 frames (spread ±0.07).
  - (b) Van box fit at f14 and f38 with the given depths. h = 6.95 m.
- Check against the prior: back-projecting the van centroid onto its height plane gives a path length that fits a = 4.0–4.1 m/s². This is consistent, but it hardly depends on f.

## Width (perpendicular distance between the back-projected curb lines on the ground; final.py)

| f (px) | R1, h from van | R1, h from pedestrian | R2, h from van | R2, h from pedestrian |
|---|---|---|---|---|
| 820 | 11.82 | 11.88 | 12.15 | 12.21 |
| 850 | 11.74 | 11.91 | 11.86 | 12.03 |
| 880 | 11.66 | 11.94 | 11.58 | 11.85 |

- R1's width hardly depends on f.
- At f ≈ 850 both roads are about 11.9 m wide.

**Answer: 11.9 m.**

Uncertainty about ±3%:
- choice of camera height route;
- whether the curb band is raised, which would add about 1% to the width.

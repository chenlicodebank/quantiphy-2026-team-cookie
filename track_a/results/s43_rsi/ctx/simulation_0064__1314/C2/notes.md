# q1314: height of the traffic light (simulation_0064)

The file and the question both run at 24 fps. There are four identical signals, one on each corner. I take "height" as the asset's vertical extent: from the pole base on the sidewalk up to the apex of the warning sign on top.

## Where the earlier answers part ways
C1 got 4.97 m and C2 got 3.4 m. They differ in the **focal length and camera height**. C2 took f = 2727 px from an assumed size for the van. That f makes the van about 2.4 m wide and the pedestrian about 1.47 m tall, so it is wrong. C1 found f ≈ 2210 px from the vanishing points, which is close to my result. **I agree with C1** and get a slightly higher value.

## My measurements (vvp.py, model.py, solve.py, profiles.py, pedsig.py, horizon_lights.py)
- **Vertical vanishing point:** I fitted sub-pixel dark ridges along both near poles (rows 420–560, rms 0.4 px). The lines meet at (1057, 7586); C1 got 7887. I used yv between 7586 and 7900.
- **Horizon:** I placed it so the far-left signal comes out the same height as the near-left one. I compared the top and bottom of the pedestrian-signal box above the pole base on each. This puts the horizon between y = -121 and -150, which matches the record's curb vanishing point (-121). The van's own track suggests -40 to -66, but that estimate is biased because the top of the roof and the front width are at different depths.
- **Focal length and pitch:** f² = (cy - yh)(yv - cy), giving f ≈ 2160–2270 px and a pitch of about 17°.
- **Camera height:** The pedestrian's pelvis at f38 (D = 38.722 m) is placed on its ray, and the feet are at row 298. That gives H = 6.7–7.1 m and a pelvis height of 0.88 m. The cyclist at f14 (D = 33.998 m) gives the same H.
- **Traffic light:** near-left base at row 570.8 (pole x 434), sign apex at row 65.5; near-right base at 566, apex at 64. Each base is put on the ground plane and the apex row is converted to a height on the vertical through it.

| yv | yh | f | light L / R (m) |
|---|---|---|---|
| 7586 | -121 | 2158 | 5.08 / 5.08 |
| 7586 | -150 | 2205 | 5.12 / 5.12 |
| 7900 | -121 | 2206 | 4.99 / 4.99 |
| 7900 | -150 | 2254 | 5.03 / 5.03 |

Over the whole range of horizon (-180 to -80) and vertical vanishing point, the result stays between 4.9 and 5.16 m.

## Checks
- The two near lights, measured independently, agree to 3 mm.
- Using the same f, the van's paint width (120 px at a front distance of about 35.4 m) comes out 1.94 m, a realistic full-size van. The pedestrian comes out 1.67–1.71 m tall, a plausible adult, and the pelvis height of 0.88 m fits that.

Answer: **5.05 m** (middle of the range). Confidence: about ±3%.

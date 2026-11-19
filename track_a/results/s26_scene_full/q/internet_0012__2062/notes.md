# q_2062: length of the white car in the second lane from the left

**Object.** The left carriageway has three lanes. Its lane lines sit at x ≈ 753 (solid), 851, 947 and 1046 (median edge).
The white sedan "white_car_upper" (centre x ≈ 868) drives in the middle lane, between x 851 and 947. That lane is second from
the left whether you count across the image or from the driver's left, since the car travels down the image. The other white
car (x ≈ 829) is in the leftmost lane.

**Video and camera.** The drone camera looks straight down and does not move, so the scene is treated as planar. One scale
factor converts everything, following the annotators' convention.

**Lane width in pixels** (`measure.py`, column brightness peaks of the lane lines at four dash rows, y ≈ 1430–2615):

| lane | width (px) |
|---|---|
| left | 98.0–98.6 |
| middle | 96.0–96.1 |
| right | 98.4–98.5 |

The mean is about 97.3 px, and I used **97 px = 3.66 m**, which gives 0.03773 m/px.

**Car length in pixels.** I measured the half-maximum brightness ends along the car's centre column at frames
0, 20, 40, 54, 70, 90 and 107. The results were 120.9, 120.6, 119.9, 120.2, 119.9, 120.3 and 120.6 px. The scene record gives
121.5 px for the body box and 120.2–121.3 px for the per-frame edge length. I used **121 px**.

**Answer.** 121 × 3.66 / 97 = **4.57 m**.

**Check against the other lane widths.** Scaling by the middle lane alone (96 px) gives 4.61 m. Scaling by the outer lanes
(98.5 px) gives 4.50 m. This spread of ±1.5% is the main uncertainty. A typical sedan is 4.5–4.9 m long, so the result is
plausible.

**Confidence.** Good, within about ±3%.

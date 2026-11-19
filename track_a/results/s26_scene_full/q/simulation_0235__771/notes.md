# q_771: height of the green (teal) section of the wall

Prior: the basketball's diameter is 0.282 m. There is no depth_info. The file's fps and question_fps are both 24, but this is a size question, so time does not matter.

## Measurements (frame 0; the wall is static)
- **Green band** (`prof.py`): column profiles at x = 300, 600 and 1500 agree.
  - The grey ledge changes to green at y ≈ 441.6.
  - The green changes to the orange floor at y ≈ 905.0. This is where the wall meets the floor. The light court line at y 917–921 is on the floor in front of the wall.
  - Green height: **463.4 px**.
- **Ball** (`ballw.py`): the horizontal chord width at the half-contrast level is 105.6–106.1 px over frames 0, 10, 24, 40 and 49. I use **106.0 px**. The record's circle fit gives 106.1, which agrees. Scale at the ball's depth: 0.282 / 106 = 0.002660 m/px.

## Perspective correction
`stripe.py` fits the edges of the floor stripe that runs toward the camera. They converge at (959, 543), which is the image centre, so the camera is level and the horizon is at y ≈ 541.5 (±1.5).

The ball touches the floor at frame 24: its centre is at y 865.6 and its radius is 53 px, so the contact point is at y ≈ 918.6. The wall's base is higher in the image, at y 905. For floor points, depth is proportional to 1 / (y − y_horizon), so:

Z_wall / Z_ball = (918.6 − 541.5) / (905.0 − 541.5) = **1.037**

This ratio is insensitive to the horizon value: it stays at 1.0374–1.0376 for horizons from 540 to 543. The wall is about 4 % farther away than the ball, so its m/px scale is about 4 % larger.

## Result
Height = 463.4 px × 0.002660 m/px × 1.037 = **1.279 m**

## Checks and confidence
- **Checks:**
  - The band edges agree to within 0.5 px at three x positions.
  - The stripe's edges and its width both put the horizon at the same place (y ≈ 543).
  - Ignoring perspective would give 1.233 m. I don't use that value, because the ball clearly lands in front of the wall's base.
- **Confidence:** moderate to high, about ±3 %. The main risk is whether the reference counts only the visible green band, from the ledge down to the floor.

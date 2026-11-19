# q 3142: width of the bench (m)

Prior: the scooter rider's average speed is 4.46 m/s. This is an internet video, so I used one planar scale from the prior. The file and the question are both at 30 fps, so no re-timing was needed.

## Scale from the prior
- The camera is static. Drift is 2-3 px, which is negligible.
- Average pixel speed is the mean per-frame step of the horizontal reference point (from scene/tracks/rider_scooter.csv):
  - scooter_cx: 18.24 px/frame over frames 0-73 and 18.00 over 0-80.
  - rear_wheel_cx: 18.38 and 18.11.
  - upper_body_x (an independent body track): 18.23 and 17.94.
- I took about 18.1 px/frame, which is 543 px/s. Scale = 4.46 / 543 = 0.00821 m/px (range 0.00815-0.00829).

## Bench pixel size
- The bench is seen face-on at frame 0 and is static.
- bench.py thresholds dark pixels. Rows y = 600-650 give x from 1344-1347 to 1650-1657. That is about 313 px from the left back post to the end of the right armrest, which matches the record's 1343-1656.
- Its front-to-back depth cannot be seen in this frontal 2D view. The only horizontal extent visible across the face is the long side, and that is what an annotator measuring in pixels would take. So I read "width" as the horizontal extent across the face.
- Width = 313.5 px x 0.00821 = **2.58 m**. Using the frames 0-73 speed instead gives 2.56 m; using the 0-80 speed gives 2.59 m.
- Alternatives:
  - Seat and back only, without armrests (x 1343-1613, 270 px): 2.22 m.
  - Front-to-back depth: not measurable.

## Sanity check and confidence
At this scale the rider would be about 2.6 m tall (315 px), so the prior's scale is about 1.4x larger than real-world scale. The bench is also slightly farther from the camera than the path. The benchmark convention (one scale from the prior) is followed anyway. Confidence is moderate: the main risk is the "width" reading and whether the armrests are included.

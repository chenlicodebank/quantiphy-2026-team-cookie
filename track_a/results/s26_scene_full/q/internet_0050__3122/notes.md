# q_3122: width of the left basketball backboard (m)

Prior: the scooter rider's average speed is 2.9 m/s. This is internet footage, so I used one planar scale, as the annotators did. The time base is 30 fps: the file and the question agree.

## Rider speed in pixels (speed.py, using scene/tracks/rider.csv)
The rider moves at constant depth and never reverses, so the mean per-frame |dx| equals the net displacement divided by 93.

| Reference point | px per frame |
|---|---|
| bbox centre (stabilised) | 15.876 |
| centroid | 15.858 |
| front wheel | 15.860 |
| rear end | 15.892 |
| bbox centre, raw image coordinates (no drift correction) | 15.74 |

I used the stabilised bbox centre: 15.876 px/frame × 30 = 476.3 px/s.
Scale = 2.9 / 476.3 = 0.006089 m/px.

## Backboard pixel width (board.py)
I took luminance profiles across three bands: the top frame bar (y 527-537) and two rows through the board (y 560-600 and 640-670). Each edge is placed where the board's dark outer frame meets the sky or trees.

| Frame | Left edge (x) | Right edge (x) | Width (px) |
|---|---|---|---|
| 0 | ~414 | ~668.5 | 254.5 |
| 46 | ~418 | ~672.5 | 254.5 |
| 93 | ~430 | ~684 | 254 |

The edges shift between frames because the camera drifts, but the width stays the same. Width = 254.5 px, which agrees with the record's 255.

## Answer
254.5 × 0.006089 = **1.55 m**.

## Checks
- The other reference points on the rider give a scale within 0.2 %.
- Using raw (unstabilised) coordinates gives 1.56 m.
- Sanity check: 1.55 m fits a 60-inch backboard (1.52 m). It is 15 % short of a regulation 1.83 m board. The board sits slightly behind the rider's ground line, which adds a small perspective error, but the convention is a single scale.

Confidence: moderate to high under the benchmark's convention.

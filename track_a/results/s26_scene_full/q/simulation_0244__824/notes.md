# Q824: height of the rabbit (m)

Prior: the antelope's speed is 1.277 m/s. The "antelope" is the large horned creature in scene/. This is a 2D scene: both animals cross at the same depth (feet and hooves at y ≈ 1547) and the camera is static. fps = question_fps = 30.

## Scale (from the antelope's speed)
Pixel speed of the antelope over frames 0–74, from straight-line fits and end-to-end differences:
- shoulder: 6.60 px/frame
- hip: 6.73 px/frame
- mask centroid: 6.74 px/frame
- bbox centre: 6.59 px/frame
- bbox front: 6.56 px/frame

The body_mid patch gives 6.38 px/frame, but its template drifts (lowest match score), so I left it out.

Speeds over 20-frame windows stay between 6.4 and 6.8 px/frame, so the antelope moves at a steady speed. I used 6.65 px/frame = 199.5 px/s, which gives a scale of 1.277 / 199.5 = 0.00640 m/px.

## Rabbit height in pixels
I took the bbox from scene/tracks/rabbit.csv and checked it on 5x zoomed crops at frames 0, 13, 26, 38, 51, 65 and 31 (`rabbit_crops.py`, `frames/rabbit_tiles_*.png`). The box includes the ear tips and the feet.

The height changes with the hop pose:
- upright with ears up: 66–68 px (ear tip at y ≈ 1481, feet at y ≈ 1548)
- stretched mid-hop: about 50 px
- median over frames 0–69: 61.5 px; 90th percentile: 67 px

The rest/standing pose, which is probably the AABB the reference uses, is close to the upright pose. I answer with about 65 px, between the median and the upright value.

## Answer
65 px × 0.00640 m/px = **0.415 m**

The value under each reading:
- upright pose (67 px): 0.43 m
- median pose (61.5 px): 0.39 m

## Second-route check
The rabbit moves at 6.71 px/frame, almost the same as the antelope, so both animals are consistent with being at the same depth and one scale fits both. The main uncertainty is which pose defines the height (about ±5%). Confidence: moderate.

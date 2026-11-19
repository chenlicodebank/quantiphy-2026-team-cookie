# q 817 — height of the antelope (m)

Prior: antelope speed 1.277 m/s. 2D scene, static camera, file fps = question fps = 30.
The animal is a kudu-like antelope with large spiral horns. It walks across the view at constant depth: the hoof line stays at y≈1547 and its apparent size does not change.

## Scale
I fitted lines to px vs frame from scene/tracks/creature.csv (speed.py):
- chest_front_x: 6.561 px/frame
- cx_mask: 6.538
- nose_x: 6.495
- rump_x: 6.476
- net displacement / 74 frames: 6.50

Taking ~6.53 px/frame gives 195.9 px/s, so the scale is 1.277 / 195.9 = 0.00652 m/px.

## Height
The bounding box runs from the horn tip to the hoof bottom. Its height is median 423 px (IQR 422–425, range 413–428), with top y≈1128 and bottom y≈1549. I checked the top and bottom on a gridded crop of frame 36.

Height = 423 × 0.00652 = 2.76 m. Using the extreme speed estimates (6.48–6.56 px/frame), the result ranges from 2.74 to 2.78 m.

## Plausibility
A kudu stands about 1.4–1.5 m at the shoulder, and its horns add roughly 1 m above the head, so 2.76 m total height including horns is plausible. If the horns are excluded, the head top is about 70–80 px lower, which gives about 2.25 m. I answer with the full AABB height, horns included.

Confidence: moderate to high. The answer depends on the reference AABB including the horns.

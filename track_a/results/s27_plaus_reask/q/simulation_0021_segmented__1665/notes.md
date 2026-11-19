# q_1665: average walking speed of the person

The file is 29 fps and the question is 30 fps. Times use 30 fps, frames are indexed as in the file, and the clip has 89 frames.

## Method
- Track: I used scene/tracks/man.csv. Pelvis x comes from the head centre and goes 85.8 to 252.3 px over frames 0 to 88 (1.89 px/frame on average). The motion is lateral (to the right), and the apparent height stays constant at about 222 px (head top 650, ground about 870).
- Scale, route 1 (height prior): 1.87 m / 222 px = 0.00842 m/px at the man's depth. The lateral speed is 166.5/88 × 30 × 0.00842 = 0.478 m/s.
- Scale, route 2 (depth_info, solve.py): I assumed a pinhole camera with a constant camera depth Z. Requiring that the pelvis pixel positions at frames 0 and 30 reproduce d = 13.882 m and 13.768 m gives f ≈ 1493 px and Z ≈ 13.16 m. This gives a speed of 0.49 to 0.50 m/s, net 0.490. Using f from the height (1567 to 1648) gives 0.45 to 0.48 m/s.
- The given distance change (-0.114 m in 1 s) is fully explained by lateral motion toward the image centre, so the depth component of the motion is about 0.02 m/s. The motion is therefore across the view, as the constant apparent size also shows.
- Plausibility: the hydrant comes out at about 1.0 to 1.1 m and the lamp post at about 4.2 to 4.7 m, which are plausible.
- The speed of about 0.5 m/s is below the usual walking range. feet.py shows that the planted foot slides backward by about 2.5 px/frame (frames 79 to 88): the walk animation slides its feet, and the root/origin moves at only about 0.5 m/s. The given depths confirm that the origin moves at this rate, so I kept the origin speed.

## Answer
0.49 m/s, the mean of routes 1 and 2, including a small contribution from the pelvis bob. Confidence is moderate, about ±8%.

# q_2672 — ping pong ball velocity at 1.4 s (cm/s)

- The file and the question both run at 24 fps. t = 1.4 s is frame round(33.6) = 34, and t = 0.9 s is frame 22.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Centroids come from scene/tracks/ball.csv. I checked them on zoomed crops of frames 22 and 34: frame 34's centre
  is about (838, 513) and the ball spans about x 808–870, y 490–537.
- Back-projection: P = depth x unit ray, with the depth taken as the Euclidean distance to the centre.
  - A = frame 22 at 1.010 m.
  - B = frame 34 at 0.716 m.
  - |AB| = 41.7 cm.
- Depth for the other frames: the ball rolls in a straight line on the table, so I intersected each frame's ray
  with the 3D line AB. The rays miss the line by ≤ 3 mm for frames 16–35, so the path is straight.
- I did not use apparent size for depth. The mask diameters are off by 10–20 %: at frame 22 the top merges with the
  white sky, and at frame 34 the halo and motion blur make it too large.
- Speeds near frame 34, from the per-frame 3D displacements (cm/s):
  - Forward differences at frames 30–34: 80.9, 80.3, 76.6, 83.7, 75.3. The 5-frame mean is **79.4**.
  - Quadratic or linear fits of the 3D positions over frames 24–35, 29–35 and 30–35, differentiated at frame 34:
    78.3–79.9.
- Check by a second route: the mean speed from frame 22 to frame 34 is 41.7 cm / 0.5 s = 83.4 cm/s. That fits a
  slow deceleration, from about 87 to about 79 cm/s.
- I did not use frame 36: there is probably a dropped frame between 35 and 36, and the ball leaves the table there.
- Answer: **79 cm/s**. Confidence: good (about ±5 %).

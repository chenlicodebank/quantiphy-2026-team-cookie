# Q822 – height of the left tree (m)

Prior: antelope (the horned creature) speed = 1.277 m/s. No depth_info. The file and the question are both 30 fps, so no re-timing.

## Scale
The shoulder landmark (scene/tracks/creature_landmarks.csv) goes from x = 425.0 to 913.6 px over frames 0–74. That is 6.603 px/frame = 198.1 px/s, and the motion is steady. The camera is static.
Scale: 1.277 / 198.1 = 0.006446 m/px. As a sanity check, the creature's height (421 px) comes out at 2.7 m.

## Tree pixel extent (trunk.py, frame 72)
- Top of the tree: the first non-sky pixels are at y ≈ 363 (x ≈ 120).
- Base: hidden. The blue trunk (x ≈ 64–100) can be seen down to y ≈ 1372. Below that, a bush covers it, and the bush's own ground line is at y ≈ 1560 (the animals' hooves are at about 1547).
- Pixel height: 1009 px if the base is at 1372 (only the visible part) and 1187 px if the base is at about 1550 (ground at the animals' depth).

## Readings
- 2D single scale: 6.5 m (visible part) to 7.65 m (base at y ≈ 1550).
- Perspective check: the camera looks level, since the trunk is vertical within about 9 px over 300 rows, so the horizon is near y = 960. Ground-plane depth ratio = 587 / (y_base − 960). With that correction, a base at 1550 gives 7.6 m, at 1450 gives 8.4 m, and at 1380 gives 9.2 m.
- The tree stands just behind the bush, which is at roughly the creature's depth. Both routes give about 7.6 m when the base is near the bush or animal ground line, and putting the tree a little behind the bush pushes the value up slightly.

Answer: 7.8 m. Confidence is moderate, because the tree's base is hidden and its exact depth is unknown.

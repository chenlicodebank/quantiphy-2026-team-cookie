# q_1743: average speed of the eagle (m/s)

Prior: boat speed = 4 m/s. Depths at t=1 and t=2 s for the boat, the human and the eagle. question_fps = 24, file fps = 25.
The file repeats video frames 1, 26 and 51, so render frame 24 (t=1) = video frame 25 and render frame 48 (t=2) = video frame 50.

## Where the eagle is
- `scan.py` lists the connected components in every frame. The only objects are the static rock (top), the person and the boat.
  `blob.py` confirms the rock is static, with no growth or flapping, so it is not the eagle.
- The eagle is visible only at the top image edge in video frame 0 (`specks.py`, `specks2.py`, frames/specks.png).
  Three small parts sit at x about 1145-1150, 1193-1205 and 1335-1355, rows y 0-7. In frame 1 only a 1-px speck
  remains at (1346, 1-3), and from frame 2 on nothing is left. The eagle leaves upward through the top edge in about one
  frame and stays out of view for the rest of the clip.

## Scale (geom.py)
- Boat ref point at r24 (552.6, 1356.4), depth 177.2077, and at r48 (359.3, 1302.2), depth 177.9993. Requiring |dP| = 4 m
  gives f = 9070 px (HFOV 9.7 deg).
- Checks: the person walks 0.99 m/s (plausible), and the boat hull is 9.9 m long (plausible).

## Eagle speed (estimate, low confidence)
- Radial component from depth_info: (177.1009 - 179.2691) / 1 s = -2.17 m/s, toward the camera. That is a hard lower bound.
- In-plane component, from the exit at the top edge:
  - The lowest tip moves about (+4, -4) px between frames 0 and 1, and everything is gone by frame 2 (needs at least 7 px per render frame).
  - That is about 100-170 px/s, which at about 181 m and f = 9070 px is 2-3.3 m/s across the view.
- Moving up in the image while getting closer fits an eagle climbing toward the downward-tilted camera.
- Combined: sqrt(2.17^2 + (2-3.3)^2), about 3.0-4.0 m/s. **Answer 3.5 m/s.**
- Caveats: the eagle is never tracked; the in-plane part comes only from wing or foot tips over 1-2 frames, which wing
  flapping can bias. The geometry alone cannot fix the tangential speed: with two depths, |V|^2 = (d0^2 - 32910.1)/2
  depends on the unknown d0, which is very insensitive.

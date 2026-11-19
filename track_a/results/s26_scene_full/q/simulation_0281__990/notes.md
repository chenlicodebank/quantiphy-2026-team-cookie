# q_990 – width of the whale (prior: length = 19.17 m)

2D top-down render, camera static, 24 fps (file = question_fps). The whale's horizontal plane faces the camera, so
one metres-per-pixel scale from the prior's length works.

- Length = image-x extent of the whale's bounding box (snout to fluke tip). Width = image-y extent (pectoral fin tip
  to fin tip). This follows the AABB convention: width is the shorter horizontal extent, fins included.
- Frame 0 (the whale is still for frames 0-2, so this is close to the rest pose): bbox x 1117-3471 (2355 px), y 636-1617
  (982 px). I checked it by eye on a gridded crop (frames/f0.png). Scale = 19.17/2355 = 8.14 mm/px, which gives
  **width = 7.99 m**.
- Second route: the per-frame width/length ratio changes with the swim cycle, because the fins and flukes are animated.
  The per-frame value is 7.81-10.89 m (mean 9.32); the max span over the max length gives 9.76 m. (measure.py)
- Answer 8.3 m: it is weighted towards the rest pose in frame 0 (7.99 m) and allows a little for pose dependence.
  Confidence: moderate. The main uncertainty is which pose the reference bbox was taken from.

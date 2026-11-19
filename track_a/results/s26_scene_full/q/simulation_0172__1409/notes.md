# Q1409: astronaut speed at t = 1 s (m/s)

Time base: the file and the question both use 24 fps, so t = 1 s is frame 24. Speed = |p24 - p23| x 24, using the 3D pelvis (root) position.

## Measurements (scripts in this folder)
- **Camera:** static (from the scene record).
- **Root track, `pack_fine2.py`:** fits a rigid upper-body template from frame 24 to frames 16-32. The fit allows similarity motion (scale, rotation and translation) and has subpixel accuracy. Two templates were used:
  - the backpack alone ("pack")
  - backpack + helmet + upper torso ("upper")

  The fitted transform carries the assumed pelvis point (1080, 795 in frame 24) into each frame. It also gives the apparent scale relative to frame 24, so depth Z(i) = Z24 x s24 / s(i).
  - Frame 23 to 24, pelvis image step: (+29.9, -14.4) px (pack) and (+30.2, -14.3) px (upper).
  - Scale s23 = 0.9949 (pack) and 0.9938 (upper), so the astronaut is approaching the camera fast during the push-off. This agrees with the whole clip, where the scale grows from about 0.93 at frame 0 to about 1.19 at frame 79.
- **Depth:** depth_info gives 18.147 m at frame 24 (Euclidean distance; converted to Z along the optical axis, a 0.1 % correction). The principal point is taken at the image centre (1152, 648).
- **Focal length from the 2.2 m height prior:** the suit is never in a rest pose, so the rest height in pixels at frame 24's depth was estimated in three ways:
  - Upright walking frames 76-79: 438 px / scale 1.19 = 368 px, about 380 px after correcting for knee bend.
  - Segment sums on frames 36 and 42 (helmet top to hip, plus a straight leg): about 388-397 px.
  - The bounding box at frame 36 (401 px) includes a pointed toe, so it is an upper bound.

  Taking H ≈ 388 ± 10 px gives f = 388 x 18.147 / 2.2 ≈ 3200 px (range 3100-3300).

## Result (`speed.py`)
| Template | v(24) at f = 3200 | Lateral part | Depth part |
|---|---|---|---|
| pack | 5.14 m/s | 4.63 m/s | -2.23 m/s |
| upper | 5.40 m/s | 4.68 m/s | -2.69 m/s |

- Varying f from 3100 to 3300 changes v by ±2.5 %.
- **Second-route check:** the central difference over frames 23-25 gives 4.96-5.14 m/s, and v(25) gives 4.8-4.9 m/s. Speed is falling just after the push-off, which fits the take-off at frame 19.

**Answer: 5.2 m/s.**

## Confidence
Moderate. The main uncertainties are:
- the depth-rate part, which comes from the template scale (pack and upper differ by about 20 % in dz);
- the rest-height pixel estimate behind f (about ±3 %).

Overall uncertainty is about ±8 %.

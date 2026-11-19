# Q717: width of the orange chair next to the blackboard

**Answer: 0.50 m**

## Object
The chair right next to the blackboard is the pale-orange chair standing against the wall, just right of the board's
lower-right corner (x ≈ 1600–1795 px, y ≈ 740–1025 px). It faces the camera. The two foreground chairs are much
closer to the camera and are not "next to the blackboard". The scene is static, so I measured on frame 48.

## Scale
- Prior: the chalkboard length is 5 m. I used the board's outer frame, 320–1692 px = 1372 px (from scene.json; I
  checked it visually). At the wall's depth that gives u = 5/1372 = 3.644 mm/px.
- The chair is in front of the wall, so its pixels need a depth correction.
- `vp.py`: I fitted Hough lines to the receding ceiling-grid lines. They meet at (959.0, 538.6). So the camera is
  level, the principal point is at the image centre, and the horizon is at y = 538.6.
- Floor contact points, with depth Z ∝ 1/(y − y_h):
  - Wall–floor line: y ≈ 951.
  - Rear feet: y ≈ 1002, so Z_rear/Z_wall = 412.4/463.4 = 0.890.
  - Front feet: y ≈ 1022, so Z_front/Z_wall = 0.853.

## Pixel widths
Measured with `prof.py` (R−B "orange" threshold) and on zoomed crops (`crop.py`):

| Part | Pixels | Depth factor | Width |
|---|---|---|---|
| Backrest, rows 750–795 | 1601–1752 = 151 px | rear depth (posts continue down to the rear feet) | 151 × 0.890 × u = **0.490 m** |
| Front legs, outer edges | ≈ 1649–1794 | front depth | about 0.45 m |
| Overall horizontal extent (backrest left edge to front-right leg) | 141 wall-px | mixed | **0.514 m** |
| Seat, rear edge | 136 px | rear depth | about 0.44 m |

The answer, 0.50 m, takes the whole-object (bounding-box) side-to-side extent: between the backrest width and the
overall extent.

## Checks: the scale is self-consistent and realistic
- Camera height = 412.4 px × u = 1.50 m. Ceiling (wall–ceiling line at y ≈ 172) = 2.83 m.
- Chair seat height ≈ 0.42 m. Chair total height ≈ 0.85 m. Both are typical for a school chair, so the pixel-to-metre
  chain through the floor-depth correction holds.
- If the board's green surface alone (1327 px) were the "chalkboard", every value would be 3.4% larger (≈ 0.52 m).

## Ambiguity
"Width" here means the side-to-side extent across the chair's front. The front-to-back depth is poorly constrained
from this frontal view: the seat/leg depth is about 0.26–0.34 m with an estimated f ≈ 1890 px, which assumes square
ceiling tiles. This means the side-to-side extent may well be the longer horizontal extent. I still answer with the
side-to-side reading, because that is how a chair's width is normally named.

## Confidence
Moderate: about ±5% on the measurement, plus the ambiguity in what "width" refers to.

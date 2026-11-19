# q1612 — height of the vase (simulation_0212)

The question's rate (question_fps) is 24, the same as the file's rate. The camera is static and pitch is about 0.

## Focal length
- **Cat route** (`focal.py`): the cat's speed is 0.94 m/s, so from frame 0 to frame 24 it moves 0.94 m. Its depths are
  4.199 m and 4.481 m. Back-projecting the cat's core centroid gives f = 2152–2156 px. The mask centroid gives
  2147 px and the bbox centre gives 2098–2110 px. **f = 2150 px.**
- **Wall route** (`floorlines.py`, `horizon.py`, `lamp_axis.py`): the two wall–floor lines are y = 908.97 − 0.0749x
  and y = 565.05 + 0.128x. If the two walls meet at a right angle and f = 2150, the horizon is at v = 539, so the
  pitch is about 0°. The lamp's turned base is vertical in the image (dx/dy = −0.003), which also means no roll and
  a pitch near 0. With the horizon at 540, the wall lines alone give f ≈ 2141 px, which agrees.

## Floor and room
- The mirror's bottom centre is at pixel (1517, 814) and its depth is 6.407 m. That puts the camera 0.784 m above
  the floor.
- Check: the cat's lowest paw at frame 0 falls on the floor at Z = 4.02, which matches the cat's depth.
- The back wall is rotated about 28° to the image plane. The table's feet (front-left, rear-left, right) line up with
  it.

## Vase pixels (frame 48, `vase_profile.py`)
- The rim top is at y = 469.5 and the foot bottom is at y = 653.5, where it meets the table edge. That is 184 px.
- Belly x is 1502–1591, so the centre is at 1546.5.
- The record in scene/ gave y 468–634, but the bottom value there was wrong.

## Depth of the vase (Za, along the optical axis)
- **Mirror reflection** (`mirror_fit2.py`): the right edge of the vase's reflection is at x ≈ 1477, so its centre is
  about 1436. A mirror leaning 0–11° gives Za = 5.91–6.07. The leaning frame's slant (dx/dy 0.095) implies a lean of
  about 8°, which gives Za = 6.03.
  - Unresolved: the reflection's height in the image fits a vertical mirror better than an 8° lean.
- **Table plan** (feet back-projected onto the floor): if the vase sits midway between the table's front and back,
  Za ≈ 6.08.
- Check: the given leg depth of 5.69 m puts the leg centre at Z ≈ 5.54, while its foot on the floor is at 5.66. That
  fits splayed legs.
- **Za = 6.03 ± 0.08.**

## Height
Height = [113.5·(Za − r_foot) + 70.5·(Za − r_rim)] / f. The top and bottom image edges are the front points of the
rim (radius ≈ 0.05 m) and foot (radius ≈ 0.09 m), which are a little nearer than the axis.
- Za = 5.94 → 0.502 m
- Za = 6.03 → **0.510 m**
- Za = 6.08 → 0.514 m

## Confidence
The answer should be within about 3%. The main uncertainties are f (±2%), Za (±1.5%) and the bottom pixel row,
which the table edge may hide by 1–3 px (±1%).

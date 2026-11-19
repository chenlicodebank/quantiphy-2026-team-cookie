# q_2985: distance between the baby and the man (m)

Prior: total height of the sofa = 90 cm. **The sofa is not in this segmented video** (the background was replaced
by white), so its pixel height can't be measured. Only the man, the child and the toy truck are visible.
The scale therefore has to come from body proportions, chosen to be consistent with a sofa-scale planar
measurement. This is the main source of uncertainty.

Time base: fps 30.0003 and question_fps 30 agree. The answer is a static distance, so timing does not matter.

## Pixel distance (measure.py)
- Foreground mask (min channel < 200), connected components at frame 15:
  - man centroid (961.8, 285.4)
  - child centroid (265.4, 367.2)
- Centroid-to-centroid distance: 698-701 px over frames 5-15. It grows to 717 px by frame 35 because the
  camera zooms in about 1.8%. I use **700 px**.
- Bbox-centre distance: about 660 px (not used).

## Scale (metres per pixel at the people's depth)
| Reference | Pixels | Assumed size | m/px |
|---|---|---|---|
| Child head (measured) | 78 x 80 | about 0.16 m (toddler) | about 0.0020 |
| Child leg, hip to sole | about 167 | about 0.33 m | about 0.0020 |
| Man buttock-to-knee | about 265 | about 0.60 m | about 0.0023 |
| Man shoulder-to-hip joint | about 260 | about 0.52 m | about 0.0020 |
| Man head, tilted, crown to chin | about 125 | 0.23-0.25 m | about 0.0019 |

Adopted scale: 0.0021 m/px. As a check, the truck's 207 px then gives a 0.43 m toy truck, which is plausible.
A 90 cm sofa at the same depth would be about 430 px tall.

## Answer
700 px x 0.0021 = **1.47 m**

## Confidence
Low to moderate. The pixel distance is solid (±1%). The scale has roughly ±15% uncertainty because it relies on
body-proportion assumptions. If the annotators' sofa stood at a different depth from the people (for example,
behind them), their scale would differ, and that can't be recovered from this footage.

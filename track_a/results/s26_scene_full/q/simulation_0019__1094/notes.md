# Q1094 – width of the freestanding art display panel (m)

Answer: **1.53 m**

## Which object
- There are three display panels on stands behind the sculpture: an upper side panel, a lower side panel, and a wider middle panel. The middle one has a white base and sits mostly behind the sculpture.
- Its base meets the floor higher in the image (col ≈ 676, against ≈ 681–686 for the side panels), so it is ≈ 0.8 m farther back.
- The nearest panel (d = 11.042 m) is therefore a side panel, most likely the upper one. The two side panels are identical.
- Each side panel is a grid-mesh frame with a canvas, a light bar on top and a two-tier dark plinth.
- The plinth is the widest part:
  - plinth bottom tier: ≈ 121–130 px
  - frame: 95 px (rows 312.5–407.5)
  - light bar: ≈ 105 px

## Camera
- Focal length f ≈ 885 px, from two routes:
  - (a) The person's two given distances (6.84 m and 6.49 m), with pelvis pixel positions from the track, give f = 887.6 px. Both times give the same depth z = 6.336 m, which is consistent.
  - (b) Rest height 1.87 m against a maximum walking height of 257–261 px gives f = 868–884 px.
- Pitch ≈ 0: the wall's vertical edges stay at constant rows (±0.3 px across 320 px of columns), so the horizon is at col 539.5.
- Camera height H = 1.747 m. This comes from the person's sole contact at col ≈ 783.5 (near foot ≈ 787, far foot ≈ 781) at z = 6.336 m.

## Panel geometry (scripts: `contact.py`, `recon.py`)
- The plinth's floor-contact edge slopes in the image (col = 710.0 − 0.080·row for the upper panel, and the mirror image for the lower one).
- So both side panels are turned ≈ 29–31° toward the centre, in an arc.
- Footprint reconstructed on the floor plane:

| Panel | Front-edge length L | Depth D | Turn | Extent along the wall axis (AABB) |
|---|---|---|---|---|
| Upper | 1.580 m | ≈ 0.41 m | 28.9° | 1.536 m |
| Lower | 1.591 m | — | 30.8° | 1.543 m |

- Second route, using the given 11.042 m as the scale: the reconstructed distance to the panel origin is 11.36 m (origin at the centre) or 11.47 m (origin at the bottom). Rescaling to 11.042 m gives L ≈ 1.52–1.54 m and an AABB extent ≈ 1.47–1.49 m.
- The two scales disagree by ≈ 3–4%. I could not resolve this: a 1 px change in the contact columns is ≈ 0.7%, and the true position of the panel origin is unknown.
- A naive frontal estimate gives 126 px × 11.042 / 885 = 1.57 m.

## Readings
| Reading | Value |
|---|---|
| Full object including the plinth, across the face | 1.52–1.59 m |
| World AABB along the wall axis | 1.47–1.54 m |
| Frame/canvas panel only, without the plinth | ≈ 1.15–1.2 m |

The answer is the full object, about midway between the routes: 1.53 m.

## Confidence
- Moderate: about ±4% if the reference includes the plinth.
- If the reference measures only the frame, the answer is ≈ 25% too high.

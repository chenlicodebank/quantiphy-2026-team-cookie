# Q1583: length of the letter (paper slip) under the gun. Answer: 0.148 m

File fps = question fps = 24. 3D Blender scene, static camera, principal point taken at the image centre (1062, 540).

## Focal length (fitfall.py)
- The typewriter falls from rest at frame 0, and its track (scene/ ref = bbox centre, frames 2-9) is clean.
- I fitted a 3D free fall with g = 9.8: P(t) = A + ½ g t² d, with |A| = 4.32 m (given), and the camera
  pitch and focal length left free.
- Result: f ≈ 2770 px, pitch ≈ 12.2-12.7° down, rms 2 px.
- Simple check: the bottom edge's pixel acceleration is 11.46 px/frame², and a·Z/g gives f ≈ 2640-2690.

## Desk plane (geom.py, letter3d.py)
- Near desk corner at pixel (697, 885), distance 3.593 m. Far-right corner at (1995, 652), distance 5.009 m.
- I assumed zero roll and solved for the pitch that puts both corners at the same height: 11.6° at f = 2770.
  This agrees with the pitch from the fall fit.
- Checks with f = 2770:
  - The typewriter at rest (t = 0.5 s, distance 4.501 m) has its origin 0.13 m above the desk, which is plausible.
  - Its drop from t = 0 to t = 0.5 s is 0.89 m. The free fall gives 0.885 m for landing at frame ≈ 10.2.
  - The desk comes out about 2.4 × 1.1 m with an 86° corner, and the camera sits 1.14 m above the desk top.

## Letter (paperseg.py, tipprof.py)
- I measured the paper's edges at subpixel level on frame 0 (half-level crossings) and fitted lines to them.
- Corners:
  - left (1318.5, 625.5), the acute tip, partly blurred
  - front (1362.5, 643.1)
  - right (1413.5, 634.9): this tip lies in the gun's shadow and was found from the warm b channel of Lab
  - the back corner is hidden by the gun, so I completed it as a parallelogram
- I back-projected the corners onto the desk plane:
  - front-to-back side: 0.147 m
  - side along the desk front: 0.113 m
  - corner angle: 84°
- The slip's short edge is parallel to the desk front edge (1.4° off), so it is aligned with the desk and
  presumably the world axes.
- Bounding box in desk axes: 0.149 × 0.126 m. Length = longer horizontal extent ≈ 0.148 m.
- Sensitivity:
  - ±2 px on either tip gives ±0.007 m.
  - f from 2650 to 2900 changes the result by less than 0.001 m (the depths are fixed by depth_info).

## Second route and a discrepancy
- If the gun's given distance (4.704 m) is used as the paper's depth, the scale is 4.704/4.93 smaller, so the
  length would be ≈ 0.140 m.
- That distance does not fit the gun lying on the desk: the desk plane at the gun's pixels is at about 4.98 m,
  so its origin would have to float about 0.07 m above the desk or sit off the mesh.
- The desk plane rests on two given distances plus two typewriter checks that agree with each other, so I
  trust it more.
- Confidence: moderate, about ±7%.

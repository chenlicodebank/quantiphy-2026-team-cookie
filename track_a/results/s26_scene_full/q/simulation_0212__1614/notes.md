# q1614 — width of the floor mirror (simulation_0212)

Answer: **0.62 m** (horizontal extent across the mirror's face, frame included).
File fps = question fps = 24.

## Scale: focal length
- The prior is cat speed 0.94 m/s; the depths are cat 4.199 m (f0) and 4.481 m (f24). Back-project the cat at f0 and f24
  with those depths and solve |P24 − P0| = 0.94 m for f (principal point at the image centre):
  - torso-core centroid as origin: f ≈ 2150 (focal.py), range 2100–2158 for other reference points.
  - origin on the ground under the body (rig root, paw line y≈945 at f0, ≈908 at f24): f ≈ 2133 (focal_ground.py).
- Consistency checks with pitch 0 (see below): camera height from the cat ground points = 0.760 m (f0) and 0.761 m (f24),
  from the mirror bottom centre (6.407 m) = 0.777 m. The front-left bench leg's floor point then has a predicted distance
  of 5.70 m; the given value is 5.69 m (check_leg.py). With a body-centre origin the cat's f24 depth would come out at
  4.64 m, not 4.48 m (check_cat.py), so the ground-root reading fits better. I used f ≈ 2135.

## Room orientation (pitch/yaw), room_lines.py + pitch.py
- Back-wall/floor line: y = 907.5 − 0.075x. Right-wall/floor line: slope +0.131 through the corner (1690, 781).
- Treating these as perpendicular floor directions gives the horizon at y ≈ 535, so pitch ≈ 0.15° (the corner vertical
  is also near vertical). The back wall's vanishing point is at x ≈ 4970, so the wall, and the mirror leaning on it,
  is yawed about 28° to the image plane. Ignoring this would give 0.47 m, so the yaw has to be modelled.

## Mirror edges (frame 48, edges_fit.py, sub-pixel line fits, rms < 0.3 px)
- Inner glass left edge: x = 0.0874y + 1391.5. Inner glass right edge: x = 0.0953y + 1517.9.
- Outer right frame edge: x = 0.0971y + 1531.3, so the frame bar is about 15 px wide.
- On the left, the visible outer edge (x = 0.0969y + 1363.5) also includes the frame's side face, which is visible
  because of the yaw (24 px compared with 14 px on the right).
- Bottom outer edge: y ≈ 808 − 0.08(x − 1550), and its bottom centre is at about (1530, 810).

## 3D width (width_final.py)
- The bottom line is M + s·d, where M is 6.407 m along the ray to the bottom centre and d is the back-wall direction
  from its vanishing point.
- Each side edge's back-projection plane is intersected with this line.
- Results:
  - glass = 0.498 m, frame bar = 0.058 m
  - front-face width = glass + 2 bars = 0.614 m (f = 2150), 0.628 m (f = 2100), so ≈ 0.619 m at f = 2135
  - including the visible left side face: 0.629–0.643 m (this is frame depth, not width, so not used)

## Confidence
The geometry is consistent across checks: camera height from three objects, and the leg distance reproduced to 0.01 m.
The main uncertainties are f (about ±2%) and the assumption that the left frame bar matches the right one (about ±1%).
Expected error is about 3%.

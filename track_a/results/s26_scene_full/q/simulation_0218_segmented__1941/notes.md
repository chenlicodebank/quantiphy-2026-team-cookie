# q_1941 – long side of the white-line box on the floor

Prior: big robot speed = 5.924 m/s. fps = question_fps = 24, so no re-timing question. No depth_info.

## Data
- Frame 49 is the unsegmented background (camera static). The floor has two image-horizontal white lines
  (centre rows 843.0 far and ~908 near, at every x) and two wide slanted stripes joining them (left x≈517-642,
  right x≈1626-1799). Together they form the box (`lines.py`, `vp.py`, crops `frames/ldiag.png`, `frames/rdiag.png`).
- The stripe centrelines, fitted per row, meet at (960.7, 552.8). That is the vanishing point of the depth direction,
  close to the image centre, so the camera looks almost straight ahead and the stripes are perpendicular to the
  horizontal lines. Box pixel length between stripe centrelines grows linearly with row:
  1013.6 px at y=843 and 1240.7 px at y=908 (3.494 px/row; it reaches zero at y=552.9, the horizon).
- Robot: tread-band phase correlation gives 50.79 px/frame (frames 12→22: 50.784, 15→25: 50.795), so 1218.9 px/s.
  This matches scene/. Every rigid point moves at 5.924 m/s, so the scale at the depth of the near tread's outer face is
  s = 5.924/1218.9 = 0.004860 m/px. The tread's ground contact (silhouette bottom, middle columns) is at row
  891.5 ± 1.5 (`robot.py`).
- Note: scene/notes.md has the face visibility reversed. On the left of the image the robot's front fender
  shows, and on the right its rear shows. This does not affect the measurement.

## Method
On the ground plane the pixel length of an image-horizontal segment is proportional to (y − y_horizon). Applying the
robot's scale at the row where the robot touches the ground: the box length at row 891.5 is
1013.6 + 3.494·48.5 = 1183.1 px, and 1183.1 × 0.004860 = **5.75 m** (stripe centre to stripe centre).
- Between the stripes' inner edges: 5.40 m. Between their outer edges: 6.10 m. The answer uses the centrelines.

## Second route
Use the horizon explicitly. Camera height Hc = s·(891.5 − 552.9) = 1.646 m, which is plausible; the robot comes out
≈3.0 m tall. Then L = 1013.6·Hc/290.1 = 5.75 m from the far line, and the near line gives the same. If the horizon is
taken at the image centre instead (y = 540), the far line gives 5.72 m and the near line 5.76 m. A ground-contact row
of 889 or 893 gives 5.69 or 5.78 m.

## Which side is longer
The box's depth extent is D = f·Hc·(1/290 − 1/355) = 0.00104·f m. Assume the painted horizontal lines are as wide as
the stripes (0.36 m). Their 4 px (far) and 6 px (near) thickness then gives f ≈ 4600 px both times, so D ≈ 4.8 m. D
would only exceed 5.75 m if f > 5540 px (HFOV < 20°), which the robot's strong perspective makes unlikely. So the
long side is the image-horizontal side.

Confidence: good. The estimated error is about 2%, mostly from the exact ground-contact row and from where the line
centres are taken.

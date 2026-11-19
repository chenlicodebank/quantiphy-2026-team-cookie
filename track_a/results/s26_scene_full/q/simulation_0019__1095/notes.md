# Q1095: height of the freestanding art display panel. Answer: 2.01 m

The video is a 3D Blender render, rotated 90°: world up points to image −x, so heights are measured along image x. The camera is static.
The question's time base (33.26 vs 33 fps) does not matter here: t = 1 s gives frame 33 under either rate.

## Camera geometry
- **Floor seams** (`seams.py`): four depth-direction tile seams, fitted on frame 96, all meet at (540, 539), the image centre.
  - So the camera is level, with no pitch and no yaw.
  - The horizon is at image x = 540, and the principal point is the image centre.
  - Vertical world segments therefore project with length f·H/Z.
- **Focal length** (`focal.py`): from the person's two given distances (6.84 m at t = 0, 6.49 m at t = 1) and the pelvis pixel positions.
  - The walk is parallel to the image plane: the person's apparent height shows no trend.
  - Result: f = 888 px (±14 px from the rounding of the depths), with the person's optical-axis depth Z = 6.336 m.
  - Check: a 1.87 m person at that depth should be 262 px tall. The observed standing or walking height is 261–267 px (soles at x ≈ 788, head top at x ≈ 521 in frame 6).

## Panels
There are three identical display panels on stands in front of the wall (upper, middle and lower in the image).
- Each is a canvas in a dark frame, with a thin post at the top edge and a dark foot bar on the floor.
- The upper and lower panels are turned about 30° about the vertical axis. Their foot lines slant: x goes from 677 to 686 across the panel.
- The middle panel is mostly hidden by the sculpture.

Column-wise edges (`edges.py`, frame 0):
- Top of the panel (the post) is at x ≈ 517–519 for every panel.
- The foot's floor edge is at x ≈ 681 at the centre column of the side panels, and 677–688 for the visible part of the middle panel.
- The pixel height in a column is 159–170 px, and 163 px at the panel centres.

## Route A: floor geometry plus person scale
- Camera height: h = 1.87 × (788 − 540) / (788 − 521) = 1.737 m.
- In each panel column, H = h × (x_bottom − x_top) / (x_bottom − 540).
- Results:
  - Lower panel: 2.014–2.016 m.
  - Middle panel: 1.995–2.003 m.
- If h is instead taken from the depth-pair Z/f, it becomes 1.768 m and H rises to 2.04 m.

## Route B: given panel depth
- Floor geometry puts the panels in one row at Z ≈ 11.0 m.
  - The centre floor contact at x ≈ 681 gives Z = h·f / 141 ≈ 11.0 m.
  - The side-panel centres then come out at a distance of about 11.3–11.4 m.
  - So the nearest panel is the middle one, at D = 11.042 m, which implies Z ≈ 11.015 m. This is consistent.
- H = 163 px × 11.015 / f:
  - f = 888 gives 2.02 m.
  - f = 901 (from the person's pixel height) gives 1.99 m.

## Result and confidence
- Both routes agree on 2.00–2.02 m. **Answer: 2.01 m.**
- Estimated uncertainty is ±3%. The main sources are the person's foot and head pixel positions and the focal length.
- Correction to `scene/`: the record says the camera looks slightly down. The floor seams show it is level, with the horizon at x = 540.
- The record's panel height (canvas only, 122 px) excludes the stand and post. The full object spans x ≈ 518–686.

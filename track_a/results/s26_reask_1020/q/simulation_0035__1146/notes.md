# Q1146 – eagle wingspan (m)

File fps = question fps = 24. 3D Blender render, static camera, 1080x1080, principal point assumed (540,540).

## Scale (focal length)
- Prior: person height 1.75 m; depth_info person 139.10 m at t=1 and t=2 (constant; apparent height constant 40-42 px, so the body stays at ~that depth).
- Person head-to-sole height = 41 px (scene track median, re-checked with row-contrast profiles at frames 22-26, 46-50: top ~706.5, soles ~747).
- f = 41 x 139.10 / 1.75 = 3259 px (HFOV ~18.8 deg). Range for 40-42 px: 3180-3340 px (+-2.5 %).

## Eagle geometry
- Back-projected the eagle origin (mask centroid, frames 24 and 48) with depths 139.70 / 147.16 m:
  P1 = (-11.36, 2.02, 139.23), P2 = (-2.83, 2.43, 147.11) -> velocity (8.5, 0.4, 7.9) m/s, 11.6 m/s
  (a plausible eagle speed). The bird therefore flies diagonally away from the camera (~43 deg from the image plane).
- Check: the straight line through P1, P2 reproduces the image-x track at every other frame within ~1-9 px
  (frames 0-66), and the V-shaped wing-up views (both wings separated sideways) confirm an oblique rear view.
- Wings are horizontal and perpendicular to the flight direction: direction (-0.68, 0, 0.73) in camera axes, so
  the image shows only ~0.68 of the span (foreshortening). Projected endpoints of a 1 m span at each frame's position
  give 14.2-14.8 px per metre.

## Span measurement (measure.py)
Wings-level frames, horizontal extent of the dark mask (integer run 29-31 px; subpixel coverage sum 25.6-27.4 px, which
under-counts thin tapering tips): frames 4,5,29,30,31 -> 29.5-30.5 px; frames 52-53 -> 27.5-28.5; frames 62-63 -> 25-25.5
(wings visibly arched there, not fully spread).
Wingspan = span_px / (px per m):
- frames 4/5/29/30/31 (fully spread): 2.08, 2.12, 2.03, 2.10, 2.06 m
- frames 52/53: 1.86, 1.93; frames 62/63 (arched): 1.69, 1.72
Answer from the fully spread frames: ~2.05 m (two independent wing-beats, t~0.2 s and t~1.25 s, agree within 3 %).

Naive face-on value (ignoring the oblique flight) would be ~1.2-1.3 m, which is too small for an eagle and inconsistent
with the depth change in depth_info; the oblique geometry gives a realistic eagle wingspan (1.8-2.3 m).

## Confidence
Moderate: +-2.5 % from the person pixel height, +-3 % from span pixel quantisation, and some uncertainty in the assumed
wing direction (exactly perpendicular to the flight path, horizontal). Answer 2.05 m.

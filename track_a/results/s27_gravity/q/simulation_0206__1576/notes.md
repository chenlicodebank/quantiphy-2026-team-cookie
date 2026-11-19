# Q1576: typewriter length (m). Answer 0.44

File fps = question fps = 24. A 3D Blender scene. The typewriter falls from the top of the frame onto the desk (impact between frames 10 and 11) and comes to rest by about frame 23.

## Scale (focal length) from the gravity prior (`fit_fall.py`)
Pinhole camera with the principal point at the image centre and zero roll. Unknowns: focal f, camera pitch, start pixel, and initial speed.
- I fitted the bbox-centre track for frames 2-9 (scene record, checked) with 3D free fall at g = 9.8. The start point is at 4.32 m (t=0). The rest point at t=0.5, 4.501 m, at pixel (1233, 609.5), must lie on the vertical line below it.
- Result: f = 2810 px (2862 with the initial speed free), pitch 16° down, rms 1.9 px. Without the rest constraint the fit gives f = 2680-2750.
- Self-consistency: the predicted drop is 0.885 m, so impact at about 0.425 s (frame 10.2). That matches the impact seen between frames 10 and 11.
- Desk-plane check (`check_plane.py`, `locus.py`): at f = 2810 and pitch 16°, the nearest desk corner (697, 872) at 3.593 m and the gun at 4.704 m lie on one horizontal plane: 1.377 vs 1.421 m below the camera, and the gun sits a little above the desk. The "far right" corner at 5.009 m then falls on the desk's back-right corner region (y ≈ 575 at x ≈ 1750), not the front-right corner (1998, 655). If I wrongly use the front-right corner, the solution is f ≈ 1890, which would make the typewriter 0.68 m: implausible, so I rejected it.
- Everyday-object check at f = 2810: alarm clock about 0.18 m tall, telephone about 0.27 m, banker's lamp about 0.47 m. All plausible.

## Length
- Route 1, falling and almost frontal (frame 2, `measure_len.py`): mask width 291 px (290-297 over frames 0-4; the minimum is closest to frontal). The origin's camera Z is 4.263 m. L = 291 × Z / f = 0.441 m at the origin's depth, or 0.426-0.431 m if the extreme points sit 0.10-0.15 m in front of the origin.
- Route 2, at rest (`rest_plane2.py`): I back-projected the base's bottom-left (1097, 663) and bottom-right (1365, 640) extremes onto the desk plane (1.38-1.40 m below the camera). The span is 0.441-0.448 m, and the corner distances (4.35-4.55 m) bracket the origin's 4.501 m. With f = 2862 the span is 0.43-0.44 m. This route is sensitive to pitch.
- Combined: 0.44 m.

## Caveats
- The typewriter rests yawed about 9° from the desk's front edge. If the reference used a world-axis bounding box at rest, the x-extent could be about 0.47-0.48 m. I answer with the object's own length.
- Confidence: moderate-good, about ±5%.

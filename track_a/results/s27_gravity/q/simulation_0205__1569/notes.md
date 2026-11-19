# Q1569 — width of the typewriter (m)

Answer: **0.252 m**. This is the typewriter's front-to-back horizontal extent, which is the shorter horizontal side.

## Setup
- The video is 2124x1080 at 24 fps, and question_fps is also 24. The camera is static.
- The typewriter sits on the desk, axis-aligned with it: its front edge is within 0.3 deg of the desk's long-edge direction.
- I measured its base footprint on frame 24 in code (`edge.py`, darkest-outline profile) and checked it on an overlay (`mark.py`, frames/mark.png):
  - front-left bottom corner A = (939, 756)
  - front-right bottom corner B = (1148, 724)
  - back-left bottom corner C = (860, 707 ± 3); this is where the left-side bottom edge meets the vertical back-left silhouette.
- The paper rest top lies about 5 cm in front of the base's back (`paperrest.py`), so the base footprint sets the front-back extent.

## Focal length: the two routes disagree
- **Gravity route** (`fit_fall.py`, `joint.py`): free-fall fit of frames 0–11 with g = 9.8, depth 4.2401 m at t = 0 and 4.4097 m near t = 0.5 s. It gives f ≈ 2620–2640 px (rms 0.3 px).
- **Geometry route** (`desk.py`, `twrect.py`, `ppshift.py`): two independent rectangles need f ≈ 3630–3750 px.
  - The desk-top corners need f ≈ 3630 to form a right angle.
  - The typewriter footprint needs f ≈ 3750.
  - At f = 2635 both come out skewed by about 13 deg (103 deg instead of 90). Moving the principal point does not remove this.
  - With f ≈ 3650 the sizes are realistic: desk 1.59 x 0.86 m, magnifier 0.21 m long with a 9.7 cm lens.
  - At f ≈ 3650 the fall implies g ≈ 13.6 m/s² at 24 fps. That probably means a different time base or time scale in the render, but I cannot confirm it from the video.
- I used the geometry route. Fortunately the answer depends only weakly on f.
- The desk plane's normal comes from the desk-edge vanishing points. Its offset is anchored with the given distances (the magnifier at 4.4097 m, about 1 cm above the desk; the gun at 4.704 m; the near and far-right desk corners).

## Result (`final2.py`)
| f (px) | magnifier anchor | gun anchor | corner anchors |
|---|---|---|---|
| 3630–3750 | 0.253–0.257 | 0.260 | 0.244 |

- Mean over all variants (f, anchors, C ± 3 px): 0.252 m, range 0.231–0.275.
- The left-right base length is about 0.25–0.26 m, and the knobs and levers stick out beyond the base. So the front-back extent is the shorter side, i.e. the width.
- **Second route:** the gravity-based f = 2635 with its own desk normal gives a front-back extent of 0.27 m and a left-right extent of 0.35 m. The width is about 0.27 m under that route too, about 7% above the chosen answer.

## Confidence
Moderate. The likely error is about ±8%, coming from the back-left corner pixel, the plane anchor, and the f conflict.

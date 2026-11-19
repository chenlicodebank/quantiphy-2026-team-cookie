# Q1578 — height of the typewriter (m)

Answer: **0.17 m**

File fps = question fps = 24. 3D Blender scene. The camera is static and the principal point is assumed to be at the image centre (1062, 540).

## Camera
- **Pitch from the vertical vanishing point** (`vert.py`): I fitted sub-pixel lines to long vertical desk edges: the right pilaster (two edges) and the left desk side (two edges).
  - VP = (1072, 11436). Its x is about equal to cx, so roll ≈ 0. This gives f / tanθ = 10896 px.
- **Focal length from the free fall** (`fit2.py`): the typewriter is released at rest at t=0, with g = 9.8 (the prior) and D(t=0) = 4.32 m.
  - Fitting the bbox-centre track for frames 2–9 with the pitch tied to the VP gives f = 2789 (vz = 0) or 2824 (vz free), with an rms of 2 px.
  - Fitting the plate-top track instead gives f = 2490–2640.
- **Desk-plane check** (`heights2.py`, `desk.py`): the nearest desk corner (3.593 m) and the gun (4.704 m) lie at the same height with the VP pitch when f ≈ 2665.
  - The "far-right corner" depth (5.009 m) does not fit the corner I picked at (1590, 527) to within about 10 cm, so I left it out.
- **Adopted values:** f ≈ 2720 ± 120 px, pitch ≈ 14°.
- **Drop check:** with these values the origin's drop from t=0 to its position at t=0.5 s (D = 4.501 m) is 0.90 m. That puts impact at about 0.43 s, between frames 10 and 11, which matches the video.

## Height (`height2.py` / `height3.py`)
- Top and bottom pixel rows of the typewriter during the fall, frames 2–9 (`edges.py`, `bottoms.py`):
  - The top is the faint top of the paper rest.
  - The record's frame-9 bottom of 579 included shadow on the clock; the corrected value is 557.
- The typewriter keeps a constant attitude in the fall. I modelled its vertical pixel extent as H·cosα + d·sinα, using the exact projection with the per-frame depression angle α (about 4.6° to 13°) and the depth from the fall model.
- Fit over frames 2–9, rms 1.5 px:

  | f (px) | pitch | H (m) | d (m) |
  |---|---|---|---|
  | 2650 | 13.7° | 0.180 | 0.33 |
  | 2780 | 14.3° | 0.165 | 0.33 |
  | 2900 | 14.9° | 0.152 | 0.33 |

- At f = 2720, H ≈ 0.172 m.

## Second route
At t=0.5 s (frame 12) the origin pixel (bbox centre about (1234, 605)) at depth 4.501 m is 0.085–0.09 m above the desk top. The desk height comes from the nearest corner and the gun.

With the origin at the bbox centre, that means H/2 ≤ about 0.09: the machine is tipped forward with its rear lifted in frame 12, so the centre sits a little high. This gives H ≈ 0.15–0.18, which agrees.

## Plausibility
- In frame 2 the machine's width is about 295 px, i.e. about 0.45 m including the carriage.
- At rest its base is about 0.3 x 0.3 m: a portable typewriter, for which a height of about 0.17 m including the paper rest is realistic.

## Confidence
Moderate, about ±8%. The main uncertainty is the focal length and pitch: the answer scales roughly as 1/f, and changes by about 0.004 m per degree of pitch.

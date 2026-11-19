# Q1085 – height of the pedestal (square base) of the central sculpture

Answer: **0.62 m** (range 0.60–0.645 across the f / foot-depth uncertainty).

The file runs at 33.0389 fps and the question at 33.0 fps. I used question_fps (t = 1 s → frame 33) and frame numbers from the scene record.

## Scene geometry
- This is a 3D render with the image rolled 90°: world up points to image +x. `rot.py` and `crop.py` rotate frames upright for viewing.
- The "sofa" in scene/ is really a long bench (the bench_camera distance is 2.267 m). The "grey_block" is the dark square
  pedestal. The "light_plinth" is a tapered light-grey tier that belongs to the sculpture.
- **Camera is level.** Shelf posts at image y = 166.5, 372, 577, 822 stay at the same y from x = 600 to 1040 (`vert.py`), so
  there is no pitch and the horizon is at image x = cx = 540.

## Focal length
- **Route 1 (`focal2.py`, speed route):** the walk is parallel to the image plane, because head width and head-top x are
  constant. The image speed is about 250 px/s, so 1.3 m/s = 250 · 4.886 / sqrt(f² + 280²). Long windows give f ≈ 895–900.
- **Route 2 (depth ratio, no speed prior):** with constant forward depth, d0/d1 = 5.424/4.886. With the person's frame-0 position
  taken from the head (u0 ≈ −533, because the body is cut by the border), this gives f ≈ 898–905.
- The scene track's frame-0 pelvis (y = 20) is unreliable and gives 871 (`focal.py`).
- **Adopted:** f ≈ 900 px (HFOV ≈ 62°). The person's forward depth is Z ≈ 4.67 m.

## Camera height
- The planted sole in frames 4–16 has a sharp lower edge at image x = 348.5 against the bright floor (`sole.py`).
- h = 191.5 · Z / f ≈ 0.99 m (±0.02 for which foot is nearer).
- This matches the pelvis lying on the horizon (pelvis x ≈ 540).

## Pedestal (`pededges.py`, `topprof.py`, `solve.py`)
- **Front top edge:** image x = 476. Below it is the dark face; then a highlight at 476–477, a gap at 478–479, and the tier
  from 480.
- **Front corners:** y = 404.5 and 654.5, so 250 px wide, centred at y = 529.5 (on axis).
- **Bottom:** hidden behind the bench cushions (cushion top x ≈ 382). The floor at the pedestal front projects to x ≈ 369,
  which is hidden, consistent with that.
- **Depth:** square footprint with the origin at its centre. Z_c = sqrt(5.963² − Yp² − Xp²) ≈ 5.92 and
  Z_front = Z_c − w/2 ≈ 5.20 m, with w = 250 · Z_front / f ≈ 1.44 m.
- **Height:** H = h − (540 − 476) · Z_front / f = 0.993 − 0.370 ≈ **0.62 m**.
- **Sensitivity:** f from 875 to 910 gives 0.616–0.639. A foot-depth error of ±0.1 m moves it by ±0.02.

## Checks
- **Origin check:** the pedestal centre is about 0.68 m below the camera. The sculpture's bounding-box centre, from the tier
  bottom to the tip at x = 782, is about 0.61–0.63 m above the camera. The given distances (5.963 vs 5.962) need
  |Yp| ≈ |Ys|, which roughly holds; a small tip depth offset would close it.
- **Rejected reading:** taking "pedestal" to include the light tier (height ≈ 0.93 m) breaks this check badly
  (Yp² − Ys² ≈ −0.33 vs a given +0.012), so it is not used.
- **Panel depth not used:** the freestanding art display panel distance (4.223 m) cannot belong to the panels near the wall,
  whose bases stand on the floor at x ≈ 465 and so must be far away. That depth was not used.

## Confidence
Moderate. The main uncertainty is the camera height, which comes from one foot contact. Error is about ±5 %.

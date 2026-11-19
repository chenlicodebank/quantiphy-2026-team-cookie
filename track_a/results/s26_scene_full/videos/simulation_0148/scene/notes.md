# simulation_0148 — measurement record

Video: 1920x1080, 24 fps, 26 frames (t = i/24 s). Source: simulation (Blender). Declared 2D.
The camera is static and looks through a large dark arch (foreground, with a central pillar at x 1105-1205)
onto a subway track. One subway train/car passes right to left. Behind the track there is a lit platform
with a fence, a yellow traffic cone, a red sign and a dark green post. All units are pixels and frames. No metric scale is assumed.

## Files
- `scene.json`: inventory (train plus static objects with pixel extents), camera, events, train length and shift summary.
- `tracks/train.csv`: one row per frame 1-21 (the train is visible in frames 2-20). Columns:
  - `near_front_x`, `near_rear_x`, `near_centre_x`: x of the train's near-side wall front corner, rear corner and midpoint
    (the "near layer": the window frames and the dark body side). These are extrapolated when off-screen.
  - `far_front_x`, `far_rear_x`: the same corners on the far side (pixel scale 0.72 about x=960).
  - `origin_x_mid_depth`: the body centre projected at mid-depth (scale K=0.837 about x=960). This is the best estimate of the origin.
  - `near_shift_px` = x(i-1) - x(i) for the near layer, with `near_shift_source` (measured or line_fit), and
    `origin_shift_px` = 0.837 x near shift.
  - `bbox_*`: the visible silhouette clipped to the arch opening (approximate in y because the arch is curved). Also the window band y and an occlusion note.
- `scripts/`: `view.py`, `diffview.py`, `overlay.py` (render frames and checks), `mask.py`, `edges.py` (change-mask
  extents), `shift1d.py` (column-profile shift matching), `patches.py`/`patch.py` (patch NCC matching),
  `vert.py` (vertical extents and static items), `build.py` (builds the track from the measured numbers; it prints the fit).

## How it was measured
- Near-layer shift per frame: NCC of x-gradient column profiles (window band) between consecutive frames, searched
  in -420..-330 px, with two bands that agree to within 0.5 px. Measured for frames 6-12 and 14-18:
  353.4, 355.8, 360.2, 363.7, 366.1, 368.1, 371.6, -, 379.7, 383.4, 386.0, 387.6, 391.1.
  These lie on a straight line d(i) = 334.10 + 3.199 i (rms 0.8 px), so the train accelerates steadily in the image.
  Frames 2-5, 13, 19 and 20 had too little texture or mixed layers, so they are filled from the line fit (flagged).
  A manual check of frame 13 (window right edge 1820 to 1442 to 1063) gives about 378 px, which agrees within ±3 px.
- End corners: near front corner at f4 x=1511 and f6 x=810. Near rear corner at f17 x=1479 and f19 about 700 (the rear end
  face is visible from 700 to 776). Together with the integrated shifts these give a near-side length of 4768 px
  (4775 from f19). The train is longer than the image and never fully visible.
- Overlays (`overlay.py`) of the corner and bounding-box predictions on frames 2, 3, 4, 6, 7, 13, 17, 19 and 20 hit the observed
  edges. The model also predicts the train is gone at frame 21, which matches.

## Important ambiguity: perspective / two layers
The train is very close to the camera. Two layers of the same train move at different pixel rates:
the near side (window frames, dark body, near corners) and the far side (graffiti seen through the windows
such as 'otm', the sticker, 'NOT AGAIN' and 'AKC', plus the far edge of the lit front end face in frames 3-4). Matched far features move
0.72x as fast (249.6 vs ~347 at f4, 254.6 vs 353.4 at f6, 276.9 vs 386.0 at f16).
- For questions that combine the train's own length (or speed) prior with its speed, acceleration or distance, use one layer
  for both. The ratio length/shift is the same in every layer, so the near layer (best measured) is fine:
  near length 4768 px with near shifts d(i).
- For the origin (body centre) at mid-depth, scale the near values by K=0.837: length 3992 px, shift 0.837·d(i).
  The far layer gives length 3433 px.
- Distances to static background objects (cone, platform post) are at a different depth again. The cone is on the far
  platform, behind the train's far side, so planar conversions involving it are only approximate.
- The origin itself is never visible. Its x is computed, not observed. Its y is unknown (the roof and wheels are hidden by the arch;
  the visible body spans y≈330-450 down to 865, with windows at y 455-740).
- Whether this is one car or several coupled cars is not clear. No gap between cars was seen in the visible part, and the record treats it as one body.

## Other notes
- Headlight glow and floor-lighting changes ahead of and below the train (frames 2-6, y 870-1050) are lighting effects, not objects.
- Motion blur is small. Windows repeat, so naive block matching aliases (ignore `shift.py`'s output, which was an early attempt).
- Reliability: near shifts ±1 px (measured frames) and ±3 px (fill frames). End corners ±5-10 px. Near length ±15 px.
  The 0.72 layer ratio is ±0.02, and the end-face edges suggest 0.735-0.74, so K is ±0.01. Static extents are ±5 px.

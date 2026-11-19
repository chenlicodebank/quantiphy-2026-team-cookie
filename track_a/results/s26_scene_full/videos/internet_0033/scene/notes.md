# internet_0033 – measurement record (pixels, seconds)

Video: 2560x1440, 47 frames, 19.293478 fps (t = frame/fps). Internet footage, overhead view of 8 people at a
wooden dinner table. **The only object that travels is the dark-grey bowl of cherry tomatoes**, passed by the
curly-haired man (bottom right) up and to the right toward the bald man (right side) / pink-blazer diner (top right).
Everyone else stays seated and moves only their arms (eating).

## Files
- `scene.json` – inventory (moving bowl, plates, table items, people), events, camera, static extents.
- `tracks/tomato_bowl.csv` – bowl, every frame 0-46: `cx,cy` = centre of the fitted outer-rim circle (visible
  centre, image px); `rim_diameter_px`; bbox of the rim circle; `rim_inlier_rays_of_180` (fit support);
  `partial_occlusion_hand` (always 1, fingers on rim); `tomato_centroid_x/y` (centroid of red tomato pixels near the
  bowl, an independent cross-check of the centre); `cx_bgcomp_f0, cy_bgcomp_f0` = centre mapped into frame-0
  background coordinates (camera drift removed).
- `camera_motion.csv` – per-frame similarity transform frame_i→frame_0 (ORB + RANSAC, 1700-3700 inliers):
  content shift at image centre, scale, rotation, and the 2x3 matrix m00..m12.
- `camera_shift.csv` – raw phase-correlation shifts of 4 static patches (cross-check; the `floor_tl` patch is
  corrupted from frame 14 onward by an arm entering it – ignore that column there).
- `plates_f0.json` – 9 white plates at frame 0: centre, circle diameter, ellipse axes (ray + RANSAC rim fit).
- `scripts/` – all code: `track_bowl2.py` (final bowl tracker), `camera_sim.py`, `camera.py`, `plates_refine.py`,
  `static_plates.py` (Hough seeds), `bowl_steps.py` (per-frame steps), viewers `view.py`, `cropsheet.py`,
  `framelist.py`, `hsvprobe.py`. `track_bowl.py` is a superseded Hough-only v1 (noisy radius; do not use).

## Camera
NOT static: slow steady drift. Image content moves up ~0.95 px/frame (total -43.5 px in y by frame 46) and
1-4 px in x; rotation ~-0.2°, scale <0.3 %. For bowl motion use `cx_bgcomp_f0, cy_bgcomp_f0` (motion relative to
the table), per the "measure against the background" convention; raw image coords differ by up to ~44 px in y.
Mild perspective: identical dinner plates measure ~224-238 px near the top of the table and ~249-256 px near the
bottom (image bottom is nearer the camera). Annotator convention ignores this (single scale).

## Bowl track (how / reliability)
Rays from the tomato centroid walk inward from 150 px until they hit bowl-grey (S<80, V<100) or tomato-red pixels;
rays ending in skin are dropped; RANSAC circle (r 75-105 px, centre within 30 px of tomato centroid). Overlays were
checked visually (`frames/bowl_overlay2.png`). Frames 0-31: rim fit tight, centre ±2 px, diameter ±3 px.
Frames 32-46: left rim is dark against table shadow/purple flowers and fingers cover the rim; centre ±4 px,
diameter ±8 px (fit 159-173 px; a zoom at frame 42 gave ~163 x 162 px by eye, consistent).
Apparent rim diameter changes: ~186 px (frames 0-12) → ~190 (13-28, bowl lifted highest) → ~167 (32-46, bowl
lowered/further from camera). If a question gives the bowl's real diameter, the annotators' single "pixel length"
is most likely the early, clear value (~180-190 px; 180.2 px at frame 0); state which frame you use.
Motion (background-compensated): frames 0-12 nearly pure +x, step growing ~15 → ~24-25 px/frame; frames 12-24
curve from rightward to upward; frames 22-30 nearly pure -y, step ~20 → ~9 px/frame; frames 31-38 slow
(5-10 px/frame, partly jitter); frames 39-46 essentially stationary (<4 px/frame ≈ noise).
Start (0): (1520.4, 855.9); end (46): (1861.9, 479.9) image / (1861.5, 525.4) background-compensated.
Bowl is already moving at frame 0 (the lift happened before the clip).

## Events (frame, t)
- 0 (0.000 s): bowl already moving right, held by curly-haired man.
- 12-24 (0.62-1.24 s): direction change right → up.
- ~28 (1.45 s, ±3 frames): bald man's hand arrives under/at the right side of the bowl (hand-over contact).
- ~37 (1.92 s, ±3): pink-blazer diner's fingers reach the top-left rim / tomatoes.
- ~39 (2.02 s, ±3): bowl effectively stops; held above the bald man's tagliatelle plate until the end (46, 2.384 s).

## Static objects
Plates (frame 0, `plates_f0.json`, ±3 px): 224-256 px diameter (see scene.json). Other items (cutting board
~485 px long, sesame baguette ~332 x 56 px, wooden salad bowl ~170 px, olive bowl ~89 px, avocado tray ~143 x 283,
jug, flowers, spinach bowl, wine glass, table ~1630 x 873 px edges) are by eye on a gridded frame, ±10-20 px.
Static items shift with the camera drift (up to ~44 px up by frame 46); positions given are frame 0.

## Ambiguities
- Two "tomato" things: the tomato bowl vs single loose cherry tomatoes on the seafood and green-pasta plates.
- Several similar white plates (distinguished by food + nearby diner, see names); two tagliatelle plates
  (top-left red-haired man; right bald man); two green-pasta plates (top-right pink diner; right curly man).
- Hands of three people touch the bowl late in the clip; the passer (curly-haired man) holds it throughout.
- Tomato red-pixel count drops in later frames because the bowl is in shadow, not because tomatoes are removed.
- Moderate motion blur during the fast phase (frames 5-20) – rim still well defined.

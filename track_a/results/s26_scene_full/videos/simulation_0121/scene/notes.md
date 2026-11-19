# simulation_0121 – measurement record (pixels, seconds)

**Scene:** 2D Blender render, front view of a Newton's cradle. 80 frames at 30.007503 fps (t = frame / fps). The camera is static (background shift ≤ 0.035 px).
Five identical chrome balls (diameter **163 ± 1 px**, radius 81.5) hang from V-shaped string pairs on two top rods, inside a dark stadium-shaped metal loop on a dark wooden base.
- **Ball1** (leftmost) is held out to the upper left at frame 0 and released. It swings down an arc (pivot ≈ (640.6, 240.4), arm 543.2 px) and hits the row between frames 27 and 28.
- **Ball5** (rightmost) then swings out to the right (pivot ≈ (1312.6, 251.7), arm 539.9 px). It reaches its highest point at frame 54, at (1658.5, 666.2), 125.7 px above its rest height, and is swinging back at the last frame.
- **Balls 2–4** stay almost still. After the impact they drift by a few px (ball2 up to −9 px, ball3 up to −5, ball4 up to +17) and then return. Ball1 also drifts left after the impact (637.5 → 622.7 → 637), then comes back.

## Files
- `scene.json`: inventory, static object extents, rest positions, pendulum pivots and arm lengths, events, the glitch frame and camera notes.
- `tracks/ballK.csv` (K = 1..5, numbered left to right; balls never pass each other), one row per frame. Columns:
  - `cx_px, cy_px`: ball centre, which is the object origin. Image y points down.
  - `radius_px, diameter_px`: the fixed radius used in the fit.
  - `bbox_*`: the circle's bounding box. `length/width/height_px` all equal the diameter (sphere).
  - `occluded, occluded_frac`: the share of the ball disk covered by the static dark loop in front of it.
  - `gap_to_left_px / gap_to_right_px`: surface gap to the neighbour ball (centre distance minus both radii).
  - `free_radius_px, free_cx/cy`: the fit with radius left free (diagnostic only).
  - `visible = 0` at frame 1 (see below).
- `scripts/`:
  - `track_balls.py`: pass 1, Hough circles.
  - `refine_fixed_r.py`: pass 2, edge fit; also writes the ring mask.
  - `track_diffrim.py`: final pass. Run it once with free radius, then again with `fixr`.
  - `write_tracks.py`: writes the CSVs and the arc fits.
  - `static_measure.py`: static extents and the camera check.
  - `overlay.py`: overlay check images.
  - `hough_test.py`, `diff_test.py`: diagnostics.

## Method and reliability
- **Final centres:** I subtracted a background image and then fitted the ball rim.
  - Frame 1 contains no balls, so it serves as an exact background. D = |frame − frame 1|.
  - For each ball, a fixed-radius circle is fitted by maximising the drop in D across the rim, to sub-pixel precision.
  - Rim samples that fall on the static loop, or inside a neighbouring ball, are ignored.
- **Accuracy checks:**
  - Overlays drawn on frames 0, 3, 7, 14–17, 24, 27, 28, 46, 48, 57, 64, 65 and 79 sit on the ball outlines.
  - Ball1 and ball5 paths fit circular pendulum arcs with an RMS residual of 0.13 and 0.28 px.
  - Per-frame steps are smooth.
  - Estimated centre accuracy: about 0.2–0.5 px for most frames, and up to about 1 px for ball1 in frames 2–19 (the loop crosses in front of it) and for ball5 in frames 41–50 and 64–66 (it passes the loop, with motion blur).
- **Peak speeds:** about 22 px/frame for ball1 just before impact and for ball5 just after it. Motion blur is mild and symmetric, so the centres are not biased.
- **Ball size:** use 163 px diameter for all balls. Ball5's fitted radius of 82.65 is slightly inflated by blur and the loop overlap.
- **Glitch frame 1:** frame 1 is a render glitch with no balls in place. There is no measurement for it. Interpolate between frames 0 and 2 if needed; ball1 moves only about 0.6 px between them, and balls 2–5 are at rest.
- **Impact timing:** the impact falls between frames 27 and 28 (t ≈ 0.90–0.93 s). Frame 27→28 is a partial step for both ball1 (16.5 px) and ball5 (4.3 px).
- **Spacing:** hanging balls are 168.4 px apart centre to centre, leaving about 5 px of visible surface gap. Ball1 bottoms out at y = 783, while the others hang at y ≈ 791; ball1's pivot is about 11 px higher.
- **Static extents** (from frame 1's dark mask, ±2 px):
  - Loop: outer x 303–1549 (1246 px wide), top y 206, bottom about 950.
  - Front rod: x 592–1400. Back rod: x 606–1301.
  - Base plate: front edge x 428–1524 (1096 px), back edge x 499–1449, y 883–990.
  - String attachment points are approximate (read by eye).

## Ambiguities
- The balls look alike; they are identified only by their left-to-right order.
- Floor reflections of the balls appear below the base and are not objects.
- The stray half-ball in frame 1 is a glitch artefact.
- No metric scale is assumed: the answering session must take it from its prior, for example the ball diameter of 163 px or a pendulum arm length.

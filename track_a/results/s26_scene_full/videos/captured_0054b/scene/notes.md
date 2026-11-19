# captured_0054b – measurement record (pixels, seconds)

Lab video (real recording, 24 fps, 49 frames, 1280x720, t = frame/24). It has been restyled with the SAM2 demo: the
background and people are colour-tinted (purple floor, pale-green people and objects), and only the four balls keep
natural colours. Camera is **static**. Phase correlation against frame 0 gives a shift under 0.06 px in every frame.
Benchmark intrinsics for this camera: f = 762.8 px, principal point about (640, 360).

## Files
- `scene.json`: inventory, static object positions and extents, perspective lines, events, apparent-size summary,
  and camera notes.
- `tracks/<ball>.csv`: final per-frame tracks for basketball, soccer_ball, yellow_ball and white_ball. Columns:
  - `x, y`: reference point, the visible ball centre. This is the hull centroid of the mask, or a circle fit
    (`ref=circle_fit`) when the ball is occluded or clipped.
  - bbox, `len_major` / `wid_minor` (mask extent along and across its main axis), `major_angle_deg`, `area`.
  - `diam_est`: the across-axis width, which is the ball diameter even when there is motion blur. When occluded it
    is 2 × the circle-fit radius.
  - Flags: `occluded`, `blur`, and `note`.
- `tracks/*_raw.csv`: raw tracker output (mask centroid and circle fit side by side) for every detected frame.
- `scripts/`: the scripts.
  - `track.py`: the tracker. Colour rule × difference from a median background, inside a predicted search window.
  - `finalize.py`: builds the final CSVs, sets flags and draws the check montages.
  - `static.py`: static features; its output is in `static_out.json`.
  - `timing.py`: timestamps and step sizes.
  - `soccer_rest.py`: attempt to fit the held soccer ball.
  - `montage.py`, `probe.py`, `colorscan.py`: viewers and probes.
  - `bg.png`: the median background.

## Objects
- **basketball**: orange Wilson ball, the largest. Frames 0–4 it is at rest, held under the crouching person's hand
  at about (876, 666), with its bottom clipped by the image edge. It is pushed from frame 5, and the hand or arm
  crosses it until about frame 10. It then rolls up-left, away from the camera, getting smaller. It reaches the back
  wall/baseboard at frame 39 at (400, 265) and rebounds slowly down-right to (435, 293) at frame 48.
  - Apparent diameter: about 93 px at rest (circle fit), 75 at frame 13, 62 at frame 24, 54–55 from frame 36.
  - Track is very reliable from frame 10 on (sharp, round mask, ±1 px). Frames 0–9 are less reliable (±3–5 px):
    hand, arm or image edge in the way.
- **soccer_ball**: white with black pentagons. Frames 0–23 it is held still, right of the basketball.
  - In those frames its **right half is hidden behind the crouching person's body/hand**. Tracked x/y there are
    biased left and up, and the size is too small; frames 13–14 are not detected at all.
  - Best rest estimate (visual, from the free left and top outline): centre about **(918, 612)**, diameter about
    **56 px** (±4).
  - It is released and starts rolling at frame 24. It rolls up and slightly left (away), still moving at frame 48
    at (835, 372). Diameter: about 60 px at frames 26–27 (includes some vertical blur), 48 at 40, 45 at 45.
  - Frames 46–48: segmentation dropout. The ball is drawn as a flat grey disc. Silhouette and position are still
    valid (diameter about 39); the tracker uses a grey, low-texture rule there.
  - The mask sometimes drops the dark lower edge (frames 40, 42, 44), so y may be about 2–4 px too high there.
    Use `bbox_w` / `diam_est` for size.
- **yellow_ball**: small yellow ball, thrown from the left edge together with the white ball by an arm that comes in
  from the left.
  - Enters at frame 17 at the left border (partial) and arcs up-right. It is highest in the image around frame
    27 (y ≈ 239).
  - **Floor bounce at frame 37** at (696, 492), the lowest image point. It then moves up-right (away) and has nearly
    stopped at (832, 300) by frame 48.
  - Heavy motion blur up to about frame 35: the streak is elongated, so use `wid_minor` for diameter. Diameter is
    about 45 px at frame 20, 29 at 30, 21 at 37, 18 at 48.
- **white_ball**: small off-white/light-grey ball with a darker patch, about the same size as the yellow one. It
  travels just ahead of and above the yellow ball.
  - First visible at frame 20 beside the thrower's hand. It is highest in the image at frames 27–28 (y ≈ 195).
  - **Floor bounce at frame 38** at (680, 467). It then moves up-right to (791, 261) at frame 47, partly hidden
    behind the green object on the floor. At frame 48 it is hidden.
  - Faint and blurred, so the mask is less reliable (±3 px). Frames 27–29 miss its dark patch, so the centroid is
    slightly offset. Diameter is about 41 px at frame 24 (blurred), 23 at 32, 17 at 38, 18 at 45.
- **Not tracked (people)**:
  - The crouching person at bottom right (about x 910–1140, y 520–720). Only their arm/hand moves; they push the
    basketball and release the soccer ball.
  - The thrower's arm at the left edge (about frames 17–30).
  - The seated person at the desk, top right (static).
- **Static objects**: waste bin (cyan recycling bin) bbox (682, 135)–(738, 200), 56 × 65 px; tripod or light stand
  next to it; two lime floor tape strips; cabinet doors and two wall outlets on the back-left wall; green and blue
  items and cables on the floor by the desk. Positions and extents are in scene.json.

## Perspective
- Floor/back-wall baseboard (bottom edge): y = −0.3024·x + 388.8. The band is 25 px thick at x = 0 and 11.5 px at
  x = 600: the far end is to the right.
- Tape strips:
  - (315, 619)–(407, 721), 138 × 11 px. It is cut off by the bottom edge, so the length is a lower bound.
  - (610, 425)–(681, 475), 88 × 7.5 px.
- The camera looks down onto the floor from above. Balls higher in the image are farther away; apparent sizes in
  the tracks show the depth change.

## Timing caveats
- Container timestamps are perfectly uniform. However, **every moving object jumps about 2× its normal step between
  frames 35→36**, and the basketball also does **between 11→12**. One camera capture was evidently skipped at each
  of those points.
- Indices were kept as frame/24, following the benchmark convention, but speed differences across those pairs are
  doubled.

## Events (frame, t in s)
| Frame | t (s) | Event |
|---|---|---|
| 5 | 0.208 | Basketball starts moving |
| ~10 | 0.417 | Basketball free of the hand |
| 17 | 0.708 | Yellow ball enters |
| 20 | 0.833 | White ball first seen |
| 24 | 1.000 | Soccer ball starts rolling |
| 37 | 1.542 | Yellow ball bounces |
| 38 | 1.583 | White ball bounces |
| 39 | 1.625 | Basketball hits the wall and reverses |
| 46 | 1.917 | Soccer ball shown as a grey disc |
| 48 | 2.000 | White ball hidden |

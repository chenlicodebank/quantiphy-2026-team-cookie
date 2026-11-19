# captured_0008s — measurement record (pixels / seconds only)

**Scene.** This is a lab capture: 24 fps, 49 frames (t = 0 … 2.000 s), 1280×720, 3D. Segment Anything 2 replaced the background with a uniform green gradient (watermark in the bottom-right corner). A person's hand holds an orange basketball (Wilson logo, black seams) near the top of the image. The hand releases it, and the ball falls onto a square light-wood board (table top) on a grey pole in the lower centre of the image. The ball bounces twice and is falling again when the clip ends. The camera looks obliquely down at the board. As the ball falls it moves **away** from the camera: its apparent diameter shrinks from ~129 px when held to ~105 px at the board.

## Files
- `scene.json`: inventory (ball, hand, table_board, pole, ball_shadow), static-object pixel geometry, events, camera info.
- `tracks/ball.csv`: one row per frame (0–48):
  - `x,y` is the reference point, the centre of a circle fitted to the ball silhouette (= the visible centre).
  - `diam_px` is the fitted circle diameter; `diam_px_med5` is its 5-frame running median.
  - `mask_cx,mask_cy` is the silhouette centroid.
  - `bbox_*` is the silhouette bounding box; `mask_len_major/mask_wid_minor` are the PCA extents of the silhouette; `height_px` is the bbox height.
  - `occluded` (with `occluder=hand`) is set for frames 0–23; `motion_blur` is a flag; `circle_inlier_frac` is the fraction of contour points on the circle (higher = cleaner).
- `tracks/ball_raw.csv`: the raw tracker output.
- `scripts/`:
  - `track_ball.py` (tracker plus overlays)
  - `static_table.py` (board/pole geometry and camera-stability check)
  - `finalize.py` (writes ball.csv and scene.json)
  - `rawstrip.py`, `montage.py`, `probe_hsv.py` (viewing and colour probes)

## Method
- **Ball mask:**
  - Outside the board region: everything not green.
  - Inside the static board/pole mask taken from frame 0: orange pixels only (H≤14, S≥95).
  - Then I took the largest blob, filled its holes and fitted a RANSAC circle to its outer contour (2 px tolerance), which rejects finger cut-outs, motion-blur ghosts and shadow bits.
- **Checking:** I drew the overlays and inspected 24 of the 49 frames; the circle sits on the ball in every one.
- **Static objects:** board corners were read off a 2× zoom of frame 0 (±3 px).

## Camera
- **Static.** The board bounding box is identical within 1–2 px in frames 0, 10, 20, 24, 36 and 48. There is no real background to check against because it was replaced, but the board is a rigid static reference.
- **Intrinsics (task convention):** f = 0.5959·1280 ≈ 763 px, principal point ≈ (640, 360).
- **Depth from size:** for a ball of real diameter D, depth ≈ f·D/diam_px. Use `diam_px_med5` for stability.
- **Perspective:** the board's front edge is 328 px long and its back edge 207 px, so the near (front) side faces the camera and the board top recedes upward in the image.

## Ball track summary (x, y = circle centre, px)
- **Held, frames 0–21:** (522, 93–97), diameter 128–134 px (~129 median).
  - Frames 0–3: the hand is visible on the right of the ball and is part of the mask, but the circle fit ignores it.
  - Frames 4–23: the segmentation cut the fingers out, leaving green notches in the ball's right side.
- **Release:** frame 21 (t = 0.875 s). y is 94.9 at frame 21, 106.3 at frame 22 and 124.5 at frame 23. Frames 20/21 are the last ones at rest.
- **Fall, frames 22–30:** y rises to 413 px and x drifts 520 → 577 px. The diameter shrinks 132 → ~105 px.
- **First impact, frame 30 (t = 1.250 s):** y = 413.0, the lowest point. Contact happens around frame 30; frame 29 is already at y = 409.8.
- **Apex 1, frame 36 (t = 1.500 s):** (547.7, 303.7), diameter 114.3 px.
- **Second impact, between frames 41 and 42 (t ≈ 1.73 s):** y ≈ 410 in both frames.
- **Apex 2, frame 46 (t = 1.917 s):** (549.7, 371.9), diameter 108.7 px.
- **End:** frames 47–48 are falling again (y = 387 at frame 48).

## Reliability and ambiguities
- **Clean frames** (inlier fraction > 0.6): centre accurate to ~±1 px, diameter to ~±2 px.
- **Motion-blurred frames 24–30 and 39–42:** the blur shows as a semi-transparent ghost trailing above the ball, with ragged mask edges. The circle centre is uncertain by ~±3–5 px (worst at frames 26–29) and the diameter by ±5 px. `mask_cx/cy` and the bbox include the ghost, so use x,y.
  - At frames 26–27 the fall increments look small and at frame 28 large (y steps +36, +43, +74, +65). That pattern is blur/segmentation noise; smooth over several frames.
- **Diameter in the held phase:** the hand cut-out notch leaves the fit still good, but the frame-0 fit gives 133.9 because the visible hand is attached to the mask.
- **Shadow:** the ball's dark shadow on the board appears near the bounces. It is excluded from the mask (hue 16–18) except for small tails at frames 30, 41 and 42, which only affect the bbox bottom.
- **Image motion vs. world motion:** the ball's image motion mixes vertical fall and motion away from the camera, so pixel y is not the world height. Use the diameter or the given depths for the depth component.
- **Measurement gaps:** the hand is not tracked. The pole is cut off by the bottom of the image (visible length ~145 px, width ~20–25 px).

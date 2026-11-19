# captured_0014s — measurement record (pixels, seconds)

Lab video (real recording, background replaced by green via segmentation; watermark bottom-right), 3D scene,
1280x720, 24 fps, 49 frames (t = frame/24, 0–2.0 s). Camera static (table region shift vs frame 48 < 0.15 px every
frame). Benchmark intrinsics for this camera: fx = fy ≈ 763 px, principal point ≈ (640, 360).

## Scene
An elevated camera looks obliquely down at a small square wooden table with one grey central leg. On the table: a
white rectangular board (centre-back), a white/silver tumbler cup (back-left), a chocolate-chip cookie (in front of
the cup), a black pen (front-left) and a light-blue notebook (right). **The only moving object is one pale
beige/grey ball.** It rests at the far (top) edge of the white board in frames 0–7. From about frame 8 it rolls
down over the board toward the camera, crosses the board's front edge onto the wood in frames 17–19, rolls across the
table in frames 19–23, and goes over the table's front edge at frames 23–24. It then falls in front of the table and
leg, and leaves the bottom of the image at frame 30 (a sliver is still visible at frame 29). No bounce is seen.

## Files
- `scene.json` — inventory (descriptions, corners, bboxes, pixel extents of static objects), camera, events, caveats.
- `tracks/ball.csv` — one row per frame (0–48). Columns: `ref_x, ref_y` = centroid of the ball mask (the visible
  centre: use this as the reference point); `bbox_cx, bbox_cy`; bbox `x0 y0 x1 y1`; `len_major_px / wid_minor_px`
  (min-area rectangle); `height_px` (bbox height); `area_px`; `equiv_diam_px`; `occlusion`; `phase`; `reliability`.
  Rows 30–48 have `visible = 0` (out of frame).
- `scripts/` — `track_ball.py` (median-background difference + shadow removal; writes the raw csv and overlay
  crops), then `finalize.py` (adds the flag columns and writes scene.json; run it only after `track_ball.py`). Also:
  `static_objects.py` (colour segmentation of board, notebook, table top and leg at frame 48), `camera_check.py`,
  `profile.py`, `probe.py`, `crops.py`, `ovsheet.py`, `draw_track.py` (visual checks). Scratch PNGs are in `../frames/`.

## How it was measured, and how reliable it is
- Ball mask: |frame − per-pixel median background| > 30, cleaned with morphology, largest blob. Pixels that are
  saturated and darker than the background (the ball's shadow / shaded underside on the wood) are removed. Masks
  were overlaid on the frames and checked by eye.
  - Frames 0–16 (on the green background and on the white board): good, ±1 px. The apparent diameter is 27–29 px
    (about 28 px) for y ≈ 296–390.
  - Frames 17–19 (crossing the board's front edge, y ≈ 409–418): poor, ±6 px in y. There is low contrast and a
    shadow, and the mask is irregular (frame 19 is only 16 px tall).
  - Frames 20–22: fair, ±3 px. The bright upper body of the ball is tracked; a dark blob directly below it (the
    shadow, or the ball's shaded lower half) is excluded. If it were part of the ball, the true centre would be
    about 5 px lower.
  - Frames 23–28 (falling): strong vertical motion blur. Box heights are 41–69 px against a 28 px ball. The centre
    is the centre of the blur streak (≈ mid-exposure position), ±3 px. Width grows to 36–41 px (blur, plus the ball
    being somewhat closer to the camera).
  - Frame 29: only the top sliver at the image edge, so the centre there is biased upward.
- Image-plane path: x stays near 543–551 the whole time; the ball moves almost straight down the image (toward the
  camera, then downward in the fall). Per-frame steps in y:
  - At rest, frames 0–7: 0.
  - Start of motion, frames 8–11: 1–5.
  - On the board, frames 12–16: 11–19.
  - Frames 17–19: an anomaly (20, 6, 2).
  - On the table, frames 20–23: 11, 18, 10, 20.
  - Falling, frames 24–28: 22, 31, 39, 48, 52.
- Timing jitter: there are irregular steps at frame 11→12 (21 px, between steps of about 5 and 11) and in frames
  17–23. These may come from uneven frame timing in the recording or from mask error, so smooth over ≥ 5 frames as the
  reference convention does.
- Depth: the ball's depth is not measurable from the image. Answering sessions should use the given depth_info with
  fx = 763 to back-project the centres.
- Static objects (frame 48, no ball): the board, table top, notebook and leg come from colour masks (±2 px). The cup,
  cookie and pen were read off a gridded zoom (±3 px). The table's back-left corner is hidden by the cup (approximate).
  - Board corners: (502,312) (593,304) (607,409) (510,422).
  - Table-top corners: (446,330)* (659,312) (727,454) (426,509).
  - At the ball's x (≈545) the table's front edge is at y ≈ 487.
  - Leg: from (596,492) to (600,612).
  - Lengths are image-pixel lengths, so they are foreshortened by perspective.

## Ambiguities
- The white board may be an inclined ramp; this cannot be confirmed from the image.
- There is only one ball, so it cannot be confused with another object. The white cup and the board are static.
- The event frames are ±1 frame:
  - Motion onset: frame 8 (t = 0.333 s).
  - Leaves the board: frames 17–19.
  - Leaves the table edge: frames 23–24 (t ≈ 0.96–1.00 s).
  - Leaves the image: frame 30 (t = 1.25 s).

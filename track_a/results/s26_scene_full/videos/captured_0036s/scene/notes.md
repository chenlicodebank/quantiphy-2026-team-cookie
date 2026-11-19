# captured_0036s — measurement record (pixels, seconds)

Lab video, 3D, 24 fps, 49 frames (t = frame/24, 0–2.000 s), 1280×720. A real recording whose background was
replaced by a synthetic snowy-sky image (Segment Anything 2 demo; watermark box bottom-right, x≈1028–1280,
y≈690–720). Camera is static: there is no pan or shake (background change between consecutive frames < 0.1 % of
pixels). Benchmark intrinsics: f ≈ 0.5959·1280 = 762.8 px, principal point ≈ (640, 360).

## Scene
- **ball**: the only moving object, a small white/cream ball. It sits near the back-left corner of the table top,
  then rolls diagonally toward the front-right corner, toward the camera and to the right. It rolls off the right
  edge and falls beside the table's front-right corner, then leaves the view behind the watermark.
- **table** (static): a wooden top seen as a trapezoid. Corners at frame 48: back-left (403,442), back-right
  (765,450), front-left (188,590), front-right (997,598). Back edge ≈362 px, front edge ≈809 px, left side ≈262 px,
  right side ≈275 px (image lengths, strongly foreshortened). Front band thickness ≈33–35 px. Wood bbox is
  x 188–997, y 440–625.
- **table_pedestal_leg** (static): a dark column x 533–590 (57 px wide), y 622 to the frame bottom (cut off).
- **watermark_box** (static): it hides the falling ball in frames 39–40.

## Files
- `scene.json`: inventory, camera, perspective cues, static extents, events.
- `tracks/ball.csv`: one row per frame (0–48). The columns are:
  - `cx, cy`: the reference point, which is the centroid of the ball mask (its visible centre).
  - `x0 y0 x1 y1`, `bbox_w`, `bbox_h`, `area_px`.
  - `len_along_main_axis` and `width_across_main_axis`: PCA extents of the mask.
  - `main_axis_deg`: image angle of the mask's main axis.
  - `occluded`.
  - `step_px`: centroid step from the previous frame.
  - `quality`.
- `tracks/ball_raw.csv`: the same raw output of `track_ball.py`, plus bbox centre, equivalent diameter and an edge flag.
- `scripts/track_ball.py`: builds the mask by differencing against the ball-free frame 48. It rejects wood-coloured
  pixels and shadow, keeps the largest blob, fills holes, then opens it with a kernel scaled to the blob size. It
  then adds the bright segmentation halo below the ball and takes the convex hull (GrabCut is implemented but turned
  off).
- `scripts/finalize.py` writes ball.csv. `scripts/static_and_timing.py` produces the table geometry and the
  camera-stillness check. `scripts/crops.py` makes magnified crops with the boxes drawn, for checking. `probe*.py`
  are pixel probes.

## Events (frame / t)
- **0–11 (0–0.458 s): ball at rest** near the back-left corner, centroid ≈(420,430). There is a slight creep of
  ≈5 px to the left between frames 4 and 10.
- **Motion starts at frame 12 (t = 0.500 s):** the step is 3.7 px, then 10 px at frame 13.
- **Rolling on the table, frames 12–35.** The image step is ≈14–20 px/frame for frames 14–28, rising to ≈25–32 px
  at frames 31–35. The increase is partly perspective, because the ball approaches the camera.
- **Frame 35 (t = 1.458 s):** the ball centre reaches the table's right edge (the right edge passes x≈871 at y=518).
- **Probable dropped frame between 35 and 36.** The centroid step is 76 px, against 31 px before and 42 px after.
  Treat 35→36 as roughly two frame intervals if a question depends on it.
- **Frames 36–40: off the table, falling** down beside the front-right part of the table. Vertical steps are
  ≈17, 35 and 60 px/frame for 36→37, 37→38 and 38→39.
- **Frame 39:** the bottom is hidden by the watermark. **Frame 40:** only a sliver is visible. **From frame 41
  (t = 1.708 s):** the ball is out of view.

## Apparent size, for relative depth (depth ∝ 1/diameter)
Use the extent perpendicular to the motion (`width_across_main_axis`, or `bbox_h` while the motion is near
horizontal) as the diameter:

| Frames | Diameter (px) | Note |
|---|---|---|
| 0–11 | ≈27–29 | at rest; the bbox includes the 1-px halo |
| 13–22 | ≈25–26 | likely 1–3 px too small, see Reliability |
| 24–28 | ≈37–40 | |
| 30–32 | ≈41–45 | |
| 33–35 | ≈46–48 | |
| 36–39 | ≈52–53 | blurred lengths 77–100+ px |

The ball grows about 2× in the image from the start to the edge, so it ends roughly twice as close to the camera.

## Reliability and ambiguities
- **Centroid accuracy:**
  - Frames 0–33: ≈±1–2 px. In frames 13–22 the grey shaded underside, which is the same colour as the wood, is
    partly lost, so `cy` there may be 1–2 px too high and `bbox_h` 1–3 px too small. A probe at frame 20 shows the
    ball's bottom at y≈462 against a mask bottom of 460.
  - Frames 33–35: the lower outline was rebuilt from the halo; ±2–3 px.
  - Frames 36–39: strong motion blur, so the centroid is the centre of the blur streak; ±3–5 px. Frame 39 is
    truncated by the watermark, so its `cy` is biased upward.
- **Background differences:** the dark contact shadow under the ball is excluded. The thin bright halo is part of
  the segmentation artefact and is included in the extents.
- **Single object:** there is only one ball and no other moving objects, people or props. No metric scale is
  assumed anywhere.

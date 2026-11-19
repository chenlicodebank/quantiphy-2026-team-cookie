# internet_0008 — measurement record (pixels, seconds)

Video: 960x540, 30 fps, 529 frames (t = frame/30, 0 … 17.60 s). Internet footage, 2D. Long-telephoto sunset/sunrise
over the sea: a sailboat crosses the frame left to right in front of a large sun. A small motorboat crosses the bottom of
the frame between frames 224 and 351.

## Files
- `scene.json`: inventory, summary sizes, events, camera. Every number is in pixels, frames or seconds.
- `tracks/sailboat.csv`: frames 0–528. Columns are bbox centre (`bbox_cx`, `bbox_cy`), mask centroid, bbox `x0 y0 x1 y1`,
  `length_px_horiz` (bow/bowsprit to stern, along the motion direction = x), `height_px` (mast top to hull bottom),
  `hull_x0/x1/hull_len_px` (horizontal extent of the bottom 13 rows of the mask, i.e. the hull only), `area_px` and
  `occluded` (1 = bbox inflated by a merge, see below).
- `tracks/motorboat.csv`: frames 224–351, with a gap at 313–315. Same bbox and centroid columns, plus `cut_by_frame_edge`
  (1 = the boat touches the left, right or bottom frame edge, so its extents are truncated).
- `tracks/sun.csv`: frames 0–528. `disc_cx` is the median chord midpoint of the lower disc. `disc_cy` = bottom limb − 80
  (assumes the round disc with D = 161 px). `y1_bottom_limb` is the clean lower edge. The widest-row columns are only
  reliable in frames 0–360. The top of the disc is hidden by a dark cloud band in early frames and merges with glow late
  in the clip.
- `tracks/camera.csv`: horizon row per frame, plus the frame-to-frame phase-correlation shift of the sea texture (sailboat
  masked out).
- `tracks/horizon.csv`: the horizon row from `camera.csv`, copied out on its own (row 437 in every frame).
- `scripts/`: `track.py` makes the sailboat track and a first pass of the others. `track2.py` makes the motorboat, sun and
  camera tracks and overwrites `track.py`'s versions. `flag_sailboat.py` then sets the occlusion flags. `write_scene.py`
  builds `scene.json`. `strip.py`, `probe.py` and `summ*.py` are viewing and summary helpers. If you re-run, use this order:
  track → track2 → flag_sailboat → write_scene.

## Method
- **Sailboat:** dark-silhouette mask (luminance < 60 and > 22 below a 61-px local mean), closed with a 5x5 kernel, keeping
  the largest component near the previous position. The pale centre of the main sail is sometimes missing from the mask,
  so the mask centroid is biased slightly. The bbox covers the full extent: mast top at y≈393, hull bottom/waterline at
  y≈516, bowsprit to stern. I checked this on overlays at frames 0, 70, 141, 211, 282, 317, 352, 422, 493 and 528.
  - **Recommended reference point:** the bbox centre.
  - **Sizes:** median bbox length 105 px (5–95 %: 103–108 px; it grows slightly, 103 px in the first second and 107 px in
    the last), hull length ≈ 101 px, height ≈ 123 px.
  - **Motion:** bbox_cx goes from 289.0 to 855.0 px (net +566 px), roughly steady at about 1.07 px/frame with ±1–2 px
    jitter. There is no vertical motion.
  - **Flagged frames:** 11, marked `occluded=1`. Frames 313–315 are where the motorboat merges into the mask; frames 314,
    423, 489, 492, 511–518 are where a dark wave patch inflates the length past 110 px. Use the median length, or the
    unflagged frames.
- **Motorboat:** dark blob in rows below 480, outside the sailboat bbox. A vertical opening removes the thin wake line,
  and the boat is followed by nearest-to-prediction tracking.
  - **Size:** fully visible size 36 px long × 17 px high (median, frames 262–312). In frames 236–260 and 323/335 the bbox
    is sometimes 40–60 px because wake or spray stays attached, so trust the 262–312 values for size.
  - **Motion:** about 7.6 px/frame to the right, drifting down from y≈520 to y≈532.
  - **Edges and gaps:** it touches the bottom frame edge from frame 316 on, so y1 = 539 and its heights there are
    truncated. It leaves the frame at the bottom-right around frame 352. The gap at 313–315 is where it passes directly
    below the sailboat hull and the masks merge.
  - **Depth:** it is clearly nearer the camera than the sailboat (lower in the image). Per the benchmark convention, a
    single scale is still applied, but note that the two boats are at different depths.
- **Sun:** orange/yellow pixel mask (R > 215, G > 100) above the horizon, gated to the previous box.
  - **Size:** diameter 161 px (horizontal chord, frames 0–280).
  - **Motion:** the centre drifts from (492, 135) to (546.5, 108). That is +0.10 px/frame in x and the sun rising
    0.05 px/frame. It is reliable to about ±1–2 px.
- **Camera:** the horizon is detected at row 437 in all 529 frames, so there is no tilt, shake or vertical pan. Horizontal
  pan cannot be checked against a fixed landmark (there are only sea, sky and sun). The sea texture drifts about
  −0.2 px/frame (waves) and the sun +0.1 px/frame, in opposite directions and both small, so the camera is treated as
  static (tripod). Measure boat motion directly in image pixels.

## Static and other items
- **Horizon:** a straight, level line at y = 437 across the full width.
- **Sea:** wave bands below the horizon; the texture moves.
- **Sky:** a dark cloud band crosses the sun.
- **Birds:** 2–4 px specks, e.g. near (315, 347) at frame 0 and near (875, 290) at frame 176. Not tracked; too small to
  measure.
- **Perspective:** this is a 2D scene, nearly side-on. Both boats move almost parallel to the image x-axis. The sailboat is
  at the horizon, the motorboat much nearer.

## Events
- Frames 0–528: sailboat moving steadily rightward throughout. No start/stop is visible.
- Motorboat:
  - frame 224 (7.47 s): enters at the left edge
  - frame 232 (7.73 s): fully visible
  - frame ~316 (10.53 s): passes in front of/below the sailboat and starts touching the bottom edge
  - frames ~345–352 (11.5–11.73 s): leaves the frame at the bottom-right

## Reliability
- **Sailboat:** bbox positions ±1–2 px; length ±2 px.
- **Motorboat:** positions ±2 px; length ±3 px (wake contamination is possible).
- **Sun:** centre ±2 px.
- **Ambiguity:** "boat" most likely means the sailboat; the motorboat is the only other vessel.

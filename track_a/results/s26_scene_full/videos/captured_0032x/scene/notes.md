# captured_0032x — measurement notes

Lab video (real recording, background replaced by black via Segment Anything 2; watermark text bottom-right),
3D scene, 24 fps, 49 frames (t = frame/24, 0 … 2.0 s), 1280x720. Benchmark camera: f = 763 px, principal point ≈ (640,360).
All values are in pixels and seconds. No metric scale is assumed.

## Scene
A brown wooden table top on a single dark-grey pedestal pole, seen from the front and slightly above. Two balls on it:
- **yellow_ball**: the larger, yellow, tennis-ball-like ball (its outline is a little irregular). It starts at rest on the far/right part of the table, at (776,414), apparent diameter ≈ 32–33 px.
  From frame 22 it rolls left and toward the camera. It passes in front of and strikes the white ball around frame 30, rolls off the left edge of the table between frames 42 and 43,
  then falls (heavily motion-blurred) and leaves the image through the bottom by frame 48.
- **white_ball**: the smaller white ball (ping-pong-like), at rest at the far edge of the table at (648,416.5), diameter ≈ 20–21 px, frames 0–29.
  After the impact it rolls right and toward the camera until the end of the clip (diameter grows to ≈ 32 px at frame 48).
- Static: table_top, table_pole (see scene.json for corners and extents). No people, no hand visible (whatever launched the yellow ball was segmented away or is out of view).

## Files
- `scene.json`: inventory, static extents, events, camera info.
- `tracks/yellow_ball.csv`, `tracks/white_ball.csv`: one row per frame (0–48). Columns:
  `visible, occluded, out_of_frame`; `cx,cy` = mask centroid; `ccx,ccy` = circle-model centre (x = bbox mid, y = bbox top + diam/2,
  **recommended reference point while a ball is on the table**, because the colour mask misses the shaded lower rim, which pulls the centroid upward);
  for the falling yellow ball (frames 43–47) ccx,ccy = centroid of the full blurred blob; `x0,y0,x1,y1,bw,bh` = mask bbox;
  `len_major,width_minor` = extent along/across the principal axis; `diam_px` = best apparent diameter (bw on the table; width across the blur streak when falling);
  `area, eq_diam`.
- `tracks/*_raw.csv`: the unprocessed mask statistics from track.py.
- `camera_check.csv`: per-frame mean abs difference from the previous frame and background shift (phase correlation on table front + pole).
- `scripts/track.py` (segmentation + tracking + overlays), `scripts/finalize.py` (final CSVs, camera check), `scripts/static.py` (table/pole extents), `scripts/probe*.py` (pixel-value probes).

## Method
Colour masks in HSV (yellow: H 21–39, S>115; white: S<50, V>70 and different from a clean background plate made from frame 0 with the
ball spots filled from frame 48), the largest blob kept, gated to a window around the predicted position. The white mask excludes the dilated yellow mask.
For the falling yellow ball (≥ 43), the whole non-black blob that is not part of the static scene is used, so the blur halo is included.
Overlays were checked visually (frames 0, 29–32, 44–47): the masks sit on the correct balls.

## Reliability
- Rest positions: ±0.5 px. Rolling centres (ccx,ccy): about ±1–2 px. Diameters on the table: ±1–2 px (the yellow ball is slightly non-round).
- Motion blur inflates bw along the motion (the yellow ball at frames 22–23 and 27, the white ball at 33–34). The falling yellow ball (43–47) is a streak:
  len_major ≈ blur length + diameter, while width_minor (≈ 50–56 px) is the across-blur diameter. Frame 47 is cut by the bottom image edge (out_of_frame=1), so its centroid is biased upward.
- White ball 30–32: hidden behind the yellow ball (occluded=1). Frame 31 is not detected, and frame 32 is only a sliver (ccx/diam not usable). Interpolate between 30 and 33.
- **Probable dropped frame between 35 and 36**: both balls jump about twice their normal per-frame step (yellow 14.7 → 31 → 16.5 px; white ≈ 9 → 14 → 5 px),
  and the frame difference peaks at 36. Treat 35→36 as roughly two frame intervals if a question's timing is sensitive to it, but reference answers use the nominal frame times.
- Static frames 0–21 show tiny jitter (≤ 0.5 px) and some exactly duplicated frames (compression). This is not motion.
- Camera is static: the background shift is < 1 px in every frame.

## 3D / perspective cues
- Both balls move toward the camera while rolling: their image y increases and their apparent diameter grows (yellow 32 → 50 px by frame 42; white 20.5 → 32 px by frame 48).
  Apparent diameter ∝ 1/depth, so diam_px together with f = 763 px and a known ball size or depth gives the depth per frame (Z ≈ f·D/diam_px).
- Table top in the image: back edge (568,427)–(850,428), 282 px; front-top edge (463,484)–(964,496), 501 px; front face ≈ 22 px thick, bottom at y ≈ 506–517.
  The table's side edges converge near (715,347), so the camera is about level and slightly above the table, looking very slightly down. The front edge dips ~12 px from left to right (a slight roll).
- Pole: x 710–747 (37 px wide), from y ≈ 518 to the image bottom (cut off).

## Events (frame / t)
- 0–21: both balls at rest.
- 22 (0.917 s): the yellow ball starts moving left.
- 29 (1.208 s): last frame before contact (gap ≈ 20 px).
- 30 (1.25 s): impact. The yellow ball (nearer the camera) strikes the white ball, which starts to move right and toward the camera.
- 33 (1.375 s): the white ball reappears to the right of the yellow ball.
- 42 (1.75 s): the yellow ball at the table's left edge. It leaves the table between 42 and 43 and is in free fall from 43.
- 47 (1.958 s): the yellow ball reaches the bottom image border. At 48 (2.0 s) it is out of view while the white ball is still rolling.

## Ambiguities
- Which ball a question calls "the ball": yellow is the larger and the mover/striker; white is the small struck ball.
- Glossy table reflections of the yellow ball (a yellowish streak below it) and a reflection of the white ball were deliberately excluded from the masks.
- Dark segmentation fringe (~1–2 px) around both balls, so mask extents may be 1–2 px small.

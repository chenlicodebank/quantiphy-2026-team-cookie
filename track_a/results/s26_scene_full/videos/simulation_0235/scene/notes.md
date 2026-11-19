# simulation_0235 — measurement record

2D Blender render, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 to 2.0417 s). Pixel coordinates: x to the right, y DOWN.

## Scene
A fronto-parallel view of a gym wall: two rows of black window panes at the top, a grey concrete pillar
(x ~835–1000), a teal lower wall, and an orange wooden court floor below y ≈ 905. A light boundary line
runs along the wall foot at y 917–921, and a light-grey court stripe runs toward the camera below the ball.
**One moving object:** a pink/red basketball with black seams. **Static prop:** a gold basketball-player trophy
(figure holding a ball overhead, plus a cup) on a grey pedestal column with a square base, at x ≈ 1136–1226.
There are no people, animals or vehicles. The figure on the trophy is a statue and does not move.

## Files
- `scene.json`: inventory, static extents, events and camera.
- `tracks/ball.csv`: per frame (0–49, always visible, never occluded). Columns:
  - `ref_x, ref_y`: least-squares circle-fit centre, the origin.
  - `bbox_cx, bbox_cy`: bbox centre.
  - `bbox_x0..y1`
  - `length_px` (horizontal extent) and `width_px` = `height_px` (vertical extent).
  - `fit_diam_px`
- `tracks/ball_raw.csv`: the same data with the raw names, including mask area.
- `tracks/camera_shift.csv`: phase correlation of the window band against frame 0.
- `scripts/`:
  - `track_ball.py`: HSV mask (hue ≥150 or ≤6, S ≥70), merges blobs split by the seams, takes the convex hull, and fits a circle to the upper 75 % of the contour.
  - `check_static.py`: camera check, trophy/floor profiles and overlays (`frames/ov_*.png`).
  - `finalize.py`: writes `ball.csv` and `scene.json`.

## Ball (reliable to within ±0.5 px)
- **Diameter:** about 106 px from the circle fit (median 106.1, range 105.2–107.1); the bbox is 108 x 108. Use ~106–108 px as the ball's pixel size.
- **Horizontal position:** x stays at 907.0–907.8 the whole time, so the motion is purely vertical.
- **Fall:** ref_y goes from 488.1 (frame 0) to 865.6 at frame 24, the lowest sample. There the bbox bottom is at y = 920, which is the floor line.
- **Fall rate:** per-frame drops are 0.9, 2.0, 3.5, 5.0, … up to 30.3 px (frames 22→23). That is a near-constant increase of about 1.3–1.4 px/frame².
- **Release:** the ball starts from rest at frame 0.
- **Bounce:** contact happens in the interval 23→24. The drop over that interval is only 22.3 px against the ~31.5 px expected, so the ball reached the floor during it and is sitting at the floor at frame 24. Frame 24 is the direction change.
- **Rise:** after the bounce it climbs 20.6, 29.8, 27.0, … then 1.7 and 0.5 px. At frame 49 it is at y 488.5, almost back at the start height, with the apex at or just after the last frame. The bounce is almost elastic.
- **Shape:** no squash is visible.
- **Overlays:** they confirm that the circle and bbox cover the whole ball.

## Static
- **Trophy** (±3 px, read by hand from a 2x zoom; centre x ≈ 1181):
  - Total height 429 px, from y 506 (the ball on the figure's hand) to y 935 (bottom of the base).
  - Gold part (figure + cup): y 506–762, 256 px. Figure: y 506–668, 162 px tall, about 40 px wide. Cup: y 668–762, about 40 px wide.
  - Pedestal cap: x 1150–1201, y 761–786. Column: 32 px wide, y 786–905. Base: 90 px wide, y 905–935.
- **Window pane:** about 208 x 150 px, for example x 1010–1218, y 50–200.

## Camera
Static. The background shifts by at most 0.04 px. There is no perspective to speak of: the ball and the trophy
stand at about the same depth in front of the wall, so one m/px scale applies.

## Ambiguities
- The ball's reflection on the glossy floor (below y 920) and a faint shadow on the wall are not part of the ball. The tracking ignores them (the mask is limited to the ball blob, and the circle fit leaves out the bottom of the contour).
- The trophy figure is also holding a small ball; it is not "the ball".

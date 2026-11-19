# internet_0010 — measurement record

Video: 3840x2160, 97 frames, 29.662162 fps (t = frame / fps, frame 0 at t = 0). Source: internet, labelled 2D.
Content: an outdoor basketball court at Venice Beach. A man in a grey tank top (`shooter_grey_tank`) dribbles once,
gathers, and takes a jump shot. The ball goes through the hoop (made basket, f82–85) and drops through the net.
Seven other players walk around the court. A handheld camera pans right to follow the ball.

All coordinates are full-resolution image pixels, with x to the right and y DOWN.

## Files
- `scene.json`: inventory (every object, with description, distinguishing features, whether it moves, frames visible), static-object pixel extents, the best ball diameter, events, camera summary.
- `camera.csv`: per-frame camera motion relative to frame 0.
  - `h00..h22` is the homography that maps frame-i pixels to frame-0 pixels.
  - `dx,dy` (= `dx_c,dy_c`) is the background shift at the image centre.
  - `dx_L700` and `dx_R3140` are the shifts near the left and right sides.
  - `inliers_to_f0` is the number of feature matches.
- `tracks/ball.csv`: the ball in every frame. Columns:
  - `x,y`: image position.
  - `x_bg,y_bg`: the same point mapped to frame-0 background coordinates (camera motion removed).
  - colour-mask bbox `bx0..by1`, `mask_w/h`, `diam_eq` (lit orange core only; see the caveat below).
  - `occluded` flag, `status` (`auto` / `manual` / `not_visible`), `phase`.
- `tracks/ball_auto.csv`: raw tracker output, before the phase and occlusion flags were added.
- `tracks/ball_diameter.csv`: diameter of the full ball outline per frame. Columns: a sky-contrast mask, used where the background is clear sky (`sky_*`), and a Hough circle fit (`hough_diam`, noisy).
- `tracks/<person>.csv`: one file per tracked person. Columns:
  - `x,y` and `x_bg,y_bg`: the visible centre (bbox centre).
  - `bx0,by0,bx1,by1`: full-body bbox from head/cap top to shoe soles.
  - `feet_x,feet_y` and `feet_*_bg`: bottom-centre point.
  - `height_px = by1 - by0`, `width_px`.
  - `occluded`, and `source` (`key` = hand-read keyframe, `interp` = linear between keyframes 8 frames apart, `interp_gap_a_b` = long gap).
- `scripts/`: every script used. Key ones:
  - `camera.py`, `camlib.py` (`to_bg`): camera motion and background mapping.
  - `cam_check.py`: validates the camera model.
  - `ball_track.py`, then `ball_finalize.py`: ball track. Hand-entered points are in `ball_seeds.json` and `ball_manual.json`.
  - `ball_diameter.py`: full-outline diameter.
  - `people_keyframes.json` with `people_tracks.py`: people tracks.
  - `build_scene.py`: writes `scene.json`.
  - Viewers: `grid.py`, `view.py`, `overlay.py`, `overlay_all.py`.

## Camera (important for any motion question)
- The camera is handheld. It jitters slightly over f0–26 (|shift| < 20 px), then pans right over f26–70 following the ball, and is nearly still over f70–96.
- The pan is a rotation, so the background shift is NOT uniform. At the end it is about −200 px at the image centre, about −240 px at x≈1000 and x≈3050, and about −265 px near the edges.
- I modelled it with a per-frame homography (ORB + RANSAC on sky, palms, buildings and the hoop pole, matched directly to frame 0).
- Validation: I template-matched 6 static objects at several depths. The shift the model predicts agrees with the measured shift within 1–3 px (one motion-blurred frame was off by 11 px).
- There is no zoom (scale stays within about 0.3 %).
- Use `x_bg,y_bg` for ball or person motion. The raw `x,y` include the pan.
- `x_bg,y_bg` are frame-0 image pixels, not a rectified ground plane.

## Ball (tracks/ball.csv) — most reliable item
- **Phases:**
  - f0–8: dribble, moving down.
  - f9: ground bounce (lowest centre y = 1737).
  - f10–14: rising back to the hand.
  - f15–46: held. Gather and shooting motion; the set point is above the head, at y ≈ 1406–1418 over about f33–41.
  - Release: last fingertip contact at f46, first free frame f47.
  - f47–81: free flight. Apex at f65 (y_bg 874.4, raw y 886.5).
  - f82: reaches the front of the rim.
  - f83–85: inside the net. Horizontal motion reverses at f83.
  - f86–94: falls below the net (f94 partly behind `red_tracksuit`).
  - f95–96: hidden.
- **Centres:**
  - Auto frames: centroid of an orange colour mask.
  - Frames 46 and 81–85: read by hand from zoomed crops (±3–4 px). In 82–85 the ball is dark, in the rim shadow and inside the net.
  - f94: hand-read, partly occluded.
  - In flight, the per-frame jitter is about 2–3 px (seen as the scatter of frame-to-frame steps).
  - The colour centroid sits about 3–4 px toward the lit side of the true outline. This offset is nearly constant, so it hardly affects motion.
  - In f15–44 the hand touches the ball, so the mask may include some skin (f24 bbox is too big). The centre is still on the ball, as checked on overlays.
- **Ball diameter:** **45 px ± 1.5**.
  - Measured as the full outline against clear sky: f49 45.7, f51 45.5, f52 45.9, f75–77 45.1–45.2 (bbox 44–46 px).
  - The Hough fits and the dribble frames (about 42–46 by eye) agree.
  - The apparent size does not change measurably during the flight.
  - Do NOT use `diam_eq` / `mask_w` in ball.csv as the ball size: they measure only the lit orange core (about 33–37 px).

## People (hand-read keyframes, ±7 px per edge)
- **How measured:**
  - No person detector was available, so I read full-body boxes by hand on gridded frames at f0, 8, …, 96 and interpolated linearly between them.
  - I checked them on overlays (f0, f20, f44, f84): the boxes enclose the right people.
  - The reference point is the bbox centre (visible centre). The feet point is the bottom-centre.
  - Interpolated frames between 8-frame keyframes can be off by about 10 px for fast limbs. Rows marked `interp_gap_*` (long gaps while occluded) are rough.
- **Key heights (px, head/cap top to soles):**
  - `blacktee_redshorts`: 477–494, about 483 on average. He stays at a similar depth.
  - `shooter_grey_tank`: about 331–337 standing at f0–40. 366 at f48 includes the raised shooting arm: the head top is at y≈1384 and the feet are about 20–25 px off the ground (small hop, takeoff about f46, landing about f52–54).
  - `big_guy_dark_tee_cap`: 657 at f0, shrinking steadily to 517 at f96 as he walks away from the camera. Because his depth changes, his pixel height is not a constant scale.
  - `red_tracksuit`: 547 at f0, falling to about 494 at f56–64, then about 512.
  - `yellow_shorts`: 331–345.
  - `white_shirt`: 419–442 (465 at f0, when he was nearer).
  - `red_shirt`: about 326–331 (362 at f0).
  - `bald_black_shirt` (background): 293–308.
- **Visibility and occlusion:**
  - `shooter_grey_tank`: hidden behind `blacktee_redshorts` from about f84.
  - `yellow_shorts`: behind `red_tracksuit` for f10–46 and f74–96.
  - `white_shirt` and `red_shirt`: mostly behind `big_guy` before about f40/f56.
- **Similar-looking people (red clothing):**
  - `red_tracksuit`: full red hoodie and pants.
  - `red_shirt`: red T-shirt with white leggings.
  - `blacktee_redshorts`: dark-red shorts.
- **Motion summary (background coordinates):**
  - `big_guy` walks right and away the whole clip (feet_bg x 1549 → 2103).
  - `blacktee` drifts right slowly and speeds up after f64 (feet_bg x 956 → 1539).
  - `red_tracksuit` goes right until about f32, then turns back left (about f34–40), then barely moves.
  - The shooter stays roughly in place, moving about 300 px right over the clip.

## Static objects (scene.json)
- **Backboard (f80):**
  - Seen obliquely, so its pixel width (157 px) is foreshortened and is not its true width.
  - Corners: TL (2367,1008), TR (2524,928), BR (2530,1146), BL (2369,1180) estimated.
  - Left edge is 172 px tall. The right edge (218 px) includes the white side frame.
- **Rim (f92):**
  - Nearly edge-on. Horizontal extent 2351–2423 (72 ± 8 px); the right end merges with the orange bracket.
  - Centre (2387,1136); in frame-0 background coordinates (2597,1124). Net bottom at y≈1210.
- **Hoop pole (f80):**
  - Top (2775,994); ground base (2822,1745); 751 px visible.
  - Rim y is about 609 px above the pole-base y. This is only approximate as a rim height: the rim is nearer the camera than the pole, and its ground point is not visible.
- **Trash cans:**
  - Black can (f80): 75 × 113 px.
  - Green can (f8): 58 × 93 px.
- Bleachers, the restroom building, palm trees and the court lines are listed with approximate boxes only.

## Ambiguities / cautions
- The scene is labelled 2D, but it has real depth. The ball flies away from the camera toward the hoop, and people are at different depths (the nearest player is about 2× the pixel height of the background ones). With a single planar scale, results depend on which object provides the prior.
  - Ball-related questions: the ball's own size (45 px) is the natural scale.
  - Person-height priors: choose that person's height at the relevant frames.
- Motion blur is mild. In the hand and net phases the ball centres are hand-read.
- Shadows of the players on the court are long (low sun). They are excluded from all boxes.
- Faces of two people are blurred in the source.

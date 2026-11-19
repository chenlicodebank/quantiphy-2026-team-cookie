# internet_0011 — measurement notes

**Scene.** A real drone video looking straight down on an outdoor red basketball half court, with the hoop at the top
centre. 107 frames at 20.428571 fps, 3840x2160. Two players move through the whole clip:
- **player_black**: black T-shirt, ginger curly hair. He dribbles the **basketball** from under the hoop down the court (+y).
- **player_white**: white T-shirt. He moves down the court in front of player_black, back-pedalling or walking, at about 14 px/frame.

Everything here is in full-resolution pixels and in frames/seconds (t = frame/fps). No metric scale is assumed.
Treat it as 2D: the floor is roughly parallel to the image. Only the hoop and backboard are raised (~3 m), so they
appear slightly larger than floor markings would at the same scale.

## Files
- `scene.json`: the object inventory, static pixel sizes and positions, events, the camera summary and the duplicate-frame list.
- `tracks/player_white.csv`, `tracks/player_black.csv`: one row per frame (0-106). Columns:
  - `cx,cy`: the mask centroid, used as the visible centre and reference point.
  - `bbox_cx,bbox_cy`, `x0,y0,x1,y1`: the bounding box.
  - `len_main_axis`, `width_across`: PCA extents of the mask. `main_axis_deg` is the main axis angle (0 = +x, measured toward +y).
  - `mask_area_px`.
  - `occl_or_near_other`: 1 if the two players' predicted centres were less than 240 px apart. This never happens; they stay 485-760 px apart.
  - `cx_f0,cy_f0`: the centroid mapped into frame-0 coordinates (camera-compensated).
  - `dup_of_prev`: 1 if the frame is a repeat of the previous one.
- `tracks/ball.csv`: one row per frame. Columns:
  - `cx,cy`: circle centre. `diameter`: the Hough circle diameter. `x0..y1`: the circle's box.
  - `score`: detector score. `manual`: 1 = placed by hand.
  - `cx_f0,cy_f0`, `dup_of_prev`: as above.
- `tracks/camera.csv`: one row per frame. A similarity transform (current frame -> frame 0, from ORB features + RANSAC) gives:
  - the shift of the image centre in px, the scale and the rotation;
  - the inlier count.
- `scripts/`: every script used.
  - `bg.py` builds the median background and transforms.
  - `blobs.py` does foreground segmentation.
  - `track_players.py`, `track_ball.py`, `ball_manual.json` (the manual ball anchors), `review_ball.py`: tracking and the checking montages.
  - `static.py` measures court markings.
  - `dupes.py` detects repeated frames.
  - `camera.py`, `summary.py`, `ball_side.py`, `finalize_tracks.py`.
  - `_bg.png`, `_M.npy`, `_static_raw.json` are small intermediates.

## How it was measured
- **Camera.** ORB+RANSAC similarity transforms between each frame and frame 0 (half resolution). The drone is almost
  still. Over the clip the image drifts by up to about 16 px in x and 8 px in y, and the scale changes by about 1%
  (slight zoom-in or descent). Rotation is under 0.15°. Use `cx_f0/cy_f0` to measure motion against the court. The
  raw and compensated values differ by at most about 20 px.
- **Players.** Each frame is compared with a median background warped into that frame (half resolution, threshold
  40). Connected components are assigned to the nearest predicted player, and outputs are scaled x2 to full
  resolution. The mask covers head, shoulders, arms and visible legs, but not the shadows (checked on overlays every
  7 frames). The reference point is the visible centre (mask centroid).
  - player_white has a clean mask: centroid ±5 px.
  - player_black's black shirt is close in colour to the dark court and shadow stripes, so his mask has holes. Expect a
    centroid of ±15 px, and extents that vary 170-305 px along the main axis because the arms swing while dribbling.
  - Top-down view: "length along the main axis" is the body footprint seen from above (shoulders and arms). It is not
    standing height. A standing height cannot be measured in this view.
- **Ball.** Hough circles in a window around player_black, scored by brightness contrast, orange hue and radius.
  Candidates are then linked across frames by a Viterbi pass (continuity cost).
  - Every frame was checked visually on gridded crops.
  - Frames 12-15 and 103-106 are hand-placed (`manual=1`). There the detector preferred the player's ginger hair, and
    in 103-106 the ball is motion-blurred under the hand. These points are good to about ±8 px.
  - Ball diameter: median 53.4 px, IQR 50.8-57.2, over the 99 automatic frames. The per-frame value is noisy (±5 px),
    so use the median, about 53-54 px. A small real variation comes from dribble height (closer to the drone = larger).
- **Static markings.** Centres of white lines measured along rows and columns of the median background (frame-0
  coordinates), good to ±2 px. Key values:
  - Lane (key) width: 1077 px (x 1414-2491).
  - Lane length from baseline to free-throw line: about 1287 px.
  - Free-throw circle diameter: about 796 px.
  - Sideline separation: 3334 px. 3-pt straight-line separation: 2891 px.
  - Restricted-arc width: 545 px.
  - Rim outer diameter: about 130 px. Backboard width: 338 px. Both are raised, so they appear larger than they would on the floor.
  - The baseline is tilted about 0.6° (y 295 at x=400 to 260 at x=3200).

## Duplicate frames (important for frame-by-frame differences)
Frames 65 and 66 repeat 64; 70 repeats 69; 72-74 repeat 71; 77 and 78 repeat 76; 91 repeats 90; 97 repeats 96.
Their mean absolute difference from the previous frame is 0.03-0.11 grey levels, against about 0.7-1.9 for normal
frames. Positions are constant across these frames, so one-frame velocities are 0 there and jump afterwards. Prefer
fits or differences over longer spans. The frame rate in inputs.json is still used for the time convention.

## Motion summary (pixels; for orientation only)
- **player_white**: (1544,577) → (2082,1927). Net ≈1453 px, path ≈1465 px. Nearly straight, heading down and slightly
  right. Roughly constant pace, about 14 px/frame with duplicate frames counted as frames.
- **player_black**: (2022,492) → (2128,1172). Net ≈690 px, path ≈790 px. He weaves left and right while dribbling and
  goes faster after about frame 55.
- **Ball**: (2024,547) → (2052,1231). Net ≈684 px. Its image path is ≈1200 px because of the hand-to-hand moves.
- **Separation between the players**: 485 px at the start, 761 px at the end, increasing steadily.

## Events
- Neither player starts or stops inside the clip.
- **Ball side changes** (ball x minus player_black centroid x):
  - Frames 0-9: ball in front and slightly right of the player.
  - Frames ~10-56: it moves to his image-left side, up to 128 px left.
  - Frames ~56-67: crossover to the front and right, up to +78 px right during 67-80.
  - Frames ~82-92: crossover back to the left, about -100 px by frame 98.
- Individual dribble bounces and floor contacts cannot be timed reliably. The vertical motion is along the line of
  sight, and the apparent-size changes (±5 px) are within the detector noise.

## Ambiguities
- Ginger hair vs ball: similar colour; handled by the manual frames.
- The dark shirt blends into the shadow stripes, so player_black's mask is incomplete.
- Long diagonal tree shadows cross the court. They are static and are not objects of interest.
- The hoop, backboard and pole are raised and show a little parallax as the drone drifts.
- A second, larger rectangle marking (x 968-2958, from y 1212 down) overlaps the key. It belongs to another court layout.

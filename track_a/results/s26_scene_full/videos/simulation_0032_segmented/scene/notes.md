# simulation_0032_segmented: measurement notes

**Scene.** This is a 3D Blender render, segmentation version, 30 fps, 130 frames, 1920x1080. The background is plain white. One basketball player (black #23 jersey, black shorts, blanked light-grey face, white shoes) stands at x≈1230 and shoots a red basketball to the left into a hoop that is **not drawn**. The ball flies left in an arc and goes through the invisible rim and net at x≈714, y≈495. It then falls and bounces on the invisible floor. Frames 128–129 are completely black. The camera is static. All values are in pixels (x right, y down) and seconds (t = frame/30). No metric scale was assumed.

## Files
- `scene.json`: inventory, sizes, events, camera and perspective notes.
- `tracks/ball.csv`: one row per frame. Columns:
  - `state` is one of free / held / cut_bottom / hidden / partial_net / blank_frame.
  - `cx, cy` is the ball centre (the object origin).
  - Also: bbox, `w, h`, mask `area`, an `occluded` flag, and `diam_px` (apparent diameter: mean of w and h when unoccluded; the width for cut frames).
- `tracks/player.csv`: one row per frame. Columns:
  - mask bbox, `w, h`, area and mask centroid;
  - `face_cx/cy`, `head_top_y`, `feet_y`, `foot_left/right_x/y`, `head_to_feet_px`;
  - the **pelvis proxy** `pelvis_x, pelvis_y`;
  - flags: `mask_truncated`/`occluded`, and `pelvis_interp` (1 = linearly interpolated).
- `tracks/*_stage1.csv`: intermediate tracker output. `summary_stats.json`: diameter statistics, the rim-edge rows, the apex, and standing-player medians.
- `scripts/`:
  - `track2.py` is the main tracker. `finalize_ball.py` and `player_parts.py` → `finalize_player.py` build the final CSVs. `summary.py` makes the statistics.
  - `overlay.py` and `crops.py` make the visual checks. `probe*.py` were for exploration. `track.py` is the first, superseded tracker. `cleanup.py` removes scratch files.

## How measured
- Foreground = min(RGB) < 230. Ball pixels = red hue (OpenCV H < 12 or > 165, S > 90, V > 55).
- **Ball, free (frames 24–78, 100–127):** centroid of its own connected component. Precision is about ±0.5 px, and the diameter scatters by about ±1 px.
- **Ball, held (frames 0–23):**
  - Method: a matched filter with a disc of radius 17.5 px on the red mask, searched near the previous position.
  - The hands cover part of the ball, so the error is about ±2 px.
  - The player's forearms are also reddish-brown. The fits were checked visually and land on the ball.
- **Ball, cut_bottom (frames 79–94):**
  - The ball sinks behind the invisible rim and only its top cap shows. The cut is a horizontal edge at y≈493–499.
  - Centre = (bbox mid-x, bbox top + 17.5 px). The error is about ±1.5 px.
  - Frame 94 shows only a 10-px sliver, so its centre is less reliable (±3 px).
- **Ball, hidden (frames 95–99):** no data; interpolate if needed. Frame 100 has holes from the net, and its centroid (713.8, 562.3) is good to about ±2 px.
- **Ball apparent size:**
  - 35.1 ± 0.8 px through the whole flight (24–78), with no trend. So the ball's camera distance hardly changes in flight.
  - 33.4 ± 0.9 px after the net (101–127), about 5% farther away than at release.
- **Player pelvis:**
  - The simulation origin is the pelvis, which cannot be seen directly. The proxy is y = head_top + 0.47·(feet_y − head_top), on the assumption that the hip joint is about 53% of stature above the soles. x = mean mask x in the rows around that y.
  - Visually it falls at the waist/top of the shorts. Expect an absolute error of about ±8 px in y. Frame-to-frame changes are better (±2 px).
  - While the shooting arm is raised (frames 20–35), the face blob can shift, so head_top and the pelvis are noisier (±5 px).
  - The player barely translates. The pelvis proxy stays at x 1228–1232, and y runs from 698 (crouched, frames 0–4) to about 675 (rising, frame 21) to about 685 (standing, frames 54–127).
- **Player segmentation artefact:** in frames 42–53 the lower body is missing from the video (the legs disappear). The bbox and height there are wrong (`mask_truncated` = 1), and the pelvis is interpolated.
- **Player sizes:**
  - Standing (frames 56–127): bbox 59 × 217 px (head top y 583 to soles y 799).
  - Crouched (frame 0): h 194 px.
  - Maximum bbox height with the arm raised: 243 px (frames 25, 29).
  - Minimum head-to-feet: 192 px (frames 1–2).

## Events (frame / t)
- Frames 0–2: holding the ball, crouched.
- Frame 3 (0.100 s): the ball starts moving.
- Frame 5: the player rises.
- Frames 16–19: set point above the head.
- **Release: frame 24 (0.800 s)** is the first frame the ball is separate; the last frame in the hand is 23.
- Ball image apex: frame 59 (cy 447.2; flat over 51–60).
- Rim reached: frame 79 (2.633 s).
- Hidden: frames 95–99.
- Reappears under the net: frame 100.
- **Floor bounce: frame 120 (4.000 s)**, lowest cy 760.9.
- Rebound apex: frame 123.
- Second contact: frames 126–127.
- Black from frame 128.

## Ambiguities
- **Camera distance and focal length:** perspective is unknown. There is no visible ground or horizon. Focal length must come from the depth_info supplied with the question plus a known size, e.g. f = diam_px·depth/diameter, using the ball's 35.1 px in flight.
- **Possible small hop:** frames 23–37 might be a small jump or a heel lift. Feet_y rises by up to 13 px and one foot leaves the bottom band.
- **Frames 126 and 127 are identical:** this may be a held frame at the end of the render.
- **Shadows and blur:** there are no shadows. Motion blur on the ball is small.
- **Duplicates:** there are no similar or duplicate objects.

# captured_0016 – measurement record

Lab video, 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0 … 2.0 s). Container timestamps are uniform.
Protocol intrinsics: f = 763 px, principal point ≈ (640, 360), no zoom. All numbers here are image pixels; no metric scale is assumed.

## Content
An underhand throw between two people, filmed by a **static** high camera looking obliquely down at a grey carpet.
- **ball**: white football with black panels and a black logo panel. It is the only ball and the only object that travels.
- **thrower**: on the left edge, light grey T-shirt, glasses, face blurred. Only part of the body is in frame. Holds the ball (frames 0–29) and throws it underhand.
- **receiver**: on the right by the wall, dark grey T-shirt, black trousers, white sneakers, long hair. Feet stay put. Catches at frames 43–44.
- **static**: carpet floor; right wall with a dark baseboard; blurred clutter at the back (exercise balls, chair, seated people's legs, a white box); faint floor marks.

The video went through a "Segment Anything 2 Demo" effect. The background is strongly blurred. The ball and both people stay sharp, and the ball has a light **halo of about 5–10 px**. Edges were taken at roughly half-contrast, so the halo is excluded.

## Files
- `scene.json`: inventory, camera, perspective cues, apparent-size summary, events.
- `tracks/ball.csv`: the main ball track for every frame 0–48. Columns:
  - `cx, cy`: visible centre = centre of the mask extent box.
  - `bbox_*`: extent box; `bbox_w/h` are its size.
  - `len_major / width_minor`: minimum-area rectangle of the mask hull, i.e. length along the main axis and width across it. In frames 27–35 this is the motion-blur streak.
  - `ell_major / ell_minor`: ellipse fit.
  - `occluded_or_in_hand`: 1 while the ball is held or touched.
  - `source`: which mask the row comes from.
  - `note`: per-frame caveats.
- `tracks/ball_mask.csv`: held-phase mask for frames 0–27 (white panels plus black panels touching them).
- `tracks/ball_flight_mask.csv`: flight mask for frames 26–48 (background subtraction against the all-frame median, skin excluded). Both are raw inputs to `ball.csv`.
- `tracks/receiver.csv`: per-frame centroids of the two white shoes and the lowest shoe pixel (`feet_bottom_y` = 432).
- `tracks/thrower.csv`: per-frame box of the light-grey T-shirt. Coarse; it shows the torso hardly moves.
- `scripts/`:
  - `ball_mask.py`, `flight_mask.py`, `assemble_ball.py`: the final ball track.
  - `people.py`: the people tracks.
  - `background.py`: median background and baseboard line.
  - `verify_overlay.py`: overlay check.
  - `probe.py`, `pts.py`, `profile.py`: camera-shift check, timestamps, edge profiles.
  - `track_ball.py`, `hough_ball.py`, `circle_fit.py`, `ray_fit.py`, `ransac_ball.py`, `zoom_sheet.py`, `seeds.txt`: earlier attempts and viewing aids. Their outputs were superseded and deleted.

## Ball track: how it was measured and how reliable it is
- **Frames 0–18** (held still or lifted slightly):
  - The mask is white panels (min channel ≥ 200, unsaturated) plus the black panels that touch them. Hands are saturated, so they drop out.
  - The extent box agrees with manual reading on zoomed, gridded crops to about 2 px (frame 0: x 254–381, y 490–599).
  - The bottom edge is partly behind the fingers. The vertical size may be 1–3 px short.
- **Frames 19–26** (wind-up and start of the forward swing, blurred): the left and bottom edges sit against hands and dark trousers. Centre accurate to about ±4 px; frame 26 to about ±6 px.
- **Frames 27–35** (throw and early flight):
  - Strong motion blur. The mask is a streak and the box centre is the mid-exposure position, about ±5 px.
  - `len_major` includes the blur; `width_minor` (about 90–113) approximates the diameter across the motion.
  - Frame 28's left edge was set by hand (285), because the mask ran onto the forearm.
- **Frames 36–42** (late flight, mild blur): about ±3 px. Frame 40's bottom edge was set by hand (134), because the lower black panel was missed.
- **Frames 43–48** (catch): the receiver's arm or hands overlap the ball's right and bottom edges. About ±4 px.
- All overlays were checked by eye (`frames/verify.png`, crop sheets).

**Apparent size.**
- Held (frames 0–16): about 124–127 px wide × 107–111 px high. The ball sits far left of the image centre, so the off-axis projection stretches it roughly 10% along the radial direction, which is mostly horizontal there. The minor axis (about 104–109) is closest to the true angular diameter.
- Flight, frames 37–41: about 104→85 × 95→87.
- Caught, frames 44–48: about 64–74 × 60–70.
- The ball ends up about 1.7–1.8 times farther from the camera than where it starts.

## Events (frame, t)
| Frame | t (s) | Event |
|---|---|---|
| 0–13 | 0–0.54 | Held. Small lift up and to the right, from (317.5, 544.5) to (334.5, 518.5). |
| 14–24 | 0.58–1.0 | Wind-up: ball moves down-left to its lowest point at frame 24, (272.5, 601.5). |
| 24–25 | 1.0–1.04 | Reverses into the forward swing. |
| ~30 | 1.25 | Release (±1). The hand is last in contact at frames 29–30; the ball is clearly free from frame 31. |
| 36–38 | 1.5–1.58 | Apex of the arc in the image (cy ≈ 71.5; top edge y ≈ 24). |
| 43 | 1.79 | Catch contact: the receiver's forearms touch the ball. |
| 44 | 1.83 | Ball secured; carried down-right through frame 48. |

The receiver raises her arms from about frame 36.

**Anomaly:** the ball's image step from frame 35 to 36 is about 93 px. The steps before and after are about 50 and 34 px. A capture frame may have been dropped between 35 and 36, or the frame timing is irregular there. Container timestamps are uniform, so this cannot be confirmed. Treat any per-frame difference across frames 35→36 with caution.

## Camera and perspective
- **Camera:** static. Phase correlation on background patches gives ≤ 0.1 px shift per frame.
- **Floor–wall baseboard on the right:** y ≈ 0.733·x − 418 px, through (720, 110) and (1260, 506). It is hidden behind the receiver for x ≈ 950–1090.
- **Wall corner:** about x ≈ 705, y 0–100.
- **Horizon:** above the image, because the camera is pitched down.

## People
- **Receiver:**
  - Shoes at about (941, 385) and (984, 423); they drift by 3 px or less.
  - Feet bottom at y ≈ 432–435. Body spans x ≈ 924–1230 at frame 0.
  - The top of the head is cut by the image top, so the **full height cannot be measured** (the visible part is ≥ 435 px).
- **Thrower:** only partly visible (head x 0–80, y 40–240; T-shirt x 0–170, y 286–535). Height and size cannot be measured.

## Ambiguities
- Halo versus ball edge: edges were taken at about half contrast. A halo-inclusive mask would be about 5–8 px larger per side.
- Off-axis stretching of the held ball.
- Motion-blur streaks in frames 27–35.
- Hand occlusion in frames 0–30 and 43–48.
- The possible dropped frame between 35 and 36.

# internet_0057 – measurement record

Internet clip, 2D question type, 30 fps, 188 frames (0–187, t = frame/30), 1920×1080.
Indoor basketball court. A person standing left of the hoop takes a jump shot. The ball misses everything
(it passes above rim height in front of the glass and touches neither the rim nor the board), lands right
of the lane, and bounces along the floor to the right. After landing, the person walks to the right.
All values are in pixels and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory (objects, what tells them apart, static extents), camera, perspective cues, events.
- `tracks/ball.csv`: ball, every frame 0–187. Columns: `cx_px, cy_px` = visible centre in frame pixels;
  `cx_bgfixed_px, cy_bgfixed_px` = same point mapped to frame-0 background coordinates (camera drift removed;
  **use these for motion**); bbox of the red mask; `diameter_px` = widest horizontal extent of the mask;
  `mask_area_px`; `state` (`held` for frames 0–53, `free` from 54); `occluded_or_degraded` (1 = in hands or the mask
  merged with a reflection or partly lost).
- `tracks/person.csv`: person, every frame. Bbox runs from the top of the cap to the lowest sole, arms and legs
  included. Centre = bbox centre (frame and bg-fixed). Also `width_px`, `height_px`, mask pixel count,
  `feet_contact_row_px` (sole/floor row used to cut off the floor reflection), `airborne` (frames 55–66 flag).
- `tracks/camera_shift.csv`: per-frame similarity transform from frame 0 to frame i (scale, roll in degrees, shift of
  the image centre, RANSAC inlier count) from ORB matches on the whole frame.
- `scripts/`: `camera.py` (camera transform), `background.py` (median background in frame-0 coordinates),
  `track.py` (ball + person tracker), `export.py` (CSV writer + event finder), `stats.py`, `static.py`, `static2.py`,
  `floorlines.py` (static extents and court lines), plus the check renderers `overlay.py`, `ball_sheet.py`,
  `feet_sheet.py`, and diagnostics `ball_cands.py`, `fg_probe.py`, `fgfreq.py`, `peek.py`, `feet.py` (an abandoned
  mirror-axis feet finder). The scripts write scratch images to `../frames/`.

## Camera
The camera is hand-held and drifts slowly. It does not zoom (scale stays within 0.6 %). Against frame 0, the image
of the background shifts steadily: by the end dx ≈ −19 px, dy ≈ −29 px, with roll up to +1.05°. The drift is smooth,
about 0.1–0.4 px per frame, with no shake. It is small next to the ball's motion (5–50 px/frame) but not negligible
for the person or for slow motion, so the `*_bgfixed_px` columns compensate for it. Perspective: the camera faces
the baseline wall roughly square on. The lane lines meet at about (969, 599), so the horizon is near y ≈ 600. The
person and the ball stay on a band of floor at roughly the same depth: the feet's contact row is 898 → 872 over
the clip, and about 29 px of that is camera drift.

## Ball (reliability)
- Detection: red-brown pixels (H ≤ 12 or ≥ 158, S ≥ 120) that also differ from the warped median background. The
  ball is found in all 188 frames.
- Centre: x is the middle of the horizontal extent. y is the mean row where the mask is widest (the equator), so
  vertical motion blur, which eats the top and bottom, does not bias it. I checked crops by eye. The error is
  about 1–2 px in clean frames and up to about 4 px in the most blurred ones (53–54, 96–99).
- Degraded frames: 73–77 (the ball crosses the black pole and the red "3" behind the glass, so part of the mask is
  lost; the y steps there are irregular), 97/99/135/164/187 (floor contacts, where the mirror reflection touches
  the ball), and 0–53 (fingers cover part of the ball).
- Apparent diameter: 49 px in the hands, about 43 px in flight near the hoop (frames 54–96), 46 px after
  bounce 1, 47 px after bounce 2 and 48 px at the end. A manual check at frame 112 gave 47×46 px. The change
  reflects depth: the shot travels a little away from the camera, and after the bounces the ball comes back
  toward it. If a question gives the ball's size as the prior, use the diameter at the times the question is about.
  The overall free-flight median is 46 px.
- Horizontal pixel velocity: about 15.4 px/frame, nearly constant from release to the first bounce (no contact with
  the rim or board). After the first bounce it drops to about 5.5 px/frame, part of which may be motion in depth.
- Bounce frames (largest y): 97, 135 and 164, plus a 4th contact at or just after frame 187. The apexes are at
  71 (the shot), 116, 149 and 176. Their bg-fixed positions are listed in `scene.json`.

## Person (reliability)
- The mask is foreground (diff > 22) after a 7×7 opening, which removes thin edge artifacts from the camera drift.
  The x-extent comes from a column profile with hysteresis.
- The glossy floor reflects the person strongly, so I read the lowest-sole row by eye on 11 keyframes and
  interpolated linearly between them (± 3–5 px). In airborne frames 55–62 the bottom is the lowest visible foot.
- Height while standing still (0–38): median 322 px (range 316–325), cap top to sole. While walking (120–187):
  median 314 px (range 303–326). Frames 66–110 run up to 340 px when the arms are raised or the person is on
  their toes.
- The bbox can miss trailing toe tips by up to about 10 px in some walking frames (thin, low-contrast shoe tips
  over the floor). The face is blurred in the source video, so the head outline is approximate (± 3 px).
- Walking: the bg-fixed centre goes from x 611 (frame 90) to 1398 (frame 187).

## Static objects (frame-0 pixels, measured on the median background)
- Rim: outer width 90 ± 4 px (orange mask 924–1009; visual edges 921–1014), y 302–332; centre ≈ (967, 316).
- Backboard: 361 px wide including the side padding (786–1146), 332 px for the glass frame (800–1131); top
  ≈ 150, bottom of the padding ≈ 362 (height ≈ 213).
- Pole: 41 px wide. Wall pads: 634 × 237 px (8 panels of about 79 px). The scoreboard is cut off by the image edge.
- Notice boards: 79×116, 116×76 and 76×50 px. Fire extinguisher cabinet: about 48×94 px. Lane lines and the
  horizontal court line (y ≈ 855): 604 px apart at y = 860.

## Ambiguities
- Planar convention: the annotators used one scale factor from the prior. If the prior is the ball's diameter,
  note that its apparent size varies by ±6 % over the clip because of depth.
- It is unclear whether the ball passes in front of or behind the backboard glass (the glass is transparent).
  It clearly does not hit the rim or the board.
- Release is at frame 54 ± 1: the fingertips still touch the ball at 53. Takeoff is at about 55 and landing at
  about 63.
- There is no other ball, person, vehicle or animal. The floor reflections of the ball and the person are not
  separate objects.

# simulation_0252: measurement notes

**Scene.** A 2D Blender render, 1920x1080 px, 24 fps, 41 frames (t = frame/24). The camera is static: frames 0 and 40
differ by a mean of 0.13 grey levels away from the ball, so the background shift is 0 px in every frame. The
background is a plain grey studio surface. A lighter band at the top ends at a horizontal edge at y ≈ 148 px. There
are no markings, furniture or other objects.

**The only object is a ball.** It is a soccer-style ball with a light-grey body and black star patches. It enters at
the left image border in frame 4 (partly visible), is fully visible in frames 5–40, and leaves no frame early. It
moves left to right along a horizontal line. Its centre stays at y = 382.5 ± 1 px, with no vertical motion and no
bounce. Its x-centre goes from 12.5 px (frame 4) and 68.5 px (frame 5) to 1843.4 px (frame 40). The per-frame step
decreases smoothly from about 56–57 px/frame (frames 5–9) to about 45 px/frame (frames 36–40), so the ball slows
down steadily. Frames 0–3 are empty background.

## Files
- `scene.json`: inventory, ball size, motion summary, events, camera.
- `tracks/ball.csv`: one row per frame from 4 to 40.
  - `cx`, `cy`: the ball centre (its origin), the reference point to use.
  - `bbox_*`: the box from the 66 px vertical diameter and the 75.8 px blurred horizontal width.
  - `diam_vertical_px`, `width_horizontal_px`: the ball's size.
  - `left_limb_px`, `right_limb_px`: raw limb columns on the equator rows 378–388.
  - `cx_from_left`, `cx_from_right`: the two centre estimates.
  - `right_limb_shadow_contaminated`: 1 from frame 24 on.
  - `dark_y_min`, `dark_y_max`: vertical extent of the black star pixels (grey < 60).
  - `occlusion`: only frame 4 is flagged (partly out of frame on the left).
- `scripts/`: `track_ball.py` (final tracker), `edges.py`/`edges2.py` (edge studies), `background.py`
  (backdrop edge and camera check), `explore.py`, `maskview.py`, `profile.py`, `zoomdiff.py` (inspection).
  Frames 0–3 hold no ball, so frame 0 serves as the clean background image.

## Method and reliability
- **Why the simple fits failed.** The ball's grey body has almost the same brightness as the background. A
  large soft shadow sits directly above the ball (y ≈ 295–350), and in later frames it leans up and to the right.
  Because of this, background-difference masks and free circle fits were biased: the circle fits gave diameters of
  53–76 px and pulled the centre toward the shadow or the stars. I discarded them.
- **What the tracker does.** It finds the ball's left (trailing) limb on each row from 372 to 402. The shadow never
  touches that limb. It then fits a limb ellipse centred at y 382.5 with semi-axes 33 px (vertical) and 37.9 px
  (horizontal). The horizontal semi-axis was calibrated on frames 5–21, where both limbs are clean, so the left-
  and right-based centres agree.
- **Accuracy of `cx`.** About ±1.5 px per frame. The per-frame steps scatter by about ±2 px around a smooth trend;
  the outliers are frame 34→35 (44.3 then 49.7) and frame 38→39 (41.1 then 46.8). Smoothing or fitting over
  several frames is advisable before differencing.
- **The right-limb estimate.** `cx_from_right` agrees within about 2 px up to frame 23. From frame 24 on it reads
  2–10 px too far right because the shadow merges with the right limb, so do not use it there.
- **Frame 4.** The centre comes from the right limb, so it is less reliable (±3 px).
- **The vertical centre.** I set `cy` = 382.5 for all frames. The top limb is at about 349.5 and the bottom limb at
  about 414–415.5 in every frame, and the star pixels always span y 351–415.
- **Size.** The true pixel diameter is 66 ± 1.5 px, measured vertically, which motion blur does not affect.
  - On the overlays, the sharp disc is round and 66 px across.
  - A faint horizontal smear from motion blur makes the limb-to-limb width about 72–76 px.
  - For a pixel-size scale, use 66 px (length = width = height for a sphere).
  - The apparent size does not change over the clip, so the motion is at a constant depth and one pixel scale
    applies everywhere.
- **Checks.** I drew overlays on frames 4, 5, 12, 20, 26, 30, 34, 38 and 40: the centre cross, the 66 px circle and
  the 75.8 px ellipse. Both shapes sit on the ball and not on the shadow.

## Events
- Frame 4 (t = 0.1667 s): the ball enters at the left edge, already moving.
- Frame 5 (t = 0.2083 s): the ball is fully visible.
- Frame ≈21.4 (t ≈ 0.89 s): the ball crosses the image centre (x = 960).
- Frame 40 (t = 1.6667 s): the clip ends with the ball still moving and fully in view.

No release, bounce, contact, stop or direction change happens. Motion begins before the first visible frame.

## Ambiguities
- **Shadow.** Do not confuse the dark shadow above the ball with the ball itself. The ball's top limb is at
  y ≈ 349.5.
- **Rolling or sliding.** The star pattern rotates between frames (the ball appears to roll or spin); this was not
  measured.
- **Wall versus floor.** Whether the y ≈ 148 edge is a wall/floor line or a backdrop fold is unclear. It does not
  matter for this 2D clip.

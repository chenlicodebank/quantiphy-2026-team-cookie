# internet_0064 – measurement record

Internet video (real footage), labelled 2D, 1920x1080, 30 fps, 170 frames (t = frame/30, frame 0 = 0 s).
All values are in pixels and seconds; no metric scale has been assumed. Image coordinates: x to the right,
y downwards, origin at the top-left.

## Scene
A static side view of a plain light-grey gym wall, with a black baseboard (y≈979–1006) and a wooden floor strip
(y≈1015–1079). There is one person and one ball.
- **person**: a woman with a beige cap, blurred face, white tank top, olive cargo pants and white sneakers with
  orange soles. She stands at the far left (x≈33–184), facing right, holding the basketball at her hip.
- **basketball** (the only ball): a red-brown ball. She dips it (wind-up, frames 59–73), throws it up and to the
  right (frames 74–80) and lets go between frames 80 and 81 (t≈2.68 s). It flies in a parabola (apex at frame 93,
  cy=183), bounces on the floor at frame 114 (centre (1354,1006)), rises to a second apex at frame 130 (cy=536),
  bounces again at frame 145 near the right edge (centre ≈(1879,988)), and leaves through the right edge
  (partly visible 146–148, gone from 149).
- The woman starts walking right at about frame 118–121 and is still walking at frame 169
  (head x≈141 at frame 120, ≈706 at frame 169).

## Files
- `scene.json`: inventory, pixel sizes, static features, events and camera summary.
- `tracks/ball.csv` (frames 0–148). Columns:
  - `cx,cy`: centre of the fitted circle (the visible centre). This is the reference point.
  - `r_fit,diam_fit`: fitted circle radius and diameter.
  - `bbox_*`: bounding box of the ball mask (within a 1.4r disc).
  - `mask_len,mask_wid,mask_angle_deg`: min-area-rectangle extents of the mask.
  - `area_px`.
  - `held`: 1 for frames 0–80, while the ball is in the hands.
  - `occluded`: 1 when held, or when cut by the right edge (145–148; the flag for 145 was set by hand
    afterwards, so rerunning the scripts drops it).
  - `cx_bg,cy_bg`: the centre in frame-0 background coordinates (camera drift removed).
  - `method`: `colour_mask_circlefit`, or `bg_subtraction_circlefit` for frames 114, 115, 144, 145 and 146.
- `tracks/person.csv` (frames 0–169). Columns:
  - `cx,cy`: bbox centre (the visible centre).
  - `mcx,mcy`: mask centroid.
  - `bbox_*`.
  - `height_px`: cap top to shoe sole.
  - `width_px`: bbox width.
  - `foot_y,top_y,area_px`.
  - `cx_bg,cy_bg`: bbox centre in background coordinates.
  - `head_x/head_x_bg`: mean x of the top 100 mask rows (cap/head). This is the steadiest horizontal reference
    for walking.
  - `waist_x/waist_x_bg`: mean x of the band 210–260 px below the top. Arms swinging past it add bias.
- `tracks/camera_shift.csv`: per-frame similarity transform that maps frame-0 coordinates to frame i:
  `x_i = a*x0 - b*y0 + tx`, `y_i = b*x0 + a*y0 + ty`. Also lists `dx,dy` (displacement of the image centre),
  scale, rotation, inlier count and residual.
- `scripts/`:
  - `camera.py`: registration.
  - `track_ball.py`, then `refine_bounce.py`: the ball (run in that order).
  - `track_person.py`: the person.
  - `static.py`: baseboard and floor.
  - `summarize.py`: summary statistics.
  - `overlay.py`, `view.py`, `montage.py`, `person_th.py`, `camera_check.py`, `probe.py`: visual checks and
    diagnostics.

## Methods and reliability
- **Camera**: KLT features on the frame-0 background (x>350) were tracked directly from frame 0 to frame i,
  with a forward-backward check and a RANSAC similarity fit. A frame-to-frame chained version drifted, so it was
  discarded.
  - The camera is almost static: a slow drift. Background content moves about +2 px right and −7 px up over
    frames 0–70, then about 27 px left by frame 169. Scale falls to 0.992 (a slight zoom-out).
  - Median residual is about 0.3 px. Frame 144 is a weaker fit (18 inliers, dy −9.7 against about −7 for its
    neighbours).
  - The drift is less than 1 px per frame. It matters only for slow motion or for precise positions late in the
    clip; use the `*_bg` columns or the transform to remove it.
- **Ball, free flight (81–113, 116–143)**:
  - The colour mask is HSV red, S>90, V<130. Its contour is fitted with a least-squares circle.
  - Overlays were checked at frames 0, 40, 66–81, 84–148: the circle hugs the ball edge.
  - Centre accuracy is about ±1 px.
  - Diameter: median 85.0 px over all free frames; 84.4 in flight 1 and 86.0 in flight 2. It shrinks to
    about 79–81 px in frames 104–111, where the ball is fast and the motion-blurred rim drops out of the mask.
  - Background subtraction gives about 92 px on the same frames, because it includes the blur halo.
  - **For a size prior, the best ball pixel diameter is about 85 px**, the sharp-edge diameter in frames
    81–95 and 116–143. Frames 81–95 give 84.6–85.9 px.
- **Ball, held (0–80)**:
  - The circle fit is made through the hands. Overlays confirm a good centre.
  - The diameter (about 92 px) is larger than in flight. The ball is nearer the camera when held, and the hands
    may bias the fit. Bboxes in these frames include fingers or arm, so use `diam_fit`.
  - Frames 76–80: the ball is motion-blurred while being thrown.
- **Bounces (114, 145)**:
  - The ball overlaps the black baseboard and the floor, and the colour mask fails there. These frames use
    background subtraction against frame 100 (warped with the camera transform).
  - Frame 114: centre (1353.6,1006.4), r≈47 including blur.
  - Frame 145: fitted to the upper outline only, because a floor shadow merges below the ball. Centre ≈(1879.0,987.6).
  - Accuracy is about ±3–4 px.
  - In frame 145 the ball is clearly squashed or blurred, and its position is the least certain point of the
    track.
- **Ball at the edge (146–148)**: the ball is partly outside the frame. The centre comes from a circle fitted to
  the visible arc (about ±3 px).
- **Person**: background subtraction against a clean plate (frame 0 for x≥420, plus frame 169 warped to
  frame 0 for x<420), with threshold 45 and the ball disc removed.
  - **Height** is reliable: median 620 px standing (cap top about 436–446, sole about 1052–1063), 606–626 while
    walking. The face is a blurred grey patch and the tank top is close to the wall colour, so the mask has holes
    there, but the extents are not affected.
  - **Width** and **x0** are less reliable. The video has a compositing patch at the left edge (x<≈40) and a
    faint halo behind the person, so the mask was cut at x<30. Frames 86–112 report bbox_x0=30, which may be
    10–25 px too far left.
  - During walking the bbox includes the stride and the arm swing.
  - Prefer `head_x` for walking position.
- **Static features**: from vertical intensity profiles at frame 0.
  - Baseboard black band: y≈979–1006, with a dark floor-gap line down to about 1020. The top edge is at about
    984 near x=400 and 979–981 elsewhere, so it is nearly level.
  - The floor starts at y≈1015.

## Ambiguities
- **Ghost and shadows**: a faint orange "ghost" smudge trails about 100–150 px behind the flying ball, and soft
  grey shadows of the ball and person fall on the wall. They are not objects and are not tracked.
- **Shadow at frame 145**: the ball's floor shadow merges with it.
- **Depth**: the scene is labelled 2D, but the ball changes apparent size: about 92 px held, about 85 px in
  flight, and about 86–88 px in flight 2. Its path is therefore not exactly in one plane parallel to the wall.
  The bounce contact points lie in front of the baseboard, on the floor.
- **Scale convention**: following the benchmark, use one scale for everything: prior value divided by its
  pixel value. For example, ball diameter about 85 px, or person height about 620 px.
- **Motion blur**: the ball is blurred in frames 76–80 (throw) and in fast flight near frames 100–113 and 145.

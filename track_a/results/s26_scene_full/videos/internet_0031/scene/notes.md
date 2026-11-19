# internet_0031 — measurement record

**Video**: 540x960, 29.804822 fps, 173 frames (t = frame / fps, 0 … 5.771 s). Internet footage, 2D.
**What happens**: near-top-down (nadir) drone view of one end of a football pitch; the goal line is the near-vertical
white line at x≈380–386 on the right, goal mouth y≈414–512. A player in a light yellow/cream kit starts *inside the
goal* behind a white ball resting just inside the goal line (≈(384,498)), takes it out and dribbles it slowly left
(−x, slightly up, −y) across the goal area and penalty area toward the penalty spot. At the end (frame 172) the ball is
at ≈(231,467.6), ~6 px left of and ~4 px below the penalty spot (237,463), still rolling about 1 px/frame. A second player in
dark kit (keeper-like position, near the top of the goal area at ≈(349,430)) stands nearly still until about frame 84,
then walks down-left to ≈(322,457) by frame 172. Who is the goalkeeper is ambiguous: the yellow player starts in the
goal, while the dark player stands where a keeper would. Names used: `ball`, `player_yellow`, `goalkeeper_dark`.

## Files
- `scene.json`: inventory, static markings (pixel positions/extents), events, camera summary, column meanings.
- `tracks/ball.csv`: per frame: x,y (raw image px of that frame), x_stab,y_stab (frame-0 / background coords,
  **use these for motion**), a nominal 3x3 bbox, ball blob width/height at half-max (only on clean auto frames),
  source (auto/manual/predicted), occluded flag (1 = ball merged with the player's body or on the white goal line,
  so the position is interpolated or estimated).
- `tracks/player_yellow.csv`, `tracks/goalkeeper_dark.csv`: per frame: visible centre (raw and stabilized), bbox (raw),
  mask_length / mask_width (extent along/across the mask's principal axis), main_axis_deg, mask_area_px, occluded.
  These are top-down footprints (head + shoulders + limbs), **not** standing heights. Body height can't be measured
  from this view.
- `camera_motion.csv`: per frame ECC affine (frame-0 → frame-i), scale, rotation, and the shift of 3 reference points.
- `tracks_overlay_f120.png`: all three tracks drawn on frame 120 (checked visually).
- `scripts/`: stabilize.py (camera), blobs.py (stabilized ROI + median background), track.py (+ ball_overrides.json,
  hand-read ball positions), export.py, static.py/static2.py (line profiles), make_scene.py, overlay/zoom/montage
  (inspection views).

## Camera
Static hover with slow drift: by frame 172 the image has moved +1.6 px in x and −2.6 px in y. Scale change is +0.08%
and rotation is under 0.03°. This is negligible, but the tracks were measured in stabilized frame-0 coordinates anyway
(x_stab, y_stab). The view is close to orthographic: the box dimensions match standard pitch proportions in both directions,
which suggests a single px-per-length scale is valid over the action area. The image is rotated ~0.4–0.6° (goal line x 380.2 at y70 → 385.9 at y860).
Elevated objects (crossbar) show parallax shifted away from the image centre (to +x here).

## Static markings (frame 0, px)
- Goal line x≈380 (rows y 70–330), 382.4 at y600; posts (white bars seen from above) at y=414.6 and 512.4, so the goal
  mouth is **97.9 px** centre-to-centre (outer frame y 413–514, ≈101 px). Goal frame x 380–409; the bright band
  x≈394–401 is the crossbar displaced by parallax.
- Penalty area: front line x≈163.5 (top) to 166.8 (bottom); top line y≈201.5, bottom y≈727.1, so **525.6 px** along the goal
  line and **≈216.7 px** deep from the goal line.
- Goal area: front x≈309–310.5; top y≈344.7, bottom y≈583.2, so **238.5 px** wide and **≈70.9 px** deep.
- Penalty spot (236.99, 463.04): **≈143.9 px** from the goal line. Penalty arc: leftmost x≈116.1, so radius ≈120.9 px from the
  spot; the arc meets the penalty line at y≈372 and 557.
- Touchlines: top y≈46–49, bottom y≈882.5–884.3, separation ≈836 px (the full pitch width at this end).
- Other items: a dark object (bag?) at ≈(388,408) by the top post; sunlit netting strip x≈432–475, y≈258–668 with
  small white goals at about (452,198), (447,340), (455,632); a neighbouring pitch with a goal at x≈482–522, y≈410–511.
  These are approximate (±5 px). Long diagonal shadows from trees cross the pitch; the players' shadows fall toward +y.

## Sizes of moving objects (px)
- Ball: blob ≈3–4 px wide at half-max (median 4 x 3 px). The ball is barely resolved, so its pixel diameter is unreliable
  (±1 px, i.e. ±30%).
- Yellow player footprint: mask length ≈10–14 px, width ≈7–8 px (varies with stride and arm pose; may include the ball when merged).
- Dark player footprint: ≈13–14 px long; width ≈5–6 px while standing (frames 0–85), ≈9–10 px while walking (86–172).
  The apparent size is constant apart from pose changes (2D, no depth change).

## Events (frame / time s)
- 0 (0.000): ball at rest inside the goal; yellow player behind it inside the goal; dark player standing.
- ~9 (0.30): yellow player reaches the ball (they merge); the ball is nudged ~2 px into the goal over frames 0–10.
- ~20 (0.67): dribble starts. The ball centre crosses the goal line at frame 21 (0.705); it is on the white line in frames 17–21 (low contrast).
- 26 (0.872): yellow player centre crosses the goal line.
- 24–40: ball slow (≈0.5 px/frame); from frame 40 on it moves steadily ≈1.0–1.2 px/frame, mostly −x with a slight −y component.
- 84 (2.82) ±6: dark player starts walking down-left.
- 96 (3.221): ball crosses the goal-area front line; the yellow player crosses it at 102 (3.422).
- 172 (5.771): end. Ball (231.0, 467.6) stabilized; still moving.
No bounces, shots or impacts. The touches during the close dribble aren't individually resolvable.

## Reliability and ambiguity
- Ball: auto-detected as a compact bright blob (luminance +55 over the median background) near a constant-velocity
  prediction, verified on zoomed overlays. Where the ball merges with the player's bright limbs or lies on the goal
  line (frames 10–20, 56–66, 156–158), the positions are hand-read keyframes with linear interpolation (occluded=1);
  error there is about ±1.5 px. At frames 40–42 (source=predicted) the position is extrapolated. Clean frames: ±0.5 px.
- Players: centroid of the body mask (|Δluminance| > 30 against the median background). This excludes the long shadows (Δ ≈ −10 to −27)
  and a 5x5 patch around the ball. The centroid jitters by ±1–2 px frame to frame with limb motion (heavier for the
  yellow player, whose kit is similar to the grass highlights). Smooth over several frames before differencing.
- No metric scale is recorded. For internet-style answers use one scale = prior value / prior pixel value. Good pixel
  references: goal mouth 97.9 px, goal-area width 238.5 px, penalty-area width 525.6 px, penalty spot to goal line 143.9 px.

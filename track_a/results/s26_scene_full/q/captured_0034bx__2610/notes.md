# q_2610 — total distance traveled by the left tennis ball (cm)

The left tennis ball is scene track `tennis_ball_A`. It rests during frames 0–23, is pushed at frame 24, rolls right
(and passes behind the soccer ball from frame 31), hits ball B at frame 38, then drifts back left until frame 48.
question_fps = file fps = 24.

## Scale
- This video is a SAM2-demo output in which the camera image is shown **downscaled** inside the 1280x720 canvas. With the
  card's f = 763 px, a 6.7 cm ball at 0.706 m would be about 72 px across, but it measures about 31 px. So f = 763 does not fit
  these pixels. I took the scale from the prior instead.
- Ball diameter measured from RGB row/column profiles (radial.py): vertical (minor-axis) extent 30–31.5 px at rest and at frame 29
  (t = 1.2 s). The horizontal extent is 32–33 px, which matches the expected off-axis elongation. I used 31 px.
  Scale = Z/f = 6.7 cm / 31 px ≈ 2.16 mm/px at the ball.
- The effective f that reproduces the prior at d = 0.706 m (pp at the image centre) is about 294 px. The horizon is at v ≈ −287,
  from the vanishing point of the table side edges, so the camera tilts down about 65°.

## Path
- Track: scene/ circle-fit centres. Overlays (frames/ov.png) confirm the occluded-cap fits for frames 30–48.
  The 22 px jump at frames 35→36 is real (frame-timing jitter) and counts as distance.
- path2.py: each centre is back-projected onto the plane parallel to the table through the ball centre (anchored at the 0.706 m
  point at t = 1.2 s), and the 3D steps are summed. I smoothed with a 3–5 frame window **separately on each side of the
  collision** (frame 38), so the reversal is not rounded off. Rest frames 0–23 add almost nothing.
- Result (D = 31 px): pre-collision 34.0 cm, post-collision 4.15 cm, total **38.2 cm**. Unsmoothed: 38.7 cm.
  For D = 30 / 32 px: 39.4 / 37.0 cm.
- Second route: a constant-depth scale (pixel path × 2.16 mm/px) gives 38.4 cm (smoothed over the whole clip, sm = 3, frames 24+: 37.2).
  It agrees within 1%. The modelled depth changes only 0.744 → 0.667 m, and the motion is mostly lateral.

## Answer
38.3 cm. Confidence: moderate. The main uncertainty is the ±1 px ball diameter (±3%). The occluded post-collision centres add
about ±0.5 cm. The given depths for the soccer ball and pencil bag do not fit the image geometry (the pencil bag is lower in the
image but listed farther away), so I did not use them.

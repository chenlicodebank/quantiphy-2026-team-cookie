# q_1734 — width of the rock (m)

Prior: person speed 1.3 m/s. depth_info: person 179.09 m (t=1 s), 179.18 m (t=2 s). question_fps = 24, but the file is 25 fps;
frame indices are used and timed at 24 fps.

## Geometry
- The person (scene/tracks/human.csv, checked against frames) walks straight down the image at 1.331 px/frame
  (dx 0.077), i.e. 31.95 px/s at 24 fps. The person looks upright in the image, so the camera has no roll, and moving
  down the image means walking toward the camera on the ground. Over that second the given depth still rises by
  +0.09 m, which can't be the body's own motion. So the character's origin is stuck (the animated-character case),
  and the depth applies only as the person's distance (~179 m, ±1.5 m as the body moves).
- Speed: 1.3 m/s · sinα · f/Z = 31.95 px/s, so f/Z·sinα = 24.6 px/m.
- Gait: projected body height runs from 34 px (feet together) to 44 px (legs spread). With height 1.72 m plus a toe
  offset of 0.12 m, f/Z·cosα ≈ 18. That gives α ≈ 51–54°, f/Z ≈ 30.5 px/m and f ≈ 5460–5640 px. Using the 39 px median
  height instead gives α = 48° and f = 5950 px. Checks: the gait swing (10 px ≈ 0.4 m of foot reach × 24.6 px/m) and
  the torso width (16 px ≈ 0.50 m) are both plausible.
- Camera: pitch ≈ 50°, height ≈ 140 m. Ground-plane model built from the person's position.

## Rock
- Mask (min BGR < 200, holes filled, largest component above y = 680): bbox 557–1256 × 17–642 px. It is static.
- A single view can't separate the rock's depth extent from its height. I fitted ellipsoids that rest on the ground
  plane (vertical axis, free yaw, position and two horizontal semi-axes) to the silhouette for height ratios 0.3–1.3
  and three cameras (fit_rock.py, fit_shade.py). Silhouette IoU ≈ 0.88–0.90 for all of them.
  Shorter horizontal axis: 19.5–21 m (squat rock) and 16–18 m (tall rock). Longer axis: 25–37 m. Lateral extent
  across the view: ≈ 21–23 m. The real mask is ~5 % wider than the fitted ellipsoids (701 px ≈ 23.2 m at ~187 m).
- I tried to use shading to fix the height (sun at 28° elevation from the person's shadow, behind the camera). It
  couldn't: the dark regions are rock colour, not shadow.
- Answer: the shorter horizontal extent ≈ 19 m. This is the middle of the fits (height ratio 0.7–1.0), corrected up
  ~5 % for the ellipsoid underestimating the extents.
- Second route: the lateral image extent (701 px → 22–23 m) is an upper bound if the long axis runs mostly along the
  view, which the fits indicate.

Confidence: low to moderate. The scale is good to ~5 %; the rock's shape and orientation ambiguity adds roughly ±15 %.

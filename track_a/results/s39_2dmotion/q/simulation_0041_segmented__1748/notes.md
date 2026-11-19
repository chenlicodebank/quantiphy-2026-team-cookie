# q1748 — average speed of the person (prior: person height 1.75 m)

The file runs at 24 fps and question_fps is also 24. The person moves from frame 1 to frame 71 (frames 0 and 1 are identical).

## Motion in pixels (measure.py → my_track.csv)
- My own mask track (any channel < 230 in a window around the person) agrees with scene/tracks/person.csv and with
  the SAM 3 track (tracks/person_0.csv) to within about 1 px at every sampled frame. The SAM mask on frame 34 has a box of
  353-372 x 416-455 (19 x 39 px), and my mask is 18 x 39 px, so they agree within 3 pct.
- Net motion of the centroid over frames 1→71 is 1.535 px/frame. The head-top track gives 1.518 px/frame, and a centroid
  smoothed over one step (17 frames) gives 1.519 px/frame. Raw one-frame steps average 1.57 px/frame, but that figure is
  inflated by noise. I use 1.53 px/frame, which is 36.7 px/s. The person walks down the image (toward the camera, face
  visible), with 8 px of drift to the right.
- Gait: the stance foot (the bottom of the box) sits still at y = 429, 454.5, 479 and 505.5. That is 25.4 px per step
  and 16.7 frames per step, so the cadence is 1.44 steps/s (86 per minute).

## Scale: the camera looks down at a steep angle
The person's height in the image is 39–41 px when standing and 50 px with the legs apart. The camera is clearly
oblique, looking down from above: we see the boat's deck and the top of its cabin roof, and the person's body is
foreshortened. So the scale from body height does not apply to motion along the ground.
- A plain 2D scale from height would give 1.75 m / 46 px (median) → 1.39 m/s, or 1.28 m/s using the 50 px maximum. That
  implies a step of about 0.95 m at 86 steps/min, which is implausibly long for a 1.75 m walker (the plateaus show the
  feet are planted, so the stride matches the ground motion).
- Width route (profile.py): across the arms the person is 18 px wide (17.5 px allowing for soft edges). I take
  0.45–0.50 m as the arm-to-arm width of a 1.75 m human, which gives k ≈ 36–40 px/m across the image. The standing height
  in the image is about 40 px, which I model as k(1.75 cos e + 0.30 sin e), where e is the camera's downward tilt. That
  gives e ≈ 61–65°, a ground scale k·sin e ≈ 31.5–36.4 px/m, and v ≈ 1.01–1.17 m/s (about 1.12 at the middle values).
- Body proportions: the head, arm-span and leg segments give a vertical body scale of about 20 px/m. With k ≈ 37.5 that
  means cos e ≈ 0.53, which agrees with a steep view of about 58–63°.
- Gait check: v ≈ 1.1 m/s at 1.44 steps/s means a step of 0.76 m (0.44 × height), which is a normal walking ratio. The
  plain 2D-height reading needs a step of 0.54 × height.

## Answer
1.12 m/s. Confidence is moderate. The pixel speed is solid (±2 pct), but the ground scale depends on the camera tilt and
the assumed shoulder width, so the range is about 1.0–1.2 m/s. If the reference used a plain 2D height scale instead, it
would be about 1.3–1.4 m/s.

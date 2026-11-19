# q_2135: average speed of the toy truck (cm/s). Prior: total sofa height = 90 cm

## Scale (sofa.py, sofa2.py)
- Red sofa HSV mask on frames 0 and 28. Full vertical bbox runs from y=130 (top of armrest) to y=538-541 (base), about 410 px.
  The largest single-column extent is 378-387 px (x≈490-570); at the back-left it is about 362 px.
- I used 395 px, between the column reading and the bbox reading, so scale = 90/395 = 0.228 cm/px (±4 % from this choice).

## Truck motion
- Track: scene/tracks/toy_truck.csv (checked: the box covers the truck). Over frames 0→28 the raw image displacement
  is cx −360 px and front_x −364 px. Motion is horizontal.
- The handheld camera drifts right. My own template-matching check (bgcheck.py) gives these shifts at f28: man's
  shoe on the floor (y≈760) +86 px, floor grout patch (y≈800) +87 px, sofa base (y≈540) +54 px, armchair +44 px.
  These agree with the record's grout fit (87 px at y=765). The truck's wheels touch the floor at y≈725, so I
  interpolated the shift there to about 82 px.
- Displacement relative to the floor ≈ 360+82 = 442 px (cx) or 446 px (front_x) over 28 frames, about 15.9 px/frame.
  The motion is monotone, so the average speed equals net displacement / time.
- Steps alternate between about 20 and 13 px per frame (a frame-cadence artefact). Averaging over the whole clip
  removes it.

## Time base
- File rate 19.68 fps; question rate 24 fps. 19.68 = 0.82 × 24 exactly, so the clip looks re-timed from 24 fps
  footage. Following the question rate and the rule that the reference answers follow the original footage, I used 24 fps.
  Both rates give plausible speeds for a pushed toy (87 vs 71 cm/s), so physics can't decide.

## Result
- 24 fps: 86.3 (cx) / 87.1 (front_x) → **86.7 cm/s**.
- Alternatives: 19.68 fps → 71.1 cm/s. No camera compensation, at 24 fps → 70.7 cm/s.
- Second route: the front edge (front_x) and the box centre (cx) agree within 1 %. The background shift was checked
  by two features (shoe and grout) and agrees with the record's fit.
- Confidence: moderate. The main risks are the fps choice (22 %), the sofa pixel-height reading (±4 %) and whether
  the annotators corrected for camera motion.

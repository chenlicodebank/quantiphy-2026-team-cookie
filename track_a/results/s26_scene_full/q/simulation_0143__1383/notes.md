# q_1383 — speed of the man at t = 1 s (frame 24 at question_fps 24, same as the file fps)

## Scale
- 3D scene, static camera, principal point assumed at (960, 540), camera level (horizon ~538).
- Focal length: from the given depths (7.21 m at f0, 7.91 m at f12) with the man's pixel height (429 and 399 px):
  f = 1716 (f0) / 1743 (f12) for H = 1.8 m, or ~1755-1783 for a walking height of 1.76 m. I used f = 1750 and checked
  1716-1783; the answer changes by less than 1 %.
- Depth per frame: Z = K / height_px, with K = 3113 px·m fitted so that frames 0 and 12 reproduce the given camera
  distances (7.21 / 7.91 m once the lateral and vertical offsets are included). Lateral X = (u - cx)·Z / f, using the
  pelvis estimate from scene/tracks/person.csv (the torso_x column as a cross-check).

## Measurement
- height_px swings with the gait (±3 %), so one-frame differences are meaningless (0.6-5.8 m/s). Steps come every
  ~12 frames: the planted-foot plateaus in feet_y start at frames ~1, 8, 21, 34, 46, 59, 71, 83 and 95. So I compared
  frames exactly one step apart (i, i+12) for every pair spanning frame 24 (i = 12..24), which cancels the gait swing:
  - pelvis: 2.145 ± 0.10 m/s; torso_x: 2.10 ± 0.14 m/s; two-step pairs: 2.06 ± 0.33 m/s.
- Second route (independent depth cue): depth from the ground-contact row, Z = f·hc / (feet_y - 538), with the camera
  height hc = 1.29 m calibrated on frames 0-12. One-step pairs give 2.14 ± 0.13 m/s.
- Check against the given data: the given depths alone give 1.80 m/s over 0-0.5 s. The speed rises over the clip,
  with half-second chunks of about 1.7 → 2.1 → 2.35 → 2.9 m/s, so ~2.1 m/s at 1 s fits.
- Footprint route (positions of the planted foot): the step from ~f8 to ~f21 gives 1.83 m/s and the step from ~f21
  to ~f34 gives 2.17 m/s, so about 2.0-2.2 m/s around t = 1 s.

## Answer
2.12 m/s, a smoothed, step-averaged speed. The reference is a one-frame difference of the root, which may wobble
within the stride by ~±10 %. Confidence: moderate (±10 %).

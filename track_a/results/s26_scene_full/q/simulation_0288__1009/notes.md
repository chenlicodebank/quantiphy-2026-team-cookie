# q1009 – length of the koi fish (m)

2D top-down Blender render, 24 fps (file fps = question_fps, no re-timing).
Prior: fish speed = 0.67 m/s (constant swim).

## Scale from speed
- `speed.py`: per-frame displacement of the template-match track (scene/tracks/koi_fish.csv, match_x/y),
  frames 2–70: 23.53–24.04 px/frame, mean 23.80 px/frame (median 23.78) -> 571.2 px/s.
  (Frames 0–1 and 70–71 are holds and are excluded.)
- Scale = 0.67 / 571.2 = 1.173e-3 m/px.
- Body-mask centroid track gives 23.3 px/frame, but it jitters and drifts as the body bends; the match track was used.

## Pixel length
- Record's manual nose-to-tail-tip lengths: 670, 661, 658, 652, 661, 663 px at frames 12–71 (mean 661 px).
- My own check on gridded crops: frame 24 nose x≈1504, tail tip x≈2162 -> 658 px; frame 60 nose x≈665,
  tail tip x≈1329 -> 664 px. Consistent; fish axis is within ~10° of the x axis, so bbox length ≈ 661 px.

## Answer
Length = 661 px × 1.173e-3 m/px = 0.775 m.
Check: using the body-centroid speed (23.3 px/frame) would give 0.79 m (+2 %), so the result is not sensitive to the choice of track.
Confidence: good (±3 %), limited by the edges of the translucent nose and tail tip.

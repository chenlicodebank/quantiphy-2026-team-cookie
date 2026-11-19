# Q332 – length of the house (m)

2D Blender scene, static camera, 60 fps (file fps = question_fps, no re-timing). Prior: bird speed = 9.146 m/s.

## Scale from the bird's speed
- Bird track (scene/tracks/bird.csv, ref point = eroded-mask centroid) checked: speed is nearly constant along the
  arc. Per-frame displacement: mean 19.84 px (frames 4–99), 19.74 px (frames 18–99, avoiding the sun-blend frames);
  3- and 5-frame chords 19.7–19.8 px; a cubic fit of the path gives 19.74 px/frame (19.5–20.4 across the clip).
- Speed ≈ 19.74 px/frame × 60 = 1184 px/s → scale = 9.146 / 1184 = 0.007724 m/px.

## House length
- Measured in code (measure.py) on frame 99: the roof eaves span x 574–1419 → 846 px (widest row y≈680–684);
  front wall x ≈ 609–1385 → ~776 px. The house faces the camera, so its length is the horizontal image extent.
- World AABB includes the roof overhang: 846 px × 0.007724 = **6.53 m**.
- Alternative reading (walls only): 776 px → 5.99 m.

## Check
Scale from mean of per-frame speeds over frames 4–99 (19.84 px/frame) gives 6.50 m; from fit 6.53 m — agree within 0.5 %.
Confidence: moderate-high (main uncertainty: whether the reference used eaves or walls, ~8 %).

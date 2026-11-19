# q_981 — width of the whale (m)

2D top-down (orthographic-looking) Blender render, 24 fps (file fps = question_fps; no re-timing).
Width = shorter horizontal extent of world AABB = image y-extent (pectoral fin tip to fin tip), since the view is from above.

## Scale (from prior: speed 1.67 m/s)
- Blowhole (body-fixed, rigid translation) track from scene/tracks/whale.csv, verified with measure.py:
  linear fit frames 1–71 slope -5.8709 px/frame = 140.90 px/s; mean per-frame speed 140.87 px/s (constant speed).
- Scale = 1.67 / 140.9 = 0.011852 m/px.

## Width in pixels
- bbox_h (sharp silhouette edges, shadow excluded): frame 0 = 643 px (frames 0 and 1 identical = rest/initial pose),
  min 639 (f71), max 783 (f24), clip mean 725. Fins flap, so the extent oscillates.
- Independent gradient-edge check (measure.py) gives 652 at f0, 796 at f24 — a few px larger because it includes the soft drop shadow below the fins; consistent with the csv.

## Values
- Frame 0 / rest pose: 643 px -> 7.62 m
- Clip mean: 725 px -> 8.60 m; max 783 -> 9.28 m; body width without fins ~320 px -> 3.8 m
- Answer: 7.75 m (initial pose, nudged slightly toward the clip mean to hedge the pose ambiguity).

Confidence: scale is solid (±0.5%); main uncertainty is which pose the reference AABB used (±10%).

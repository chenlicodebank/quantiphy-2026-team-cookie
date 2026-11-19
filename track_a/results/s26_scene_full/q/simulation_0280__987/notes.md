# Q987: height of the whale (m). Prior: whale length = 19.17 m

Setup: a 2D side view with a static camera and one whale swimming right to left, 24 fps (file rate = question rate). The question gives no time,
and the whale's pose is animated (the tail beats, the flippers swing), so its vertical bounding-box extent changes over the clip.

Scale: the whale's full length in pixels is the bbox width while the body is nearly straight (frames 49-53, whole whale
in view), median 3451 px (axis_len agrees: 3450-3453). That gives 19.17 / 3451 = 0.005555 m/px.

Height: the vertical extent of the whale mask, flippers and fluke included (scene/tracks/whale.csv bbox_h). I checked the
mask against frame 0 visually: the top of the back is at y≈591 and the flipper tip at y≈1509.
- Frame 0 (t = 0): 919 px -> 5.10 m
- Median over all 72 frames: 900 px -> 5.00 m
- Second route, each uncut frame's own h/w ratio x 19.17 (median): 5.08 m
- Straight-body frames 49-53: 786 px -> 4.37 m. Clip range: 4.11-7.18 m (the tail is raised at the end of the clip).

Answer: 5.05 m, between the frame-0 value and the clip median and close to the per-frame-ratio check. Script: measure.py.
Confidence: moderate. The pose changes the height a lot, so the result depends on which frame or pose the reference used.
If the reference used a straight rest pose, it would be about 4.4 m.

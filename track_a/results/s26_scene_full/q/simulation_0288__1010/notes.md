# Q1010 – width of the fish (m)

2D top-down simulation, 24 fps (file fps = question_fps, so no re-timing). The camera is static.

## Scale from the prior (fish speed 0.67 m/s)
- `speed.py`: the template-match track in scene/tracks gives 23.80 px/frame (mean of frames 2–70, median 23.78; range 23.5–24.0)
  → 571.2 px/s → **1.1729e-3 m/px**. Frames 0–1 (still) and frame 71 (a repeated frame) are excluded.
- Cross-check: the net body-centroid shift from frame 2 to 70 is 23.3 px/frame (lower because the path is S-shaped and the body
  bends). The match track is the better per-frame speed.

## Width in pixels
Width = the shorter horizontal extent of the world AABB. Seen from above, that is the extent across the body,
including the pectoral fins (bbox height in the image, since the fish swims along x).
- Manual record (scene/notes.md) at frames 12–71: 231, 253, 262, 229, 237, 240 px (median about 239).
- Own code check (`finrows.py`): row extent of |frame − clean background| with shadow pixels excluded, at frames
  12/24/36/48/60/66: 240, 256, 232*, 238, 240, 232 px → median 239. (*At frame 36 the lower fin over the shadow is
  partly lost.) The record and the code agree at about 240 px.
- An eye check at frame 60 gives fin tips at y ≈ 610 and 847 → 237 px.

## Answer
240 px × 1.1729e-3 = **0.281 m** (range 0.27–0.31 over the frames, because the fins move).
Other reading: the trunk alone, without fins, is about 145–155 px → about 0.17–0.18 m. I did not use it, because the AABB includes the fins.
Confidence: moderate-high on the scale (±1 %). The width varies about ±5 % with the fin pose.

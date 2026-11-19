# q_2536 — distance white ball ↔ tennis ball at 1.6 s (cm)

- question_fps = file fps = 24 → t = 1.6 s is frame round(38.4) = 38. Both balls roll on the table there.
- Camera: lab card f = 0.5959 × 1280 = 762.75 px, principal point (640, 360).
- Centres (measure.py, re-measured with the same masks as scene/; checked on a zoomed crop frames/f38.png):
  tennis (738.5, 452.5) px, 54 px wide; white (662.0, 444.0) px, 25 px wide. These agree with scene/tracks.
- Depths from depth_info: tennis 1.190 m, ping-pong/white 0.994 m.
- Back-projection and 3D distance at frame 38:
  - depth treated as Euclidean range (unit ray × depth): 22.4 cm
  - depth used as z (ray (x, y, 1) × depth, as the method card says): 23.5 cm
  Most of the distance comes from the 0.196 m depth difference; the lateral part is only about 10 cm.
- Second check: frames 36–40 give 22.35–22.49 (Euclidean) and 23.44–23.66 (z), so the result holds across nearby frames.
- Answer: 23.0 cm, between the two depth conventions (within about 3% of either).
- Caveat: the given depths don't match the pixel sizes. A 6.7 cm ball 54 px wide would be at 0.95 m, not 1.19 m.
  The white ball also sits higher in the image (farther back on the table), yet depth_info puts it closer.
  As instructed, I used the given depths. Confidence: moderate, since the answer depends on depth_info as given.

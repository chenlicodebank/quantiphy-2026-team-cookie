# Q391 – length of the bike (m)

Prior: bike speed 5.52 m/s; fps 24 (file and question_fps agree). The clip is treated as 2D: the cyclist moves left to right, parallel to the image plane, and the camera is static.

- Pixel speed: a linear fit of the cyclist's ref_x (scene/tracks/cyclist.csv, frames 6–76) gives 21.02 px/frame. The mean per-frame step is 21.02 too (`measure.py`).
- Scale: 5.52 / 24 / 21.02 = 0.010941 m/px.
- Bike length: I measured the span of dark tyre pixels (rows 680–748) in code at frames 45, 50, 55 and 60, near the image centre. The result was 161 px every time (for example, x 821–981 at frame 45). The basket and handlebar lie inside the tyre span, and the zoomed frame `frames/f45.png` confirms this. The scene record gives 163 px for the same span (±2 px). Frame 40 was discarded because occluders contaminate it.
- Length ≈ 161.5 px × 0.010941 = 1.77 m.
- Check: the scene record's size (163 px) gives 1.78 m, and a real bicycle is about 1.7–1.8 m, so the result is plausible. Confidence: high (about ±3 %).

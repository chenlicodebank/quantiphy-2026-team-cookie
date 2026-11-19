# Q893: width (longer side) of the AC

The scene is 2D: the camera is static and faces the wall. I used one metres-per-pixel scale, taken from the pen's free-fall acceleration (prior: 9.8 m/s²).
The file plays at 24 fps, but the question states 30 fps. Following the benchmark convention, I timed everything at question_fps = 30.

## Measurements (`measure.py`)
- **Pen acceleration:** I fitted a quadratic to the pen-centre cy for frames 3–15, the free fall before the first impact at about frame 16.
  - The result is 6.868 px/frame². Fits over other frame windows (4–15, 3–13, 5–14) and fits to the top or bottom bbox edges give 6.83–6.90.
  - At 30 fps this is 6181 px/s², so the scale is 9.8 / 6181 = 1.585 mm/px.
- **AC width:** I measured the strongest-gradient edges on frame 36, on rows y = 770, 800 and 850, which are above the table.
  - The edges are at x = 131.5 and 637.5 on all three rows, so the width is 506 px.

## Answer
506 × 1.585e-3 = **0.802 m**

## Checks
- **Plausibility:** a real LG outdoor unit is about 0.77–0.87 m wide, so 0.80 m is consistent.
- **Pen length:** 65.3 px gives a pen length of 0.104 m. That is plausible, though a little short for a pen.
- **If the file's 24 fps were used instead:** the scale would be 2.477 mm/px, giving an AC of 1.25 m and a pen of 0.16 m.
- **Depth caveat:** the AC sits behind the table, at roughly the same depth plane as the wall, so it may be slightly farther from the camera than the pen. The scene is treated as 2D and I made no perspective correction.

Confidence: moderate to good (about ±5%). The main risk is the time-base convention.

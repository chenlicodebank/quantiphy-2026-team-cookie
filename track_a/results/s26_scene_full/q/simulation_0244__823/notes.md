# Q823: speed of the rabbit (m/s). Prior: antelope speed = 1.277 m/s

The scene is a 2D render with a static camera. The antelope (the "creature" in scene/) and the rabbit both move left to right at the same depth (feet at y ≈ 1547), so one m/px scale applies to both. Both move steadily for the whole clip, so the answer is rabbit_px_speed / antelope_px_speed × 1.277. I used fps = 30, which is the same as question_fps.

## Main route: whole-body matching at the same gait phase (match2.py)
- I built a background plate (frame 0 for x ≥ 540, frame 74 for x < 540, and a median in the rabbit's frame-0 box). From it I made foreground-only images.
- I took a template of each animal at frame a, matched it against later frames, and kept the best match, which is the frame at the same gait or hop phase. I refined the match peak to sub-pixel.
- **Rabbit:** a 39-frame cycle gives 261.2–261.5 px (6.70 px/frame). A 52-frame cycle gives 348.9–349.8 px (6.71–6.73). Mean ≈ **6.71 px/frame**.
- **Antelope** (body and head, mostly without the tail): a 40-frame cycle gives 261.0–262.1 px over 10 starting frames, so **6.54 px/frame** (range 6.53–6.55).
- Ratio = 1.026, so the rabbit's speed is 1.277 × 1.026 = **1.31 m/s**.

## Second route: the record's tracks (linear fits)
- Rabbit: mask centroid slope 6.71 px/frame and bbox-centre slope 6.71 (frames 0–69).
- Antelope: shoulder-landmark slope 6.61, hip 6.76, body_mid 6.22. These patch landmarks drift with the gait. That would give a rabbit speed of 1.30 m/s using the shoulder, or 1.27 using the hip.
- The whole-cycle match is the most consistent measurement, with a spread of about 0.2%, so I prefer it.

## Answer
**1.31 m/s.** Confidence is good. Across the different antelope reference points, the uncertainty is about ±2%.

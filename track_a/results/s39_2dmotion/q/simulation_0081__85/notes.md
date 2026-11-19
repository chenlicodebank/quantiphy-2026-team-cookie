# Q85: speed of the bike at 0.5 s (m/s)

Prior: the bike is 1.7 m long. This is a 2D top-down render. The file runs at 24 fps and question_fps is also 24, so t = 0.5 s is frame 12, and the speed is the backward difference from frame 11 to frame 12.

## Measurements (measure.py, own HSV cyan mask of the bicycle, per frame)
- **Bike pixel length at frame 12:** 381 px (frame 11: 382 px). Over the clip it runs from 376 to 386 px, a slight perspective trend. The value near frame 12 is used.
- **SAM 3 "bicycle" mask:** 380 px at frames 11 and 12 (box x 1046.6–1426.8 at frame 12). This is within 0.3% of my own mask, and the overlay covers the whole bike from front wheel to rear rack.
- **Bike motion:** the bike moves left at a constant speed. A linear fit over frames 2–28 gives:
  - bbox centre: −47.42 px/frame (residual sd 0.55 px)
  - front tip: −47.25 px/frame
  - rear tip: −47.59 px/frame
- **Raw 11→12 steps:** centre 46.5, front tip 46, rear tip 47 px.
  - SAM centre: 1282.5 → 1236.5 = 46.0 px.
  - These are within the 1 px quantisation of the constant fitted value.
- **Held first frame:** frames 0 and 1 are identical. This does not affect frame 12.

## Result
- Scale: 1.7 / 381 = 0.004462 m/px.
- Speed: 47.42 px/frame × 24 = 1138 px/s, which gives **5.08 m/s**.

## Second-route check
- Raw one-frame step: 46.5 px gives 4.98 m/s.
- Rear-tip fit: 5.10 m/s.
- Using the SAM length of 380 px: 5.09 m/s.

All routes fall within about 2%.

Confidence: high (about 2%).

# Q335: height of the man (m)

The prior is walking speed = 1.693 m/s. This is a 2D side-view walk at constant depth, so I used one m/px scale. fps = question_fps = 24.

- **Pixel speed:** the record's pelvis track has a mean per-frame step of 18.78 px/frame, and a linear fit gives 18.88 px/frame. My own head-x fit (measure.py, background difference, every 5th frame) gives 18.89 px/frame. I used ~18.85 px/frame = 452.4 px/s, so the scale is 1.693 / 452.4 = 0.003742 m/px.
- **Pixel height:** the standing (head-high) frames give head top y ≈ 414 and sole y ≈ 905, so 492 px. The record shows this at frames 0, 25 and 74. My re-measurement gives 492 px at frame 50 and 491 px at frame 74, and a zoomed crop of frame 25 is consistent. Frames 0, 12 and 25 in my quick mask were contaminated by background artefacts, so I disregarded them.
- **Height:** 492 × 0.003742 = 1.841 m (1.838–1.847 depending on which speed estimate is used). The peak height while walking is usually slightly below the rest standing height (knees not fully straight), so I rounded up a little: **answer 1.85 m**.
- **Second-route check:** the endpoint speed (18.78 px/frame) gives 1.847 m and the fitted speed gives 1.838 m, which agree within 0.5 %.
- **Confidence:** good, within about 3 %.

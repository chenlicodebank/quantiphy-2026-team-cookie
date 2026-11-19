# Q969: raccoon speed at 1.0 s (frame 24)

- 2D top-down render with a static camera, at 24 fps (file rate = question_fps, so no re-timing). The raccoon walks in a straight line toward +x.
- Scale comes from the prior (length including the tail = 1.51 m). In `measure.py` I took the raccoon's horizontal extent from tail tip to nose in the band y 712–765, using background subtraction. The median over frames 2–71 is 298 px (range 283–304; frames 16–33 give 289–303). The scene record's median is 296. I used 297 px, so the scale is 0.005084 m/px.
- Speed: the root step (template tracking from the scene record) into frame 24 is 20.33 px. My phase-correlation step into frame 24 is 20.76 px. The motion is steady: the mean root step is 20.58 px/frame, and linear fits of the nose and tail tip give slopes of 20.45 and 20.54 px/frame. The per-frame jitter of about ±1 px comes from the gait. The rig origin moves at a constant speed, so I used about 20.55 px/frame.
- Speed = 20.55 × 24 × 0.005084 ≈ 2.51 m/s.
- Second route: the nose and tail-tip slopes (independent of the root track) give 2.49–2.51 m/s, which agrees.
- Confidence: good, about ±3%. The main uncertainty is the pixel length used for the prior (±2%).

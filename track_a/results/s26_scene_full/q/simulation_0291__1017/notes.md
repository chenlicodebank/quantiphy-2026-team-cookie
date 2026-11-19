# q_1017 – length of the fish (m)

2D side view, static camera, 24 fps (file fps = question_fps). The fish translates along −x only.

Scale from prior (speed 0.67 m/s):
- ref_x track (head-template shifts, ±0.1 px): mean |dx| over the moving frames 2-70 = 22.45 px/frame = 538.9 px/s
  -> 1.243e-3 m/px.
- If the two held frames (1, 71) are included: 523.7 px/s -> 1.279e-3 m/px, which makes the length about 3% longer.

Pixel length, snout to tail tip, frames 5-71: median bbox_w 583 px, mask main axis 579 px. A zoom of frame 30 shows
the faint snout/barbel region about 10-20 px left of the mask edge, so the true extent is about 590 px.

Length = 590 x 1.243e-3 = 0.733 m. Range under the other choices: 0.72 (axis, moving frames) to 0.75 (bbox, all
frames).
Answer: 0.73 m. Confidence: moderate-high (±4%).
Script: measure.py

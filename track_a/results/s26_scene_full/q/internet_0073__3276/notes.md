# q 3276: width of the red package (m); prior: conveyor belt speed = 0.3 m/s

## Method (internet video convention: one scale from the prior)
- Scale = 0.3 m/s ÷ belt pixel speed. The belt's pixel speed was measured in background (frame-0) coordinates
  from scene/tracks, with the camera drift removed (`speed.py`). I fitted a line to each fully visible parcel
  over frames 0-137:
  red 1.961, white_box 2.003, white_pouch_left 2.003, flat_white_pouch 2.011, cardboard 1.967, grey 1.942,
  blue 1.928 px/frame. I used **1.96 px/frame**, which matches the red parcel itself and the median of the rest.
  (The image-coordinate speed without the drift correction is about 1.78 px/frame.)
- Red-package width means its horizontal extent along the belt, as seen in the image (bumper-to-bumper style).
  I measured it in code with a red-dominance mask (`measure_red.py 15`, masks in frames/mask0.png and
  frames/mask100.png) every 10 frames. The full extent is 90-98 px (median 94) and the widest mid-height rows are
  88-94 px. The scene record gives 93 px. I used **92 px**.
- Time base: the file is 25.11 fps and question_fps is 30. `steps.py` shows no periodic doubled steps, so the
  clip was not resampled from 30 to 25 by dropping frames. There is a single doubled step at frame 54. Frames
  are consecutive capture frames, so the clip was probably re-timed. I could not tell the two rates apart
  physically (both give plausible parcel sizes), so I followed the question's stated rate of 30 fps, as for the
  original footage.

## Result
- 30 fps: 1.96 × 30 = 58.8 px/s, giving 0.3/58.8 = 0.00510 m/px. Width = 92 × 0.00510 = **0.469 m**.
- 25.11 fps (alternative): 0.561 m.
- Other readings: the vertical extent is about 46 px, which gives 0.23 m.
- Second-route check: the per-frame pixel speed from the scene record's fitted tracks agrees with my mask
  centroid motion (409.5 → 653.5 px image-x over 137 frames, plus about 0.12 px/frame drift, giving about
  1.90-1.96 px/frame). The width is stable at about 92-94 px across all frames.
- Confidence: medium. The main uncertainty is which frame rate the reference used (±18%).

# q1030 — butterfly wingspan (width), simulation_0296

The scene is 2D, viewed from directly above, and the camera is static. The butterfly flies to the left with its wings spread up and down in the image, so its width (wingspan) is the vertical pixel extent when the wings are flat. The rate is 24 fps: the file and the question state the same rate.

## Scale from the prior (speed 0.32 m/s)
- **Template matching** (`match.py`): I took the butterfly's bounding box from one frame and found it in a frame at the same wing-beat phase, one or two periods (21 frames) later. The results were:
  - frames 18→39, 39→60 and 19→40: −323 or −324 px in x and +3 or +4 px in y over 21 frames, which is **15.38–15.43 px/frame**.
  - frames 18→60 and 1→43: about 647 px over 42 frames, which is **15.36–15.43 px/frame**.
- **Second route** (the record's ref-point track): the net displacement over frames 1→71 is 15.62 px/frame, and over frames 18→60 it is 15.41 px/frame. The per-frame steps are noisy (12–18.5 px) because the bounding-box centre shifts as the wings fold.
- **Speed used**: 15.40 px/frame × 24 = 369.6 px/s.
- **Scale**: 0.32 / 369.6 = 8.66e-4 m/px.

## Wingspan in pixels
- The record's `extent_y` over the open plateaus is 254–261 px, and frame 18 gives 261.
- On a zoomed grid view of frame 18, the wings run from y ≈ 593 to y ≈ 852, which is about 259 px.
- I used **258 px**, with an uncertainty of about ±3 px.

## Answer
- 258 × 8.66e-4 = **0.223 m**.
- Using 15.62 px/frame instead gives 0.220 m, and using 261 px gives 0.226 m.
- The spread is about ±2%. Confidence is high.

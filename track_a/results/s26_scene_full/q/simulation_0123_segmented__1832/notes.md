# q_1832 — length of the rolling cup (m)

The video is a 2D top-down view at 24 fps (question_fps is also 24, so no re-timing). The "rolling cup" is the teal object.
It is a cylinder lying on its side and rolling to the right (+x), so its axis runs along image y.
Seen from above it is 78 px along y (the axis, which is the cup's length) and 42 px along x (its diameter).

## Scale from the prior (speed 0.338 m/s)
- I tracked the HSV mask centroid in all 72 frames (`measure.py`). From frame 2 on the motion is uniform.
  - A linear fit of x over frames 3–71 gives 14.536 px/frame.
  - The mean of the per-frame |dx| is 14.534 px/frame.
  - Both agree with the scene record (14.536).
- Speed: 14.536 × 24 = 348.9 px/s.
- Scale: 0.338 / 348.9 = 9.688e-4 m/px.

## Size
- The mask's y extent is exactly 78 px in every frame (bbox and half-max profile agree, and it is the same at rest and while moving).
  Motion blur only affects x.
- Length = 78 × 9.688e-4 = **0.0756 m**.
- Other reading, for reference: the diameter (x extent at rest, 42 px) is 0.0407 m. By the named-size rule, length is
  the longer horizontal extent, so the answer is 78 px.

## Checks
- The per-frame mean speed and the linear fit agree to 0.01%. The y extent is stable over all frames (±0 px).
- A soft darkness-profile measure was contaminated by the sinks, so I discarded it.
- Confidence: high. The uncertainty is about ±1 px in 78, about 1.3%.

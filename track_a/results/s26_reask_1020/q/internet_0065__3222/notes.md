# q3222: ball velocity at 0.30 s

**Answer: 2.68 m/s.** Confidence is moderate. The scale assumption carries roughly ±5% uncertainty.

## Scene
- A handheld phone looks straight down at a gym floor.
- A basketball rolls horizontally from left to right at almost constant speed. It does not bounce or fall.
- The file runs at 30 fps, the same as question_fps. So t = 0.30 s is frame 9.

## Scale
- The prior is gravity, 9.8 m/s². The clip shows no vertical motion in which gravity acts, so the prior gives no usable scale.
- Instead, the scale comes from a regulation basketball. I assumed size 7, diameter 0.239 m.
- The ball's pixel diameter is 258 px. That is the median vertical extent, which has no motion blur, from the scene record. I checked it on a zoomed crop of frame 9: about 253 px vertically, and about 260 px horizontally including blur.
- Scale: 0.239 / 258 = 9.26e-4 m/px.

## Velocity
- Track: `cx_est_stab` / `cy_est_stab` from the scene record. These are camera-stabilised ball centroids. The camera drift is small: about 0.3 px/frame in x and up to 3 px/frame in y.
- Forward difference from frame 9 to frame 10: 95.9 px/frame, or 2.67 m/s. The raw, unstabilised track gives 95.5 px/frame.
- Backward difference from frame 8 to frame 9: 93.6 px/frame, or 2.60 m/s.
- Linear fits of position against frame number:

| Frames | Speed (px/frame) | Speed (m/s) |
|---|---|---|
| 7–11 | 96.7 | 2.69 |
| 6–12 | 97.6 | 2.71 |
| 5–21 | 98.0 | 2.72 |

- **Answer:** about 2.68 m/s, between the forward difference and the local fits.

## Sensitivity
- If the diameter is taken as the blurred length of about 270 px, the answer becomes about 2.57 m/s.
- If the ball is size 6 (0.232 m diameter), the answer becomes about 2.60 m/s.

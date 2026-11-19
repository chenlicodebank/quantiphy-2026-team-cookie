# Q734: height of the black cat including its tail (m). Prior: chalkboard length = 5 m

This is a 2D scene with a static camera, so I used one metres-per-pixel scale from the chalkboard. fps is 24, the same
as question_fps, so no re-timing was needed.

## Chalkboard (board.py, frame 0, row and column intensity profiles)
- Outer frame: left edge x ≈ 318.5, right edge x ≈ 1691, so **≈1372 px**. Green surface: x 342 to 1670, so 1328 px.
  This agrees with the scene record.
- The whole chalkboard object, frame included, is taken as the 5 m length: 5/1372 = 0.003644 m/px. If only the green
  surface were meant, the scale would be 0.003765 m/px, about 3 % more.

## Cat height (catdiff.py, catheight.py, paws.py)
- Segmentation: the difference from frame 49, where the cat has moved away from x < 450, blurred, with thresholds of
  3.5, 4.5 and 6. In frames 0–6 the rear body, the raised tail and the legs separate clearly (frames/diff0.png and
  diff3.png). The head is lost in the haze, but the tail tip is far above the ears: paws to ears is about 110 px.
- Tail tip top: y = 595–597 in frames 0–6, then 600–605 in frames 7–10 as the tail lowers.
- Paw bottom: in the row profiles of the difference, the signal falls from about 14 to the noise floor (about 4) at
  y ≈ 742–743. The paws stand on the ledge at about 743.
- Height ≈ 742.5 − 596.5 ≈ **146–147 px**. The scene record gives about 148 px, a second check that agrees.

## Result
- 146.5 px × 5/1372 = 0.534 m with the outer frame. With the green surface only, it is 0.552 m.
- The cat stands on the ledge, perhaps slightly in front of the wall, so if anything it would look a little large.
- **Answer: 0.54 m.** Confidence is moderate, about ±4 %. The main uncertainties are whether the board length includes
  its frame, the faint paw edges (±2 px), and the tail pose varying from frame to frame.

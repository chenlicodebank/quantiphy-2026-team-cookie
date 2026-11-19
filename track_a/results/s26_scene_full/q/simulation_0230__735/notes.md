# q_735: average speed of the black (dark-grey) cat, start to end (m/s)

Prior: chalkboard length = 5 m. No depth_info. fps = question_fps = 24, so no re-timing. 50 frames (0–49).

## Scale (2D, single m/px)
- Chalkboard outer frame spans x 320–1692, which is **1372 px** (green surface 1328 px), from scene/ and checked on the
  frame-0 grid view. The object's bounding box includes the frame, so I used 1372 px. Scale = 5/1372 = 0.003644 m/px.
- Sanity check: the cat's nose-to-rump length of 163 px works out to 0.59 m, which is plausible.

## Cat motion
- The cat walks steadily left→right along the ledge under the board. There is no stop or turn, and its vertical motion
  is negligible, so the mean of the per-frame speeds ≈ net x-displacement / 49 frames.
- scene/ track: ref_x goes from 274.5 (frame 0) to 713.5 (frame 49), so 439 px, or 8.96 px/frame.
- My own checks (`view_ends.py`: background-difference images at frames 0, 12 and 49, in frames/e*.png):
  - Rump/tail base: x≈198 at frame 0 and ≈303 at frame 12, so ≈8.8 px/frame.
  - Nose: ≈466 at frame 12 and ≈797 at frame 49, so ≈8.95 px/frame.
  - Lag-10 shift correlation (`track_cat.py`) gives 8.5–9.1 px/frame. It is biased slightly low because the median
    background is contaminated by the cat.
- Adopted value: 8.9 px/frame, i.e. 213.6 px/s.

## Answer
213.6 px/s × 0.003644 m/px = **0.78 m/s**. Using the green-surface width instead would give 0.80 m/s.
Confidence: moderate-high, about ±4%. The main uncertainties are which board extent is "length" and the low contrast of
the cat.

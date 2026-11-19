# q2836 – soccer ball velocity at t = 0.5 s (frame 12 at question_fps 24 = file fps)

## Finding
At frame 12 the soccer ball (white with black pentagons, at about (155, 614) px, ~66 px across) is **at rest on the floor
under the seated person's left hand**. The person pushes it only from about f23–24 (see scene/notes.md and frames/f12.png).
So its true velocity at 0.5 s is close to zero. The prior (basketball 2.21 m/s at 0.5 s) is about a different ball.

## Depth / scale
depth_info does not give a distance to the soccer ball. The camera distances (3.07 m and 3.04 m at t = 1.0 s) belong to the pale and
yellow balls in flight near the back wall: their image positions at f24 and their pixel sizes are consistent with that. I estimated
the soccer ball's depth from its 66 px diameter and an assumed ball diameter of 0.19–0.22 m. With f = 763 px that gives Z ≈ 2.2–2.5 m,
so 1 px/frame ≈ 0.07 m/s.

## Measurement (track_soccer.py)
I tracked the ball's lower half, below the hand, by template matching against f12 with sub-pixel peak fitting:
- f4–f10: steady offset of about (+1.9, −0.8) px.
- f10 → f12: drifts about 2 px left (the hand rocks it).
- f12 → f15: about 0.9 px in total.

| Route | Speed | Velocity |
|---|---|---|
| Mean per-frame speed, f10–15 | 0.60 px/frame | ≈ 0.045 m/s |
| Net displacement f10–15 (smoothed, like the reference) | 0.32 px/frame | ≈ 0.024 m/s |
| Backward difference f11 → f12 | 1.15 px | ≈ 0.09 m/s |

## Answer
I answer 0.05 m/s: essentially at rest, with a small motion from the hand.

**Confidence: low.** The true value is near zero, and any relative-error score depends on how the reference
clicks were smoothed.

# Q2336 — soccer ball diameter (cm)

Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959 x 1280 = 762.8 px.
depth_info: soccer ball 2.80 m (no time given; the ball's apparent size stays almost the same throughout, so its depth hardly changes).

## Pixel diameter (measure.py: non-white mask, thresholds 20/40/60, largest component with holes filled)
- Frames 0-25, ball held: the mask merges with the hand, so width is unusable. Vertical extent = 44-46 px (45 at thr 40).
- Frame 31 (isolated, just released, slow): width 43, height 47-48.
- Frame 34: width 43. Frames 41-48 (slow rise after bounce): widths 44-47, heights 46-51 (some blur).
- Equivalent-area diameter on slow frames: 45-47 px. Pale panels sometimes blend into the white background (width 43).
- Adopted D = 45 px (spread about ±1.5 px).

## Size
D = 2.80 m x 45 / 762.8 = 0.165 m = 16.5 cm (range 15.8-17.2 cm for 43-47 px).

## Checks
- The left person (3.13 m) is 404 px tall (from scene record) -> 1.66 m, a plausible height, so the f/depth scale is consistent.
- The prior (g = 9.8) is not needed for a size. The fall is blurred and has a dropped frame at 35->36, so it gives no better scale.
- The real-world sanity check fits a small (size-1/2) ball.

Confidence: moderate-high, about ±4%.

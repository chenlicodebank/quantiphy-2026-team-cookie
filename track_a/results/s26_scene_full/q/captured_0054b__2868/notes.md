# q_2868 – soccer ball diameter (cm)

Lab video, 1280x720, 24 fps (the file and the question use the same rate). f = 0.5959 x 1280 = 762.8 px.
depth_info: soccer ball at t = 2.0 s (frame 48) is 3.254 m from the camera.

## Pixel diameter at frame 48
At frames 46–48 the ball is drawn as a flat grey disc (154,154,154) on the purple floor. The record's mask
(37–39 px) is too small. It drops the soft rim of the disc.
- `measure3.py`: rays cast from the disc centre (180 rays). Each edge point is where the colour distance from the
  disc colour crosses a threshold. A robust circle fit follows; the overlay is in `frames/ray48.png` and fits the
  disc well.
  - Frame 48 diameter: 40.8 / 42.1 / 42.2 / 43.9 px at thresholds 6 / 8 / 10 / 14. The floor contrast is about 20–25,
    so the half-contrast edge is at about 11, which gives **≈ 42.8 px**.
- `measure2.py`: colour-distance masks and centre-line profiles. The half-contrast crossings give about 44 px wide
  and about 43 px tall at frame 48.
- Trend check: the real ball's circle fit (`measure.py`, `frames/fit45.png`) gives 46.2 px at frame 44 and 47.9 px
  at frame 45. The disc gives 45.1 px at frame 46, 44.4 at frame 47 and 42.2–43.9 at frame 48. The ball is rolling
  away, so the diameter shrinks smoothly, which matches about 43 px at frame 48.

## Result
Diameter = 3.254 m x 42.8 px / 762.8 px = 0.1826 m ≈ **18.3 cm**. The plausible pixel range of 42–44 px gives
17.9–18.8 cm.

## Checks and caveats
- An 18.3 cm ball is plausible for a small (size 3) soccer ball.
- The orange-ball depth_info is not self-consistent with the basketball's apparent size: about 75 px at frame 12
  gives 22 cm, but about 62 px at frame 24 gives 14.7 cm. So no cross-check of the scale was possible from the other
  balls. The answer relies only on the soccer ball's own depth at t = 2.0 s.
- Confidence: moderate. The main uncertainty is the edge of the disc (±1 px, about ±2.5 %) and the given depth.

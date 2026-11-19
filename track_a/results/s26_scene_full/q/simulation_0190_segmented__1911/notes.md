# Q1911 — speed of the box at t = 1 s (frame 120, fps 120 = question_fps)

2D clip: the truck body rises vertically and carries the cardboard box on top (camera is static).
- Scale: box width is 1.33 m. The box measures 278–280 px wide across the clip (scene record, plus my own mask
  in measure.py, median row width 280). I used 279 px, so 0.004767 m/px.
- Motion: the box moves rigidly with the container. I used the container's subpixel template offset (container_dy, ±0.1 px)
  because the box's own bbox centre is distorted by its foreshortening top face.
  - Quadratic fit over frames 5–400: v(1 s) = 18.99 px/s, a = 8.1 px/s².
  - Local quadratic fit over frames 100–140: 19.08 px/s.
  - Second route, box bbox: the box-centre fit gives 18.3–18.6 px/s and the box-bottom fit 19.7 px/s.
    These agree within about 4 %.
- Speed = 19.0 px/s × 0.004767 = 0.0906 m/s.

Confidence: good (about ±4 %). The main uncertainty is the box-width pixel scale.

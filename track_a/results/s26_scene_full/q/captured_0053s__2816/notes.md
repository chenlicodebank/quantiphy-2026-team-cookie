# q_2816 – length of the book (cm)

- Book = the "white_card" in scene/ (flat white printed booklet lying on the floor at ~(664, 614) px, static all clip).
  File fps = question_fps = 24; t = 0.4 s -> frame 10. depth_info: book 2.082 m.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Route 1 – method card (depth x pixel extent / f)
Mask = residual vs polynomial background fit (measure_book.py, rectify.py), minimum-area rectangle long side on frame 10
(identical on frames 0, 24, 47): 73.2–78.9 px depending on threshold / morphology (78.9 px with the scene/ mask, which
includes a blurred edge and the book's grey side edge; 74–75 px for tighter masks).
-> 2.082 x (73.2..78.9) / 762.8 = 20.0 – 21.5 cm.

## Route 2 – floor-plane rectification
Plane fitted to back-projected centres of bin, cup, book, ball with their approximate heights above the floor (plane.py):
camera ~1.67 m high, tilted ~35 deg down, residuals < 1 cm. Mask contour projected on the plane through the book centre,
min-area rect long side: 20.3 – 21.4 cm (short side 11.5–13 cm). Hand-picked top-face corners: long edges 19.8 / 21.4 cm.

## Answer
Both routes centre on ~21 cm -> **21.0 cm**. Confidence: moderate-good (about ±5%; the mask edge spread is the main uncertainty).

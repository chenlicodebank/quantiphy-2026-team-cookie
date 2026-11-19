# q_2526 — diameter of the white ball (cm)

File fps = question fps = 24. t = 1.6 s -> frame 38.

Method (lab method card): f = 0.5959 x 1280 = 763 px. D = depth x pixel diameter / f.
- White ball pixel diameter at frame 38: gradient edge fit (measure.py, sub-pixel max gradient per row, widest row)
  = 28.3 px; frames 37/39 give 27.5 / 28.3; scene record edge-circle fit = 29 px (frames 38–39). Used 28.6 px.
- D = 0.994 m x 28.6 / 763 = 3.73 cm (range 3.69–3.78 for 28.3–29 px).

Check / caveat: the same formula for the tennis ball (55 px at 1.19 m, record + by eye 54 px) gives 8.6 cm,
not the 6.7 cm prior, so the given yellow depth and the prior are inconsistent by ~28%. Scaling the white ball
from the tennis ball instead (ratio of pixel sizes x ratio of depths x 6.7) gives 2.95 cm. I answered with the
method-card value (the white ball's own measured depth), which is also close to a ping-pong ball's ~4 cm.
Confidence: moderate.

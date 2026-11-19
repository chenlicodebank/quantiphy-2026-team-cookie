# q2047: distance between the two players at the beginning (frame 0)

- The camera is static and looks almost straight down, so I used the annotators' planar convention: one scale taken from the prior.
- Scale: the singles court width is the distance between the left and right singles sidelines (court-line positions in scene.json, checked on a frame-0 crop with a grid). It is 1340 px at y=975 (right player's row), 1345 px at y=1500 (left player's row), and 1342.5 px at the midpoint between them. Scale = 8.23 / 1342.5 = 0.006131 m/px.
- Player positions at frame 0: I used the "core" centroids (the black clothing and hair, which is the visible body centre). Right player (1486.1, 973.5), left player (641.7, 1500.8). Both checked visually on frame 0.
  The separation is 995.5 px, which gives **6.10 m**.
- Other readings: the full-mask centroids, which include the racket, give 1012.6 px = 6.21 m. Frames 1-2 give 6.04-6.07 m because the right player is already moving. Reading the body centres by eye from the gridded frame-0 crop gives about 993 px = 6.09 m.
- Time base: only frame 0 is used, so the fps question does not affect the answer.
- Confidence: good, about ±3%. The main uncertainty is which reference point on each body the annotators used.
- Script: measure.py.

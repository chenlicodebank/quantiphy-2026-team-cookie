# Q2070: initial distance between the two players

- This is a top-down drone view of the pitch, so the scene is planar and one scale applies everywhere. The camera is static.
- **Scale.** I re-fitted the centre circle on frame 0 (`measure.py`, algebraic fit to the white line pixels, 1365 points): R = 116.95 px, which matches the scene record (116.9). The median of the ray-profile radii is also 116.95 px. Scale = 9.15 / 116.95 = 0.07824 m/px.
- **Players at frame 0 (t = 0).** From the record's stabilised tracks: A (light) is at (1406.6, 520.4) and B (dark) is at (1462.0, 530.2), which gives d = 56.2 px = 4.40 m.
- **Second route.** I read the body centres by eye from a 6x zoomed crop of frame 0 (`frames/players_f0.png`). A is at about (1407.5, 520) and B at about (1461.7, 529.7). That gives d ≈ 55.1 px = 4.31 m.
- B is already moving slowly, so frames 0-2 give 4.28-4.40 m.
- **Answer.** 4.38 m. I weighted the frame-0 tracked centroids most. Confidence is high, at about ±3%.

# Q2080 – distance between the two players at the beginning

- "The two players" = the two players in the rebound play at the bottom basket: A (white shirt, on the left
  lane line) and B (black shirt, inside the lane, reaching up). Player C stands alone near the far basket
  and is not part of the play. Frame 0 (t = 0). Using fps 29.90 or 30 makes no difference here.
- Scale: prior inner court (lane/key) width = 4.88 m. I measured the lane width in code (measure.py, line
  intensity profiles on frame 0) at the players' rows y = 3100-3650: line centre to centre 635-641 px, outer edge
  to outer edge 646-653 px. I used about 642 px (between the two readings at y ≈ 3220-3530), which gives
  7.60 mm/px.
- Positions at frame 0 (from the scene mask centroids, which I checked on a zoomed crop of frame 0): A (763.5, 3529.4),
  B (1037.0, 3223.8). Distance = 410.1 px, which is 3.12 m (3.13 m with the 639.5 px centre-to-centre width,
  3.08 m with the 650 px outer width).
- Second route: head/torso points read by eye, A ≈ (750, 3530) and B ≈ (1030, 3240), give about 403 px, or 3.06 m.
- Answer: 3.1 m. Confidence is moderate. The main uncertainty is which reference point the annotator used for
  each player (about ±2%) and that B's arms are raised.

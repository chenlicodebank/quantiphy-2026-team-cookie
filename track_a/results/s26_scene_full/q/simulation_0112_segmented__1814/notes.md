# q_1814: wheel diameter (m). Prior: car speed = 6.66 m/s

The file and the question both use 24 fps, so no re-timing was needed. The camera is static, the motion is horizontal and uniform, and the scene is treated as 2D.

## Wheel size in pixels (wheel5.py)
- **Method:** in frames 14-37 I walked outward from each hub centre (starting from the scene/ Hough track) along rows y=498-512 and along columns, stopping at the tyre's outer edge.
  - Tyre pixel = grey: R-G<12, max channel ≥22, not white.
  - The wheel-well shadow is near-black or red, the body is red and the background is white, so the edge is sharp. For example, frame 25 rear: x 407-475 and y 471-539.
- **Rear tyre:** 69.25 px horizontal, 69.2 px vertical (mean of 24 frames, spread ±1 px).
- **Front tyre:** 66.9 px horizontal, 67.6 px vertical. It is a little smaller, or partly hidden by the fender.
- **Used:** the mean of both wheels, ≈ 68.2 px.
- The scene/ Hough radius (33.5 px, i.e. 67 px diameter) agrees.

## Scale
- The car moves at a constant 6.66 m/s, which is 0.2775 m per frame.
- **Perspective:** the near-side wheels sit closer to the camera than the car's origin, so they move faster on screen. Measured on the wheels' own extents, the wheel centres move 28.24 px/frame (rear) and 28.16 px/frame (front); the silhouette centre, which stands in for the origin, moves 27.29 px/frame.
- To keep the size and the speed at the same depth, I paired the wheel's pixel size with the wheel's own pixel speed: 0.2775 / 28.2 = 0.00984 m/px.

## Result
- **Diameter:** 68.2 × 0.00984 = **0.671 m**.
  - Rear wheel alone: 0.681 m.
  - Front wheel alone: 0.662 m.

## Checks
- **Silhouette scale instead:** using the silhouette speed (the origin's depth) gives 0.693 m, about 3% higher. I rejected it because it mixes two depths.
- **Car length:** with the origin-depth scale, the car's 421 px length is 4.28 m, which fits a 911-type coupe. A wheel of about 0.67 m is also realistic.

**Confidence:** about ±3%. The main uncertainties are front versus rear wheel and the depth pairing.

# Q682: width (vertical) of the Chinese chess board, in metres

The prior is that one piece is 0.097 m across. The scene is 2D: a static top-down camera looks straight down on the board, so I used a single metres-per-pixel scale. fps is 24 and question_fps is also 24. Time does not matter for this question.

## Measurements (scripts: measure.py, profile.py, refine.py)
- **Board's vertical extent in the image** (frame 44; the board is static). I took column profiles every 10 px for x = 470 to 1450 and found the strongest gradient at each edge.
  - Outer top edge (tatami to orange rim): y = 73.5. Outer bottom edge: y = 1016.5. That gives **943 px** (the scene record says 944).
  - Inner playing field: y = 80.5 to 1008.5, which is 928 px.
  - Horizontal outer extent, for reference: 1030 to 1042 px.
- **Piece diameter**: I measured the silhouette of 12 isolated static pieces. Each edge was taken where the mean RGB is halfway between the board and the piece rim.
  - Horizontal average: 85.2 px. Vertical average: 85.4 px. Overall **85.3 ± 0.5 px**.
  - The moving general near the centre (frame 25) measures about 85.7 px with the same profile method. Its mask bounding box is 86–87 px.
  - I used about 85.5 px.
- **Scale**: 0.097 / 85.5 = 1.134e-3 m/px.

## Result
- Width (vertical extent) = 943 × 0.097 / 85.5 = **1.070 m**.
- Range from the reference choices:
  - Static-piece diameter of 85.3 px: 1.072 m.
  - General's diameter of 86.5 px: 1.057 m.
- Other reading: the inner playing field alone would be 928 px, or 1.053 m. I answered with the outer bounding box, which includes the rim.
- Perspective: the pieces' tops stand slightly above the board surface. That makes them look about 1% bigger, which is within the uncertainty.

## Checks
- The board edges agree across about 90 columns. Most fall at 73.5 ± 1 at the top and 1016 ± 1 at the bottom.
- The piece diameters agree between static and moving pieces and between the horizontal and vertical directions, to within 1.5%.

Confidence: high. The expected error is about 2%.

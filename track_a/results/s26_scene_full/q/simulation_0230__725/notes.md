# Q725: chalkboard height (prior: chalkboard length = 5 m)

- Static camera; the chalkboard is a flat board facing the camera head-on, so the height:length pixel ratio equals the world ratio. fps 24 = question_fps, but time doesn't matter here.
- `edges.py`: grey-level profiles on frame 0. The vertical profile is averaged over x 1100–1500 and the horizontal one over y 320–380, both away from the sunbeam.
  - Outer wooden frame: top y≈296, bottom y≈737, left x≈318, right x≈1691, so **1373 x 441 px**.
  - Green surface: x 342–1670, y 315–716, so 1328 x 401 px.
  - These agree with the scene record (1372 x 440 and 1328 x 402).
- I assume the object is the whole board, frame included, since its bounding box is the mesh extent. That gives height = 5 x 441 / 1373 = **1.606 m**.
- Cross-check: the scene record's numbers give 5 x 440 / 1372 = 1.603 m. If only the green surface counted, the answer would be 1.51 m (about 6% lower). I chose the outer frame.
- Confidence: high for the ratio (±1%). The main uncertainty is whether the frame counts as part of the board.

# Q207: distance between the shark and the boat at 0.5 s

The prior is that the shark's acceleration is 1 m/s². The video is a 2D sim with a static camera at 24 fps, and question_fps is also 24, so no re-timing is needed. t = 0.5 s is frame 12.

## Scale (shark_track.py)
- I template-matched the shark's front body (nose to before the tail, which avoids the tail swing) in every frame with subpixel peaks.
- A quadratic fit of x(t) gives an acceleration of 86.8 px/s² over frames 2–53. Sub-windows give 87.4 (2–28), 87.2 (28–53) and 86.5 (5–50).
- The record's centroid track gives 87.5 independently.
- I used 87.0 px/s², so the scale is 1/87.0 m/px = 0.01149 m/px.
- Sanity checks:
  - The shark's length is 260 px, which is 3.0 m.
  - The boat's length is 858 px, which is 9.9 m.
  - The boat moves at 430 px/s, which is 4.9 m/s.
  - All of these are plausible.

## Positions at frame 12
- **Shark:** the mask centroid is at (1555.0, 905.5). The template track agrees.
- **Boat:** the bow tip is at 716.8 (subpixel) and the full length is 858 px, so the bbox centre is at x = 287.8. The stern is off-screen at this frame.
- **dx:** 1267.2 px.

## Boat origin height (the main uncertainty)
- The origin is not visible, and the mast is cut off by the top of the frame.
- The candidate heights and the distance each gives:
  - y = 436.5 (midpoint of hull plus wheelhouse): 1351 px, 15.53 m
  - y = 566 (waterline/horizon): 1312 px, 15.08 m
  - y = 637 (keel): 1295 px, 14.89 m
- **Answer: 15.3 m**, the middle of this range. Every candidate is within 3% of it.
- If the shark origin were its bbox centre (x = 1581.5) instead of the centroid, the distance would rise by about 2%.

## Confidence
Moderate to good. The scale is solid, agreeing within ±1% across two tracking methods. The vertical origin of the boat is the remaining uncertainty, at about ±4%.

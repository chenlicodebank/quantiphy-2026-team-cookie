# q_1853 — length of the blue car including the extending wire

Prior: tyre diameter = 0.369 m. No depth_info. The clip plays at 24 fps, the same as question_fps, and the time base doesn't matter for a size.
Side view, static camera, with the car driving straight across at constant depth. I treat it as planar and use one px→m scale from the tyre.

## Car length in pixels (length.py)
- I took the horizontal extent of the largest mask component, from the slanted roof "wire" tip on the left/rear to the front bumper.
- Frames 29–41 were used. In these the front face doesn't show; in frames 22–28 it inflates the length.
- At thresholds of 230, 243 and 250 the median is **546 px** (543–552). Frame 39 (535) is a tip dropout in the segmentation.

## Tyre diameter in pixels (tyre_edge.py, chords.py)
- The outer dark silhouette is wider horizontally (about 56–57 px on one side, or 112 px across as in scene/notes) because the tread shows in perspective. That makes it unusable as the diameter.
- I used the clean sidewall circle instead:
  - Hub to bottom edge: front 52.0 px, rear 52.4 px (median of frames 29–41).
  - Rear tyre, hub to left edge: 51.2 px. The left-edge chords at dy = 20–48 below the hub fit a circle of r ≈ 52 centred on the hub.
- Result: **D ≈ 104.4 px** (±1.5).

## Answer
L = 546 / 104.4 × 0.369 = **1.93 m**.

## Checks
- Wheelbase 336 px gives 1.19 m. The length/tyre ratio of 5.2 matches a real golf cart (2.4 m / 0.46 m).
- If the inflated outer tyre width of 112 px were used instead, the answer would be 1.80 m. I rejected this because it contradicts the 52 px radius measured downward.
- Perspective: the near-side scale is about 4 % above the centre plane. The tyre and the bumper extremes are both on the near side. The wire may be off that plane, so ~2 % uncertainty is possible.

Confidence: moderate-high, ±4 %.

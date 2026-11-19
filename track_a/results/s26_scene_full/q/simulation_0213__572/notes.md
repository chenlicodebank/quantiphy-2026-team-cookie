# Q572 — black cat height incl. tail (m)

Prior: cat speed 0.94 m/s. 2D scene, the cat walks steadily left→right; one scale comes from the cat itself, so the dog's different depth lane doesn't matter here. fps = question_fps = 24.

- Pixel speed: I fitted lines to the visible frames (0-22, 44-49) of scene/tracks/cat.csv (`measure.py`). The slopes were nose (bbox_x1) 17.76, torso 17.86, centroid 17.81 and bbox_cx 17.71 px/frame, so 17.76 px/frame × 24 = 426 px/s.
  Scale = 0.94 / 426.2 = 0.002205 m/px. Using 17.85 instead would change it by 0.5%.
- Height in pixels: tail tip (top, y≈794-806) to paw bottoms (y≈1016-1023). I checked this by eye on zoomed grid frames 0 and 12: the tail tip is at about 795 and the paws at about 1020 in frame 0.
  Over the unoccluded frames the median is 222 px (range 213-228; the tail pose varies).
- Height = 222 × 0.002205 = 0.490 m. The range is 0.47-0.50 m.

Second-route check: the spread across frames and reference points is under 3%. A height of 0.49 m for a cat including its raised tail is plausible.
Confidence: moderate-high. The main uncertainty is which frame or pose the reference AABB used.

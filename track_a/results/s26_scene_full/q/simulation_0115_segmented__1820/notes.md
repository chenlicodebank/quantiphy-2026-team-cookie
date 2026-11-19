# q_1820 — width of the boat (m); prior: boat acceleration = 3 m/s^2

2D top-down Blender render (segmented), 24 fps (file fps = question_fps, no re-timing). Camera static.
The boat moves in −x and speeds up evenly; y is constant and it does not rotate.

## Method (measure.py)
- Boat mask in each frame: non-white threshold (max(255-RGB) > 40), 3x3 opening, the component below y = 600.
- Pixel acceleration: a quadratic fit of x(t) over all 37 frames.
  - centroid: −138.5 px/s² (rms 0.40 px)
  - bbox midpoint: −137.6 px/s² (rms 0.27 px)
  - left edge: −136.4 px/s²; right edge: −138.9 px/s²
  - fits on each half separately: 131 to 148 px/s²
  - mean of per-frame speed differences: 133 px/s² (this is noisy)
  - Adopted value: 138 px/s².
- Scale: 3 / 138 = 0.02174 m/px.
- Boat width: the across-hull extent, which here is the vertical pixel extent because the hull axis is horizontal.
  - It is 88 px in every frame (median; range 86–90).
  - PCA width in the scene record is 88–90 px.
  - Adopted value: 88.5 px, allowing for the soft anti-aliased edge.
- Width = 88.5 × 0.02174 = 1.92 m.

## Checks
- Using acceleration from the different reference points (136–139 px/s²) gives a width of 1.91–1.95 m.
- The length is 226 px, which gives 4.9 m. The boat is then 4.9 x 1.9 m, a plausible dinghy shape.

Confidence: good. The main uncertainty is the pixel acceleration, about ±3%.

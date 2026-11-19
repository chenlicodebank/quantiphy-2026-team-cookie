# Q2: length of the pier (m). Prior: boat length = 3.62 m

The camera looks straight down and does not move, so this is a 2D case: one metres-per-pixel scale from the boat.
fps is 24 = question_fps, but time does not matter for this size question.

## Measurements (frame 0, `measure.py`, `boatprof.py`, overlay in `frames/overlay.png`)
- **Pier:** mask of low-saturation bright pixels.
  - Outer-contour minAreaRect: 321.5 × 95.0 px at −25.5°.
  - PCA along-axis extent: 321.1 px (318.6 px with 0.1–99.9 percentile trimming).
  - The land end is partly in tree shadow, but the fitted rectangle reaches the corner posts. Length ≈ 321 px.
- **Boat:**
  - Total along-axis extent is 209.7 px. This includes a small stick or oar tip, about 6 px, protruding past the
    lower-left end. Without it the hull is about 203 px.
  - The boat and pier axes are both about 23–25° off the image axes. The assets are probably world-aligned and the
    camera rolled, so along-axis lengths stand for the AABB extents.

## Result
- Scale: 3.62 / 209.7 = 0.01726 m/px, which gives a pier of 5.55 m.
- With the hull only (203 px): 0.01783 m/px, which gives 5.73 m.
- Answer: **5.6 m**. This leans toward including the stick, because it is boat geometry and would count in the
  bounding box.

## Check
The axis-aligned image boxes give the same answer: pier bbox height 308 px vs boat bbox width 198 px, so
308 / 198 × 3.62 = 5.63 m.

Confidence: about ±3%.

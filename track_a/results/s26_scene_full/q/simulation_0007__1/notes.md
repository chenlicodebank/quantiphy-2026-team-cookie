# Q1: width of the wooden pier (m). Prior: boat length = 3.62 m

The view is a 2D top-down shot from a static camera, so I used one metres-per-pixel scale taken from the boat length.
The question's fps (24) matches the file's fps (24), and the size does not depend on time anyway.

## Measurements (scripts: pier_profile.py, measure2.py)
- **Pier width.** I averaged brightness profiles across the pier (bilinear sampling, 0.25 px steps) and refined the
  axis angle to 65.9° by maximising edge sharpness. Each edge was taken as the sub-pixel 50% crossing between the
  deck and the water.
  - Widths in four separate segments along the pier: 83.06, 82.89, 82.47 and 82.68 px, giving **82.8 px**
    (±0.3 px).
  - A second route, the mask extent across the axis, gives about 75–84 px per slice. The noisy slices come from
    dark plank shadows inside the deck. The scene record's minAreaRect width of 94 px is too large because it
    includes the shadowed edge.
- **Boat length** (filled mask, extent along the principal axis): 210.7, 209.7 and 207.8 px at frames 0, 10 and
  20. The scene record gives 209.7 px at frame 0, and about 205 px if the small stem or stick at the lower-left
  tip is left out. Later frames lose the tip to tree shadow.
  - I used **209.7 px**: the protrusion looks like part of the boat model, so the bounding box would include it.

## Result
- Scale: 3.62 / 209.7 = 0.01726 m/px, so the width is 82.8 × 0.01726 = **1.43 m**.
- If the tip is excluded (boat 205 px), the width would be 1.46 m. That is a 2% difference, so the answer is not
  sensitive to this choice.
- Height differences between the deck, the boat and the water are ignored (planar assumption).

**Confidence:** good, roughly ±3–4%.

# Q34 – length of the turning yellow (tan) car

The scene is a 2D top-down render at 24 fps (file fps = question_fps). The camera is static and there is no perspective, so a single metres-per-pixel scale applies.

**Prior:** the white van has an acceleration of 4 m/s², and it drives straight north the whole time.
- `measure.py` finds the van's front edge, rear edge and centre with a white mask in the van's column, then fits a quadratic to each over several frame windows (4-71, 10-71, 4-40, 36-71).
- Fitted acceleration: 0.2856-0.2872 px/frame² across edges and windows; residual rms 0.2 px. The acceleration is uniform, so the early and late windows agree.
- Value used: 0.2868 px/frame² = 165.2 px/s².
- Scale: 4 / 165.2 = 0.02421 m/px.

**Asked object:** the tan sedan, which turns right from heading north to heading east.
- Its length along the axis was measured from a colour mask with an axis-aligned box when the car is axis-aligned. At frame 0 (vertical) it is 218 px, and at frame 71 (horizontal) it is 218 px.
- The scene record's median is 219 px, which agrees. Length used: 218.5 px.

**Answer:** 218.5 × 0.02421 = 5.29 m.

**Checks:**
- The two independent orientations (frame 0 and frame 71) give the same pixel length.
- The acceleration agrees between the front edge, the rear edge and the centre, and between early and late windows (within 0.5%).
- Sanity check: the van comes out at 234 px ≈ 5.67 m, which is plausible.

Confidence: good (about ±2%).

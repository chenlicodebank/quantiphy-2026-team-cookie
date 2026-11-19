# q_1837 — width of bottom towel (of three stacked towels on the sink)

- 2D top-down scene, 24 fps (file fps = question_fps, no retiming). The "tray" in scene/ is actually the stack of
  three towels (nested rectangles at centre ~(911,199), rotated ~26 deg); the bottom towel is the largest, outer outline.
  The "cup" in the prior is the moving teal block (the only moving object).
- Scale (measure.py): cup centroid linear fit, frames 2–71 = 14.5365 px/frame; its left edge gives 14.538 and its
  right edge 14.530, and the mean per-frame dx is 14.533, so the four estimates agree. That is 348.9 px/s, and
  0.338 m/s / 348.9 px/s = 9.688e-4 m/px.
- Bottom towel: minAreaRect of the outer non-white contour = 374.0 x 188.3 px (f0), 373.2 x 187.4 (f36),
  373.2 x 187.6 (f71). The rectangle drawn in frames/towel_rect.png fits the outline. Short side = 188 px ±1.
- Width = 188 x 9.688e-4 = 0.182 m (length would be ~0.362 m).
- Alternative reading (world-axis AABB of the 26°-rotated towel): extents ~418 x 331 px, so "width" = 0.321 m. I did not
  use it: width is taken as the towel's own short side.
- Caveat: one plane scale is assumed (2D convention). If the towels sit higher than the cup's plane, perspective
  would change this a little. Confidence: moderate-high under the 2D convention.

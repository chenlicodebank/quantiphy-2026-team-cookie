# q2736: diameter of the white cup's rim (cm)

The video's file rate and question_fps are both 24. The cup does not move.

## Method (lab method card)
- Focal length f = 0.5959 × 1280 = 762.8 px. Distance from camera to cup = 0.874 m (from depth_info).
- `width.py` takes the median of frames 0, 12, 24, 36 and 48 and measures the cup's width on each image row, with
  sub-pixel edges at the half level against the black (segmented) background.
  - The rim's widest point (rows 382–390, just below the metal lip) is 71.8 px wide, from x 723.6 to 795.4.
  - This agrees with scene.json's top width of 72 px.
- The rim's horizontal extent in the image is its full diameter: the ellipse's major axis is horizontal.
- Diameter = 0.874 × 71.8 / 762.8 = 0.0823 m = **8.2 cm**.

## Checks
- If the Euclidean distance is converted to the optical-axis depth (Z = 0.863 m, since the cup is about 120 px off
  centre), the diameter is 8.13 cm. The answer rounds to 8.2.
- The blue card (102 px wide at 0.6867 m) gives 9.2 cm against the prior's 85.6 mm. The card lies flat and at an
  angle, so it is not a clean check of scale, but it shows the scale is about right.
- A tumbler rim of 8 to 8.5 cm is a realistic size.

Confidence: good (±4%).

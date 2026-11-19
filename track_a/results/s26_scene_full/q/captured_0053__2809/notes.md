# q_2809 – diameter of the white cup's rim (cm)

The question and the file both use 24 fps. The "trashbin" in the prior is the blue moving object that scene/ calls the "car". The cup sits still at about (565, 430) px.

## Method (lab method card)
- f = 0.5959 x 1280 = 762.75 px. Depth to the cup from depth_info: D = 2.516 m.
- `measure_rim.py` averages all 48 frames of a 50x60 crop around the cup. This reduces noise, which is fine because the cup and camera are static.
  For each row through the rim ellipse it finds the bright rim line on the left and right (sub-pixel peak) and the
  outer edges, where the brightness is halfway between the rim and the carpet.
- The widest row of the ellipse is the horizontal diameter, which perspective does not shorten.
  - Outer edge to outer edge: 25.7–26.0 px on rows 14–17 (one noisy row reads 26.6).
  - Centre of the rim line to centre: 23.8–24.7 px.
- Diameter = D x px / f:
  - outer edges, 25.8 px -> **8.5 cm**
  - rim line centres, 24.3 px -> 8.0 cm
  - largest single row, 26.6 px -> 8.8 cm

## Check
- Single raw frame 10, read from the grey values: the rim's bright pixels run from column 13 to columns 37/38, giving an outer width of about 25–26 px. This agrees with the averaged result.
- The cup body is about 23–24 px wide, a little narrower than the rim, which fits a cup that tapers.
- Scale check: the basketball is 64–68 px wide at 2.925 m, which gives 24.5–26 cm. A real basketball is about 24 cm, so the scale is plausible.

## Answer
8.5 cm (outer rim diameter). Confidence: moderate, about ±5%. The edge blur is only about 1 px, but at this size 1 px is about 4%.

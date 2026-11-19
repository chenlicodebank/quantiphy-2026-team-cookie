# Q726 — width of the orange chair next to the blackboard (prior: chalkboard length = 5 m)

## Object
The chair "next to the blackboard" is the salmon/orange chair against the back wall just right of the board, below
the clock (x≈1600–1797, y≈737–1022). The two orange chairs in the foreground are cut off by the image bottom and are
not next to the board. The chair faces the camera, so its width is the left–right extent (seat/backrest side to side).
The camera is static (record), so I used a median of frames 0,10,20,30,40,49. Scripts: `enh.py` (CLAHE crop, `frames/enh.png`),
`measure.py`, `measure2.py`.

## Measurements (px)
- Chalkboard outer frame: x 320 → 1693.5 (right edge measured at 1693.5; green surface 341.5–1671.5, so the frame is
  22 px wide on each side and the left outer edge is ≈320). Length = 1373 px → 5 m. Scale on the wall plane:
  3.642 mm/px. (Using the green surface only, 1330 px, would make everything 3 % larger.)
- Chair backrest, half-max extent of the orange-ness (R−B) profile over rows 745–795: x 1602–1751 = 150 px. The strongest
  edges are at 1599.5 / 1751.5, so 150–152 px.
- Wall–floor line: y = 951.5 (measured at two places). Back-right leg foot y ≈ 1000–1010. Front feet y ≈ 1020–1022.
  Seat front edge y ≈ 885. Backrest top y ≈ 740.

## Depth correction (the chair stands in front of the wall)
The camera is level (verticals stay vertical), so the horizon is at cy ≈ 540. For points on the floor, depth ∝ 1/(y − 540).
- Back legs/backrest: k = (951.5−540)/(1005−540) ≈ 0.885 (0.876–0.89 over the foot-y range 1000–1010; ±20 px on cy
  changes k by less than 1 %).
- Front legs: k ≈ 411.5/481 = 0.855.

## Result
Width = 150–152 px × 3.642 mm/px × 0.876–0.89 ≈ 0.478–0.493 m. **Answer: 0.48 m.**

## Checks (second route)
- Same scale on other chair dimensions: overall height (backrest top 740 → back foot ≈1005) = 265 px × 3.642 × 0.88 ≈ 0.85 m.
  Seat height (885 → 1022) = 137 px × 3.116 mm ≈ 0.43 m. Both are typical for a school chair, so the scale and depth
  factors are consistent.
- The front-leg spacing at the front depth is about 142 px × 3.116 mm ≈ 0.44 m. The backrest is a little wider than the
  leg frame, and the bounding-box width follows the widest part, the backrest.
- Other reading: if "width" meant front-to-back depth, I could not measure it reliably. The feet differ by only about
  15 px in y, and the focal length is unknown (no depth_info). So I answer with the side-to-side width.

Confidence: moderate, roughly ±5 %. The main uncertainties are whether the 5 m prior includes the frame (3 %) and the
foot positions used for the depth factor (1–2 %).

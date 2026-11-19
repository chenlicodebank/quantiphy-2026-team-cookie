# q_463: height of the box (prior: box width = 1.33 m)

Object: "the box" is the brown cardboard box on the truck roof, not the truck's cargo body.
- Under the other reading (cargo body width 1.33 m), the rear face is 520.4/570 x 1.33 = 1.21 m.

fps 120 = question_fps, so no re-timing. The time does not matter for a size anyway.

## Measurements (frame 0, level.py + scene record)
- Box width: 281.5 px (edges at x 806 and 1087 at rows 180 and 250).
  - Scale at the box's depth: 1.33/281.5 = 4.725 mm/px.
- Box front top edge: y = 163.4. The flap tip is at y = 147.6, so the flap adds at least 15.8 px.
- The bottom is hidden behind the body's roof edge (y = 338.1). Visible height: 174.7 px.
- The camera is level: the wall seams and truck edges are exactly vertical (level.py). So the horizon is at the principal row, y = 540.
  - The camera is below the roof, so the box, which sits farther back on the roof, has its bottom edge projected below the roof edge.
  - Box bottom: y_b = 540 - (540 - 338.1) x Zr/Zb.

## Depth ratio Zr/Zb (rear face to box)
- **Motion route:** box pixel rise / body pixel rise.
  - Mid-clip windows (frames 70–230) give about 0.96. Cumulative over frames 200–300 gives about 0.89.
  - The box is not rigidly coupled to the body (it lags at the start and stops at the end), so this is only indicative.
- **Sanity route:** at the box's depth scale the truck would be 2.69 x Zr/Zb m wide. A realistic 2.5 m truck gives about 0.93.
- **Adopted:** 0.93, so y_b = 352.2.

## Result
- Without the flap: 352.2 - 163.4 = 188.8 px, which is 0.89 m.
- With the open flap in the bounding box: about 205 px or more, which is about 0.97 m.
- **Answer: 0.93 m.** This is the midpoint, within about 5 pct of both readings.

Range over the plausible depth ratios (1.0 to 0.88): 0.83–0.99 m.

Confidence: moderate. The main uncertainty is the hidden bottom (box depth) and whether the flap counts.

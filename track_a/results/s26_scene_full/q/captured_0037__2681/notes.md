# q2681: height of the white cup (cm)

The file and the question both run at 24 fps. The camera is static.

## Method (lab method card)
- f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Cup pixel height: `edges.py` thresholds vertical intensity columns (gray > 160) across the cup (x 750-800) in
  frames 0, 24 and 48. In the central columns (x 770-790) the top rim is at y = 377 and the bottom at y = 501-502,
  giving 125-126 px. The cup is static, so all three frames agree. A visual check on frames/cup_raw_24.png shows the
  rim at y ≈ 377 and the base/shadow line at y ≈ 502, which matches the scene/ bbox (377-502, 125 px).
- Size = d x px / f = 0.845 x 125 / 763 = 0.1384 m = **13.8 cm**.

## Cross-check
- Using the axial depth Z instead of the range (Z = d/sqrt(1+r²/f²) = 0.8275 m) with a level camera gives 13.6 cm.
  A camera pitched down about 10° would give about 14.0 cm. 13.8 cm sits between these, and it is a sensible size
  for a tumbler.
- Prior check: the ball's apparent diameter is about 26 px at t = 1.0 s and d = 1.055 m, which gives 3.6 cm against
  the 4 cm prior. The half-intensity mask with motion blur underestimates the ball, so this agrees roughly.

Confidence: good (±3%).

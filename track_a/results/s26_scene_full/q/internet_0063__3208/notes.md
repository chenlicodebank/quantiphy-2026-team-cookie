# q_3208: diameter of the water bottle (cm). Prior: g = 9.8 m/s^2

## Scale from gravity (fit.py)
- The camera is rotated 90°, so the bottle falls toward image +x (frames 40–52, free fall before it hits the skirting board at frame 53).
- Quadratic fits to x(frame) over several windows (40–52, 41–52, 40–50, 42–52, 39–51, 41–49):
  - cap centroid: 11.98–12.60 px/frame²
  - bottle centre: 11.83–12.54 px/frame²
  - The second differences scatter between 9 and 14. I adopt **a = 12.3 px/frame²**.
  - The y component is about −0.2 px/frame², which is negligible.
- Time base: 30 fps (question_fps; the file's 30.016 fps is practically the same). a = 12.3 × 900 = 11070 px/s².
- Scale: 9.8 / 11070 = 8.85e-4 m/px. The camera drift (~0.2 px/frame) is negligible.

## Bottle diameter in pixels (profile.py, held frames 5, 15, 30)
- Vertical intensity profiles across the horizontal bottle:
  - top edge at y ≈ 543–545 (sharp)
  - bottom of the plastic body at y ≈ 612–616 (x = 200, 350)
  - the label alone ends at y ≈ 602
- Diameter ≈ 70 px (range 67–72). This agrees with the scene record (≈70 px, 62–78).

## Answer
70 px × 8.85e-4 m/px = 6.2 cm.

## Checks
- Bottle length is 260 px, which gives 23 cm. A 6.2 cm × 23 cm bottle is plausible for a 500 mL to 0.75 L water bottle.
- Uncertainty: about ±3% from the acceleration fit and about ±4% from the pixel diameter.

Confidence: moderate-good.

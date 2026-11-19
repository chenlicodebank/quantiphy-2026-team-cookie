# Q161: height of the car (prior: car speed = 30 m/s)

This is a 2D side-view scene with a static camera and fps 24 (file and question rates agree). The scale comes from the car itself, so any depth offset cancels out.

- **Speed** (`measure.py`, colour difference from the background, threshold 20, frames 11–37 unclipped): linear fits give 28.40 px/frame for the bbox centre and 28.39 for the centroid. The edges give 28.53 (x0) and 28.27 (x1); the bbox length shrinks slightly from perspective. The per-frame step is constant, so the speed is 681.6 px/s.
- **Scale:** 30 / 681.6 = 0.04402 m/px.
- **Height** (`height_sub.py`): the thresholded bbox runs from y 631 to 673, which is 43 px in every frame. The edge rows are partly covered: the top row (631) is about 0.7 of full contrast and the bottom row (673, wheel bottom) about 0.45. That gives a subpixel height of about 42.2–42.5 px.
- **Result:** 42.5 × 0.04402 = 1.87 m. The integer 43 px gives 1.89 m. **Answer: 1.88 m.**
- **Check:** height/length = 42.5/130 = 0.33, which is close to a real Cybertruck (1.79/5.68 = 0.32), and the size is plausible. Using the fitted speed from either edge instead changes the result by less than 0.5 %.
- **Confidence:** high, about ±2 %.

# Q2693 – height of the white cup (cm)

The file and the question both run at 24 fps, and t = 1.0 s is frame 24. The camera is static and the cup never moves.

## Method (lab method card)
f = 0.5959 x 1280 = 763 px. Depth of the white cup from depth_info = 0.845 m.
`measure_cup.py` builds a white mask (gray > 150, low saturation) and reads gray profiles at frames 24, 30 and 40. They give the same result:
- top of the cup silhouette: y ≈ 376.5 (the black-to-white step between rows 376 and 377). The dark rim line is at about 379, because the camera sees the top only at a grazing angle.
- bottom edge: y ≈ 503.3 (the cup turns into the contact shadow at rows 503–504).
- silhouette height ≈ 127 px. From the front of the rim to the front of the base it is about 124.5 px. The width is 71 px.

Height = 0.845 x 127 / 763 = 14.06 cm. Using the front-rim extent of 124.5 px gives 13.8 cm.

## Checks
- Ball prior: at frame 24 the ball measures about 25–26 px, which gives 1.055 x 25.5 / 763 = 3.5–3.6 cm against the true 4 cm. So the depth-based scale may read about 10 % low, possibly because the SAM mask erodes the ball's edges. If I rescaled with the ball, the cup would come out at about 15.3 cm. I did not adopt that, because the ball's mask is small and blurred and the method card says to use depth_info directly.
- Cup diameter from the same scale: 7.9 cm. That gives a height-to-width ratio of 1.8, which fits a tall tumbler.

Answer: 14.0 cm. Confidence: moderate (±7 %).

# q_1816: width of the plane (m)

2D top-down clip (1080x1920, file fps 24 = question_fps 24). The plane drops straight down the image from rest, with constant acceleration.
Width of an aircraft = its wingspan (the horizontal x extent in this view).

## Scale from the prior (acceleration = 18 m/s^2)
`measure.py` builds a colour/darkness mask on every frame from 0 to 78 and fits a quadratic to the y position over the frames where the plane is fully in view (0-75):
- tail-top edge y0: 0.5954 px/frame^2, which is 342.95 px/s^2 (RMS 0.8 px). The windows 0-40, 35-75 and 10-75 give 340.5, 343.3 and 343.5.
- mask centroid: 344.0 px/s^2. The windows give 341.5, 346.1 and 344.8.
- The scene record's ref_y track agrees: its quadratic fit has RMS 1.1 px.
I used a = 343 px/s^2, so the scale is 18 / 343 = 0.05248 m/px.

## Size
- The wingspan is 167 px, the same in frames 0-10 and the median over all frames. It does not change with motion blur, because the blur is vertical.
- Width = 167 x 0.05248 = **8.76 m**.
- Length (tail to nose), for reference: 107 px, which is 5.6 m.

## Check / confidence
- The two tracking points and three time windows agree on the acceleration to within ±1%.
- The wingspan is good to ±1 px (0.6%).
- 8.8 m is a plausible span for a small light aircraft.
- Confidence: high, about ±2%.

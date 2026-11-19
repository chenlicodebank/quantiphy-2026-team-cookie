# q555: typewriter length (m)
Prior: free fall a = 9.8 m/s^2 before 0.45 s (frames 0-10, impact between frames 10 and 11). 2D convention: one m/px scale from the pixel acceleration. File fps = question_fps = 24.
- Pixel acceleration, route 1 (tm.py): chained template matching of the typewriter, frames 0-10. Second differences are 12.5-12.9 px/frame^2, steady. Quadratic fits over frames 0-6 to 0-10 give 7346-7376 px/s^2. I used 7350.
- Route 2 (fit.py): quadratic fit to the bbox-centre track in scene/. Gives 7080-7360 px/s^2, about 7200 typical. This route is biased by the vertical motion blur on the bbox edges and the slight rotation in the air.
- Scale = 9.8/7350 = 1.333e-3 m/px.
- Length: the horizontal (left-right) extent in the air is 292-293 px on frames 0-9, constant, so the depth is constant. I did not use the resting bbox (332 px) because it includes rotation and foreshortened depth.
- Length = 293 px x 1.333e-3 = 0.391 m. Route 2 scale gives 0.399 m. This is a realistic typewriter length (about 0.3-0.45 m).
Confidence: moderate-high (about 3 pct).

# q3241 — velocity of the acorn at 0.20 s

The object the scene record calls the "cup" is the acorn: a black cap over a white body, pulled left to right by a cord. The camera is static and fps = question_fps = 30, so t = 0.20 s is frame 6.

## Scale (prior: acorn height = 8 cm)
- Script `height2.py`: the top of the cap is the half-max point of darkness relative to the background (median of frames 9–11). The bottom of the body is the half-max point of (B−R) "whiteness" relative to the background. Both are taken in a column band through the centre.
- Height in px: f3 617–623, f4 621–626, f5 620–630, f6 642–652 (the acorn gets a little closer to the camera, and blur widens the base). I used 630 px, so the scale is 0.08/630 = 1.27e-4 m/px.

## Motion
- Script `measure.py`: the half-max edges of the black cap's horizontal darkness profile (rows 1180–1300).
- Left edge: f5 1714, f6 2556, f7 3434. Centre: f5 1969, f6 2839, f7 3636 (the f7 centre is biased because the right side is cut off by the frame edge).
- Forward difference (the annotators' convention) f6→f7, using the left edge, which is not clipped: 878 px/frame. Backward check f5→f6: 870 px (centre), 842 (left edge), 897 (right edge). The vertical drift of about 15 px/frame is negligible.
- v = 878 × 30 × 1.27e-4 = 3.34 m/s.

## Second route
Backward centre difference: 870 px gives 3.31 m/s. Using the frame-6 height (645 px) for scale gives 3.27 m/s. The routes agree to within about 2%.

Confidence: moderate-high. The main uncertainty is the pixel height (±3%) and the motion-blurred edges.

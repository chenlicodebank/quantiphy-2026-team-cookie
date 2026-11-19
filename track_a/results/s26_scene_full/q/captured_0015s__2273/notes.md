# q2273 — height of the toy (cm); prior: g = 9.8 m/s^2; no depth_info

File fps = question_fps = 24. No depth was given, so the scale comes from gravity acting on the toy itself
(the toy is near-planar motion, vertical toss, static camera).

## Scale from free flight (measure.py, fit2.py)
- Toy segmented as |frame - scene/bg.png| > 45 in the column x 380-520, taking the top-most detached component.
  It is detached from the hands in frames 17-22 (toss 1) and 52-58 (toss 2).
- Quadratic fits of the vertical position vs frame (2*p2 = px/frame^2):
  centroid 4.79-5.43, box mid-point 5.14-5.21 across both tosses and several frame windows.
  Top edge reads higher (5.3-5.9) and bottom edge lower (4.6-5.1) because the dangling legs/tail shift during flight;
  the centroid and mid-point agree on ~5.17 px/frame^2.
- a = 5.17 x 24^2 = 2978 px/s^2, so the scale is 9.8 / 2978 = 3.29e-3 m/px.

## Toy height in pixels
- Toy is upright in flight. Toss 2 mask heights are 93-96 px (95-96 at apex frames 54-55). On a 3x zoomed frame 54
  the toy spans y = 102-200 (about 98 px). The scene record gives 92-98 (PCA length 93.5-98). My best value is 96 px.
  My toss-1 mask is a little smaller (87-90) because the threshold cuts off faint edges.
- Height = 96 x 0.329 = 31.6 cm (range 93-98 px gives 30.6-32.3 cm).

## Check
- Applying the same scale to the person's standing height (508 px) gives 1.67 m, which is plausible.
- Both tosses give the same acceleration to within about 1%.

Answer: 31.6 cm. Confidence moderate (±5%); the main uncertainty is the acceleration fit (short flights, motion blur).

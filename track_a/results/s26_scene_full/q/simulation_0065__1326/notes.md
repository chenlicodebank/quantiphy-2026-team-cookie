# q1326 – height of the traffic light (simulation_0065)

Answer: **5.03 m** (vertical extent from the pole base on the sidewalk to the top of the pedestrian-crossing sign).
The file rate and question_fps are both 24 fps; t = 0.58 s is frame 14 and t = 1.58 s is frame 38.

## Which light
There are 4 traffic lights. The main one is the near-right one: base (1367.5, 578), sign top (1389.5, 119.5), 459 px tall.
The far-left one is the same model, and its height (computed separately) is the same, 5.025 m. The far-centre one is
cut off by the top edge, and the near-left one is cut off by the left edge.

## Camera calibration (all from frame 0, full resolution, measured in code)
- Principal point: assumed at the image centre (1080, 540). Camera roll ≈ 0.
- VP1 (forward road) = (807.6, -194.6). This is the least-squares intersection of 6 edge fits (left/right far-road curbs
  and the near-right diagonal curb, using colour and luminance edges). Each edge crosses the horizon at x = 806-809
  (`vp3.py`).
- VP2 (cross street) lies on the horizon y = -194.6. Edge fits of the near and far cross-street curbs and the tree-grate
  front edge put it at x = 19840-21330 (median 20255).
- Focal length from the orthogonality of VP1 and VP2: **f = 2164 px** (range 2140-2230; with VP2 left free, 2223).
  This gives a horizontal FOV of about 53°.
- The pole-convergence (vertical VP) estimate was also tried (`poles.py`). It was too noisy (short poles, biased by
  shading) and was not used.
- Sidewalk plane: the pedestrian's pelvis at the given depth (25.3568 m at f14, 25.9200 m at f38) is placed by its pixel.
  The lowest foot pixel is then intersected with the vertical line through the pelvis. This puts the camera
  8.09 / 8.10 m above the sidewalk (the two times agree), with the pelvis 0.92-0.93 m above the foot.

## Height (`height.py`, `compare.py`)
The base ray is intersected with the sidewalk plane, giving a base 24.16 m from the camera. The top ray is then
intersected with the vertical line through the base:
- f = 2100: 5.156 m; **f = 2164: 5.026 m**; f = 2230: 4.897 m. The height scales roughly as 1/f.
- A ±1 px change in the base or top pixel changes the height by < 0.01 m.

## Checks
- Second object: the far-left light (base (326, 321.5), top (291, 10.3), 38.1 m away) gives 5.150 / 5.025 / 4.902 m.
  This agrees with the near-right light to within 0.01 m at every f, so the plane geometry and the pixel measurements
  are consistent.
- Prior: with this calibration, the white van's position along its straight path (bbox-centre rays) fitted with a
  quadratic gives an acceleration of 4.18-4.27 m/s² (prior: 4). That is about 5% high, reasonable for a bbox-centre
  proxy, so the metric scale agrees with the prior.
- Other constraints on f were weaker or depend on assumptions:
  - If the two light bases sit at symmetric corners, f ≈ 2100.
  - If the pedestrian walks parallel to the curb, f ≈ 1915-2240.
  - The cyclist's wheel-bottom pixel is too noisy to give the curb height.

Confidence: moderate-high. The main uncertainty is f, about ±3%, which carries straight into the height (about ±3%).

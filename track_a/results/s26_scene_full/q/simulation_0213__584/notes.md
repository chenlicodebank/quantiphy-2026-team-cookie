# q_584 — dog height (incl. tail), simulation_0213

Prior: black cat speed = 0.94 m/s. fps = question_fps = 24 (no re-timing issue).

## Scale
- Cat nose (bbox_x1) linear fit over the frames where it is clearly visible (0-22, 44-49): 17.76 px/frame; torso fit gives 17.86 px/frame (second route, within 0.5 %).
  So 426.3 px/s, and 0.94/426.3 = 0.002205 m/px in the cat's lane.
- The dog walks in a nearer lane (it occludes the cat; paws at y≈1066 against y≈1020 for the cat). Horizon estimate: the lamp-shade bottom rim (y≈605) shows no ellipse,
  the vase bands below y≈700 curve as if seen from slightly above, and the table top is visible from above (y≈785). That puts the horizon at y≈600-650.
  Depth ratio dog/cat = (1020-y_h)/(1066-y_h) = 0.89-0.90, so the dog's lane is ≈0.001975 m/px.

## Dog height
- Height in pixels, paws to top of back or raised tail (scene/tracks/dog.csv; y1 clamped to 1066 at shadow frames 25/43): mean 296.6, median 293, frame 0 298, range 279-342 (tail curled up).
- Height = 296.6 px × 0.002205 × 0.895 ≈ 0.585 m (median 0.58; with the tail at its highest, 0.67).
- Without the perspective correction (one 2D scale) it would be 0.654 m.

Answer: 0.59 m. Confidence is moderate. The main uncertainties are which pose or frame the reference uses (the tail swing gives ±8 %) and the depth correction (≈10 %).

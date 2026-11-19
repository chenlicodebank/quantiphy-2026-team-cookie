# Q2113 — width of the grey notebook (cm)

Prior: the mouse is 57 mm wide (a white Magic-Mouse-style mouse left of the keyboard). Internet video with an overhead static camera,
so I used one planar scale from the prior. Both objects lie flat on the desk and stay still for the whole clip. Timing does not matter
for this question.

Grey notebook = the dark grey closed notebook/tablet at the top right of the desk (centre ≈ (3067, 995) px, called "tablet_dark" in scene/).
Width = its shorter horizontal extent.

## Measurements (frame 0; frame 35 gives the same, ±2 px)
- Mouse (`measure.py` mask minAreaRect; `edges.py` line fits to the straight long sides):
  width 102.5 (mask), 102.8 (grey-level edges), 105.1 (saturation edges) px. Used **103.5 px**. Length is about 198 px
  (ratio 1.92, consistent with a 113.5 x 57 mm Magic Mouse).
- Notebook (`edges.py <frame> sat`: edge points along the normals in the saturation channel, robust line fits, corners from the
  line intersections; overlay in frames/edge_notebook_0.png):
  corners TL (2920, 820), TR (3284, 923), BR (3221, 1180; behind the pen holder, extrapolated), BL (2866, 1050).
  The short sides are 236 px (left) and 265 px (right). The gap between the two long-edge lines is 245 px, and the mask minAreaRect gives 250 px
  (scene record 253). The long edges differ by about 4°, probably because a white cable or clip lifts the notebook's top-left corner.
  Used **≈249.5 px** (mean of the two ends). Long side ≈ 377 px.
- Scale: 57 mm / 103.5 px = 0.551 mm/px.
- Width = 249.5 × 0.551 = 137 mm = **13.7 cm**. (Length ≈ 20.8 cm, a plausible notebook size of about 14 x 21 cm.)

## Check
- Range from the different edge choices: 236/105 → 12.8 cm up to 265/102.5 → 14.7 cm. Line separation 245 px with the grey mouse width
  102.8 px gives 13.6 cm, and the scene-record values (253/102.9) give 14.0 cm.
- Confidence: moderate-good, about ±5%.

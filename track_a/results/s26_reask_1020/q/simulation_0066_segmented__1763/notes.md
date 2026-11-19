# q_1763 — width of the lane (road surface, curb to curb)

File fps = question fps = 24. Segmentation render: the road is not drawn (white). The only road-edge cues are the
near sidewalk corner piece (bottom of the frame), the parked cars, two far brown ground patches and the walkers.

## Camera model (scripts: sidewalk.py, vp.py, wheels.py, calib.py, pedheight.py, width.py)
- Principal point = image centre.
- VP1 (the van road): the sidewalk right edge, van centroid track and cyclist tracks meet near (605, 62).
- VP2 (the cross road): the sidewalk left edge, the purple sedan wheel bitangent and the side-on taxi wheel bitangent
  (frame 71) meet near (3102, 79).
- Focal length:
  - The two roads are perpendicular (rounded 90° sidewalk corner), which gives f = 860 px (HFOV ≈ 103°).
  - Check: the pedestrian's walking height, from the given depth and a vertical line through the origin, is
    1.74–1.80 m at f = 860 (1.68 at 920, 1.60 at 1000), which fits an adult of about 1.8 m.
  - Van acceleration: back-projecting the given depths with f = 900–1100 gives about 4 m/s², which matches the prior.
    This route only weakly constrains f.
- Ground normal comes from the horizon (VP1–VP2). Camera height h:
  - From the pedestrian depths (pelvis about 0.9 m above the feet): h = 7.09 m at f = 860.
  - From the taxi wheelbase (Crown Victoria, 2.913 m): h = 6.92 m.
  - From the cyclist depths: h ≈ 7.1–7.25 m.
  - Pedestrian position on the far side: ground-plane feet at a = 19.49 m against 19.65 m from the depth-based pelvis,
    which agree.

## Layout (top-down, a = distance across the cross road from the camera, f = 860, h = 7.09)
- Near curb (sidewalk left edge): a = 5.54 m. The sidewalk corner's other edge is the curb of the van's road.
- Purple sedan: a ≈ 8.8–10.7. Taxi after its right turn: ≈ 13.6–15.6. Green sedan (parked along the cross road beyond
  the intersection): ≈ 12.6–14.5.
- Far brown patches (2.4 m planting or tree beds on the far sidewalk): near edges at a = 18.57.
- The pedestrian walks on the far sidewalk at a ≈ 19.5.
- Far curb is taken at the patches' near edge. Width = 18.57 − 5.54 = 13.0 m. This is stable across f = 820–940
  (13.00–13.09) when h comes from the pedestrian depth; with the taxi-wheelbase h it is 12.8 m.
- Second route (symmetry): the purple sedan centre (9.7) and the taxi centre (14.6) put the road centre at ≈ 12.1, so
  the width is ≈ 2 × (12.1 − 5.5) ≈ 13.2 m.
- The van's road, if the intersection is symmetric (curb at b = 2.2, so the far curb is near b = 15), is consistent with
  the green sedan (b ≥ 16.9) and the far patch (b ≥ 18) lying beyond it.

Answer: 13.0 m.

Confidence: moderate. The far curb itself is not rendered. If the patches are set back from the curb, the true width is
somewhat smaller (≈ 12.5 m).

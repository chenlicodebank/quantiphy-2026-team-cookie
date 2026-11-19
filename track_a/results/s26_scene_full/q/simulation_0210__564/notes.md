# Q564: height of the wooden bench (m). Prior: black cat speed = 0.94 m/s

fps = question_fps = 24, so no re-timing. The camera is static. The "wooden bench" is the slatted wooden table on the
right that holds the lamp and vases.

## Measurements (scripts: bench.py, profile.py)
- Cat pixel speed: a linear fit of x(t) gives 427.7 px/s for the mask centroid, 427.2 for the torso, 426.4 for the
  nose and 426.1 for the bbox centre. The mean per-frame |dx|×24 is 430. I used 428 px/s, which gives
  0.94/428 = 2.196 mm/px in the cat's plane.
- The cat's paws touch the floor at y≈1030 (median lowest paw; I used ~1028 for its centre line).
- Bench, from a wood-colour mask on frame 0: the top surface runs from y=791 (back edge) to ≈811 (front edge),
  followed by the front face down to 817 and the apron to 841. The front feet reach y=1005 and the back feet y=975.
- The bench sits deeper than the cat (its feet are higher in the image), so a single 2D scale is not right. I
  used ground-plane geometry with a level camera and the horizon at v0 = 540 (the image centre).
  - Camera height h = s_cat × (v_catfoot − v0) ≈ 1.07 m.
  - Bench height H = h × (v_foot − v_top)/(v_foot − v0) = s_cat × (v_catfoot − v0) × (v_foot − v_top)/(v_foot − v0).
  - Back legs (791 to 975): 0.453 m. Front (811 to 1005): 0.447 m. Average depth (801 to 990): 0.450 m.
- Sensitivity to the horizon: v0 = 400 gives 0.441 m and v0 = 650 gives 0.470 m, so the result depends only weakly
  on the assumed horizon.
- For comparison, a naive single 2D scale (the 214 px bbox × 2.196 mm/px) gives 0.47 m, which ignores the bench's
  greater depth.

## Answer
0.45 m. Confidence: moderate-good, about ±5%. The main uncertainties are the camera tilt (I assumed it level) and the
splay of the legs relative to the edges of the top.

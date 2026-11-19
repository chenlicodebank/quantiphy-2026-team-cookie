# q556: height of the typewriter (m). Answer: 0.179 m

The prior is g = 9.8 m/s² for the free fall in frames 0-10. The file and question_fps are both 24.

## Geometry
- Mat side edges (mat.py) meet at (1061, 539.5), which is the image centre. So the camera is level and the
  horizon (eye level) is row 539.5. The scene is a perspective 3D render, not flat 2D: the typewriter is seen from
  below at the top of the frame and from above at rest. Because of this, raw bbox heights (125 px at f0, 176 px at
  rest and at f10) are not the true height. The object also rolls a few degrees in the air, which adds to the bbox height.
- The paper-rest top is the highest point, and it is one fixed physical point. Its pixel acceleration (centre columns
  900-1060, frames 0-8) is 6760-6850 px/s², so s_top = 690-699 px/m at that point's own depth.
- Route 1 (cols.py): the bottom edge crosses eye level at frame ≈5.9. At that moment its image row equals the
  horizon whatever its depth, so the gap horizon − top = s_top × h exactly. The gap is 123-126 px in the
  centre columns, which gives h = 0.178-0.180 m (7 columns, mean 0.179).
- Route 2 (route2.py): the top crosses eye level at frame ≈7.45, and the gap bottom − horizon = 136.4 px. The bottom-front scale
  comes from the bottom/top velocity ratio in frames 6-9 (≈1.114), so s = 773 px/m and h ≈ 0.176 m.
- Route 3 (rest pose): bottom-front at row 1023 gives camera height 483.5/773 = 0.625 m. The paper-rest top at row 848
  gives (848−539.5)/694 = 0.4445 m below the camera, so h ≈ 0.18 m (the yaw at rest makes this rough).
- Consistency: the velocity ratios suggest a depth of about 4 m and f ≈ 2950 px (a 50 mm lens on a 36 mm sensor). The width is
  292 px / ~0.72 px/mm ≈ 0.40 m, which is a plausible full-size typewriter.

## Confidence
Good, about ±4%. Route 1 is the main result because it does not depend on the unknown focal length.

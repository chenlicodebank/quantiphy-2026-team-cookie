# q_917 – height of the mug (m)

The file rate and question_fps are both 24 fps. The prior says the mug falls at 9.8 m/s² before 1 s, and there is no depth_info.

## Scale (measure.py)
- I re-tracked the mug with my own mask: difference to a clean background, threshold 14, then an opening, keeping the
  largest component. The centroid y agrees with scene/tracks/mug.csv to within 0.1 px.
- The fall runs from frame 0 to frame 18; impact is between frames 18 and 19. I fitted a quadratic to the centroid y in
  several windows (0-16 up to 2-18). It gives a = 5083-5099 px/s², with residuals of 0.12-0.29 px. I take
  a = 5090 px/s².
- Scale: s = 9.8 / 5090 = 1.925e-3 m/px in the fall plane. x stays constant and the width stays constant, so the mug
  stays at one depth.

## Height in pixels
- The apparent height depends on the image row: 112 px near the top of the image, 88-89 px near the centre row, and
  102 px at rest. This happens because the bottom or top rim ellipse becomes visible away from eye level.
- Direct reading (measure.py): at frame 14 the mug centre is at y = 956, almost on the eye level. The mask of the
  body columns gives 88 px; the half-max edges give 86.4 px. The mug's front face is nearer than its origin, by
  about 1.4 % (r/Z), so this corresponds to about 85-87 px at the origin's depth.
- Model fit (fit_exact.py): an exact pinhole silhouette of a cylinder (radius 40.75 px, from the body width of
  81.5 px), fitted to the bbox heights of frames 0-18 and 24, 30 and 40. Free parameters: H, f and the horizon row.
  - Result: H = 86.5 px at the origin's depth, f ≈ 2990 px, horizon row ≈ 983, rms 1.1 px.
  - With the horizon fixed at 960: H = 86.3 px.

## Answer
- H = 86.4 px × 1.925e-3 m/px = 0.166 m.
- Second route: the direct frame-14 reading gives 0.164-0.167 m, which agrees.
- Plausibility: the body diameter is 0.157 m. That makes a large mug, but the gravity prior is exact and it is shown
  in the clip (a clean uniform acceleration), so I kept its scale.
- Confidence: about ±3 %.

# q_1613 — height of the floor mirror (m)

The file and question_fps are both 24. The answer is **1.47 m**.

## Focal length (focal.py)
- I took the cat's core centroid at frame 0 and frame 24. Frame 24 is partly occluded, so I extrapolated it from a
  linear fit over frames 12–23.
- I back-projected both points with the given depths (4.199 m at frame 0, 4.481 m at frame 24). Then I solved for f
  so that the 3D displacement over 1 s is 0.94 m (the prior speed, taken as constant).
- Three choices of endpoints gave f = 2099, 2132 and 2156 px (hfov about 48–49°). I used f = 2130 px.

## Geometry (geom.py, f = 2130, principal point at the image centre, no roll)
- Pitch: assuming the motion is horizontal, the cat's motion gives a pitch of −0.5° and the dog's gives +2.5°. I used
  the mean, +1.0° downward.
- Floor: the plane through the mirror's bottom centre. Pixel (1523.5, 812) at depth 6.407 m gives a camera height of
  0.68 m.
- Check: the hip heights come out sensible (cat 0.18 m, dog 0.32 m), and the dog's speed comes out 1.05 m/s. The
  front-left bench leg's bottom, placed on the floor plane, is 5.67 m from the camera; the given value is 5.69 m.
- Mirror outer frame in pixels (frame 49, measured on zoomed crops):
  - top-left (1397, 307), top-right (1563, 317)
  - bottom-left (1437, 817.5), bottom-right (1610, 806.5)
  - The mirror leans against the back wall.
- Route A (rectangle): the bottom corners are put on the floor. Each top corner is placed so that the side edge is
  perpendicular to the bottom edge. Top height: 1.462 m (left), 1.470 m (right). The lean is about 7°.
- Route B (wall): the top corners are placed on the vertical back-wall plane, which runs through the skirting line
  y = 905 − 0.068x. Top height: 1.467 m (left), 1.477 m (right).
- Rough pinhole value ignoring lean and pitch: 500 px × 6.407 / 2130 = 1.50 m.
- Sensitivity:
  - Pitch from −0.5° to +2.5°: 1.455–1.51 m.
  - f from 2100 to 2160 px: 1.49 to 1.45 m.
- The mirror's width comes out 0.64 m, so the shape (0.64 × 1.47 m) is plausible.

## Confidence
The answer is about ±3%. The main uncertainty is the focal length, which comes from the cat's gait-noisy centroid.

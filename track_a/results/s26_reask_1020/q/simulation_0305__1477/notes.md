# q_1477 – width (wingspan) of the plane

The file and the question both run at 24 fps, so frame = round(t × 24): t=1 s is frame 24 and t=2 s is frame 48.

## Scale / focal length (geom.py)
- Prior: the plane's speed is 22.16 m/s. The plane flies in a straight line at constant speed, so it moves 22.16 m
  between frames 24 and 48. The camera distances are 102.666 m and 121.826 m. The law of cosines gives an angle of
  5.706° between the camera rays to the plane's origin at those two frames.
- The origin is taken as the mask centroid from scene/tracks, which I re-measured in tips.py. Solving for the focal
  length that gives this angle: f = 3392 px. Using the bbox centre instead gives f = 3364 px.
- Check: a constant-velocity 3D path through those two points, with V = (-10.63, -6.30, 18.39) m/s in camera
  coordinates, reproduces the tracked image path. Over frames 9-71 the fit is within about 2 px; frames 2-8 are worse
  with the centroid (23 px at frame 2) but within about 4 px with the bbox centre.
- Frames 0 and 1 are identical: a duplicated first frame.

## Wingspan
The plane flies away from the camera, so the wing does not face the camera squarely: the right wingtip is about 7-9 m
further away than the left one. A plain "pixel extent × depth / f" therefore gives only 17.2-17.9 m.

- Route 1 (tri2.py): I tracked the left and right extreme silhouette points (the wingtip and fin corners) in every
  frame. Assuming the plane only moves (no rotation) with the known V, and that the wingtip vector is perpendicular
  to the direction of flight, I solved for the wingtip vector. Result: 19.60-19.88 m across frame windows (rms
  1.2-2.9 px).
- Route 2 (sfm.py, sfm2.py): I tracked about 150 features with LK optical flow from frame 2 to frame 71 and placed
  each in 3D using the known motion.
  - The body's long axis comes out within 4-8° of V, which confirms the plane flies nose-first.
  - Wingtip features: left tip at lateral +9.04 m, right tip at -10.73 m, with a vertical tilt of about 3 m between
    them. Tip to tip this is 20.0 m; the lateral extent alone is 19.8 m.
- The same calculation without the "perpendicular to flight" constraint gives a noisier 18.4-19.9 m.

## Answer
Width = 19.8 m.
- A 20 m wingspan is plausible for a jet or fighter-sized aircraft, so the scale passes the size check.
- This assumes the plane's bounding box is aligned with its own body axes (flight direction along a world axis).

Confidence: moderate-high, about ±4%. The main risks are the frame-timing offset (estimated at about 1-2%) and how
the bounding box is defined.

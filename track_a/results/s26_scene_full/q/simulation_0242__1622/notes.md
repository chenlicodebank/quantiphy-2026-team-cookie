# q1622: width of the house (simulation_0242), answer 8.06 m

The file runs at 24 fps and question_fps is also 24, so t = 1 s is frame 24. The camera is static, the principal point
is taken at the image centre, and roll is about 0: the vertical vanishing point lies at x ≈ 962.

## Focal length (scripts geom2.py, fcheck.py)
- Prior: the brown horse moves at 0.874 m/s. I fitted torso_cx linearly over frames 0-48, which skips the reset at
  frame 49. The depths at t = 0 and t = 1 then fix the 3D positions. Requiring |P(24) - P(0)| = 0.874 m gives
  **f = 2605 px**. This value does not depend on where the origin sits horizontally within the body.
- Check: assuming each animal walks parallel to camera X at constant depth Z, the given depth change alone fixes f.
  The rabbit gives 2564 px. The brown horse gives 2447 px if its origin is at the torso centroid, or about 2600 px if
  the origin is about 60 px further back (the hip). The motion vectors confirm that all three animals move along
  camera X.

## Ground plane and the wall's depth (width.py, upper.py, edges.py, corners2.py)
- I took the ground contacts (bbox bottom), back-projected them with the given depths, and fitted the plane
  y·cos p + z·sin p = H. With f = 2605 this gives a pitch of 35.9° and H = 9.44 m. The residual SD is only 0.015 m
  across the 6 points (3 animals × 2 times).
- Independent check of the pitch from the building's vertical corner edges: they slope about 0.12 px/px, which puts
  the vertical vanishing point near y ≈ 4400 and the pitch near 34°. The window frame edges give a noisier 43°.
- The wall base line is at y ≈ 376 at the image centre. Intersecting it with the ground gives a camera depth of
  Z ≈ 17.6 m at the wall base. The brick storey works out about 2.1 m tall, the windows about 0.77 m wide, and the
  horse about 1.7 m tall, so the scale is plausible.

## Widths
- Brick ground floor, base corners x 463-1461 (998 px): **6.76 m**. Between pitch 33° and 43° and f from 2450 to
  2605, this ranges from 6.6 to 7.2 m.
- Timber upper storey, x ≈ 320-1600 (1280 px), which overhangs the brick on both sides. It sits at the top of the
  brick wall, where Z ≈ 16.4 m: **8.06 m** (range 7.7-8.5).
- I answer with the upper-storey extent. The reference sizes are world axis-aligned bounding boxes, and the house's
  box includes the overhanging upper storey. The roof is cropped by the frame top, and wider eaves could make the
  true box slightly wider. If only the brick wall counts, the answer would be 6.8 m.
- If "width" meant the shorter horizontal side, that is the house's front-to-back depth, which is not visible. I
  answer with the horizontal extent across the visible facade.

## Confidence
The geometry is good to about ±4%. The main uncertainty is which part of the house is meant (brick 6.8 m vs whole
house 8.1 m).

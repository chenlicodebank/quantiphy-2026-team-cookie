# q 2670 - length of the table (m)

Lab video, 24 fps (file fps = question fps = 24), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
Prior: ball diameter 4 cm. depth_info: ball at t=0.9 s (frame 22) 1.010 m, at t=1.4 s (frame 34) 0.716 m.

## Geometry problem
The table top is seen at a grazing angle (camera only ~18 cm above the top), with its long axis pointing away from
the camera, so the pixel-extent x depth / f rule cannot be applied directly. I reconstructed the table-top plane:
- `table_edges4.py`: on frame 48 (checked on frame 43, identical to 0.3 px) the 4 table-top edges were fitted as lines:
  side and back edges = half-level crossings of the feathered (SAM-composited) saturation transition, front edge =
  steepest brightness drop to the dark front face. Corners: BL (418,437), BR (761,444), FL (185,586), FR (997,592).
  The record's right-edge line equation (x = 1.782y - 40.5) was inconsistent with its own FR corner; corrected.
- Vanishing points: long axis (side edges) (582.5, 332.1); lateral (front & back edges) (11070, 663.5).
  Plane normal = cross product of the two VP directions. Check: back-projecting the quad onto this plane gives a
  rectangle with corner angle 89.8 deg (independent check of the orientation).
- Plane offset: ball centres at frames 22 (569,457) and 34 (838,513) (circles verified on zoomed crops,
  frames/ball_crops.png) back-projected with the given depths; table top = 2 cm (ball radius) below them.
  Camera height above the top: 0.1838 (frame 22) / 0.1740 (frame 34), mean 0.1789 m.
- Result (`geom2.py`): front = back = 0.567 m (width), left = right = 0.731 m (long horizontal extent = length).

## Second routes / checks
- Scale from the prior alone (ball diameter vs image position fitted over frames 14-35, `ball_plane_fit.py`):
  camera height 0.1746 m -> length 0.713 m (diameter-implied depths are 2.6-5% below depth_info).
- Edge-noise perturbation (`sensitivity.py`, side edges +-2/3 px, back +-1.5 px, front +-0.7 px):
  length 0.73 (16-84%: 0.712-0.750), width 0.567 +-0.004.
- Alternative normals forcing equal ball heights (`geom3.py`) give non-rectangular quads (83-85 deg, left != right),
  so rejected; they span 0.70-0.83 for the side lengths.

Answer: length = 0.73 m (width 0.567 m). Confidence: about +-3-4 %.

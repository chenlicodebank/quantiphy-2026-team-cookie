# q 2545 — length of the table (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720, f = 0.5959*1280 = 762.75 px, principal point (640, 360).
Prior: tennis ball diameter 6.7 cm. depth_info at t=1.5 s (frame 36): tennis ball 1.183 m, ping-pong ball 1.353 m.

## Method (scripts: edges.py, recon.py, check.py)
1. `edges.py`: table-top mask (non-background) -> least-squares lines for the left/right side edges (per-row extremes),
   the back edge (per-column top) and the front top edge (vertical gradient between top surface and front face).
   Corners (frame 48): BL (573.8,423.3), BR (852.4,426.1), FR (963.3,494.9), FL (460.0,482.4); frame 10 almost the same.
   Overlay frames/edges_f48.png sits on the edges.
2. `recon.py`: vanishing points of the side edges (723,346) and of the front/back edges (-3656,381) give the horizon line ->
   table-plane normal (K^T l). The angle between the two edge directions comes out at 86 deg (should be 90 deg, so a small model error).
   Plane offset: tennis-ball centre at f36 = 1.183 m x unit ray of its pixel centre (583.0,433.5); plane = centre - 3.35 cm along the
   normal -> camera 0.167 m above the table plane. The corner rays intersected with the plane give the 3D corners.
   - front edge 59.0 cm, back edge 59.0 cm (across the view)
   - side edges (front-to-back) 72.6 cm (centroid centre) / 73.7 (circle-fit centre); frame-10 corners: 70.9 / 71.9.
3. `check.py` (second route): the plane model predicts that the resting tennis ball (frames 0-21) is at 1.597 m. Its apparent
   diameter of 32-33 px gives 1.55-1.60 m with 6.7 cm, so the plane tilt and offset agree to within about 2 %. Scaling with the
   rest-size depth (32.5 px -> 1.572 m) instead would give about 71.2 cm.
   The ping-pong depth (1.353 m) would give H = 0.178 m -> 77-78 cm. However, the ping-pong ball's own image (29 px wide at f36, lower in the
   image than the tennis ball) does not fit that depth for a 4 cm ball. The tennis-ball route (prior object, two independent checks) is used.

## Result
Table top about 72 cm front-to-back x 59 cm across. "Length" = the longer horizontal extent -> **72 cm**
(the reading as the side facing the camera would be 59 cm).
Confidence: moderate. The front-to-back extent is sensitive to the plane tilt (near-grazing view); the estimated uncertainty is about ±4 cm.

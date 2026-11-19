# q1354 — width of the turning yellow car (taxi), simulation_0067

Answer: **1.92 m** (file fps 24 = question_fps 24; frame = round(t*24); t=0.58 -> frame 14, t=1.58 -> frame 38).

## Object
"Turning yellow car" = the yellow/orange taxi (scene/ "taxi"). It drives up the diagonal road, turns right by ~90 deg
(frames ~16-56) into the right-hand road. Width = shorter horizontal extent (local car width; at frame 0 the car is
aligned with the road).

## Camera calibration (f)
- Vertical VP from 8 pole/lamp shafts fitted in code (poles.py): (1080, 2642), stable to +-10 px when dropping any one pole
  -> roll 0, principal point x = centre.
- Road VPs from Hough curb lines (curbs.py): VP1 (2711,-47) [right road], VP2 (115,-47) [diagonal road]; horizon y=-47.
- f from VP1.VP2 orthogonality = 1109 px; from vertical VP + horizon = 1111 px -> **f = 1110 px**, pitch 27.9 deg.
- Prior (van a = 4 m/s^2) only loosely constrains f (bbox-centre van track gives 4.4 at f=1110, but the van's
  near-camera bbox centre is biased; heights at f14/f38 disagree by 0.3 m); not used for the scale.
- Check with depths: taxi silhouette fit (scale-free) rescaled by the depth at f38 gives scale 0.9563; the depth at
  f14 (pose extrapolated from f16-21) gives 0.9561 when the origin is at the box centre -> f and the origin assumption
  reproduce both given taxi distances to 0.1 %. Pedestrian walking bbox height 1.81-1.88 m; camera ~7.25 m above road.

## Width measurement
1. Silhouette masks of the taxi (mask2.py: bg difference, shadow and white-van pixels removed, holes filled), frames 16-65.
2. Route A, 3D model fit (silfit2.py): body box + cabin + sign + tire contacts, heading and position per frame,
   convex-hull distance residuals (rms 3.4 px); metric scale from the depths (analyze.py). Body box W = 1.856 m
   (L 4.44, sign-top height 1.56). With mirror points: body 1.84 m. The box's sharp corners overshoot the rounded car
   in 3/4 views, so this W/L is biased low (L keeps shrinking with iterations).
3. Route B, tail-on frames (tailon.py, profile.py, rows.py): fitted heading equals the viewing azimuth at frames 33-34
   (relative yaw +1.1 / -0.6 deg). Widest silhouette rows 146-150 px (rows y 430-478 = rear corners at trunk height).
   Projecting rear corners (1.9-2.5 m behind the centre, 0.5-1.0 m high) with the metric pose: W = 1.91 (f33), 1.95 (f34),
   with +-0.02 from corner position/height assumptions. Mirror tips (y~372-384): span ~126 px further forward -> ~1.9 m,
   i.e. the mirrors do not stick out beyond the body width, so the bbox width = body width.
4. Frames 35-37 grow wider (side becoming visible) and are not used for B.

Routes: A 1.86 (biased low by box corners), B 1.91-1.95. Answer 1.92 m (B weighted). If the widest point were at the
rear wheel arches rather than the rear corners, B would give ~2.0 m. Confidence: moderate (+-4 %).
Note: the video looks upscaled 2x (silhouette edges fall on even pixels), so extents are +-2 px (~1.3 %).

# q_1476 – length of the plane (simulation_0305)

Answer: **14.4 m** (nose-to-tail extent along the body / pod axis).

## Scale (focal length) – geometry.py / jac.py / fitf.py / spanfit.py
- question_fps = file fps = 24. Frames 24 (t=1 s, d=102.6664 m) and 48 (t=2 s, d=121.8263 m).
- Rays through the aircraft mask centroids (scene/tracks/aircraft.csv; cx,cy) at frames 24 and 48, principal
  point (1280,720). Requiring |P48 - P24| = 22.16 m (constant speed, 24 frames) gives **f = 3391 px** (HFOV 41.4 deg).
  The motion is mostly away from the camera (depth +19.2 m per s, lateral about 11 m per s); its direction in camera coordinates is
  a = (-0.48,-0.28,0.83).
- Since a chord can never be longer than the path, the prior forces f >= 3391. A check from apparent size (bbox_w x depth
  vs the foreshortening of an axis perpendicular to a, frames 2-71) fits best at f of about 3400-4000 (rms 0.7 pct) and
  reproduces the 13.6 pct growth of size x depth over the clip, so f = 3391 is consistent. Shifting the origin off the
  centroid by a few metres changes the result by less than 0.1 m.
- Track-only and feature-residual fits weakly prefer a smaller f (2500-3000; residuals 1.7 px vs 2.3 px). That would
  break the exact speed prior, so I did not use it. It is the main source of uncertainty (f=3000 would give 15.5 m).

## Orientation (which image axis is the length)
- The long horizontal image extent (about 20 m) is perpendicular to the motion. Two long pods (cylinders with rounded
  front and pointed rear) are separated purely along that axis (8.8-8.9 m, the same in frames 2 and 71). Their image
  length shrinks like the motion-direction foreshortening (pitched about 11 deg nose-up): the body / pods run along the flight
  direction. So the horizontal extent is the **wingspan** (wingtip fins at both ends, about 20.7 m tip to tip), not the length.

## Length – tri.py (frames 2/36/71) and tri2.py (frames 12/60)
Hand-picked features were triangulated in the object frame, assuming rigid translation along the straight
constant-speed path through the two given depths. Residuals were 0.3-2 px.
- Rearmost: tip of the centreline ventral triangle fin, -7.54 m along the body axis (route 2: -7.89).
- Frontmost: rounded front of the left pod, +6.76 m (route 2: +6.65). The nose probe on the centreline is at +6.14 / +6.22.
- Length along the body axis: route 1 = 14.30 m, route 2 = 14.54 m. Along the motion direction a: 14.2 m.
- Final answer 14.4 m (mean). Other extents: wingspan about 20.7 m, pod length 9.4 m.

Confidence: moderate. The orientation analysis is solid. The scale depends on f from the speed prior (+-5-8 pct),
and some extreme point might be hidden inside the silhouette (would add a few tenths of a metre at most).

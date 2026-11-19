# q1364 – height of the walking pedestrian (simulation_0074)

Answer: **1.96 m**

Time base: file fps = question_fps = 24, no re-timing issue.

## Camera (fixed, 2160x1080)
- `vp.py`: sub-pixel kerb edges (road -> kerb transition) on 7 kerb lines, two orthogonal road directions.
  VA = (-1364, -280), VB = (2739, -279) -> horizon y = -279.5, roll ~0. f(VA,VB) = 1840 px.
- `poles.py`: centre lines of 7 lamp/signal poles -> vertical VP (1097, 4736).
  f(A,vert) = 1865, f(B,vert) = 1846, f(horizon,vert) = 1854; orthocentre of the three VPs = (1097, 527),
  i.e. at the image centre (consistency check), f = 1842. Used f = 1850 px (HFOV ~60 deg), pitch 23.9 deg down.

## Pedestrian pixels
- `ped.py`: median-background subtraction in a window around the record's bbox; head-top / lowest foot per frame.
  Frames 0-9 (clean, feet on sidewalk, no occluder): top 156-158, bottom 254-255 -> ~98 px.
  Frames 10-18 bottom drifts to 257-259 (shadow / bin) -> not used. Frames 19-46 feet behind the bin.
  Frames 58-68: my mask picks up a spurious blob below the feet, so feet taken from the record (bottom_y 232-235).

## Height (height.py)
Foot pixel ray -> vertical segment of height H in the world (up vector from pitch) whose top projects onto the
head-top row; scale fixed so that the pelvis (0.53 H above the feet) is at the given camera distance
(linear interpolation/extrapolation of 37.07 m @0.58 s and 37.90 m @1.58 s).
- frames 0-9: 1.93-1.96 m (f=1850); f=1840 -> +0.5 %, f=1865 -> -0.8 %.
- frames 58-68 (late.py, depth extrapolated to ~38.8 m): median 2.00 m (less reliable: record feet, extrapolated depth).
- naive d*px/f = 37.0*99/1850 = 1.98 m.
Answer 1.96 m (weighted towards the clean early window).

## Checks
- `depthcheck.py`: with camera height 9.63 m from the pedestrian route, the given depths of taxi, van and cyclist
  imply origin heights of 0.7-1.0 m (taxi), 1.0-1.3 m (van), 0.9-1.0 m (cyclist), pedestrian pelvis 0.9 m and feet
  at ~0 m: all physically sensible object-centre heights -> geometry and scale consistent across objects.
- `vancheck.py`: van wheelbase from eyeballed wheel contacts 3.25 m (0.54 of the 6 m length; eyeballed contacts
  uncertain by ~10 %), van ground-centre depth 31.6-31.9 vs given 31.28 (~1-2 %). Rough only.

Confidence: moderate-high; main uncertainties are walking-phase height variation (~±2 %) and f (~±1 %).

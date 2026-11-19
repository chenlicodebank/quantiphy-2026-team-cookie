# q1175 — height of the walking person (simulation_0045)

File fps = question_fps = 33, so t=1 s is frame 33 and t=2 s is frame 66.
Pedestrian = white T-shirt, on the right sidewalk. Cyclist/bike = dark jacket, blue bike.
Pixel tracks from scene/ were checked on frames 0/33/66/98 (frames/crops.png). The boxes fit both people.
Pedestrian height_smooth_px: 314.4 at frame 33 and 280.0 at frame 66. Cyclist (head to rear wheel): 284.6 and 195.4.

## Problem: depth_info does not match the image
- Height ratio (1/Z) between t=1 and t=2: pedestrian 1.12 vs depth ratio 1.070; cyclist 1.44 vs 1.394.
  No focal length or principal point fixes both (consist.py, solve.py, grid.py).
- Taken literally (pedestrian at 17.2 m, bike at 12.1 m), the pedestrian's feet would be 1.49x farther below the
  camera axis than the bike wheel (ratio does not depend on f). They would be about 0.5-1 m below the road, but the
  pedestrian stands on a raised sidewalk on a street that rises away from the camera. Impossible.
  In the image the pedestrian's feet (row 572) sit at about the cyclist's wheel row (563). So the pedestrian is at
  about the same depth as the bike, slightly nearer.
- Conclusion: the pedestrian's depth_info does not describe the body seen in the render (probably an offset origin).
  The bike's depths do agree with the speed prior: d rises 4.78 m/s, |dP| = 4.83-4.96 m over 1 s for f = 1000-2000.

## Focal length (manhole covers, independent of depth_info)
- Road-plane horizon from the cyclist's wheel-contact row vs pixel height: v - 209 = 1.243*h, linear for frames 9-96.
- Near manhole: ellipse fitted in code (manhole2.py, frames/near_ring.png). Aspect 0.254-0.262, so the view hits the
  road at 15 deg; atan(353/f) + atan(174/f) = 15 deg gives f ~ 2000 px.
- Far manhole (row ~407): aspect ~0.093 gives f ~ 2100 (rough).
- The speed prior is met at f = 2000 (|dP| = 4.83 vs 4.87). Only a weak check: any f from 1300 px up gives 4.79-4.9.
- f = 2000 makes things realistic: rider+bike 1.65-1.72 m, parked bike ~1.2 m, manhole ~0.9-1.06 m.

## Pedestrian height
Route 1 (depth matching through the curb): a cross-street line (VP ~ (11600, 383), slope 0.018) runs from the
pedestrian's foot to the curb. The curb's road edge is about 20 px lower, and that road row matches the cyclist's
wheel row at frame ~26 (t=1 s) or frame ~34 (t=2 s). Using the bike depth there (interpolated linearly):
- t=1: 314.4 * 11.1 / 2000 = 1.745 m
- t=2: 280 * 12.27 / 2000 = 1.72 m

Route 2 (sidewalk vs road plane):
- Pedestrian (v_foot - 209)/h ~ 1.17 on average; road gives 1.243 for the cyclist.
- Curb height is ~4-7 % of the camera height (curb face 16-27 px at row ~578).
- So H_ped ~ 1.00 (0.985-1.017) x H_cyclist_rig.
- H_rig = 285 * 12.09 / 2000 = 1.72 (t=1) and 1.65 (t=2). If the bike origin is ~0.4 m ahead of the rider/rear
  wheel: 1.67 / 1.61.

Combined: 1.64-1.75 m. Answer **1.71 m**. This is the mean walking height from the smoothed pixel height; standing
height may be ~1-2 % more.

Not used: the literal reading (pedestrian depth 17.17 m x pixel height / f) gives 2.6-2.7 m at f = 2000
(3.4-3.6 m at f = 1450). It conflicts with the image geometry above.

Confidence: moderate. Scale error is about ±7 % (f ±5 %, bike origin offset ±4 %). The main risk is that the reference
used the literal depth (~2.6 m).

# Q1365 – average speed of the yellow taxi, start to end (m/s)

Answer: **4.14 m/s**

## Time base
fps = question_fps = 24, 72 frames (0..71). Frames 0 and 1 are identical (mean abs diff 0.02 grey levels, vs 0.3 for
later pairs), so frame 0 is a duplicate of frame 1 in the render.

## Camera (3D scene, static camera)
- Focal length, route 1: vanishing points of the two road directions from kerb edges fitted in code (`vp.py`, rms 0.3-0.6 px,
  kerbs drawn on `frames/kerbs.png`). With orthogonal roads and the principal point at the image centre, f = 1776 px.
- Focal length, route 2: vertical VP from 7 poles/lamp posts (`vvp.py`) combined with the horizon -> f = 1795-1828 px
  (it does not assume the roads are orthogonal). Used f = 1795 px (hfov ≈ 62°).
- Ground-plane normal from the two road VPs. Check: with the given depths, each object's origin comes out at the same
  height above the ground plane at t = 0.58 and 1.58 s (pedestrian centroid -8.61/-8.61, taxi sign plane -7.85/-7.83).
  The camera is about 9.6 m above the ground (from the pedestrian's feet).
- The van prior (6 m) was used only as a sanity check: its wheelbase at frame 71 comes out at 3.88 m, which is plausible
  for a 6 m Chevy Express-type van. This check is only weakly sensitive to f.

## Taxi track
The taxi turns left: it heads toward the camera, then turns to drive up-left. On a turn, path length depends on how far
the tracked point is from the car's centre line. So I tracked the roof taxi sign, which sits on the car's centre line
mid-roof (`sign.py`, a saturated-yellow blob on the roof). It is visible in all 72 frames and is not hidden by the cyclist.
Each frame's sign ray is intersected with a plane parallel to the ground. That plane's offset is solved so that the origin
(sign minus δ along the up-normal) reproduces the given taxi depths, 31.0495 m at frame 14 and 30.4267 m at frame 38.
The offsets from the two frames agree to 0.015 m. Speed = per-frame backward difference × 24.

| f (px) | δ = 0.8 m: mean per-frame speed, frames 2-71 |
|---|---|
| 1776 | 4.18 |
| 1795 | 4.14 |
| 1828 | 4.08 |

- Changing δ from 0 to 1.6 m changes the result by about ±0.03.
- The per-frame speed is constant at about 4.1 m/s (noise ±0.2, no trend), so the taxi drives its curve at constant speed.
- Including the zero step from the duplicated frame 0→1 gives 4.08; 3-frame smoothing gives 4.05. I answer with the
  constant-motion value, 4.14.

## Second route
For frames 22-71 (unoccluded), I took the record's taxi tracks, intersected them with the plane through the frame-38
depth point, and computed the speed. Bbox centre gives 4.32 (noisy bbox edges) and mask centroid gives 3.96; the sign
route gives 4.15 over the same frames. The chord speeds for frames 21→71 agree within 3% (3.90 sign, 3.84 bbox, 3.79
centroid); the small differences come from points off the centre line on a curved path.

Confidence: about ±4%. The main uncertainty is f (1776-1828).

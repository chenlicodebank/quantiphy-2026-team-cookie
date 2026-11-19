# q1318 – average speed of the yellow car (taxi), start to end — answer 3.90 m/s

The video is a 3D Blender render: 2160x1080, 24 fps, 72 frames. question_fps is also 24, so there is no time-base issue.
Frame 0 is an exact repeat of frame 1 (mean |diff| 0.03 grey levels), so nothing moves in the first interval.
Average speed = mean of the 71 per-frame speeds = path length / (71/24 s), with the f0→f1 step equal to 0.

## Camera (static)
- Road vanishing point VP1 = (809.2, -195.8). Fitted from the far-road curbs plus the near-right sidewalk edge, which is
  collinear with the far-road right curb (`vp1.py`).
- Vertical vanishing point VP3 = (1033.5, 7621.7). Least-squares intersection of 4 poles (near-right lamp, near-right and
  near-left traffic-light poles, far-right lamp); all 4 pass within ±7 px of it (`poles.py`, `vp3calib.py`).
- Principal point taken at the image centre. f from the VP1 ⟂ VP3 condition: **f = 2280 px**. Ground normal from VP3.
- Rejected: the cross-street VP2 (from near-horizontal curbs, `curbs.py`). With the centre principal point it gives
  f = 2067 (pair VP1–VP2) and 2389 (pair VP2–VP3); the orthocentre solution puts the principal point at y = 358. These are
  inconsistent, so the cross street is probably not exactly perpendicular, or VP2 (about 18,700 px away) is poorly
  determined. Path length depends only on the ground plane and f, not on VP2.
- Checks of f = 2280 (`fconsist.py`): the pedestrian walks parallel to the cross street (within 1°) at about f = 2240.
  The heights implied by the depths are plausible at f = 2280–2350: pedestrian pelvis about 1.0–1.25 m, cyclist hips
  about 1.0–1.2 m, van centre about 1.0–1.2 m, taxi roof sign about 1.8–2.0 m above the taxi origin.

## Taxi path (main route: roof sign)
- The scene/ bbox centre is a biased origin proxy. The car turns 90° (rear view to side-on), and the bbox centre drifts
  across the car. At t = 0.58 s and 1.58 s, intersecting it with one fixed plane misses the given depths by about
  ±0.2 m in opposite directions. A free 3D box-model fit was unstable (`boxfit.py`, `corrfit.py`; not used).
- Instead I tracked the TAXI roof sign. It is rigid, sits mid-roof near the car's vertical centre axis, and is at a
  fixed height. Tracking was NCC template matching from frame to frame (`track_sign2.py`):
  - forward from f0 (1075, 494), valid to f40;
  - backward from f71 (1722, 335), valid from f45;
  - f41–44 (sign hidden behind the signal pole/heads) bridged by a smoothing spline.
- Sign positions → horizontal plane at drop `a` below the camera. The origin is taken as the sign plus 0.25 m along
  the heading, at drop `b`. `a` and `b` are solved from the two given taxi depths (23.7441 m at f14, 27.0055 m at f38).
- f = 2280: a = 6.11 m. Path over f1–71 = 11.55 m → **3.903 m/s** (`final_answer.py`). Speed profile is about 3.8–4.15 m/s
  throughout.

## Sensitivity
| Variant | Average speed (m/s) |
|---|---|
| f = 2200 / 2280 / 2350 | 3.98 / 3.90 / 3.84 |
| Sign-to-origin offset 0, 0.25, 0.5 m | ±0.5 % |
| Forward/backward junction 38/47 instead of 40/45 | 3.899 |
| Less smoothing | 3.945 |
| Counting f0→f1 as a normal step (70 speeds instead of 71) | about 1.4 % higher |

## Checks
- **Prior, white van a = 4 m/s²** (`van_check.py`). With the same camera, the van's bbox-centre track on the plane fixed by
  its two depths gives a = 4.04 (centre), 3.84 (top) and 4.16 (bottom) m/s², starting from near rest. This confirms the
  metric scale from depth_info.
- **Route 2, taxi bbox** (`route2.py`): bbox top-centre gives 4.00 m/s and bbox centre gives 4.26 m/s at f = 2280. Both are
  higher because the bbox centre shifts across the car during the turn and is noisier. I trust the sign route.
- An early run used the cross-street VP and f = 2067 and gave about 4.1 m/s. That frame was rejected (see Camera).

## Confidence
Moderate to good, about ±4 %. The main uncertainty is the focal length (f between 2200 and 2350 gives ±2 %), then the
duplicate first frame (1.4 %).

## Data notes
- scene/ times were computed at 24 fps, the same as question_fps.
- scene/ taxi track: the y1 jitter and the hidden x0 at f56–58 are confirmed. Its bbox centre is not a good origin proxy
  during the turn.

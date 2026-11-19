# Q2862 – velocity of the green ball at 1.5 s (frame 36)

File fps = question fps = 24. Frame 36 = t 1.5 s. Camera f = 0.5959·1280 = 762.8 px, principal point (640,360).

## Identification
- green ball = the small yellow-green (tennis) ball, `scene/tracks/yellow_ball.csv`; white ball = the pale
  small ball (`pink_ball.csv`). Both are about 3.04–3.07 m away at t=1.0, in the standing person's hands, which
  matches depth_info. (The soccer ball would come out about 0.28 m across at 3.07 m, so it is not the "white ball".)
- orange ball = basketball.
- I checked the track centroids on zoomed frames 24 and 33-39 (view.py); they are correct.

## Dropped frames
Both small balls jump about 2.2× their normal per-frame step between f35 and f36. The basketball does the same
between f11 and f12 (31 px instead of about 16). That looks like one source frame dropped per second, e.g. a
25→24 fps conversion. The 3D fit puts the gap at δ = 0.87–1.06 extra frame intervals, so about one missing frame.
Both the prior's time (f12) and the question's time (f36) fall right after one of these gaps.

## 3D trajectory (depth at 1.5 s is not given)
- ballfit.py fits both small balls jointly as gravity arcs (|g| = 9.81, shared gravity direction, fitted gap δ)
  through frames 23/25–36. Anchors: |P| = 3.0735 m (white) and 3.039 m (green) at f24. RMS 0.83 px. Result:
  green at f36 is 2.38 m away, instantaneous speed 5.10 m/s.
- profile.py fixes the camera tilt over a range of values. The instantaneous speed at f36 stays at 4.7–5.25 m/s.
- fullfit.py adds the bounce on a common floor plane (green bounces at about f37, white at about f38) and fits the
  post-bounce frames up to f41. The floor is optionally tied to the rolling basketball centre.
  - With the floor tie: f36 at 2.35 m, instantaneous speed 5.00 m/s.
  - Without it: f36 at 2.51 m, instantaneous speed 5.04 m/s.

## Calibrating the convention with the prior (orange 2.21 m/s at f12; orange2.py)
The basketball depth is taken as linear in real time between the given depths (2.3557 m at f12, 1.81 m at f24).

| convention at f12 | orange speed (m/s) |
|---|---|
| true (clean) speed | 1.60 |
| backward difference (spans the dropped frame) | 3.04 |
| forward difference | 1.60 |
| central difference | 2.32 |
| 3-frame mean | 2.07 |
| 5-frame mean | 1.87 |

The prior (2.21) lies between the 3-frame mean and the central difference. So the reference is inflated by the
dropped frame through light (about 3-frame) smoothing.

The same conventions for the green ball at f36:

| fit | 3-frame mean | central difference | interpolated like the prior |
|---|---|---|---|
| floor tie | 5.26 | 5.82 | ≈ 5.57 |
| no floor tie | 5.54 | 6.33 | ≈ 5.98 |

Other values: instantaneous speed 5.0; backward difference 8.7–9.6 (rejected, it did not reproduce the prior);
forward difference to the bounce 3.1.

## Answer
**5.5 m/s.** It sits between the instantaneous physical speed (about 5.0) and the prior-calibrated convention
values (5.6–6.0).

Confidence: moderate. The physics is robust at about 5.0 ± 0.2 m/s. Most of the uncertainty comes from how the
reference handled the dropped frame and the bounce at f37.

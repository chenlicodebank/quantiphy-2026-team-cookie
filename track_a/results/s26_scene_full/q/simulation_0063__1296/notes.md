# Q1296: length of the white car (the white cargo van), in metres

Prior: the van's acceleration is 4 m/s². Depths of the van origin: 29.2444 m at t=0.58 s (frame 14) and 29.8093 m at
t=1.58 s (frame 38). question_fps = file fps = 24, so the frame numbers below are the same in both.

## Observations
- The "white car" is the white cargo van (scene/ calls it `van`). It drives left to right and **recedes**: its rear
  face is visible in every frame (it is 24 px wide at f30 and 65 px wide at f71), so its heading points well away from
  the camera (about 28° from the image x-axis). A plain metres-per-pixel scale would be wrong here.
- The camera is static and close to level (horizon at y≈532). Principal point assumed at (1080, 540).

## Measurements (my scripts, kept in this folder)
- `windows.py`, `wintrack.py`, `wintrack2.py`: colour mask of the van's two brown cargo windows (near side).
  The left edges give clean rigid-point tracks: window B over f0-42 and window A over f14-71 (about 1 px noise).
- `early.py`: sub-pixel template match of the windows over f0-15. The motion is a clean quadratic (uniform
  acceleration) with a small start speed.
- `rearedges.py`: rear silhouette from |frame − clean background|. The body edge and the rear bumper edge are
  separate; the bumper sticks out 5-10 px past the body.
- `edges.py`: the front bumper at f69/70/71 is at x = 1392/1417/1441, about 5 px beyond the record's `bbox_x1`,
  which stopped at the body. Late `rear_x` in the record (f69-71) is the body edge, because the taxi hides the bumper.
- Rear-face/side crease, read by eye on 4x zooms: f30 82, f38 255, f50 557, f56 720, f71 1146.

## Model (`fit4.py`)
- Top-view box model with a level pinhole camera. The origin is the bbox centre C(t) = C38 + s(t)·d, with s uniformly
  accelerated. The box is L × W, with a rear-bumper overhang b.
- Fitted to all the pixel tracks above plus the two depths. The unknowns are f, the heading, C38, v38, L, W, b and
  the two window offsets; a is fixed to the prior's 4 m/s².
- Result with a = 4: f = 2147 px (hFOV 53°), heading 28.0°, v(t=0) = 0.17 m/s, **L = 5.80 m**, W = 1.80 m.
  The window-track rms is 0.95 px, and D14/D38 are reproduced as 29.232/29.821 (given 29.244/29.809).
- Sensitivity:
  - Weighting my crease readings more pulls W to 2.0-2.1 and gives L = 5.73 / 5.70. The box can't fit the body edge
    and the crease exactly, because the corners are rounded.
  - Shifting the crease readings by ±4 px changes L by under 0.01 m.
  - Shifting the front edge by ±3 px moves L to 5.74 / 5.86.
  - The origin's image row (centre or bottom) has no effect.
  - Forcing the van to start from rest at t=0 fits much worse (cost 967 vs 168), so I rejected it.

## Second route and checks
- Leaving the acceleration free (the depths + perspective fix f on their own) gives a = 4.10 m/s², f = 2094 px and
  L = 5.99 m. That is within 2.5 % of the prior's acceleration, so the geometry and the prior agree. I answer with the
  prior-constrained fit.
- The cyclist's 3D heading, computed from its own two given depths, is 27.5-29° for any f. That matches the van's
  fitted 28°, so the road direction is consistent.
- Sanity: at f = 2147 the man is about 2.0 m tall, the van about 5.8 m long and 1.8 m wide, and the camera about
  2.3 m high, all plausible real-world sizes.

## Answer
L ≈ 5.77 m: the mean of the a = 4 fits (5.70-5.80), measured bumper to bumper. Confidence: roughly ±4 %, limited by
the box-corner approximation and the acceleration-to-focal-length step.

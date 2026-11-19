# q_1889: acceleration of the astronaut at t = 3 s (frame 72 at 24 fps)

The file fps and question_fps are both 24, so t = 3 s is frame 72.

## Scale
- Prior: astronaut height 2.2 m. depth_info: 18.147 m at t = 1 s (f24).
- At f24 the legs are close together and the bbox height is about 380 px (smoothed). That gives a focal length of
  f = 380 x 18.147 / 2.2 ≈ 3135 px (HFOV ≈ 40°).
- Depth at other frames: distance ∝ 1 / apparent size. The size comes from the bbox height (scene track) and from the
  width of the upper-body band (`rigid.py`). Template registration of the scale (`regscale.py`) had low correlation
  because the body turns, so I did not use it.
- Ground-plane sanity check: the foot-contact rows (f12 at y=1013, f72 at y=1055) and the depths from size give a
  horizon near y≈827 and a camera height of about 1.2 m. The pelvis sits near the horizon, which is consistent.
  Between f16 and f60 the body rises about 0.7 m, matching a lunar hop (g=1.62 over 1.83 s gives 0.68 m). This
  supports a fixed camera.

## Motion near t = 3 s
- After landing at about f60 the astronaut walks and turns slightly toward the camera.
- The image x-speed falls steadily: 11 px/f (f60-67), 8 (f68-73), 6.5 (f74-79). Converted with the depth, the lateral
  speed goes about 1.4 → 1.0 → 0.8 m/s, a lateral deceleration of about -0.9 to -1.1 m/s².
- The depth falls from about 17.1 to 15.9 m over f60-79, but part of the bbox-height growth comes from the legs
  straightening, so the radial rate is uncertain.
- `final.py`: 3D pelvis/centroid path for several depth models, Savitzky-Golay smoothing, and the slope of the scalar
  speed over f64-79:
  - linear depth from height: -0.7 m/s²
  - constant depth: -1.2 m/s²
  - depth from the foot plants: -2.2 m/s²
  - quadratic depth: +2.5 m/s². I rejected this one: it just follows the bbox-height growth that the leg pose causes.
- The raw one-frame differences are far too noisy to use; the reference value from a mocap root may itself be noisy.

## Answer
The astronaut is decelerating. I answer with the magnitude, about **1.0 m/s²** (the middle of the -0.7 to -1.2 range
from the more credible models).

Confidence: low to moderate. The depth rate near the end is the main uncertainty.

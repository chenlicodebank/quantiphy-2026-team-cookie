# Q1409: astronaut speed at t = 1 s (m/s)

**Answer: 5.15 m/s.**

## Setup
- File and question both run at 24 fps, so t = 1 s is frame 24.
- Speed is the backward difference of the 3D pelvis/root, |p24 - p23| x 24.
- Scale comes from:
  - the prior: the astronaut is 2.2 m tall;
  - depth_info: 18.147 m at frame 24.
- The camera is static.

## Where the candidates part ways
- **C1 (5.2):** uses f ≈ 3200 px and includes motion toward the camera (dZ ≈ -2.2 to -2.7 m/s).
- **C2 (4.0):** treats the motion as purely in the image plane, which drops the depth part. It also uses f = 3465, from a 420 px "standing height". That figure is the walking height near the end of the clip, when the astronaut is about 19 % closer to the camera, so it was not corrected back to frame 24's depth. Both of C2's steps bias its answer low.

## My measurements
Scripts: `scale_track.py` and `speed.py`; outputs in `scale_pack.npy` and `scale_upper.npy`.

**Depth change (`scale_track.py`).** A similarity fit of a rigid template from frame 24 to all 80 frames, with two templates: the backpack, and backpack + helmet + upper torso.
- The apparent scale grows from 0.93 (frame 0) to 1.19 (frame 79).
- Around frame 24 the scale rate is about 0.0045-0.0061 per frame, so dZ ≈ -2.2 m/s (pack) and -2.7 m/s (upper) as raw backward differences. A linear fit over frames 20-28 gives a smaller value.
- The depth motion is real:
  - The ratio of depth step to lateral step gives a consistent heading of about 27-30° toward the camera in frames 0-14, 20-28 and 35-45.
  - The foot contact rows move down from y ≈ 1023 (take-off) to about 1055-1063 (end of clip).

**Focal length.**
- In the most upright walking frames (73-79), bbox height / scale gives a height of about 368-372 px at frame 24's depth.
- The suit is never at rest (forward lean, bent knees), so walking height is about 96-98 % of standing height. That gives a rest height of about 378-390 px.
- f = H_px x 18.147 / 2.2 ≈ 3120-3220. I use about 3160-3200 (hfov ≈ 40°).
- Bounding-box heights on frames 36-42 (legs spread, pointed toes; about 400 px at frame 24's depth) give an upper bound of 3300.

**Pelvis step from frame 23 to 24 (`speed.py`).** About (+30, -14.4) px, from the point (1080, 795) carried by the template transform.

**3D speed (`speed.py`):**

| f (px) | pack, raw | pack, smoothed | upper, raw | upper, smoothed |
|---|---|---|---|---|
| 3100 | 5.27 | 5.17 | 5.51 | 5.30 |
| 3160 | 5.19 | 5.09 | 5.43 | 5.22 |
| 3200 | 5.13 | 5.03 | 5.38 | 5.17 |
| 3300 | 5.01 | 4.90 | 5.26 | 5.04 |

All values are in m/s.
- At f = 3160-3200 the components are lateral ≈ 4.2 m/s, vertical ≈ -2.1 m/s and depth ≈ -2.2 to -2.7 m/s.

## Second-route check
Assume the astronaut moves along a fixed heading of about 28° toward the camera (taken from the other frame windows).
- Horizontal image step: 30 px ≈ 0.172 m.
- So dZ ≈ 0.172 x tan 28° ≈ 0.091 m per frame. This matches the template-scale value (0.089-0.11 m).
- Speed = sqrt(0.172² + 0.083² + 0.091²) x 24 ≈ 5.1 m/s.

## Conclusion
I agree with C1 (5.2). C2 leaves out the depth component and uses an unscaled height for its focal length.

## Confidence
About ±8 %. The main uncertainties are the rest-height pixel estimate (behind f) and the noise in the depth rate.

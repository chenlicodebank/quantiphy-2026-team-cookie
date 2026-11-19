# q3151 – height of the walking person (internet_0055)

## Problem
The prior is "average speed of the person riding scooter = 1.95 m/s". I checked the contact sheet (16 frames) and
full-res frames: the 75-frame clip has NO scooter rider, only the walking woman, a distant white SUV and a
shuttle bus. So the prior's object can't be measured here. The prior is also not about the walker. Her gait
(about 0.5 s per step) at 1.95 m/s would mean steps of about 1 m, which is far too long, and with any plausible
height she walks at about 1.4 m/s. The annotators' scale (1.95 m/s / scooter px speed) can't be reproduced, so the
height is estimated from scene geometry instead (fps 30 = question_fps, no re-timing issue).

## Measurements (frame-0 / stabilised px; scene/tracks/pedestrian.csv was checked against crops)
- Woman's pixel height (cap top to shoe, mid-stance): 269 (f4), 283 (f21), 289 (f35/36), 303 (f50), 313 (f67).
- At frames 35-37 she passes just in front of the bicycle-sign pole. The pole base enters the island mulch at y ≈ 662
  (frame 0, zoom crop).
- Bicycle warning diamond W11-1: 161 px diagonal -> 113.8 px side. Taking the standard 30 in (0.762 m) size gives
  0.00668 m/px at the pole's depth. The arrow plaque (97 px wide ≈ 24 in) is consistent with that.
- White SUV (Model Y-like, 1.62 m tall): 65 px tall, wheel contact at y ≈ 495.

## Geometry (flat ground, pinhole)
Unknowns: horizon y_h and camera height h_c. Car: h_c = 1.62·(495−y_h)/65. Sign pole: h_c − e = 0.00668·(662−y_h),
where e is how far the pole base (island mulch) sits above the path.
Woman at f36: H = h_c·289/(699−y_h).
- e = 0     : y_h = 434, h_c = 1.52 m, H = 1.66 m
- e = 0.06 m: y_h = 431, h_c = 1.61 m, H = 1.73 m
- e = 0.12 m: y_h = 427, h_c = 1.69 m, H = 1.79 m

Check: the bollard (top y 655, base y 1035) comes out 0.96–1.05 m tall, a normal bike-path bollard. Fitting the
horizon from her own foot-y vs height over the clip was unstable (the depth change is too small and gait adds
noise), so I didn't use it.

## Answer
1.70 m: the low-to-middle part of the geometric range, which also matches a typical adult woman's height.

Confidence: low to moderate. The prior's object isn't in this clip, so the annotators' scale is unknown, and the
answer assumes their scale was physically reasonable.

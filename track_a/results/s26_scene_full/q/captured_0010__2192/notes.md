# q_2192 – ball diameter (cm)

File fps = question_fps = 24. Depth times → frames: 0.3→7, 0.6→14, 0.9→22 (21.6), 1.2→29 (28.8), 1.5→36, 1.8→43 (43.2).
Lab card: f = 0.5959 x 1280 = 762.75 px. D = depth x pixel diameter / f. (Gravity prior is not needed for a size.)

## Measurements (measure2.py)
Half-level edge crossings of a redness profile (R - max(G,B)) through the scene/ track centroid, horizontal and
vertical, max chord over ±6 px rows/cols. measure.py's looser HSV mask was rejected: it bleeds into the reddish
background (see frames/ball_14.png).

| frame | depth m | W_h px | W_v px | D_h cm | D_v cm | strict-mask eq. diam cm |
|---|---|---|---|---|---|---|
| 7  | 1.706 | 28.4 | 30.2 | 6.36 | 6.76 | 6.21 |
| 14 | 1.344 | 38.3 | 38.3 | 6.75 | 6.74 | 6.52 |
| 22 | 1.4605| 34.4 | 35.1 | 6.58 | 6.71 | 6.83 |
| 29 | 1.784 | 27.4 | 28.7 | 6.41 | 6.70 | 6.24 |
| 36 | 1.717 | 28.8 | 32.3 (motion blur) | 6.48 | 7.28 | 6.50 |
| 43 | 1.350 | 37.3 | 37.0 | 6.61 | 6.54 | 6.28 |

Horizontal mean 6.53 ± 0.13 cm; vertical (no f36) 6.69; the strict-mask equivalent diameter (which the scene notes say
sits 1–2 px inside the rim) gives 6.43. The adjacent frames ±1 agree to within about 0.3 cm.

## Answer
6.6 cm (the edge profile mean, h and v combined). The six depth/frame pairs agree with each other, so the scale holds
together. Confidence: about ±4%.

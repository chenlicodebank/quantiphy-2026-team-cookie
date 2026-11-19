# Q110 — length of the bike (m); prior: car acceleration = 4.03 m/s^2

fps = question_fps = 24 (no re-timing). The scene is a top-down 2D view with a static camera, so I used one metres-per-pixel scale taken from the car's pixel acceleration.

## Car acceleration in pixels (scripts: edges.py, tmatch.py, tm_an.py, centre.py)
- I tracked the car three ways: sub-pixel front and rear bbox edges, and template matching of three rigid
  patches (front/cabin, middle, rear bed) cut from frame 52, with sub-pixel peak refinement.
- The speed profile is smooth but the acceleration is NOT constant. It is about 0.88–0.92 px/frame^2 over frames 2–45
  (front-edge quadratic fit 0.876, front-template speeds 26→40 give 0.92). It rises to about 1.35 around frames 52–57, then
  falls to about 0.3 at frames 64–71, where speed levels off near 63–64 px/frame.
  The cyclist moves at a uniform 26.6 px/frame across the whole image, so this is not a perspective artefact.
- Average acceleration from rest:
  - speed route: (v70 − v1)/69 = 63.9/69 = 0.926;
  - position route: total displacement from frame 1 to 70 = 2263 px (linked front edge → front template → rear template),
    which gives 0.935–0.95.
- A real-scale cross-check also supports about 0.88: if the Cybertruck-like car (~715 px) were the real 5.68 m, then a = 0.88.
- Adopted a = 0.91 ± 0.03 px/frame^2 = 524 px/s^2, so scale = 4.03 / 524 = 0.00769 m/px.

## Bike length (bike.py, bikeprof.py)
- The bicycle is teal including its tyres, and its length runs front-tyre to rear-tyre along x (I checked this on a zoomed crop at frame 37).
- I measured it on the luma channel, which is full resolution (the chroma is subsampled), using the half-contrast crossing
  between background ~135 and tyre ~57:
  - frame 40: 737.35 → 950.29, which is 212.9 px;
  - frame 52: 417.33 → 629.57, which is 212.2 px.
  - Wider thresholds give 208 (saturation 30%) to 214 (any deviation). I used 212.5 px.
- Perspective: the rider-vs-bike parallax slope is 0.017, which puts the camera about 40 m away (FOV about 20°). Height differences
  therefore change the scale by less than 1%, so I ignored them.

## Answer
L = 212.5 px × 0.00769 m/px = 1.63 m.

Sensitivity to the choice of a:
| a (px/frame^2) | bike length |
|---|---|
| 0.88 | 1.69 m |
| 0.93 | 1.60 m |
| 1.0 | 1.49 m |

## Confidence
Moderate. The pixel length is good to about 1%. The main uncertainty is which "acceleration" the prior refers to,
because the car's acceleration is not uniform.

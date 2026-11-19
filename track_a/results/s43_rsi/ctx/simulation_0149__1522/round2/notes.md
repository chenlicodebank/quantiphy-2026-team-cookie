# Q1522 – speed of the car at t = 0.5 s (m/s) – round 2 verification

3D Blender render. File fps 24 = question_fps 24, so t = 0.5 s is frame 12, and the speed is |P12 − P11| × 24 (the backward difference of the near-front hub, the car's right-front wheel). Static camera.
Prior: tyre diameter 0.764 m. depth_info: |P(f0)| = 14.244 m to the right-front tyre. That is the image-left front wheel at f0 (the car faces the camera), and it stays the visible near-side front wheel as the car turns. I checked this on zoomed frames.

## Task: verify round 1's proposed switch to 6.8 (from the submitted 7.2336)
Crux: how the frame-12 derivative of the near-front-rim depth track is taken. Local fits give 6.5–7.1 (C1, C2). A constant-rate 1/h line over an accelerating window gives 8.2 (C4). C3 chose 9.0, above its own fits.

## My measurements (own code)
- `verticals.py`: the vertical scene lines in f49 have a tilt of exactly 0 at |u−cx| up to 500 px. So the camera has no pitch. The horizon at v≈829 comes from a lens shift, so the principal point is (960, 829). Round 1 had modelled a pitched camera, but this changes the speed by only about 1%.
- f: the round-1 VPs (4021,824) and (−875,820) with the principal point (960,829) give f = 2370 px. The tyre route gives 2388–2453 (below).
- `rim.py`: rim (white face) half-max crossings per column, adaptive threshold between rim and tyre levels. I checked the overlay at f0/11/12/13 (frames/rim_overlay.png), and the edges follow the rim outline. The vertical extent comes from an ellipse-column fit H_fit and from the top-5 median of the column heights. H_fit f0 87.25, f11 97.25, f12 99.29 (round 1: 87.21 / 97.88 / 99.68). The hub row stays at v 828.7–830.
- `ellipse.py` (second estimator): 72 radial half-max edge points around the rim with a general conic fit, giving the ellipse's vertical extent: f0 86.35, f11 97.03, f12 99.47.
- `speed.py` / `ellipse.py`: Z = K/H, X = (u−cx)Z/f, Y = (v−cy)Z/f, with K set so that |P0| = 14.244. At f = 2370:
  - Column H_fit, windows 0-23 d4 / 0-20 d3 / 2-22 d3 / 6-18 d2: 6.70 / 6.57 / 6.64 / 6.50 (short windows 5.95–6.35).
  - Column H_top5: 6.82 / 6.85 / 6.84 / 6.71.
  - Ellipse: 6.93 / 6.86 / 6.97 / 6.82 (short windows 6.07–6.30).
  - Raw single-frame differences are noisy (6.3–8.3), so I do not use them.
  - The components at f12 are about dX +4.2 and dZ −5.9 m/s.
  - Dependence on f: about −0.3 m/s per +350 px.
- Central value of my long-window fits: about 6.8 (range 6.5–6.97). Round 1 had 6.75 (rim) and 6.84 (body ECC). The two agree within 3%.

## Rechecks
a. Closure: tyre outer extent at f0, from a vertical profile through the hub column, runs from about 759 to 899 px (≈ 137–140 px). The hub is at u = 68, so the off-axis factor is sqrt(f² + 892²) = 2532. This gives D = 0.771–0.788 m vs the prior 0.764 (+0.9 to +3%). The given distance 14.244 m is reproduced by construction.
b. Plausibility:
  - The rim comes out at K/f = 0.486 m (19 in), with a tyre/rim ratio of about 1.6. Both are realistic.
  - The car accelerates from rest (raw ≈ 1–2 m/s at f1-3, ≈ 9 m/s by f18-20). 6.8 m/s = 24 km/h at f12 is plausible in a car park.
  - Round 1 measured the wheelbase at 2.6–2.9 m.
c. Units/time: m/s. t = 0.5 s → frame 12 at question_fps 24 (the file fps is also 24). Backward difference 11→12.
d. Fault proof:
  - C4 8.2: a straight line fitted to 1/H over f8-23 gives d(1/H)/dframe −2.27e-4, against the local cubic value of −2.0e-4 (+13%). The speed from that line is 7.82, against 6.8 locally. This reproduces round 1's +15% claim.
  - C4 also reduced the depth anchor by 1 m by treating the asked tyre as the far one, which is wrong: the right-front tyre is the near one. It also used f = 1924, below the VP value of 2370.
  - C3 9.0: chosen above its own frame-12 fits (7.5–8.5), on a speed-limit-sign argument. That is a guess, not a measurement.
  - C2 7.1: same method as mine, +4%. I find no clear fault.
  - C1 6.5: pulled down by a single fascia ECC. −4%, within noise.
  - Submitted 7.2336: the geometric blend of C1 with the DeepSeek median, whose upper half rests on the C3/C4 faults above.

## Decision
I reproduced round 1's fault: C4's linear fit inflates the depth rate by +13 to +15%. My own value, about 6.8 (two rim estimators, several windows), agrees with round 1's 6.8 to within 3%. The switch stands: **answer 6.8 m/s**. Confidence medium, about ±4%, limited by derivative noise across windows.

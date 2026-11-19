# Q1883: acceleration of the astronaut at t = 0.5 s (m/s^2). Round-3 investigation

## Inputs and time base
- Prior: the astronaut is 2.2 m tall. depth_info: 18.147 m at t = 1 s (f24). question_fps = file fps = 24, so
  t = 0.5 s is f12 and acc12 = (s12 - s11) x 24, with s_i = |P_i - P_(i-1)| x 24.
- Submitted answer: 0.25 (C1). Round 2 proposed a switch to 0.40 (C6). Its fault proof says C1's silhouette
  landmark drifts against the rigid body. My first job was to verify that switch.

## Crux
All plausible candidates share the scale (about 0.0059 m/px at f12). They part on which image track supplies the
curvature of the root path at f12, inside the first smooth segment (f0-14). C1 used silhouette-edge landmarks.
C6 and round 2 used sub-pixel rigid-patch registration.

## My measurements (new route: dense optical flow, not ECC)
- `flow.py`: median DIS and Farneback flow per step f0-18 over three regions: the helmet (head), the upper body
  (top 40 %) and the backpack (pack). It also registers the f12 template directly to f4-16 (no chaining). That
  registration has cc < 0.95 beyond about 6 frames, so its tracks are short and noisy and I only report them.
- `hip.py`: pelvis-level tracks.
  - hip: median flow of the rear waist band, rows 45-62 % of the mask height, behind the band's mean x. The
    overlay `frames/overlay_12.png` shows that the band covers the waist and belt below the backpack.
  - tor: median flow of the torso.
  - rig: a rigid (rotation + translation) fit of the torso flow, carried to a pelvis point.
  - The torso turns steadily in the image by about 0.7 deg/frame. Lower body points therefore move more slowly in x,
    and their speed falls faster.
- Image steps are smooth from f0 to f14 and jump at 14→15 (about 11 to 20 px/frame); every fit ends at f14.
  - dx rises slowly: about +0.07 to +0.15 px/f² (head largest, waist smallest).
  - dy falls from 8 to 1.7 px/frame (about -0.6 px/f²).
- `acc2.py` (f = 3134 px, Z12 = 18.47 m, constant depth) gives acc12 in m/s^2:
  - head: -0.10 to -0.26, raw one-frame +0.35/+0.68. The head turns and leans, so it is the least pelvis-like part.
  - upper body / backpack: position fits -0.19 to -0.38, speed-series fits -0.19 to -0.56; median about -0.28.
  - pelvis level (waist band, torso):
    - quadratic position fits over windows starting at f0/2/4/6: hip -0.42 to -0.47, torso -0.41 to -0.43;
    - cubic fits: -0.28 to -0.48;
    - local quadratic speed-series fits: -0.25 to -0.51.
    - Median of the waist-band fits is about -0.43. The rotation-extrapolated "rig" point gives -0.4 to -0.8; it is
      noisy and I do not use it.
  - Median of all tracks and fits: -0.36.
  - Speed at f12 is 1.45-1.65 m/s.
- My value for the origin (pelvis): about 0.42 (range 0.36-0.46). The upper-body-only value would be about 0.28.

## Rechecks
- a. Closure: f = 380 px (bbox_h at f24, upright pose) x 18.147 / 2.2 = 3134 px. This comes from the prior itself, so
  the closure is 0 % by construction. The depth at f12 comes from a rigid proxy (`packh.py`: helmet top to
  backpack-bottom row, sub-pixel). It is 176.8 px at f12 against 180.4 at f24, so Z12 = 18.147 x 1.02 = 18.5 m. This
  agrees with rounds 1-2 (1.018).
  - The flow-divergence vertical scale (`vscale.py`) grows about 0.5-0.9 %/frame in both segments. bbox_h and the
    backpack height are flat, so this growth is an estimator bias, as round 2 found for the affine ECC scale. Rejected.
- b. Plausibility: the speed at f12 is 1.45-1.65 m/s, a normal walk. At this scale the f12 figure is 343 px x 0.0059 =
  2.0 m tall in a bent-knee walking pose, against 2.2 m standing. That is plausible. No other objects are in view.
- c. Units and time base: m/s^2. t = 0.5 s → f12 at 24 fps; the file fps equals question_fps.
- d. Fault proof:
  - C1 (0.25): `c1check.py` re-implements C1's landmarks: the mean of the buttock and backpack rear-edge medians,
    with y the integer backpack-bottom row.
    - The x landmark drifts by 9.5 px against my sub-pixel backpack flow track over f0-14 (+5.7 to -3.8 px,
      detrended). This happens because the silhouette outline slides over the turning body.
    - The drift gives a spurious x curvature: 2cu = +0.11 to +0.16 px/f², against +0.06 to +0.10 for the rigid
      tracks.
    - The y steps are integers (9, 8, 7, ... 2, 1).
    - With C1's own fits (quadratic, windows 2/4/6-14, Z = 18.4) the landmarks give exactly C1's -0.24, -0.26 and
      -0.06. The same fits give -0.31 to -0.36 on the backpack flow track and -0.41 to -0.47 on the waist-band
      tracks.
    - So round 2's fault is reproduced with a different tracker (DIS/Farneback flow rather than ECC).
  - C3 (2.2), C4 (6.5) and C11 (1.5) fit across the f14→15 velocity step (rounds 1-2). C9 (2.6) uses a
    silhouette-size depth trend that the flat backpack height contradicts.
  - C12 (0.574) uses a depth trend from a size scale. My vscale.py shows that such flow/affine scales grow
    spuriously.
  - C2 (0.35), C5 (0.28), C7 (0.42) and C8/C10 (0.5) are inside or near my spread. No concrete fault was checked for
    them.

## Decision
I verified round 2's switch:
- The fault in C1's measurement is real and reproduced.
- My own pelvis-level value, about 0.42 (all-track median 0.36), agrees with C6's 0.40 within about 10 %.

I therefore switch to C6: 0.40 m/s^2, the magnitude of a deceleration (the scalar speed falls as the image path
straightens).

Confidence: medium. This is a small second derivative. The result depends on which body point stands in for the
origin: the upper body gives about 0.28, the waist about 0.43. The camera cannot be checked on the white background.

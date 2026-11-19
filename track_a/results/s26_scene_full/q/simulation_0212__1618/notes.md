# q_1618: speed of the dog at t = 1.5 s (frame 36 at 24 fps; file fps = question fps = 24)

## Camera
- **Focal length, cat route** (`calib.py`): the cat's core centroid at f0 (408.5, 842.7) with d = 4.199 m and at f24
  (869.4, 805.3) with d = 4.481 m, principal point at the image centre. Setting the chord over 1 s equal to 0.94 m
  gives f = 2150 px (2152 px if f24 is extrapolated from f22/f23). HFOV is about 48 deg.
- **Floor/wall lines** (`floorline.py`, subpixel edge fits, residuals 0.2 px): back wall y = 909.3 - 0.0754 x and
  right wall y = 562.9 + 0.1292 x. If the walls are orthogonal and roll is 0, f and the horizon are tied:
  f = 2117 px needs horizon 540, f = 2150 px needs about 537, f = 2330 px needs 520. The room corner is vertical
  within about 2 px (`corner.py`), so pitch is about 0-1 deg and f is between 2117 and 2330 px. This agrees with
  the cat's 2150 px. I used f = 2150 px (horizon y = 537), with 2250 px as the alternative.
- **Camera height** about 0.79 m. It comes from the mirror's floor point (about y = 800 at 6.407 m). It also gives the
  nearest bench leg at about 5.6-5.7 m, against the given 5.69 m.

## Dog depth near f36
- **Core-plane route** (`dogspeed.py`): with the given depths at f0 and f12, the core centroid sits at a constant
  0.450 / 0.453 m below the camera. That is self-consistent, so I kept it as a constant-height plane. It gives
  z of about 4.0-4.2 m over frames 30-42 (mean about 4.12 m), but the core y jitters by ±5 px.
- **Floor-contact route** (`feet.py`): paw and cone contacts with a median-plate mask, D = f·h/(v - 537). At f36 the
  front contacts are at 4.12-4.2 m and the hind stance at 4.27 m, so the body centre is at about 4.25 m.
- I used z ≈ 4.2 m.
- **Caveat**: between f0 and f12, the floor contacts and the dog's pixel height show only about 0.15 m of approach.
  The given depths show 0.47 m. The rig origin may not follow the visible body exactly. I assumed it does.

## Image velocity at f36
- Template tracking of torso texture over frames 30-42 (`tmpl.py`):
  - rump: 16.0-16.3 px/frame
  - mid-back: 18.0 px/frame
  - shoulder: 18.5 px/frame (the dog is slowly turning)
  - vertical motion: about 0
- I took the pelvis/body origin at about 16.5 px/frame.
- The core-centroid fits give 15.7-17.3 px/frame.

## Speed
- Lateral: 16.5 × 4.2 / 2150 × 24 = 0.77 m/s (0.74 m/s if f = 2250 px).
- Radial, from the floor-contact trend: cone 4.17 → 4.06 m over f32-f40 and hind stances 4.36 → 4.27 → 4.23 m
  (f28 / f35 / f39), so about 0.25-0.35 m/s toward the camera.
- **Combined: |v| = sqrt(0.77² + 0.30²) ≈ 0.83 m/s; the range is 0.78-0.87 m/s. Answer 0.82 m/s.**
- **Second route**: the core-plane 3D track with linear and quadratic fits over ±3 to ±5 frames gives 0.73-0.80 m/s.
  That route has a smaller, noisy radial part.

## Confidence
Moderate, about ±8 %. The main risks are where the dog's origin sits (rump versus mid-body, since the image speed
differs by 10 % along the body), the radial component, and f.

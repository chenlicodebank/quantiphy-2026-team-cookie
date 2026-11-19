# Q1540, round 2: acceleration of the blue car (light-blue utility cart) at t = 1 s

The file rate and question_fps are both 24, so t = 1 s is frame 24. The convention gives a = (speed(24) - speed(23)) x 24 = (x22 - 2 x23 + x24) x 576 x (m/px). The camera is static and the cart drives right to left parallel to the image plane, at a constant image row and tyre size. The scale comes from the prior's cart tyre (0.369 m) measured in the cart's own side plane, so no focal length is needed. The yellow tyre and depth_info serve as closure checks only.

## Job 1: verify round 1's proposed switch (1.643 → 1.40, following C4)
Round 1's fault proof rests on two numbers: a pixel acceleration of 0.50 px/f² at frame 24 (not the 0.67-0.75 behind blend component B) and a tyre of 74.5-77 px. I reproduced both with my own code and different routes.

### Pixel acceleration (crux)
At frames 18-26 the cart body is hidden behind the yellow car, and only its roof, handle and rear LED panel show. Direct frame-to-frame velocities there are unreliable: masked matching pixel-locks to integers (`chain_r2.py`). So I measured the ease curve on the clean frames and anchored it at both ends.

- **`track_r2.py`.** 2D masked SSD against a frame-30 template, yellow excluded, cubic-resampled 0.02 px search.
- **`chain_r2.py`.** Neighbour-frame chained velocities for the roof top, the roof band and the body.
- **`led_r2.py`.** A template-free route: intensity-weighted centroid of the three rear LED blobs (V > 235). Frames 23, 24 and 27-41 are clean; frames 25-26 are contaminated by the car's spoiler and dropped.

Fits (`fit_r2.py`), with a23 = x22 - 2 x23 + x24 in px/f²:

| route | a23 |
|---|---|
| LED 23, 24, 27-41: smoothstep = cubic (rms 0.068 px) | 0.472 |
| LED 23-24, 27-34 | 0.499 |
| LED 27-41 only (extrapolated) | 0.446 |
| body / top / roof chains 27-41 (extrapolated) | 0.555 / 0.545 / 0.564 |
| linear fit to the clean LED second differences 28-40 (a = 0 at frame 29.55, jerk -0.076) | 0.497 |
| joint velocity smoothstep: record frames 1-13 + LED 28-41 (i0 = -0.1, T = 59.3) | 0.501 |
| same, with early speeds rescaled by 1/1.061 | 0.531 |

- **Motion model.** The early record speeds rise about 2.2 px/f per frame, which matches 6Δ/T² = 2.25 for a smoothstep. The acceleration falls linearly to zero near frame 29.6. This is a single Blender ease, so the late-only extrapolations (0.45-0.56) bracket the anchored values.
- **Adopted:** 0.51 px/f² (range 0.50-0.53). Round 1 had 0.501.

### Tyre pixel diameter (`tyre_r2.py`, overlay `frames/tyre_ov36.png`)
Front cart tyre, frames 33-41:
- Dark-mask horizontal width: 75-77 px (median 76).
- Edge-ray circle fit on the left arc: 76.9-78.5 px (median about 78; frames 32 and 38 rejected as bad fits).
- Vertical profile at the hub column (`blur_r2.py`): the top edge sits at row 743, which equals the circle fit's 742.5, so the fender does not occlude it. The bottom is at 818-819, 2 px short of the circle because of ground contact. The vertical extent is about 75-76.
- **Motion blur.** LED edge transitions are about 2-3 px both horizontally and vertically, so blur does not inflate the horizontal extent.
- **Adopted:** 77 px (range 76-78), scale 0.369/77 = 0.004792 m/px.

### Result
a = 0.51 × 576 × 0.004792 = **1.41 m/s²**. The range is 1.36-1.46 from the pixel acceleration range and the tyre range of 76-78 px (74.5 px would give 1.45). This agrees with round 1 / C4's 1.40 to within 1 %.

## Rechecks
- **a. Closure (yellow-tyre prior; the cart tyre is the scale itself).**
  - The yellow rear tyre at frame 24 measures D = 188-189 px vertically: hub row 789.5 from the rim top and bottom, tyre bottom 883.5 (`ytyre_r2.py`). It is vertical only because the car is horizontally blurred at 97 px/f.
  - The ground rows are 884 (car) and 817-820 (cart), with the horizon at 539.3. This gives Z_car/Z_cart = 1/1.228 to 1/1.241, so the car-plane scale is 0.00386-0.00390 m/px.
  - The yellow tyre comes out at 0.730-0.738 m against the prior's 0.764: closure **-3.5 %** (range -3 to -4.5).
  - Camera heights derived from each tyre's hub and ground rows also agree to 3.4 %.
  - depth_info check: 11.38 m to the yellow front tyre at frame 12 gives Z ≈ 10.98 and f ≈ 2720 px. This reproduces the yellow tyre's 189 px.
- **b. Plausibility** (0.00479 m/px at the cart, 0.00388 at the car):
  - cart height 325 px → 1.56 m
  - cart speed 33 px/f → 3.8 m/s
  - yellow car length 1148 px → 4.45 m
  - car peak speed about 9.5 m/s
  - All are realistic.
- **c. Units and time base.** The answer is in m/s². Frame 24 = 1 s × 24 (question_fps equals the file rate). The second difference is centred on frame 23, per the backward-difference convention.
- **d. Fault proof.**
  - **Blend component B (DeepSeek, 1.875).** At a 77 px tyre this needs about 0.68 px/f². Every route of mine gives 0.45-0.56, and the anchored routes give 0.50-0.53, so B is about 30-35 % high. The submitted blend of 1.643 is therefore about 17 % high. This reproduces round 1's fault.
  - **C5 (2.1) and C6 (1.65).** Same fault (0.67-0.75 px/f²); C6 also used an 86 px tyre, against my 76-78.
  - **C2 / C3 (1.2 / 1.15).** These imply about 0.42 px/f², below my anchored range. They come from noisy polynomial windows on the record's occluded roof track.
  - **C8 / C9 (1.2).** Same low reading.
  - **C1 (1.44), C4 (1.40), C7 (1.40), C10 (1.49).** All are within my range.

## Decision
I reproduce round 1's fault, and my value of 1.41 agrees with its proposed 1.40 to within 1 %. I switch to **1.40** (following C4). Confidence: high.

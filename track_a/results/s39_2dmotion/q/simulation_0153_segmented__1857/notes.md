# q_1857: acceleration of the blue car at t = 1.5 s

Prior: the blue car's tyre diameter is 0.369 m. This is a 2D segmentation video at 24 fps (file fps = question fps = 24).
t = 1.5 s is frame 36. Convention: a = (v36 - v35) x fps, with v_i = |x_i - x_{i-1}| x fps.
**Answer: 1.22 m/s².** The cart is decelerating at this time, so the signed value is about -1.22 m/s².

## Motion: x track, px
- **Tracks used** (the cart moves horizontally and its y is constant):
  - scene/ template tracks: front hub, rear hub, wheel midpoint and sill marker.
  - My own NCC tracks of the front and rear wheel patches, cut from frame 36 (`measure.py`).
  - The SAM 3 "blue car" track (`tracks/blue_car_0.csv`).
- **Raw second differences are noisy.** x36 - 2x35 + x34 comes out at -305 to -328 px/s² from the scene tracks and at -361 / -411
  px/s² from my wheel tracks (noise about ±0.1 px, which is ±60 px/s²).
- **Cubic fits are tight.** Local cubic or quartic polynomial fits over frames 26/28/29-41 (`fit.py`) leave an rms of only 0.04-0.06 px. The
  backward-difference acceleration at frame 36 from the fitted curve is:
  front hub -362, rear hub -361, wheel_mid -362, marker -366, own front wheel -356, own rear wheel -367 px/s².
  - Accepted: **-362 px/s²**.
  - The deceleration is not constant. It grows from about -0.4 to -1.2 px/frame² over frames 33-41, which looks like the
    ease-out of a Bezier keyframe. A quadratic fit therefore over-reads it (-395 to -430), so I used the cubic.
- **SAM 3 track:** the box centre jitters by ±5 px because the roof-extension segmentation flickers. It is too noisy for an
  acceleration (a cubic fit gives -200 to -260 px/s², rms 5.5 px), so I used it only to confirm which object is tracked. The SAM mask
  at frame 36 covers the whole cart (box 724-1263 x 468-949), which matches the scene bbox.

## Scale: tyre diameter, px
| Method | Front tyre | Rear tyre |
|---|---|---|
| Circle fit to the tyre/white edge, frames 32-39 (`tyre_circle.py`) | 108-110 | 108-110 |
| Median of the circle fit | 110.0 | 110.0 |
| SAM 3 "tire" masks, frame 36: box w x h | 111 x 108 | 110 x 109 |
| Horizontal chord through the hub (`tyre.py`) | 113 | 109 |
| scene/ record | 112 | — |

- The front tyre's horizontal chord, 113 px, is about 3% above the circle fit and the SAM extents. The zoomed crop
  (frames/front_tyre36.png) shows a slightly elliptical silhouette, which looks like tread or sidewall seen in perspective, so
  I trust the circle fit.
- Accepted D = 109.5 px, giving 0.369 / 109.5 = 3.370e-3 m/px.

## Depth check
- The wheelbase shrinks about 1.6% from frame 20 to frame 41.
- The vertical size (flat roof top to ground: 449 ± 0.7 px) and the hub y are constant, so the depth does not change and one planar
  scale applies (`depthcheck.py`).
- The front and rear hubs give the same acceleration (-362 / -361), so the horizontal foreshortening does not affect the result.

## Result and checks
- a = -362 px/s² x 3.370e-3 m/px = **-1.22 m/s²**. The answer is its magnitude, 1.22.
- **Independent routes:**
  - Rear hub and front hub tracks, my own wheel NCC tracks and the marker all give 1.20-1.24 m/s² at D = 109.5.
  - The raw unsmoothed backward difference gives 1.03-1.10 (noise-dominated).
  - With D = 112 or 113 px the answer would be 1.19 or 1.18.
- **Confidence:** moderate-good, with about ±5% from the choice of tyre px diameter and the fit.

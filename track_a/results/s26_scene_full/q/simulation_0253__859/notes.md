# Q859 – acceleration of the box at t = 0.5 s (simulation_0253)

Prior: box width along the slope = 0.611 m. No depth_info. fps = question_fps = 24, so t = 0.5 s is frame 12.
At frame 12 the box is still clipped by the top edge. A box sliding on a straight ramp has a constant acceleration,
so I estimated it from the fully visible frames 15–44.

## Findings that change the scene/ record
- **The scene has strong perspective; it is not a flat 2D layout.** A plain quadratic fit to the record's centroid track
  gives a pixel acceleration that falls from about 930 px/s² (frames 15–26) to about 680 px/s² (frames 29–44).
  - The ramp recedes from the camera: the box's front face shrinks, a side face is visible on the down-slope side early
    and on the up-slope side late (about 33 px wide at frame 44), and the ramp band narrows from 49.5 to 46.3 px.
- **The silhouette centroid is not a fixed point on the box.** It shifts as the side faces appear and disappear: the
  tape patch moves about 26 px relative to it over the clip.
  - Reference point used instead: the bright tape patch on the box's top-front edge (`patch.py`). It is a physical point
    on the front face. Its track stays within ±0.5 px of the path line.
- Frame 27 shows frame 28's content (a dropped frame followed by a duplicate). I excluded frame 27.

## Route 1 (main): projective line model plus constant acceleration (`patchfit.py`, `scale.py`)
- Model: u(t) = u0 + S/(1+γS), with S = v0·τ + A·τ²/2 and τ = t − 0.625 s. S is in pixel units at the frame-15 position.
- Fit on frames 15–44: γ = 5.5e-5, A = 977 px/s², rms 0.25 px (a plain quadratic gives rms 2 px).
  - Other windows (13–44, 15–35, 20–44, 15–30) give A = 977–1007 px/s².
  - Adding Blender's default linear damping (0.04) gives a(0.5 s) = 984 px/s².
- Scale: the front-face length along the slope (`ruler.py`, frames 15–29) is referred back to S = 0 with the fitted γ.
  - Result: L0 = 94.4 ± 0.7 px. The values stay constant across frames, which independently confirms γ.
  - The patch lies on the front face, so the patch track and the ruler are at the same depth and the scale ratio is exact.
  - The box origin translates rigidly with this point, so its acceleration is the same.
- a = 977 × 0.611 / 94.4 = **6.32 m/s²** (6.36 with damping).

## Route 2 (check, no projective model) (`route2.py`)
- Physical speed = 0.611 × (patch pixel speed) / (local front-face pixel length), for frames 16–29.
- A straight-line fit of speed against time gives a = 6.23 m/s², and v(0.5 s) ≈ 3.0 m/s, which agrees with route 1.

## Answer
a ≈ 6.3 m/s². The two routes agree within 1.5%. As a sanity check, an incline of about 44° gives g·sin θ ≈ 6.8 m/s²,
so 6.3 m/s² implies a small amount of friction.

Confidence: moderate to good, about ±4%. The main uncertainties are the ruler length (about ±1%) and the A fit
(about ±3% across windows).

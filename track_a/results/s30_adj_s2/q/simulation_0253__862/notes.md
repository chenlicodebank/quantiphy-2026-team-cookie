# Q862 – acceleration of the box at t = 1.75 s (m/s²)

Prior: the box's side parallel to the slope = 0.611 m. No depth_info. The file and the question both run at 24 fps, so t = 1.75 s is frame 42.
Track: scene/tracks/box.csv `s_along_path_px`, frames 15–44 (box fully in view), with frame 27 dropped (it repeats
frame 28's image). The silhouette is close to centrally symmetric, so its centroid is the box centre (origin).

## Where the candidates part ways
- C2 (4.6) treats the view as flat. It takes the image-plane acceleration near frame 42 (657 px/s²) and multiplies it by one
  scale averaged over the clip (86.5 px per 0.611 m).
- C1 (6.07) models perspective: the slope recedes from the camera.

Perspective is real, and I checked it three ways:
1. **End faces in rotated crops** (`crops.py`, frames/rot*.png): the downhill end face shows at frame 16, it is
   edge-on near frame 28, and the uphill end face shows at frame 42.
2. **Ramp band edges on frame 0** (`band.py`, `vpfit.py`): the band narrows from 49.9 px to 47.2 px going downhill.
   The two edge-line fits leave 0.1–0.16 px rms. The vanishing point of the slope direction is about 19,830 px down
   the path (bootstrap 19,340–20,300; each half of the band gives 19,200 and 19,600).
3. **Image-plane acceleration**: it falls from about 900 to about 650 px/s² over the clip. A quadratic fit leaves
   2.0 px rms; the perspective (Möbius) model leaves 0.6 px.

In perspective, the image-plane acceleration includes a −2g·v² term, so C2's flat conversion underestimates
the acceleration by about 25%. C2 is rejected.

## Scale
I measured the along-slope extent of the silhouette (`extent.py`, b* 50% crossings in four bands). It bottoms out
at 91–93 px over frames 26–31, where both end faces are edge-on, so the front edge is 0.611 m = 92 px near frame 28.
This agrees with C1. The box origin lies half a box depth behind the front face, so its magnification is
1/(1 + k/2) of the front face's, with k = 0.031 (k = 0.025–0.037 changes the answer by ±0.3%).

## Fits (`fit.py`, `vpfit.py`, `final.py`)
The image position is s = s_V − B/(1 + X/Z), where X(t) is the world path. The answer uses the per-frame convention:
(speed(42) − speed(41)) × fps.
- Constant acceleration, vanishing point free: 6.14 m/s² (rms 0.600 px; at rest at t = 0.026 s). This reproduces C1's route 1.
- Constant acceleration, vanishing point fixed from the band: 6.02 m/s² (rms 0.646 px; at rest at t = 0.006 s). This is C1's route 2.
- Vanishing point fixed from the band, linear damping c free: c = 0.048/s (rms 0.590 px). That is close to Blender's
  default rigid-body damping of 0.04 (c = 0.041/s). With c = 0.041/s: a0 = 6.38, and the acceleration at frame 42 is
  **5.90 m/s²** (5.88–5.93 across the vanishing-point uncertainty). The speed at frame 42 is 10.35 m/s.
- Second route, fitting subsets of frames: frames 15–35 give 5.91 and frames 25–44 give 5.98 (5.95 with damping;
  6.05–6.07 at constant acceleration).

The free-vanishing-point constant-acceleration fit needs a vanishing point near 17,500 px. That is about 4σ from the
measured band value, so the data slightly favour a small damping term. Either way, the answer lies between
5.88 and 6.14.

## Answer
**5.95 m/s²**. This sits between the damped reading (5.90) and the constant-acceleration reading with the measured
vanishing point (6.02), and is within 2% of both. I agree with C1's method and scale; the difference from C1 is
only whether the box's acceleration is constant or slightly damped.

Physical check: with an image incline of about 44°, g·sin θ = 6.8 m/s², which implies a friction coefficient of about 0.12.
Confidence: good, about ±4%.

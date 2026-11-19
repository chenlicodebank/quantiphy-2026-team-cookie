# Q1865 – acceleration of the astronaut at t = 3 s

The video is 2D, 24 fps; question_fps is also 24, so t = 3 s is frame 72. The prior is the astronaut's height, 2.2 m.

## Scale
- My own mask (min RGB < 225, largest blob) gives a vertical bbox extent of 90, 91 and 90 px on f0–f2, where the figure stands upright and at rest.
- SAM 3 ("astronaut", f0) gives vert_px = 90 and length 91.0 px, which agrees within 1 %.
- H = 90.33 px, so the scale is 2.2 / 90.33 = 0.02435 m/px.

## Motion
The figure rises with an ease-in/ease-out profile, which matches Blender's Bezier keyframe interpolation. The speed per frame peaks at about 5.4 px around f40 and reaches zero at about f78.
- **Route 1 (own mask centroid, `measure.py`):**
  - I fitted a smoothstep position curve, 3s² − 2s³, between keyframes. The fit gives fa = −0.4 and fb = 78.3, with RMS 0.33 px (noise level).
  - Taking the backward-difference speed, the acceleration at f72 is (speed(72) − speed(71)) = −0.2175 px/frame².
  - A local quadratic fit over f64–78 gives −0.219 px/frame²; over f66–78 it gives −0.217.
- **Route 2 (SAM 3 track, `check_sam.py`):**
  - The same smoothstep fit gives −0.2147 px/frame².
  - Local quadratics give −0.214 and −0.228 px/frame².
- SAM's centroid at f72 is (1310.4, 250.2) and mine is (1310.6, 250.1), which agree within 1 px. The extents agree within 1 % on f0 and f72, so no differences above 3 % needed resolving.

## Answer
The acceleration is −0.216 px/frame² (± about 0.002) × 24² × 0.02435 m/px ≈ −3.03 m/s². Route 1 gives 3.05 and route 2 gives 3.01. The magnitude is **3.04 m/s²**: the astronaut is decelerating as it approaches the top of its path.

Confidence: good, within about 3 %. The main uncertainties are the pixel height (±1 px, about 1 %) and the exact form of the interpolation curve.

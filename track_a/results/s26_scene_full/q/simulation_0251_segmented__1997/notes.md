# Q1997: soccer ball speed at t = 2 s

- 2D scene at 24 fps (file fps equals question_fps). t = 2 s is frame 48. A single ball moves horizontally to the right. The camera is static.
- `measure.py` thresholds the darkness (255 − grey) at > 10, applies an opening and keeps the largest component.
  For each frame it records the darkness-weighted centroid, the bbox and the diameter estimates.
- **Diameter (scale)**: the vertical bbox extent is 47–51 px, median 48. It has no motion blur, and the threshold is about half the
  ball's interior darkness. The half-max area-equivalent diameter is 49.6 px, but that is inflated slightly by motion blur along x.
  I used D = 48.5 ± 1 px, so the scale is 0.344 / 48.5 = 0.00709 m/px.
- **Pixel speed at frame 48** (`fit.py`):
  - one-frame step 47→48: 25.96 px (centroid) and 25.50 px (bbox);
  - linear fits over frames 40–50, 42–50 and 44–50: 25.85–26.03 px/frame;
  - global quadratic over frames 2–50 at frame 47.5: 25.60 px/frame (rms 0.5 px).
  - Adopted 25.8 px/frame, which is 619 px/s.
- **Speed** = 619 × 0.00709 = 4.39 m/s. With D = 49 px it is 4.35 m/s.
- **Answer**: 4.38 m/s. Confidence: about ±3%, dominated by the uncertainty in the pixel diameter.

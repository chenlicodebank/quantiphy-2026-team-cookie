# q_1735 — height of the person (m)

The prior is the person's speed, 1.3 m/s. Depth to the person is 179.09 m at t=1 s and 179.18 m at t=2 s.
The file runs at 25 fps but the question uses 24 fps, so I convert frame numbers with 24 fps.

## Observations (measure.py, tilt.py)
- The camera is static and looks down at an angle. The person is small (about 17 x 34–44 px). They walk straight
  down the image: the head-top track fits a line at dx = 0.079 and dy = 1.331 px/frame (residuals 0.4 and 0.7 px).
  That is 1.3335 px/frame, or 32.0 px/s at 24 fps. Path slope dx/dy = 0.059.
- The body's vertical axis and its walking direction both point down the image. So the person walks toward the
  camera in the vertical plane through the camera. Under that geometry the depth should fall by about
  0.8 m/s, but the given depth rises by 0.094 m/s. So the depth_info origin does not follow the body (it is the
  static-origin case). I use Z ≈ 179.1 m only for scale; the body moves only about 4 m over the clip.
- Ground scale along the walking direction: g = s·sinθ = 32.0 / 1.3 = 24.6 px/m. The gait spread of the image
  height (34 → 44 px, about 10 px for a forward foot reach of about 0.4 m) agrees with this.
- Image height with the legs together (head top to lowest foot): 33–35 px. This includes a few px of toe reach,
  the head-top silhouette and anti-aliasing, so the effective vertical extent is about 30–34 px.

## Route A (geom.py)
I assumed the principal point is at the image centre and the camera has no roll. The path line extended passes
through the nadir vanishing point, which gives f/tan(pitch). The 1.3 m/s image speed at Z = 179.1 m gives
f·sinθ. Together these give f ≈ 5670 px (hFOV 15.4°) and pitch ≈ 50°.
H = heff·tanθ/g = 1.61 / 1.71 / 1.81 m for heff = 32 / 34 / 36 px.
This is sensitive: a path-slope error of ±0.008 changes H by ±0.17 m.

## Second check
- I measured the upper-body axis tilt in the image: about 0.13, with high noise from arm swing and shading. That
  does not confirm the 0.059 nadir direction, and it would imply an implausible height. I treat it as unreliable
  because the figure is only 17 px wide.
- Body-width proportions (shoulders with arms about 17 px) give 1.6–2.1 m. That range is too sensitive to be
  decisive.

## Answer
1.7 m. This is the centre of route A (1.6–1.8 m) and agrees with a standard adult height. Confidence is moderate:
roughly ±10 %.

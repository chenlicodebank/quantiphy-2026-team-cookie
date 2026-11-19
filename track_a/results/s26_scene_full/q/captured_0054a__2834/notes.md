# q2834: orange ball (the basketball) diameter, in cm. Answer: 21.5 cm

The file and the question both run at 24 fps. t=0.5 s is f12 and t=1.0 s is f24. f = 0.5959 x 1280 = 763 px, principal point (640,360).

## Pixel diameter (code: fitsphere_lib.py, sizeseries.py, analyze.py)
- The ball rolls toward the camera, low and on the left of the image, so its image is a perspective ellipse (radial/tangential = 1/cos(theta) = 1.12 at f12),
  motion-blurred along about 18 deg. Its bottom is shaded and merges with the floor contact shadow.
- Edges: the sub-pixel half-level crossing along rays from the centre. Two edge metrics were used: R-B (orange-ness) and |frame - background median of f40-48|.
  I used only the upper and side sector (rays at 15-165 deg, which point down, excluded) to avoid the shadow. I fitted the constrained sphere image
  (tangential semi-axis a, radial a/cos theta, free centre). The tangential axis 2a = f·D/Z.
- f12: 68.1 (R-B) / 69.7 (bg) px. Smoothed over f10-26 with f/s linear in t: 67.7 / 69.4 px at f12 and 84.8 / 87.8 px at f24.
  For comparison, the naive mask bbox is 76-80 px at f12. It is inflated by the perspective elongation, the blur and the shadow, so I did not use it.

## Scale
- Depth read as camera Z (the card's back-projection convention). f12: D = 68.7 x 2.3557 / 763 = 21.2 cm. f24: 86 x 1.81 / 763 = 20.4-20.8 cm.
- If the depth is the sensor value at the ball's front surface (centre = +R): about 22.0 cm. If it is the Euclidean range to the centre: 19.2 cm.
  That is implausibly small for this real basketball (seams and a logo are visible at f0).
- Answer: 21.5 cm, between the centre and the surface readings.

## Second route: the velocity prior (2.21 m/s at f12)
- The track jumps 31.7 px between f11 and f12, against about 15-17 px for the neighbouring steps. It looks like a dropped frame.
- With Z-convention 3D points from the given depths, the average speed over f12-24 is 1.91 m/s. A 5-frame smoothing window that includes the double step gives
  about 1.2 x 1.91 = 2.29 m/s, which is close to the 2.21 prior. The Euclidean reading gives 1.98 m/s. So the Z convention is the self-consistent one.
- Diameter from the ball's own speed in diameters per second (s, u, v series): about 8.9 D/s without the jump, which gives 24.8 cm.
  With the jump-inflated window it gives about 20.7 cm. The second figure agrees with the depth route.
- Apparent size ratio s24/s12 = 1.25-1.27. Predicted ratios: 1.30 (Z), 1.28 (Z surface + R), 1.26 (Euclidean). This is only weakly informative.

Confidence: moderate. The likely range is 20.5-23 cm; the main uncertainty is how the depth was defined.

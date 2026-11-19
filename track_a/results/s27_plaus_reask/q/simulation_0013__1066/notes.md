# q1066 — diameter of the cart's wheels (simulation_0013)

The file runs at 21.75 fps, but every time here uses question_fps = 24, as instructed. The camera is static and looks
roughly level; the horizon is near the centre row 977.

## Scale: focal length from the nest's free fall (gravity prior)
- The nest leaves the branch at about frame 26–27 and falls in front of the camera. While falling its apparent size stays
  about the same (~390–410 px, about the same as in the tree), so its depth stays close to the given ~4.9 m.
  (Distances are 4.932 m at t=0 and 4.895 m at t=1, so about 4.88 m at frame 27.)
- I fitted a parabola to the nest centroid v(t) (scene record mask_cy, t = frame/24). Frames 27–33 are the clean part:
  the nest is ball-shaped with no blur, and the residuals are only 1–3 px. Pixel acceleration = 5790 ± 210 px/s²
  (28–33: 6040; 27–32: 5750).
  The pinhole relation acc_px = f·g/Z gives f = acc·Z/9.8. Converting the given Euclidean distance 4.88 m to optical-axis
  depth (the ray is off-axis at u≈384, v≈520) gives Z ≈ 4.72 m, so **f ≈ 2790 px**. If the nest also comes toward the
  camera at about 0.4 m/s (the rest point on the ground is ~4.5 m away), **f ≈ 2650 px**
  (fit3d_vz.py, fit_fall2.py). I used **f ≈ 2720 ± 150 px** (HFOV ≈ 39°).
- Frames 34–40 have strong blur and deformation (hair-like streaks), and their centroid lags. Fits that include them
  give a lower f (1700–2100) with poor residuals (rms ~20 px), so I rejected them.
- Consistency check: free fall from frame 27 (v0 ≈ 1.3 m/s, drop ≈ 2.2 m) reaches the ground at frame ≈ 40.2, which
  matches the observed impact between frames 40 and 41. With f = 2720 the camera height is ≈ 1.5 m (from where the cart
  touches the ground at v ≈ 1143), and the nest rests ≈ 4.5 m away, which matches its rest size.

## Wheel
- The near wheel is cut by the right edge. Its rim fits an ellipse with centre ≈ (1915, 1043.5), horizontal semi-axis
  ≈ 80 px and vertical semi-axis ≈ 99–100 px. The outer rim edges, read from intensity profiles (wheel_edges.py,
  wheel_view.py), are: top ≈ 943, bottom ≈ 1144, left ≈ 1834. The vertical diameter is **≈ 199 ± 3 px**; the vertical
  axis is the true diameter, since the wheel plane is about 35° off the image plane.
- The distance from the camera to the cart is 26.342 m (Euclidean). The off-axis ray is r = (955, 66, f):
  D = 199 · 26.342 / |r| = 199 · 26.342 / 2884 = 1.82 m.
- Small correction: the visible near wheel is probably ~0.5 m closer than the cart's origin, which lowers D by about 1–2%.
  **Answer: 1.80 m.**

## Plausibility / confidence
With this f, all the scene objects come out large: the wheel is 1.8 m, the nest is ~0.7 m across, the bird's wingspan
is ~2 m and the white bush is ~1.3 m. A real magpie-sized bird (~0.55 m wingspan) would need f ≈ 10000. That would mean
a pixel acceleration of ~35 px/frame² for the falling nest, but only ~10 px/frame² is observed, so gravity rules it
out. I therefore kept the gravity scale; the bird is a large model or a large species.

The main source of uncertainty is f (±8%). The wheel's distance relative to the cart origin adds ±2%. Confidence is
moderate: about ±10%.

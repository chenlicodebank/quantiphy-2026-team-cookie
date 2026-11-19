# q1410: acceleration of the astronaut at t = 1 s (m/s^2)

The answer is 1.9 m/s². This is the magnitude: the 3D speed of the pelvis is falling at frame 24, so the signed value is about -1.9 m/s².

## Time base and convention
- The file and the question both use 24 fps, so t = 1 s is frame 24.
- Acceleration = (speed(24) - speed(23)) x 24, where speed(i) = |P(i) - P(i-1)| x 24 and P is the 3D pelvis position.
- Frame 24 is in the middle of the second leap. Take-off is at f19, an abrupt velocity kink at f29/30 is still in the air, and landing is at f58. The f29/30 kink is in the animation itself: the centroid shows it too.

## Image track (torso.py, regions.py)
- I tracked the body by chaining template matches with sub-pixel peaks on six regions: helmet, upper body, backpack, chest, hip and trunk. All six agree to within about 0.3 px/frame.
- The mask centroid in scene/ is biased by the swinging legs, so I used the hip and trunk regions as the pelvis proxy. At f24 the pelvis is near pixel (1050, 800).
- Pixel speed (px/frame), f22 → f26: 32.8, 33.4, 33.5, 33.0, 32.0. The in-plane pixel speed peaks right at f23-24.

## Depth (ecc_all.py, ecc_cmp.py)
- **Method.** I estimated the upper body's apparent scale change frame to frame with an affine ECC fit, without a mask.
  - I ran it forward and in reverse and took the geometric mean, which cancels the fitting bias. A masked version was biased by about +0.3 %.
  - I used two box heights (110 and 175 px).
- **Result.** The scale grows by about 0.4-0.7 % per frame around f24, and the growth rate is falling.
  - Across the clip the scale grows 1.17-1.18x from f24 to f79, and 1.27-1.30x from f0 to f79.
  - So the astronaut is approaching the camera at about 2 m/s, and that approach is slowing.
- **Ground check.** The ground contacts are consistent with this scale. Feet are at y ≈ 1023 at f17 and y ≈ 1060 at f79. That implies a horizon near y ≈ 860 and a camera about 1 m high, which is plausible because the terrain ridge at y ≈ 990 lies below it.
- **Distance.** Z(i) = Z24 / S(i), with Z24 = 18.115 m, from the given 18.147 m Euclidean distance.

## Focal length
- I took the upright walking frame f79, where the bounding-box height is 438 px.
- Its distance is Z79 = Z24 / S79, which is about 15.4-15.5 m.
- With the 2.2 m prior height this gives f ≈ 3050-3100 px. Assuming a 445 px rest height instead changes the acceleration by less than 1 %.
- The resulting speeds are lateral ≈ 4.3 m/s, vertical ≈ 2.1 m/s and toward the camera ≈ 1.8-2 m/s, for |v| ≈ 5.2 m/s.

## Result (accel.py)
Raw backward-difference a24, for each depth-smoothing model:

| Depth model | Raw a24 (m/s²) | Range in this model (m/s²) |
|---|---|---|
| quadratic or cubic log-scale fit (captures the measured slowing of the approach) | -1.2 to -2.4 | hip -1.2…-2.0; trunk/upper -1.6…-2.4 |
| constant approach rate (linear fit) | -0.1 to -1.2 | |

- A second route, the derivative of a quadratic fit to the speed over f20-28 at frame 23.5, gives -1.5 to -2.6 m/s² with the curved depth models.
- The 3D speeds are 5.25 (f22), 5.24 (f23), 5.16 (f24) and 4.94 (f25) m/s, so speed is clearly falling after f23.

**Answer: |a| ≈ 1.9 m/s².**

## Confidence
Low to moderate. The value is the small difference of two speeds near a speed maximum, and the depth-rate curvature makes up about half of it. The plausible range is roughly 1.0-2.5 m/s².

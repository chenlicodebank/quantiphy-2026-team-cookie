# Q1333 — length of the white car (the white Chevy-style van), simulation_0066

The question asks for the white car's length. The white car is the white van (`van` in scene/). The prior says it accelerates at 4 m/s². depth_info gives the van's distance as 23.5892 m at f14 and 19.9903 m at f38, plus depths for the taxi, bike and human. The file runs at 24 fps and question_fps is also 24.

## Camera calibration
- **Vanishing points** (`vp.py`): I fitted the curb edges at sub-pixel precision on scene/bg.png.
  - Road A (lines A1–A3): VP at (623, 82).
  - Road B (lines B2, B3): VP at (3130, 76).
  - Assuming the two roads are perpendicular and the principal point is at the image centre, f ≈ 855 px. Treat this as ±30 px; the taxi check below supports 855–870.
- **Rotation**: taken from the two road directions. The ground normal is their cross product.
- **Camera height** (`boxfit.py`): I fitted a 3D box model to the van's per-frame bounding boxes over f0–71. The model drives along road A with s = s0 − 2(t − t0)², i.e. the prior's a = 4. It is constrained to reproduce both van depths exactly. Result: camera height hc = 6.84 m (f = 855, origin on the ground; 6.93 m with the origin 1 m up). The fitted t0 ≈ 0 s.
  - The box model itself gives L = 5.1 m. This is biased low: a box cannot represent the lower hood and front, so the fit pulls the front back. I did not use it for the length.

## Length measurement (`front2.py`, `side71.py`), frame 71, where the van's side is visible
- **Side plane**: I read the near-side wheel hub centres by eye from zoomed crops: rear (1458, 704), front (1822, 966). I put them on a plane at wheel-centre height (0.38 m), which gives a wheelbase of 3.78 m. Their direction is within 1.5° of the road direction. The vertical plane through them is the near side of the van.
- **Rear-most point**: the leftmost silhouette pixels (x 1394–1404, y 600–640). Intersected with the side plane, they give s = −1.09 m relative to the rear hub, at heights 0.7–1.2 m.
- **Front-most point**: the bottom edge of the front bumper at about (2000–2010, 1031–1035), at a height of 0.35–0.45 m. This gives s = +4.71 to 4.73 m.
  - Consistency check: the far-front hood corner (2094, 880) on the far-side plane gives s = 4.49 m at a height of 1.1 m. The bumper sitting 0.2 m ahead of the hood is plausible.
- **L = 4.72 − (−1.09) ≈ 5.80 m** (f = 855, hc = 6.84). Variants:
  - f = 800: 5.86–6.0 m; f = 906: 5.6–5.7 m.
  - Origin 1 m up (zo = 1, hc 6.93): +0.08 m.

## Scale checks (second routes)
1. **Taxi at f38** (`taxicheck.py`): I put its near-side hubs on the calibrated ground and placed its centre half a width inward. Matching the given taxi depth of 16.549 m needs hc = 6.71–6.89 m, i.e. a factor k = 0.98–1.01 relative to the box-fit height. The taxi's wheelbase comes out at 2.93 m; a real Crown Victoria is 2.91 m. This supports both f ≈ 855–870 and real-world scale.
2. **Motion stereo on the van's orange front marker** (`stereo.py`, `stereo2.py`): I tracked the marker automatically over f56–71 and used the baseline implied by a = 4. Its 3D distance at f71 is 0.4–4% larger than the side-plane reconstruction, depending on t0.
3. **Back-propagating the f71 centre with a = 4 to the given depths** (`scale_solve*.py`): this gives k ≈ 1.08. It is badly conditioned: a 0.3 m position error is amplified about 2.5 times over the 12–17 m extrapolation. It disagrees with checks 1 and 2, so I did not use it.
4. **Plausibility**: the box fit gives W ≈ 2.06 and H ≈ 2.06 m, close to a real Chevy Express (width 2.0, height 2.1). Length over wheelbase is 5.8/3.78 = 1.53, close to the extended Express (6.2/3.94).

## Answer
The length is about 5.8 m on the calibration above. I added a small allowance (+0.03–0.05 m) because the centres of the bumpers stick out a little past the corner points I measured, and leaned slightly toward the stereo and taxi scale (k ≈ 1.00–1.01). **Answer: 5.85 m.**

Confidence: moderate. The estimated error is about ±5%. The main sources are the front bumper point (±0.1 m), f (±3% on L) and scale (±2%).

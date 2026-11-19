# q_1848 — height of the forklift (m)

Prior: "gravity acc = 9.8 m/s^2"; no depth_info. 2D side-view clip, 24 fps (file = question fps), 40 frames.

## Measurements (pixels)
- From scene/tracks/forklift.csv, which I checked against frame 0 at 3x zoom: the bbox height is 195 px (median of frames 0–11) and the length is 257 px. Wheel bottoms are at y ≈ 927 and the mast/overhead-guard top is at y ≈ 733.
- fit_acc.py fits a quadratic to x(frame) for frames ≥ 3. It gives uniform horizontal acceleration from rest at t ≈ 0: 0.91 px/frame² = 527 px/s² (rear edge x0) and 523 px/s² (bbox centre), with residual rms < 0.8 px.

## Scale decision
- Nothing in the clip falls; the forklift drives horizontally on the ground. If its horizontal acceleration were taken as 9.8 m/s², the scale would be 0.0186 m/px. That makes the forklift 3.6 m tall and 4.8 m long, with an operator cab about 1.9 m high. A compact cab-type Toyota forklift is about 2.0–2.2 m tall (overhead guard) and wheelbase about 1.2–1.6 m, so that scale is implausible by more than 60 %. The gravity prior describes motion this clip does not show, so it gives no usable scale.
- So the scale comes from the forklift's real size (a standard object). Estimates:
  - typical overall/overhead-guard height of a 1.5–2.5 t Toyota counterbalance forklift: about 2.1 m
  - front tyre about 0.58 m over about 65 px gives height about 1.75 m; rear tyre about 0.46 m over 55 px gives about 1.65 m (rough, because the fenders partly hide the wheels)
  - wheelbase 158 px against 1.4–1.6 m gives about 1.75–2.0 m
  - seat-to-roof clearance (about 85–100 px) against about 1.0 m gives about 2.0–2.4 m
- Answer: **2.05 m** (the middle of these routes).

## Confidence
Low to moderate. The answer depends on the real-world size of the asset, not on a measured scale. If the reference instead used the acceleration as g, the answer would be about 3.6 m.

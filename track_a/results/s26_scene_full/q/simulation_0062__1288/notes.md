# Q1288: height of the traffic light (m)

File fps = question_fps = 24, so no time-base conversion was needed.

## Scale (scale.py)
- Route 1, from the prior: the white van moves parallel to the image plane at constant image size. A quadratic fit to its track (f2–71) gives a = 307.18 px/s². The prior is 4 m/s², so the scale at the van's depth is s = 0.013022 m/px.
- Route 2, from depth_info alone: the van's distance is 30.065 m at f14 and 29.307 m at f38, and its depth is constant. That gives s = 0.012929 m/px (0.7 % from route 1). Depth Z ≈ 29.16 m and f ≈ 2240–2256 px.
- Camera height: the van's tyres are at y = 615 and the horizon/principal point at y ≈ 539.5–540, so h_cam = 75·s ≈ 0.974 m (0.970–0.977).
- Checks: the predicted ground row for the cyclist at depth 27.1 m is 621, against 619.5 measured. The pedestrian (on the sidewalk) is within a few px, as expected for feet versus pelvis.

## Traffic light (profile.py, lights.py; frame 0)
- The question doesn't say which light; there are four. The near-right light (triangular crossing sign) is the largest and clearest. Its sign top is at y = 121.5 and the pole base, standing on the sidewalk, at y = 641.5, so Δ = 520 px.
- Sidewalk height: the curb faces measure 5.5 px over a road row at 661.5 (near-right) and 12 px over 814 (near-left). That puts the sidewalk top at about 0.045·h_cam ≈ 4 cm above the road.
- Ground-plane geometry: H = h_cam·(1 − 0.045)·Δ/(y_base − y_h) = 0.974 × 0.955 × 520/102 = 4.74 m. Without the curb correction it would be 4.97 m.
- Second route, the other lights:
  - Far-left (same model): top 295, base about 599, giving 4.75 m.
  - Near-left (twin-head model, top 140, base 637): 4.74 m.
  - Far-right gives about 4.6 m, but its thin top flag is probably under-detected.
- So all the lights come out at about 4.75 m.

## Answer
4.76 m. Confidence: moderate-high, about ±4 %. The main uncertainties are the horizon row (±0.5 px ≈ 0.5 %), the scale (0.7 %) and whether the bounding box starts at the sidewalk surface (the curb correction is 4.5 %).

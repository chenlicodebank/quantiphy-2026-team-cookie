# q_2363 — velocity of the white jar at t = 0.60 s (cm/s)

File fps = question fps = 24 → t = 0.60 s is frame round(14.4) = 14, the release frame (checked on a zoomed frame:
the jar has just left the near person's fingers, centroid ≈ (408, 238) px, motion-blurred).

## Method (fit3d.py, joint.py)
- Pinhole camera, f = 0.5959·1280 = 763 px, principal point (640, 360).
- Free-flight centroids from scene/tracks (checked). White jar frames 14-17 and 20-26; yellow toy ("carrot")
  frames 14-17 and 20-23. Frames 18-19 are left out because the two objects overlap in the image there, and
  yellow 24-26 because the toy touches the catcher's hands.
- 3D model: P(t) = P0 + V t + ½ g t² with |g| = 9.8 m/s² (the prior). The direction of g is fitted, and
  |P0| equals the depth_info value at frame 14 (jar 1.9735 m, carrot 2.63 m). Fitted by least squares on the
  reprojection error.
- The jar and the carrot fitted separately give the same gravity direction (optical axis tilted 57° and
  60° below horizontal), which is an independent check of the geometry. The rough vertical vanishing point in
  scene/ (46°) fits worse (rms 2.5 px against 1.4 px) and was not used.

## Results (jar speed at frame 14)
| fit | |V| at frame 14 | forward diff 14→15 | mean of 5 forward diffs |
|---|---|---|---|
| jar alone, g free | 285.8 | 274.4 | 247 |
| jar + carrot joint g | 280.0 | 267.5 | 235 |
| jar with g from carrot | 274.8 | 261.5 | 226 |
| jar with g from vanishing point (rejected) | 328 | 317 | 288 |
- Jar depth goes from 1.97 m at release to about 2.8-2.9 m at the catch (far person at 3.24 m with arms
  forward), which is plausible. The carrot moves from 2.63 m to about 1.7 m, near the near person's hands.
- Image-plane check: frames 12→13→14→15 move 53, 44 and 48 px/frame. At 1.97 m, 48 px/frame is about
  2.97 m/s of motion across the image, so a smoothing window centred on frame 14 gives about the same value as
  the instantaneous speed.

## Answer
277 cm/s: the instantaneous speed at release is 275-286 cm/s, and a forward difference gives 262-274 cm/s.
Confidence: moderate, about ±10%. The main uncertainty is the depth-rate component and whether the
reference smoothing window includes the in-hand frames.

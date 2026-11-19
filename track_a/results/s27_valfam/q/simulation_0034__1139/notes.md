# q1139 — average speed of the boat (m/s)

File fps = question_fps = 24, 72 frames; no time-base conversion needed.

## Method (measure.py)
- The boat approaches the camera almost head-on (scene/ record: image x is constant, y drifts 6.4 px/s, apparent
  scale 1.000 -> 1.138 with 1/scale linear in t, so the speed is constant).
- depth_info: boat distance 96.8995 m at t=1 s and 92.8490 m at t=2 s, so the line-of-sight rate is 4.0505 m/s.
- Focal length from the person: 1.75 m tall, 67 px high (median bbox) at about 92.19 m, so f ≈ 3530 px. The 3D position
  is the back-projected hull-centre track times the depth, with depth linear in t. The mean of the per-frame
  backward-difference speeds is 4.055 m/s. With f = 2500 or 5000 it is 4.060 or 4.053, so the result hardly
  depends on f because the sideways motion is only about 0.17 m/s.

## Second route
- Apparent scale of the boat: (d - c) = k/scale, with k and c fitted to the two given depths. This gives
  c = 3.4 m (the origin is behind the bow, which is plausible), d(0) = 100.80 m and d(71) = 88.97 m. The net approach
  rate is (100.80 - 88.97)/(71/24) = 4.00 m/s. Per-frame scale differences are too jittery to use directly.
  This agrees with the depth-based route to about 1.3 %.

## Answer
4.05 m/s. Confidence: high (within about 2 %).

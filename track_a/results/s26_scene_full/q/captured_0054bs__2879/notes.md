# q_2879: soccer ball displacement between 1.0 s and 1.4 s

The question uses 24 fps, the same as the file. So t = 1.0 s is frame 24 and t = 1.4 s is frame 34 (round(33.6)). The source frame missing between 35 and 36 falls outside this interval. It is accounted for (src index = frame+1 for frames ≥36) in the time fits.

## Camera
- f = 0.5959 × 1280 = 762.75 px, principal point (640, 360).
- The soccer ball has only one depth: L(t = 2.0 s, frame 48) = 3.254 m. Its depth at frames 24 and 34 therefore has to come from its apparent size, scaled by that one value.

## Measurements
- **`radial.py`:** I measured the ball myself. Each frame is compared with the median background. The disc edge is found along 120 radial rays, then a robust circle is fitted. Frames 29–46 give a smooth diameter trend with rms 0.7 px. The record's values are noisy at frames 39, 40, 44 and 45 (about 63 px); mine are 51–53 px there.
- **Centres:**
  - frame 24 (ball still partly hidden by the masked hand): (917, 604) radial and (920.7, 607.0) in the record;
  - frame 34: (884.7, 489.5).
- **Fitted diameter:** about 69–70 px at frame 24 (extrapolated, which agrees with frames 25–27), about 59 px at frame 34 and about 49–51 px at frame 48.
- **Ball size:** D = 3.254 × d48 / f ≈ 0.20–0.22 m, which is a plausible soccer ball.
- **Motion:** the ball shows almost no vertical acceleration (a gravity check gives about 0.1 m/s²). So it is rolling away along the floor, not flying, and the camera looks down; the horizon is far above the frame. Two depth models were therefore used:
  - (a) 1/Z linear in image v, which holds for motion on a plane;
  - (b) Z linear in time, for near-constant velocity.

## Results (`final.py`, `fit2.py`)
- **Pure pinhole, d = f D / L:**
  - L24 ≈ 2.25–2.50 m, L34 ≈ 2.63–2.82 m;
  - displacement 0.44–0.51 m, with the cluster at about 0.48–0.49.
- **With the off-axis enlargement of a sphere's image corrected** (the ball is 20–26° off-axis): displacement 0.42–0.47 m, cluster at about 0.44–0.45.
- The lens distortion of the real camera (barrel distortion would partly cancel the correction) is unknown, so I took the midpoint.
- Quadratic-in-time depth fits were unstable when extrapolated (0.5–0.9) and were rejected.
- About 2/3 of the displacement is the depth increase (about 0.35–0.45 m). The rest is the image-plane motion (about 120 px, about 0.25 m up and 0.04 m sideways).

## Checks
- **Prior check:** the basketball's velocity at t = 0.5, with size-based depth anchored at 2.24 m and smoothed over 4 frames, comes out at about 2.1 m/s. The prior is 2.21 m/s (about 4 % off), which supports the size → depth method.
- **Inconsistent depth:** the basketball's given depth at t = 1.0 (1.81 m) contradicts its shrinking image (76 → 60 px). That depth is probably a sensor artefact. It does not affect this answer.

## Answer
**0.47 m.** Confidence is moderate: the plausible range is 0.43–0.51, driven by how depth is extrapolated to frame 24, where the ball is half hidden, and by the off-axis/lens assumption.

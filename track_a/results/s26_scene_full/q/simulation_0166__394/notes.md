# Q394 – speed of the police car at 1 s (m/s)

Prior: speed of the bike = 5.52 m/s. No depth_info. fps = question_fps = 24, so t = 1 s is frame 24.
The camera is static. Both the van and the cyclist move purely horizontally (dy = 0) at constant pixel speed along the same cross street.

## Measurements (measure.py, cyc.py: SSD template matching with sub-pixel parabola)
- Van, upper-body template from f66, frames 45–79: 26.97 px/frame (step std 0.21). The scene CSV fit over f24–79 gives 27.01 and over f24–40 gives 27.03.
  At f24 the van is only partly in frame, but its speed is constant over the whole clip, so the speed at f24 equals this value.
- Cyclist, rigid basket/front-wheel template from f45, frames 30–64: 21.0 px/frame (steps 20.7–21.3). The scene CSV fit gives 21.03 over f0–79.
  The helmet/torso template is noisier (pedalling) and loses lock once the van approaches.
- Pixel-speed ratio van/bike = 27.00 / 21.02 = 1.284.

## Scale
- 2D convention (one m/px from the bike): 5.52 × 1.284 = **7.09 m/s**.
- Perspective correction: the tyre contacts are at y ≈ 743 (van) and y ≈ 738 (bike), with the horizon at y ≈ 598.
  Ground-plane depth is proportional to 1/(y − horizon), so the bike is 145/140 = 1.036 times farther away than the van.
  That gives a true van speed of 7.09 / 1.036 = **6.84 m/s**.
- Sanity check with the bike scale (0.01094 m/px): van length 438 px → 4.8 m, bike plus rider 163 px → 1.78 m. Both are plausible.

## Answer
6.95 m/s. This is the midpoint of the two readings (6.84 and 7.09), 1.6 % from 6.84 and 2.0 % from 7.09, so it is within 5 % under either.
Confidence: high that the answer is in the range 6.8–7.1.

# q2126 – mug velocity at 0.50 s (cm/s)

Internet video, overhead static camera (shift < 1 px), 25 fps (file and question rates agree). Single planar scale from the prior.

## Scale (prior: earphone case width = 45 mm)
AirPods case (static, centre ~(2602,975)) lies on its face, rotated ~30°. The seam/hinge line and the port edge run
at ~28-36° below horizontal, so the case width (shorter side) is the extent along that direction.
`case_measure2.py`: low-saturation mask (it includes the shaded side wall), projected extent along 30-32° = 195-202 px;
the side lengths are ~197 x 215 px (ratio 1.09-1.2, consistent with a 44 x 53 mm AirPods case).
I used width = 197 px, which gives 0.2284 mm/px (±2 %).

## Velocity
t = 0.50 s → frame 12.5; round() → frame 12. Forward difference p(13) − p(12) spans 0.48–0.52 s, so it is also centred on 0.50 s.
- Recorded rim-centre track: (3020.4,1477.2) → (2967.9,1514.8): 64.6 px/frame.
- Coffee-disc centre: 64.9 px/frame.
- Independent template match of the cup interior, frame 12 → 13 (`cup_check.py`): 67.2 px/frame. This is slightly high
  because the cup grows as it is lifted.
- Adopted value: 65 px/frame = 1625 px/s, × 0.02284 cm/px = **37.1 cm/s**.

Alternative reading (frame 13, p14 − p13 ≈ 72 px/frame) would give ≈ 41 cm/s.
Confidence: moderate (±5-10 %). The main uncertainties are which frame the reference uses and the case pixel width.

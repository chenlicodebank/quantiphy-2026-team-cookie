# q_575 — lampshade height (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 (file) = question_fps 24, so no re-timing.

## Scale from the cat
- The cat walks steadily left to right in its floor lane (paws at y≈1020). I fitted a straight line to its x position on the visible frames, using scene/tracks/cat.csv and checked by `shade.py`:
  - nose bbox_x1: 17.76 px/frame
  - centroid: 17.81 px/frame
  - torso: 17.86 px/frame
  - mean step of the nose: 17.78 px/frame
- Using 17.78 px/frame × 24 = 426.7 px/s gives a scale at the cat's depth of 0.94 / 426.7 = 0.002203 m/px.

## Lampshade pixel height (`shade.py`)
- I separated the white shade from the wall by a brightness threshold on frame 48 and took its largest component. The mask was checked by eye in frames/shade_mask.png.
- Box: x 1411-1621, y 503-607. Height = 105 px (the pleated bottom edge is at 605-607), width 211 px. This matches the scene record (502-607).

## Depth correction (the lamp is farther than the cat)
The lamp stands on a table against the back wall, behind the cat's lane.
- Horizon: I fitted the front-to-back table-top slat lines and took their vanishing point (`slats2.py`, 7 lines with rms 0.25-0.57 px). Least squares gives (872, 500). Slope versus x gives y≈483. I used a horizon at y≈490.
- On the floor, depth Z ∝ 1/(y − y_h):
  - cat paws at y=1020 → 530
  - table front feet at y≈991 → 501
  - table back feet at y≈965 → 475
- On the table top, Z ∝ 1/(y − y_h):
  - front slat ends at y≈797 → 307
  - lamp base contact at y≈790 → 300
  - back edge at y≈782 → 292
- Check: the table's front-to-back depth ratio is 1.051 from the top and 1.055 from the feet. They agree, so the legs are close to vertical in depth.
- Lamp depth / cat depth = (530/501) × (307/300) = 1.058 × 1.023 ≈ 1.08. With the horizon anywhere from 470 to 510 this ratio stays between 1.079 and 1.086.

## Answer
105 px × 0.002203 m/px × 1.08 ≈ 0.250 m.
Without the depth correction (pure single-plane 2D scale) it would be 0.231 m.

## Confidence
Moderate. The pixel height (±1-2 px) and the cat scale (<1%) are solid. The main uncertainty is the depth ratio, about ±3%, which depends on the vanishing point and where the cat's origin sits in depth.

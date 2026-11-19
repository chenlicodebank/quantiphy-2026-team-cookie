# q_230 - length of the car (prior: speed = 6.66 m/s)

## Time base
I used fps = 24.007, from the file. question_fps (24.0) differs by only 0.03 %, so the choice doesn't matter.
v = 6.66 / 24.007 = 0.27742 m/frame.

## Measurements
- **Motion (scene/tracks/car.csv, checked):** the near-side hub midpoint moves at 28.227 px/frame, uniform and
  horizontal. The rms residual is 0.65 px. So the near-side wheel plane has a scale of 0.27742/28.227 = 0.009828 m/px.
- **Silhouette length:** bumper to bumper, 421-423 px in frames 20-28 near the image centre (frame 24: x 308-729,
  checked on the frame). I used 422 px.
- **Perspective (`tyre_profile.py`):** I measured where the far-side tyre peeks out beyond the near tyre.
  - Frame 7 (near front hub at u = -374.5): the far hub is at about -340, so the far/near depth ratio is about 1.10.
  - Frame 45 (near rear hub at u = +466.5): the far hub is at about +417, so the ratio is about 1.118.
  - These edges are the far tyre's inner face and the near tyre's outer face, which are about one track width apart.
    So the depth of the car centre / near outer face is about 1.06.
- **Focal length estimate:** about 1340 px, which puts the bumper rays at about 9 deg. The silhouette extremes are
  rounded-bumper tangent points about 0.3 m nearer the camera than the centreline, and set back about 0.03 m from
  the tips.

## Length
- Near-side-depth reading: L = 422 x 0.009828 = 4.15 m.
- Centre-depth reading: 4.15 x 1.062 = 4.41 m.
- Tangent-point model: about 4.36 m.
- The answer is somewhere between 4.15 and 4.41 m.

## Second route
- The near-side wheelbase is 232 px, which gives 232 x 0.009828 = 2.280 m. The wheelbase lies in the near wheel plane,
  so it needs no depth correction.
- That matches a real Porsche 930 Turbo (wheelbase 2.272 m, length 4.29 m), so the model looks real-scale and
  consistent with the prior. Scaling 4.29 by 2.280/2.272 gives 4.31 m.

## Answer
4.33 m (blend of 4.36 from geometry and 4.31 from the wheelbase ratio). Confidence: about ±3 %.

# Q2535 — white ball speed at t = 1.6 s (cm/s)

File fps = question_fps = 24 -> t = 1.6 s is frame 38. Lab camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
Given: white ball distance 0.994 m at t = 1.6 s. The tennis-ball prior (6.7 cm) is not needed: the white ball's own depth
at frame 38 plus how its apparent diameter changes give its distance in every frame.

## Method
- The ball rolls almost straight toward the camera, so the depth change is most of the speed (image-plane part only ~6 cm/s).
- `circfit.py`: per frame, finds radial edge points on the top and side arcs (excluding the shaded bottom and the shadow)
  and fits a circle -> centre (u, v) and diameter D. D at frame 38 = 25.7 px (smoothed 25.2), 18.5 px at rest, 29.8 px at frame 48.
  Checked by eye against the segmentation outline on zoomed frames 30, 38 and 48 (frames/w*.png).
- Distance(i) = 0.994 x D(38)/D(i), with D smoothed by a polynomial over frames 16-48. Each position is the back-projected unit ray x distance.
- `velocity.py`: smooth (quadratic or cubic) fits of u, v and D give a speed of 35.9-36.4 cm/s at frame 38 (backward, forward and
  centred differences agree). Using the threshold-width diameters (`diam.py`, which run ~2.5 px smaller) instead gives 37.5-38.1 cm/s.
- Second route (`plane.py`): fits the plane of the ball centre to all of the diameter depths (rms residual 2%), then takes depth
  from each frame's precise image position and that plane. Speed at frame 38 = 37.1 cm/s (centred), 37.3 back / 36.9 forward.
  The mean of five forward differences is 35.8, and the 4-frame displacement gives 33.7.
- Velocity components at frame 38 (camera frame): about (-6, 0.5, -36) cm/s.

## Answer
36.5 cm/s. Confidence moderate (about ±10%). The speed depends on the diameter growth rate (about 0.37 px per frame), so a
systematic diameter bias of 1-2 px would change it by roughly 5%.

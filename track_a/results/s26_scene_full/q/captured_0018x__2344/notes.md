# q_2344 — distance between the box and the soccer ball at t = 3.0 s (in cm)

## Key problem
At question_fps 24, t = 3.0 s is frame 72, but the clip only has frames 0-48 (it ends at 2.0 s). The file rate is also 24 fps.
So the answer is **extrapolated** and comes with low confidence.

## Inputs
- Camera f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Soccer ball distance is 2.80 m (given). The box's depth is not given. I estimated it from floor-contact rows: the lying
  box's bottom is at y≈609 and the ball's floor contact is at about 570, which puts the box's forward depth at about 2.28 m.
  Measured against the left person's feet (y 577, about 3.0-3.1 m), it comes out at about 2.62 m. Using the ball's own
  distance (2.8) is a third option. The result changes by less than 4 cm across these choices.
- The gravity prior was checked: the ball's free fall (frames 31-35) has a second difference of about 5 px/frame² ≈ 2900 px/s².
  That gives 3.4 mm/px, which agrees with 2.7 m / 763 px = 3.5 mm/px at the ball's depth.

## Positions (scene tracks, checked on the frame-48 crop)
- Frame 48: the ball is at (552.5, 407), near the top of its rebound. The box lies flat on the floor at (418.5, 594).
  The 3D distance there is 77-80 cm.
- Extrapolating to frame 72:
  - Ball: rebound heights shrink by a factor of about 0.48 per bounce (136 px for the first). By frame 72 the ball is
    in a low third hop, with its centre at about y 510-550. It drifts right at 2.2 px/frame, so x ≈ 598-607 if the drift
    continues (≈552 if it stops).
  - Box: lying flat, it has probably stopped at x ≈ 410, y ≈ 595.
- Distance at frame 72: about 68-73 cm with the drift and about 50-57 cm without it. The answer is 66 cm (drift mostly kept).

## Confidence
Low. The asked time is outside the video, and the box's depth is not given.

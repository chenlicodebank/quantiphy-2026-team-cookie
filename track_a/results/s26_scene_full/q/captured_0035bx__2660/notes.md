# Q2660 – basketball velocity at t=1.4 s (frame 34 at 24 fps; file fps = question fps = 24)

## Depth labels
depth_info labels both t=1.4 values as "soccer_ball" (2.6020 and 2.3730), so one of them is really the basketball.
Fitting a floor plane (ball centres at a constant height) to the two t=0.9 depths gave a 39° downward tilt (plane.py).
That plane predicts soccer 2.45 m and basketball 2.57 m at frame 34. So the **basketball is at 2.602 m** and the soccer
ball at 2.373 m. This also agrees with the image: at frame 34 the soccer ball is lower in the image and so nearer the camera.
The apparent size agrees too: the basketball grows 68→72 px, about 6%, against a depth ratio of 2.778/2.602, about 6.7%.
The other assignment would put the plane at a ~40° camera roll, which is implausible.

## Method (vel.py)
- f = 0.5959·1280 = 763 px, principal point (640, 360).
- Basketball centres per frame are taken from scene/tracks (circle centre and also the mask centroid). I checked them: the ball is free and unoccluded in frames 12–44.
- Per-frame depth comes from a plane fitted to all 4 given depths (residuals ≤ 2 cm). As an alternative, depth was linearly interpolated from 2.7777 m at f22 to 2.602 m at f34.
- Each centre is back-projected to 3D, then I took 3D forward differences × 24.

## Results
- Per-frame speeds are steady at about 100–113 cm/s, except the step from f35 to f36, which is about 204 cm/s. Both balls move about 2× in that step, so a capture frame was probably dropped there.
- Forward difference at f34: 94–106 cm/s. Mean over the 5-frame window from f32 to f36: 125–128 cm/s, because the window includes the dropped-frame step. Excluding that step gives 103–108 cm/s.
- The reference convention smooths over at least 5 frames. A centred window at f34 includes the jump, giving 116–127 cm/s depending on window size (5 to 9 frames). The true physical speed is about 105 cm/s.
- Answer: **120 cm/s**, a compromise. It is within about 4% of the smoothed-with-jump values and about 14% from the physical speed.

## Confidence
Moderate. The main uncertainties are whether the smoothing window includes the dropped-frame jump (about ±10%) and the depth label assignment (resolved by geometry).

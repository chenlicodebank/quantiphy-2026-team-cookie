# Q1208 — bicycle height (handlebar top to ground), simulation_0050

Answer: **0.97 m**. File fps = question fps = 33, so t=1 s is frame 33 and t=2 s is frame 66.

## Pixel measurements (crop.py zooms, frames/c33.png and frames/c66.png)
- Frame 33: top of the handlebar ≈ y 533 (the hand's top is at ≈529 and is not counted). The ground under the
  handlebar, where the front wheel touches it, is ≈ y 688.5. That gives **155.5 px**.
- Frame 66: handlebar ≈ y 543 and ground ≈ y 670.5, giving **127.5 px**. The ratio 1.22 agrees with the depth ratio
  14.642/11.896 = 1.23.

## Focal length: the main problem
- **Prior route (rejected).** Take the walking person's speed of 1.236 m/s, place the given person depths at the
  visible torso and pelvis (m1.py), and solve for f. This gives f ≈ 3000 px. But at that f the pedestrian is
  1.42 m tall, the rider's head is 1.09 m above the ground, a wheel is 0.38 m across and the handlebar is 0.62 m
  high, which is implausible. The person's motion would also not be parallel to the street. In the image the
  person's feet move along the line to the street's vanishing point. At any reasonable f, the given person depths
  change faster (0.81 m/s) than walking along the street allows. So the person's depth origin does not follow the
  visible body, and this route is unreliable.
- **Route A: vanishing points (vp2.py, image only).** LSD line segments with RANSAC. The facade horizontal lines
  meet at (-2800, 581). The verticals meet at (650, -23300). Requiring the two directions to be at right angles
  gives f ≈ 1877 px. This is sensitive to the x of the vertical vanishing point: f is 1750–2130 over the plausible
  range.
- **Route B: direction of the bike's motion (solve.py).** Back-project the bike centre (between the hubs) at t=1 and
  t=2 using the given bike depths. Its direction of motion matches the facade vanishing point (x ≈ -2800) at
  f ≈ 1800–1850.
- **Route C: real-world sizes.** At f ≈ 1870 the wheel is 101.7 px tall at frame 33, which is 0.65 m (a standard
  26-inch wheel). The rider's head is 1.73 m above the ground and the bike moves at 4.9 m/s. All of these are
  realistic.
- I used **f = 1870 px**, with a plausible range of 1800–1950.
- At this f the pedestrian comes out about 2.27 m tall. That figure does not depend on f alone: from the image and
  the horizon, the rider's head is only about 0.76 of the pedestrian's height. The pedestrian asset therefore seems
  oversized, or their depth origin is offset. The bike and rider are mutually consistent and realistic, so the
  scale comes from them (routes A, B and C) and not from the pedestrian prior.

## Height in 3D (solve.py)
- The bike centre is placed at the given distance along its ray.
- The ground point under the handlebar is that ground pixel's ray intersected with the bike's vertical mid-plane.
  The plane is built from the travel direction and the up direction, which comes from the vertical vanishing point.
- The height h is found so that ground + h × up projects onto the handlebar row.
- At f = 1870: h = 0.987 m (t=1) and 0.960 m (t=2), mean **0.97 m**.
- Over f = 1800–1950: 0.92–1.02 m.
- With the rejected prior-route f (3000) it would be 0.62 m, and with f from a 1.75 m pedestrian (2430) it would
  be 0.76 m.

## Confidence
Moderate. The two image-based routes and the real-world sizes agree on f to within about 5%. The pedestrian prior
contradicts them, and I explained above why I set it aside.

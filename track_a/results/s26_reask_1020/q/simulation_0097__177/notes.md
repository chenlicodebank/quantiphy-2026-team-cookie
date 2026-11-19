# Q177 – length of the plane (m)

2D simulation, 24 fps (file fps = question fps). Prior: car acceleration = 10 m/s^2.

Method (fit.py): the car's mask-centroid x track (scene/tracks/car.csv, frames 0–40) is fitted with a quadratic.
The acceleration is 0.370–0.371 px/frame^2 for every start frame (0, 1, 2, 5), and a rest-then-uniform-acceleration
piecewise fit also gives 0.3713. Residuals are 0.15–0.2 px. The per-frame speeds rise linearly.
a = 0.371 px/frame^2 × 576 = 213.9 px/s^2, so the scale is 10 / 213.9 = 0.04675 m/px.

Plane length: 800 px on every frame where the plane is fully in view (frames 18–38, range 799–801). It is measured
nose to tail, along the direction of flight.
Length = 800 × 0.04675 = **37.4 m**.

Check: the same scale makes the car 121 px × 0.04675 = 5.66 m long, which matches a real Cybertruck-like pickup
(about 5.7 m). A plane length of 37.4 m is a realistic narrow-body jetliner. Confidence: high (±1–2 %).

# q_1060 — cart wheel diameter (simulation_0011)

File fps = question_fps = 24. Cart depth (origin) 33.235 m; nest 17.27 m; crow 46.65 -> 43.97 m; house 63.60 m.

## Wheel in pixels
Near cart wheel at frame 0 (frames/cart.png, 3x crop): rim x 1650-1820, y 1262-1432 -> diameter ~171 px,
nearly circular (faces the camera). Centre (1735,1347), ~8 deg off axis (correction ~1 %).

## Scale route 1: gravity (prior) on the falling nest -> rejected
The black fuzzy object = the nest (17.27 m). Re-tracked it (track_nest.py, fit2.py). Quadratic fits of the centroid /
bbox over frames 33-49 give a pixel acceleration of 1250-1350 px/s^2 (bottom/top edges 650-1900, noisy because of
trunk occlusion, tumbling and blur). f = a_px * Z / g = 2200-3050 px. That scale makes the doorway (200 px at ~61 m)
4-5 m tall, the barrels (~85 px) 1.7-2.3 m tall, the crow's wingspan (~148 px at ~40.5 m late in the clip) 2-2.6 m
and the cart wheel 1.8-2.4 m: every everyday object 2-2.7x too large (>40 % off). The fall timing is internally
consistent with that slow acceleration (it slides off the branch ~f24-33, then lands f50), so I could not find a
geometric error; the nest's motion apparently does not follow 9.8 m/s^2 at the scene's real scale (damping / time
scale). Per the instructions the scale is taken from standard objects instead.

## Scale route 2: standard objects (used)
- Doorway 200 px tall at ~61 m (front wall ~2.5 m before the 63.6 m house origin), door ~2.05 m -> f ~ 5950.
- Barrels ~85 px tall at ~60.5 m, 0.85-0.9 m -> f ~ 5700-6050.
- Crow max wingspan bbox ~148 px at ~40.5 m (depth extrapolated from the given 2.68 m/s approach), ~1.0 m -> f ~ 6000.
Adopted f = 6000 px (hFOV ~18 deg).

## Answer
Near wheel centre ~0.4-0.5 m closer than the cart origin -> ~32.8 m. D = 171 * 32.8 * 0.99 / 6000 = 0.93 m
(range 0.85-1.05 for f 5400-6500). A plausible farm-cart wheel.
Gravity-route alternative (not used): ~1.8-2.4 m.

Confidence: moderate; the main risk is the scale-route conflict above.

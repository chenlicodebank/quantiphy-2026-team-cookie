# q929 — length of the spacecraft (hover car), simulation_0264 (2D)

Prior: acceleration 4 m/s^2 at t = 1.0 s. The motion is a uniform acceleration from rest, so the prior sets the scale. fps = question_fps = 24.

## Pixel acceleration (fit.py, quadratic fits to scene/tracks/hovercar.csv)
- Front edge x0, frames 2–52: 1.138 px/frame^2 (rms 0.5 px; the rest point fits frame ~0.1).
- Front edge x0, frames 20–52: 1.146. bbox centre, frames 9–52: 1.159 (rms 1.0).
- A cubic fit of x0 shows that the acceleration is close to constant (1.12 to 1.155).
- The rear edge x1 is noisy (thin fins and antennas, rms 9.6) and was not used.
- Adopted value: about 1.145 px/frame^2 = 660 px/s^2, so the scale is 4/660 = 0.00606 m/px.

## Pixel length
- The bbox length when the car is fully visible runs from 1021 px (frame 9) to 1008 px (frame 24, the prior's time) to 1001 px (frame 30) to 975 px (frame 52). The change comes from mild perspective and view change.
- I checked the bbox at frame 30 on a grid crop: it runs from the nose tip at about 1068 to the rear fin at about 2075, so it is correct.
- Adopted length: about 1000 px (mid-traverse / median).

## Result
- 1000 px x 0.00606 m/px = 6.06 m.
- Using x0 alone (0.00610 m/px) gives 6.10 m.
- Answer: 6.07 m.
- The range over the frame-dependent pixel length (975–1021 px) is 5.9–6.2 m.

Confidence: moderate-high (about ±4%). The main uncertainty is which pixel length the reference used, given the perspective.

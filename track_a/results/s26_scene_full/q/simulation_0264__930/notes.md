# q930: height of the spacecraft (hover car), simulation_0264
This is a 2D simulation at 24 fps. The file fps equals question_fps, so the clip was not re-timed. Prior: acceleration at 1.0 s = 4 m/s^2.

## Pixel acceleration (fit.py)
- The car accelerates uniformly from rest. A cubic fit shows the acceleration is constant: -1.126 px/frame^2 at frame 10, -1.136 at frame 24 and -1.150 at frame 45.
- Quadratic fits:
  - Front edge x0, frames 2–52: 655 px/s^2 (rms 0.49 px).
  - x0, frames 10–40: 654.
  - x0, frames 2–30: 651.
  - Bbox centre, frames 9–52: 667.
  - Bbox centre, frames 4–40: 654.
- Adopted 658 px/s^2, so the scale is 4/658 = 0.00608 m/px.

## Pixel height (height.py)
- I masked the car by difference from the empty background (frame 71) and removed the shadow (y > 1060).
- Over frames 12–44 the car spans y 728 to 1041/1042, a height of 314–315 px. Thresholds 8 / 15 / 30 give 318 / 315 / 310 px.
- The rear antennas are included, since the mesh bbox includes them. I checked the box on an overlay (frames/box24.png).
- Adopted 315 px.

## Answer
- 315 x 4/658 = **1.915 m**.
- Across the acceleration estimates (651–667 px/s^2) the height ranges from 1.89 to 1.94 m.
- Second route: the accelerations from the centre track and the front edge agree within 2%.
- Caveats:
  - There is mild perspective: the camera is slightly above the car and its length shrinks 5% across the frame.
  - The body without antennas is about 265 px, which gives 1.61 m.
- Confidence: moderate to high.

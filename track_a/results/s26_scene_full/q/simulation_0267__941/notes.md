# Q941 – length of the spacecraft (m)

Prior: acceleration at 1.0 s = 4 m/s^2. 2D scene, static camera, 24 fps (file and question agree).
The spacecraft (a flying car) accelerates uniformly to the left from rest (starts at about frame 1). It does not move vertically.

## Pixel acceleration (fit.py, fit2.py; quadratic fits to the scene/ track)
- Nose tip x0, frames 10-52: -1.142 px/frame^2. Tail tip x1, frames 10-52: -1.146. Tip midpoint ref_x: -1.144 (rms 1.4 px).
- x0, frames 2-52: -1.139 (rms 0.5 px). ref_x, frames 14-34 (around t = 1 s): -1.162.
- The whole-car template is about 4 % higher at -1.189. It follows near-side panels and outline changes, so I did not use it as primary.
- Adopted value: 1.144 px/frame^2 = 659 px/s^2, which gives a scale of 4 / 659 = 0.00607 m/px.

## Pixel length
- Nose to tail-fin tip at frame 24 (t = 1 s): x 1252-2269 = 1018 px, checked visually on frames/f24.png.
- The median over frames 10-52 is 1009 px. The apparent length drifts from 1031 to 982 px with perspective.

## Answer
L = 1018 × 0.00607 = **6.18 m**.
Checks: using x0 frames 2-52 gives 6.21 m. Using the median length gives 6.12 m. Using the template acceleration gives 5.95 m.
Confidence: good, about ±4 %.

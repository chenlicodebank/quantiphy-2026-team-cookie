# q195: shark height (m), prior: shark acceleration = 1 m/s^2

2D side view, fps 24 (file rate = question rate). Static camera.

- Pixel acceleration: quadratic fits x(t) to the shark track (scene/tracks/shark.csv, frames 1-72), run in fit.py.
  centroid -85.9 px/s^2 (rms 0.35 px), bbox centre -86.6, tail -86.4, nose -86.8. Split windows 1-36 / 36-72 give
  -85.2 / -86.8. Taken as a = 86.0 px/s^2, so the scale is 1/86.0 m/px.
- Pixel height: the mask y-extent is 850/851 to 957/958 in every frame, about 107.5 px (dorsal-fin tip to
  pectoral-fin tip). Confirmed on the zoomed crop of frame 36 (frames/crop.png).
- Height = 107.5 / 86.0 = 1.25 m.
- Sanity check: the length of about 275 px gives 3.2 m, which is plausible for a shark.
- Confidence: good, about ±3%.

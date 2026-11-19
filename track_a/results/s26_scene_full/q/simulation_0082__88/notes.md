# Q88 – width of the yellow car (prior: length = 5.67 m)

2D top-down render, 24 fps (same as question_fps). The yellow vehicle is a car (roof and glass, not a pickup bed as
scene/notes.md says). It is in the upper lane, front pointing left. One metres-per-pixel scale comes from the length prior.

## Measurements (measure2.py, measure3.py)
* Length (x extent, half-max edges of |frame − median background| on rows 390/401/412):
  frame 40: 305.7 px, 50: 305.7, 55: 302.6, 60: 303.8. The car is near the image centre at frames 55–60, so I use 303.5 px
  (the notes say perspective shrinks length ~3% across the frame). scene record: 304 px near the centre, which agrees.
* Width (y extent, half-max edges of the HSV saturation profile, column by column along the car at frame 55):
  - widest body (front and rear fenders): 112.0–112.6 px (edges y 345.3–457.8), same at frames 40/50/60 (112.2–112.3);
  - mid-body (doors): 106.3 px; the scene record's 108 px is a thresholded band, not the full extent;
  - including the side mirrors: about 128 px.
* Scale = 5.67 / 303.5 = 0.01868 m/px.

## Answer
Width taken as the body's bounding-box width without mirrors (wheel to wheel / widest fender): 112.5 px × 0.01868 = **2.10 m**.
Other readings: mid-body only 106.3 px → 1.99 m; with mirrors 128 px → 2.39 m.
Check: with the frame-average length of 304.7 px instead, the width is 2.09 m. The width/length ratio of 0.37 is plausible for a large car.
Confidence: fairly high. The main uncertainty is whether the reference bounding box includes the mirrors.

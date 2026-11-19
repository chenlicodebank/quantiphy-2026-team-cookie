# Q95 — width of the yellow car (m)

Prior: yellow car length = 5.67 m. 2D top-down video (fps 24 = question_fps), static camera.

## Scale
Yellow car bbox length along motion = 270 px in frames 0–30 (near image centre; it grows to 277 px at the left
image edge because of perspective, so the edge frames are not used). Scale = 5.67 / 270 = 0.02100 m/px.

## Width (width.py, profile.py, measure.py)
Per-column top/bottom silhouette of the car (yellow chroma R−B>40 or grey<118, which drops the soft shadows),
frames 18–34; every frame gives the same result:
- main body (between the wheel arches): rows 370..463 -> 94 px -> 1.97 m
- at the wheels / wheel arches (front and rear): rows 368..467 -> 100 px -> 2.10 m (dark tyre visible at 465–467)
- including the side mirrors: rows 358..473 -> 116 px -> 2.44 m
Perspective: the car sits 125 px above the image centre, so you see its lower side a little. Scaling the length
growth (7 px at an 800 px offset) gives about 1 px of extra width, so the wheel-to-wheel width is about 99 px.

## Answer
The convention is that a car's width runs wheel to wheel, so I take the wheel/arch extent: about 99.5 px x 0.0210 = **2.09 m**.
Other readings: body without arches 1.97 m; full bounding box with mirrors 2.44 m. The car looks like a
Cybertruck-style pickup. The real one is 5.68 m long, about 2.03 m wide with mirrors folded and 2.41 m with mirrors
out, so both readings are plausible.
Second route: the scene record lists a body width of 94 px and a width of 116 px with mirrors, which matches my
measurement. Confidence: the pixel measurement is good (±1 px); the main uncertainty is whether the mirrors count.

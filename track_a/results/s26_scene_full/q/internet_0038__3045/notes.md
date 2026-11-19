# q_3045: speed of the right hand, 0 to 0.54 s

**Answer: 0.45 m/s**

## Scale
- The prior gives the Apple Magic Mouse width as 5.71 cm. I measured the mouse's white mask in frame 14 (`measure.py`). It spans x 972-1040, which is **69 px** wide, and it is 133 px long (rows 414-547).
- The length-to-width ratio is 1.96. The real mouse is 11.35 x 5.71 cm (ratio 1.99), so the two agree.
- Scale = 0.0571 / 69 = 8.28e-4 m/px. The view is top-down and the camera is static (checked in scene/notes.md).

## Time base
- The file's rate is 18.48 fps and the question's rate is 26 fps.
- At 26 fps, 0.54 s is frame 14.04, the last frame of the clip, so the question covers the whole hand movement from the mouse to the keyboard. At 18.48 fps it would cut the motion off at frame 10, partway through.
- I used **26 fps**, so the interval is frames 0 to 14 and lasts 14/26 = 0.538 s. The resulting speed of about 0.45 m/s is a plausible speed for a hand moving across a desk.

## Hand motion
- **Route 1 (skin-mask centroid, scene track):** (988.4, 535.3) to (713.4, 438.2). Net displacement is 291.6 px and path length is 295.5 px. That gives 0.448 m/s (net) or 0.454 m/s (path).
- **Route 2 (my own frame-to-frame template match of a back-of-hand patch):** net 291.3 px, path 300.4 px. That gives 0.448 or 0.462 m/s.
- The two routes agree to within about 1-3%. Answer: 0.45 m/s.
- At 18.48 fps (frames 0-10) the answer would instead be about 0.35 m/s.

## Confidence
Moderate to high. The main risk is the time base: 26 fps versus 18.48 fps.

# q773: acceleration of the basketball at t=0.5 s (frame 12 at question_fps 24, same as the file's 24 fps)
2D video. The prior gives the basketball diameter as 0.282 m, which sets one m/px scale.

Ball pixel diameter:
- Half-contrast edge crossings along rows through the centre (diam.py), horizontal so there is no motion blur: 107.2 px (frames 0-1), 105.9 (frame 12), 106.4 (frames 48-49).
- SAM 3 masks (frames 4 and 12): horiz 107 px, vert 109 px. The vertical size is inflated by motion blur. The area-equivalent diameter is 108.9.
- Record: bbox 108 px, circle fit 106.1 px.
- Own HSV mask bbox: 108 x 108.
I used 107.0 px, so the scale is 0.282/107 = 0.0026355 m/px. All values are within 3 pct of 107: 105.9 is 1.0 pct off and 109 is 1.9 pct off.

Motion: purely vertical free fall from rest at frame 0, bouncing at frames 23-24, so frame 12 is mid-fall with uniform acceleration.
I fitted a parabola to y over frames 0-23 (never across the bounce):
- own tracker, minimum-enclosing-circle centre (measure.py): 1.346 px/frame^2 (1.347 from frames 3-23, 1.354 from frames 6-23), rms 0.27 px
- SAM 3 track centres (second route): 1.343 px/frame^2
- record circle-fit centres: 1.337 px/frame^2
Raw backward differences at frame 12 are noisy (560-1170 px/s^2) because of +/-0.3 px centre jitter. Since the acceleration is uniform, I used the constant from the fit.
a = 1.345 x 576 = 775 px/s^2, and 775 x 0.0026355 = 2.04 m/s^2. The scene is not at real scale, so this is not 9.8.
Confidence: high, about +/-2 pct (it depends on the diameter convention: 106-108 px gives 2.02-2.06).

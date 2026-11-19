# q_2167 — basketball diameter (cm)

Lab video at 24 fps (the file and the question use the same rate), 1280x720. f = 0.5959 x 1280 = 763 px.
D = depth x pixel diameter / f (lab method card). The acceleration prior plays no part in a size.

## Main route: frame 36 (t = 1.5 s, apex, depth 1.5225 m)
The ball is sharp here, with no blur and no occlusion. Pixel diameter:
- scene RANSAC circle: 114.3 px
- my mask (measure.py): bbox 112 x 112, minimum enclosing circle 115.4, equal-area diameter 111.6
- overlay frames/m36.png: the circle sits on the edge

Adopted 113.5 px, so D = 1.5225 x 113.5 / 763 = 0.2265 m.
Using the exact sphere formula 2d·sin(atan(r/f)) changes this by less than 0.3%.

## Check: frame 24 (t = 1.0 s, depth 1.401 m)
- RANSAC 124.1 px, bbox 120 x 128 (slight motion blur): D = 1.401 x 123 / 763 = 0.226 m
- Frame 29 (t = 1.2 s, depth 1.564 m) is heavily blurred: 107.5 px gives 0.220 m (less reliable)

## Answer
22.6 cm. Confidence: good (±2%). It is plausible for a size-6/7 basketball.

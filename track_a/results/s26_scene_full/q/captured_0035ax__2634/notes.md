# Q2634 – soccer ball diameter (cm)

The file and the question are both 24 fps. t=0.6 s is frame 14 and t=1.6 s is frame 38. The camera is the lab Femto Mega: f = 0.5959*1280 = 762.8 px, principal point (640, 360).
depth_info: soccer 2.758 m at f14, basketball 2.270 m at f14, soccer 3.052 m at f38. A fourth line, "soccer 2.412 m at f38",
is the basketball's distance: it fits the basketball's apparent size, since 74 px * 2.412 = 79.8 px * 2.27.

## Method (measure.py)
I traced rays every 5° from the centres in the record and found the sub-pixel 50% crossing of a non-green score, then fitted a circle and an ellipse to those points.
Size = depth * pixel diameter / f.

## Results
- Basketball check against the prior (23.2 cm): f14 gives 23.75 cm (79.8 px) and f38 gives 23.44 cm (74.1 px). So my edge reads about 1–2% large, a scale factor of about 0.983.
- Soccer ball at f38 (sharp, slow ~4 px/frame): 45.9 px -> 18.38 cm. Frames 36–40, using the same 3.052 m, give 18.1–18.2 cm.
  After the basketball-derived 0.98–0.99 correction this is about 18.0–18.2 cm.
- Soccer ball at f14 (heavy motion blur, ~19 px/frame): 57 px -> 20.7 cm. The ellipse minor axis gives 19.3 cm. Blur inflates the size here, so I rejected this frame.
  As a check, the f38 size scaled by the depth ratio predicts 50.8 px at f14.
- The scene record's tighter RANSAC circle (43.6 px at f38) would give 17.4 cm. The record's basketball circle likewise reads small (69 px -> 21.8 cm against the 23.2 prior),
  so my edge calibrated on the basketball is preferred.

Answer: 18.0 cm. A size 3 ball is about 18–19 cm, which is consistent. Confidence: good (±3%).

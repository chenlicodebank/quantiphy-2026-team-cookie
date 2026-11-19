# q97: width of black/white car (2D top-down, 24 fps)
Scale from prior: yellow car length 5.67 m = 270 px (bbox x-extent near image centre, frames 24-42, measure.py; matches scene record 270).
m/px = 0.02100.
Black car y-extent per column (measure.py, frames 24/30/36/42): body over wheel arches = 100 px (wheel to wheel, stable),
cabin 90 px, incl. side mirrors 116 px. Yellow car identical profile (100 / 116), consistent.
Width (wheel to wheel, the convention for car width) = 100 x 0.0210 = 2.10 m.
Alternative reading incl. mirrors (full AABB): 116 px -> 2.44 m.
Check: black car length 269-270 px ~ yellow, so same-model scale; ratio width/length 0.37 plausible.
Confidence: moderate-high for 2.10 under wheel-to-wheel convention.

# q_1841 — length of the black car (m)

Prior: speed of black car = 26.085 m/s. 2D top-down render, static camera, 24 fps (file fps = question_fps, no re-timing).
Black car = `car_dark` in scene/ (dark navy, mean brightness ~50–70), leading car.

## Scale from the prior (speed)
The car moves at constant pixel speed (per-frame step 27.1 ± ~0.7 px, no trend), so the prior speed applies throughout.
- scene ref points (template fit), frames 2–48: chord speed k=1..4 → 27.10–27.17 px/frame
- my own mask centroids (measure.py), clean frames 4–45: 27.05–27.12 px/frame
- adopted 27.12 px/frame = 650.9 px/s → scale = 26.085 / 650.9 = 0.04008 m/px

## Length in pixels (measure.py, clean frames 4–45, tree-occluded 31–35 also consistent)
- min-area rectangle of mask (threshold min RGB < 235): median 115.6 px (record: 115.8)
- 50 % anti-alias coverage extent along the principal axis: median 115.0 px
- adopted 115.3 px

## Answer
115.3 px × 0.04008 m/px = 4.62 m (width ~49 px → ~1.96 m incl. mirrors, plausible car).
Second route: per-frame-step scale (1.0869 m/frame / 27.12 px) and the two independent length
measurements give 4.60–4.64 m. Confidence: high (±2 %).

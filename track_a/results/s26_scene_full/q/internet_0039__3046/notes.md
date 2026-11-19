# q3046 – swimmer speed 0–1 s (m/s)

Prior: swimmer height 1.68 m. Top-down 2D view, static camera (the lane ropes stay fixed). One planar scale.

## Scale
Body length from cap top to feet, measured on the mask (scene track `head_to_feet`, checked by eye at frame 19: cap top ≈ y1665, feet ≈ y2660, so ≈ 1000 px).
Frame 0: 1007 px. Mean over frames 0–27: 1014 px. Clip median: 1041 px. I used ≈ 1030 px, so the scale is 1.68/1030 = 1.63 mm/px.

## Time base
The file runs at 18.54 fps but has exact duplicate frames (1, 11, 20, 30, 40, 50, 60, 70). That leaves 64 unique frames, about 16.5 unique fps.
This means the file was frame-rate converted. I take the original footage to be question_fps = 25 fps, one unique frame per 1/25 s.
Plausibility check:
- At 25 fps the stroke cycle is ≈ 2.0 s and the speed ≈ 0.85–0.9 m/s, which is normal recreational freestyle.
- At the file rate the cycle is 3.0 s and the speed 0.59 m/s, which looks like slow motion.

## Measurement (measure.py)
I dropped the duplicate frames and took 0–1 s as unique frames 0 to 25 at 25 fps.
- Head (cap) moves 540 px, giving 0.88 m/s.
- Hip (trunks) moves 512 px, giving 0.835 m/s.
- Second route, a linear fit over the whole clip (unique frames): 0.845 m/s.

Alternatives, not used:
- File frames at file fps: 0.59 m/s.
- File frames 0–25 read at 25 fps: 0.77 m/s.

Answer: 0.87 m/s (head reference, slightly weighted toward hip and fit). Confidence is moderate; the main uncertainty is the time base.

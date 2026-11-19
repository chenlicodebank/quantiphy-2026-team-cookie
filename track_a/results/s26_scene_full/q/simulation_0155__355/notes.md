# Q355 – shark length (m), prior: shark speed = 7 m/s

2D scene (shark swims right→left parallel to image plane, constant apparent size, static camera), 24 fps (file = question fps).
One m/px scale from the prior speed.

## Pixel speed
- scene record: dorsal apex 58.6 px/frame (frames 7-38, also 58.6 over 14-26); tail tip 58.4 (15→46), 60 (15→26); snout 58.9 (6→30).
- own check (measure.py): template matching of frame-20 body/front/rear crops into frames 14, 26, 32: 59.0–61.0 px/frame (high-correlation matches ~59.6–60.7).
- adopted: 59.0 px/frame = 1416 px/s → scale = 7/1416 = 0.004944 m/px.

## Pixel length
- snout tip to tail tip at frame 20: 652→1577 = 926 px (verified on grid frame); 926–929 at frames 15-23, 914–919 at 24-30 (tail flex). Adopted ~921 px.

## Answer
921 × 0.004944 ≈ 4.55 m; range of routes 4.45 (915 px, 60.7 px/f) to 4.61 (926 px, 58.6 px/f). Answer 4.57 m.
Confidence: good (±3 %); main uncertainty is which body point represents the rig-origin speed.

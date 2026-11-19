# Q825 – length of the rabbit (m)

Prior: antelope (the horned creature) speed = 1.277 m/s. 2D scene: static camera, both animals walk sideways at about the same depth (feet/hooves both at y ≈ 1547), so one m/px scale is used. fps = question_fps = 30.

## Scale (measure.py)
Creature translation, px/s: shoulder 198.1 (mean of per-frame speeds; the linear fit gives 198.3), hip 201.9–202.7, body_mid 186.6–195. The rig origin speed is taken as ≈ 199 px/s, because all rigid points share the same mean translation and the shoulder track is the smoothest.
Scale = 1.277 / 199 = 0.00642 m/px.

## Rabbit length
Horizontal bbox extent, frames 0–69 (scene track): median 73 px, mean 73.7, p10–p90 69–79.
Independent check: frame differencing against a frame 30 frames away, at clean frames (5, 25, 45, 65), gives 72–74 px at thr 20–30. Frames 15, 35 and 55 were contaminated by creature legs in the reference frame and were not used.
Length = 73 × 0.00642 = 0.468 m (range 0.44–0.51 over the hop-pose spread).

## Second-route check
Using the hip speed (202 px/s) instead gives 0.461 m, and using the shoulder (198 px/s) gives 0.471 m. Both are within 2% of the answer.

Confidence: moderate-high. The main uncertainty is the pose-dependent bbox (±7%).

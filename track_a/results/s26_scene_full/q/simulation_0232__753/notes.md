# Q753 – paper airplane speed at t = 1.25 s (frame 30, 24 fps; question_fps = file fps)

Object: the "arrow" in scene/ is the paper airplane, seen edge-on as a thin grey streak about 132 px long
(checked on a zoomed crop of frame 30). The scene is a 2D render with the motion parallel to the wall, so I used
one metres-per-pixel scale. Relative sizes agree with the plane and cat being at about the same depth:
plane/cat-body ratio 132/186 = 0.71.

Scale (prior: cat speed = 0.714 m/s): the cat's torso centroid (scene/tracks/cat.csv) moves at a constant speed with
gait jitter. Linear fit of x over frames 0–49 = 8.96 px/frame (8.95 from the full-mask centroid, 8.99 over whole
gait cycles from frame 6 to 42, 9.11 net from the endpoints). Using 8.97 px/frame = 215.3 px/s gives
s = 0.003317 m/px.

Plane: re-tracked in `track_plane.py` (median-background difference, PCA axis, tail and tip ends; the tail
end is the reliable one). The centre is tail + 66 px along the axis. Per-frame steps fluctuate by ±3 px from
measurement noise; the tail-based and mid-based tracks fluctuate in different ways. So I took the backward
difference at frame 30 from smooth polynomial fits (`speed.py`):
- centre, cubic fit over frames 24–36: 61.4 px/frame; quadratic 24–36: 60.3; quadratic 26–34: 61.0; cubic 22–37: 61.1
- tail end (second route): 60.1–61.1 px/frame
- raw 29→30 difference: 63.8–64.1 px/frame (noisy)

Adopted step: 60.9 px/frame, giving 60.9 × 24 × 0.003317 = 4.85 m/s. The fits span 4.79–4.89 m/s and the raw
difference gives 5.1 m/s.

Confidence: moderate-high (about ±5 %). The main uncertainties are the cat-speed convention (net vs. fit: ±1.5 %)
and the assumption that the plane and cat are at the same depth.

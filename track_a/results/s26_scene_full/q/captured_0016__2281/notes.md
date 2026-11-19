# q2281 – distance between the two people (cm)

Lab video, 1280x720, 24 fps (file fps = question fps). Lab protocol: f = 0.5959*1280 = 763 px, principal point (640, 360).
depth_info at t = 1.5 s (frame 36): near person (thrower, left edge) 0.843 m; far person (receiver, right by the wall) 2.372 m.

Method: back-project each person's visible-body centre on frame 36 with its depth (the depth is the Euclidean distance along the ray),
then take the 3D distance (`dist.py`).
- Near person: visible body (head x 0–80, torso/arm x 0–230, y 260–720) has its centre at about (90, 400).
- Far person: visible body (x ≈ 930–1230, y 0–435; head cut off) has its torso/hip centre at about (1070, 230).
- Result: 216.9 cm.

Check: varied both click points over plausible centres (near ±30–50 px, far ±50 px).
The distances range from 211 to 222 cm, because the separation is dominated by the depths and the large lateral angle.
Prior (g = 9.8) is not needed. Confidence: moderate-high, about ±3%.

Answer: 217 cm.

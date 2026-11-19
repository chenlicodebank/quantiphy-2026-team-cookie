# Q75 – distance black shirt ↔ white shirt at 2.0 s (frame 48)

Overhead 2D render, 24 fps (file fps = question_fps, no re-timing). Scale from prior: white-shirt (B) speed = 1.3 m/s.

Method (analyze.py): from scene/tracks, B's pelvis_est x fitted linearly over frames 17–71 → 14.50 px/frame
(347.9 px/s) → 0.003736 m/px. Steady walk, so the prior speed equals the mean speed.
At frame 48: A pelvis (559.0, 544.8), B pelvis (1371.4, 562.4) → 812.6 px → 3.036 m; with linear-fit positions
(removes gait bob) 809 px → 3.023 m. Same result using head-top points (perspective factor cancels as distance and
speed use the same point at the same height): 3.036 / 3.023 m.

Second route (check.py, own segmentation, whole-silhouette centroids): vB 14.22 px/frame, fitted gap at frame 48
804 px → 3.06 m; raw centroid gap 820 px → ~3.06 m with record speed.

Answer: 3.03 m. Confidence: good (±2–3 %).

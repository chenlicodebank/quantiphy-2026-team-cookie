# q1509 — total distance walked by the man (simulation_0141)

File fps = question_fps = 24; 60 frames (0..59) -> 59 per-frame displacements.

## Main route (prior)
Prior: walking speed = 1.693 m/s. The man walks steadily for the whole clip: foot-contact plateaus (sole_y,
scene/tracks/man.csv; sole.py) every 12 frames, and the ground-plane inverse depth 1/(sole_y-536) increases
by equal steps (0.000356, 0.000359, 0.000360, 0.000338, 0.000361) -> constant speed, no start/stop.
Total distance = mean per-frame speed x 59 frames / 24 = 1.693 x 59/24 = **4.162 m**.

## Second route (perspective + depth_info)
Pelvis depth relative scale from the sole plateaus (pelvis ~ over stance foot at mid-stance): Z(59)/Z(0) ≈ 1.958.
With d(0)=4.15 m (Z0 ≈ 4.0–4.15 depending on focal length), horizontal net advance ≈ 0.958 x Z0 ≈ 3.9–4.0 m;
lateral position nearly constant. Per-frame path adds pelvis bob/sway (a few %) -> ~4.0–4.15 m, agreeing
with 4.16 within ~2–4 %. (measure.py with height_px gives 3.5–3.7 m but height_px shrinks with gait and
underestimates the depth ratio; not used.)
Note: the given depths (4.15 -> 5.03 in 12 frames, ratio 1.212) are slightly inconsistent with the image
scale ratio (~1.19), so they were used only as a sanity check; the exact prior sets the answer.

Confidence: moderate-high (main uncertainty: whether the prior is the clip-average speed; constant gait supports it).

# q_2190 – basketball distance from camera at t = 1.8 s

The question's depth_info states the measured value directly: "t=1.8s, distance_ball_camera = 1.5835m".
t = 1.8 s means frame 43 at question_fps 24, which is also the file's rate. The answer is that value: **1.5835 m**.

Check with the apparent size (scene/tracks/basketball.csv, circle-fit diameter, f = 0.5959 x 1280 = 762.8 px):
- Frame 0: d = 136.1 px at a given distance of 1.321 m. After the off-axis correction this gives a ball diameter of about 0.225 m (a basketball is about 0.24 m, so this is plausible).
- Frame 43: d = 106.9 px, which gives about 1.65 m. Frame 46 (near the 1.92 s rebound apex): about 1.60 m, against 1.5795 m given.
- The size route agrees within about 4%. It is less precise than the measured depth because of mask and blur noise in the diameter, so the given depth is the answer.

Confidence: high. The value comes straight from depth_info.

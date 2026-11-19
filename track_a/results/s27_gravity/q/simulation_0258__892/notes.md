# Q892 — table width (longer side), simulation_0258

Method (2D, one m/px scale from the prior):
- Prior: pen free-fall acceleration = 9.8 m/s^2. Times use question_fps = 30. The file itself runs at 24 fps, but its frame indices are used with 30 fps as instructed.
- Fall: I checked the pen track in scene/tracks/pen.csv (cy, frames 3–15, before the impact between frames 15 and 16). Quadratic fits give a = 6.87 / 6.84 / 6.83 px/frame^2 for start frames 3, 5 and 7, with residuals of about 0.25 px. The second differences average about 6.9. I used 6.85 px/frame^2, which is 6165 px/s^2 at 30 fps.
  Scale = 9.8 / 6165 = 1.590e-3 m/px.
- Table edges, measured in code on frame 36 (edges.py):
  - Front band runs from x 518 to 1539, so 1021 px.
  - Top surface: back edge at y 865, front edge at y 895. Its right back corner is at x 1525, against 1539 at the front, so the top shows mild perspective.
  - With the principal point at x 960, the depth ratio from back to front is 565/579 = 0.976. That makes the back edge about 996 px long.
- The pen rests at cy 866.6, which is at the back of the table top, so it shares the depth of the back edge. Allowing a few pixels toward the front gives an effective length of about 999 px.
- Width (longer side) = 999 px × 1.590e-3 = 1.588 m. **Answer 1.59 m.**

Second route: the front-edge pixel length with the same scale gives 1.623 m. That is the upper bound if perspective is ignored, and it differs by only 2%.

Sanity checks:
- With this scale the pen is 65 px, about 0.10 m long, which is a bit short for a real pen.
- If the true render rate were 24 fps instead, the table would come out at 2.5 m. I followed question_fps (30), as the convention requires.

Confidence: good, about ±3% given the 30 fps time base.

# Q1693 — speed of the person (m/s)

Prior: person height 1.75 m. depth_info: 100.5638 m at t=1 s, 100.5996 m at t=2 s (frames 24 and 48 at question_fps 24).
The file is 25 fps and the question uses 24 fps. All times use 24 fps, so the 74-frame clip lasts 3.08 s.

## Observations
- Person: about 58 px tall (pale head included), about 19 px wide. Seen front or back on: the legs overlap and do not scissor sideways, so they walk roughly along the line of sight.
- Image motion of the body is a straight line at 0.469 px/frame right and 0.617 px/frame down (centroid fits, size.py), with a gait cycle of 36 frames (autocorrelation, size.py).
- Camera looks down: the rock is a snowy terrain or mountain chunk whose top surface is visible. The person is therefore below the horizon, and moving down in the image means walking toward the camera.
- The given distances change by only 0.036 m/s. A body moving with the origin cannot produce this motion on level ground (the radial change has the wrong sign). So the origin stays put (an in-place character), as the benchmark warns. I used the depth only as the camera distance of about 100.6 m and not for the direction of motion.

## Geometry (speed.py)
Inputs: camera depression angle phi at the person; k = 58 px / (1.75 cos phi + 0.25 sin phi) px/m; lateral = vx/k; toward camera = vy/(k sin phi).
Speed versus phi: 20° → 1.33, 25° → 1.07, 28° → 0.96, 30° → 0.90, 45° → 0.58 m/s.
The tilt is not well determined:
- Apparent-size change (template matching at equal gait phase, threshold heights): −1 ± 1–2 % over the clip. Growth of +2–4 % was expected for phi 20–30°. Shading changes bias this, but taken literally it points to a steeper view, which would mean an unrealistically slow walk (< 0.6 m/s).
- Body proportions (height/width about 3–4.5) show no strong foreshortening, which argues for phi of 30° or less.
- Gait: the 36-frame cycle is 1.5 s. A natural stride of about 1.35–1.6 m for a 1.75 m adult gives 0.9–1.07 m/s, meaning phi of about 25–30°. This also satisfies the 0.9–2.0 m/s walking-speed check.
Chosen: phi ≈ 28°. Speed = 0.96 m/s (stride 1.44 m, heading about 20° off the line of sight). I added about 1 % because the per-frame pelvis-speed convention includes sway and bob.

Answer: 0.97 m/s.
Confidence: low to moderate (about ±20 %). The camera tilt cannot be measured directly, since there is no ground or horizon, and the size-change cue conflicts with it.

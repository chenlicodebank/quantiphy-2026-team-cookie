# Q366 — turtle speed at t = 1.5 s (frame 36), prior: turtle acceleration = 2.639 m/s^2

2D scene, static camera, 24 fps (file rate = question_fps, so frame 36 is used). The turtle swims left at constant y (550 px).

## Method
- Scale: metres per pixel = 2.639 / (pixel acceleration). This gives speed = 2.639 x (pixel step at frame 36 / pixel accel) / 24,
  so the result depends only on the ratio of pixel speed to pixel acceleration.
- `track_steps.py`: my own frame-to-frame template matching (high-pass grey image, carapace band y 515-585, sub-pixel peak)
  gives the per-frame pixel step for every frame 1-47 (match scores 0.83-0.98).
- `fit_steps.py`: the steps grow linearly, so pixel acceleration is constant: a_px = 0.939-0.949 px/frame^2 (fits from frames 1, 5, 15 or 22 to 47,
  residual about 0.45 px). The fitted velocity is zero at frame ~0.6-0.95, so the turtle starts from rest at the start of the clip.
  Fitted step at frame 36 = 33.28 px/frame, raw = 33.69.
- Speed = 2.639 x 33.28 / 0.945 / 24 = 3.86-3.90 m/s, depending on the window.

## Checks
- Ideal uniform acceleration from rest at frame 0, using a backward difference: v = a x 35.5/24 = 3.90 m/s. This agrees.
- Quadratic fits to the record's ref_x track (scene/tracks/turtle.csv, `fit.py`) over the full range give 3.90-3.96. Short late
  windows scatter more (4.1-4.6) because of chaining between the record's templates. The direct step tracking is cleaner.
- (a x t = 3.96 m/s if the reference used a continuous v = a t, which is 2 % away.)

Answer: 3.88 m/s. Confidence: high (within about 3 %).

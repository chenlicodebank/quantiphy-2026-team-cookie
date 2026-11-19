# q1162 — speed of the person at t = 1.0 s (frame 24, question_fps 24 = file fps)

The question reads "average of the person at 1.0s". I read it as the person's (pelvis) speed around t = 1 s.

## Scale
- Prior: eagle length 0.8 m (body length, beak to tail). Measured in code (birdlen.py): mask extent along the flight
  heading is 27.7 px median over frames 4-45 (very stable). Add about 0.5 px for anti-aliased edges and correct for
  the slight foreshortening of the heading in the oblique view: about 28.6 px. f = 28.6 x 179.27 / 0.8 ≈ 6400 px
  (horizontal FOV ≈ 9.6°).
- Check: the man's shirt (shoulder) width is 16 px, which gives 0.47-0.50 m. That is plausible.

## Geometry (the camera is oblique, not top-down)
- We see the man's front, legs and feet, so the camera looks down obliquely. He walks down the image, which means
  toward the camera. His depth_info rises by only 0.09 m/s, which does not fit that motion. So, as the brief warns,
  his origin stays put and is not his body. I did not use 182.9 m for the body.
- Body distance: the bird's shadow offset compared with the man's shadow (shadowtip.py, solve.py) puts the eagle
  about 4.3·H (≈7.5 m) above the ground at t≈1 s. The eagle is at 179.27 m and sits over the man's feet in the
  image, so the man's feet are at about 179.3 + 7.5/sin α ≈ 188-189 m.
- Pitch α from the man's apparent height. At frame 17 (legs together) the head top to the toe spans 40.7 px. Minus
  the foot and head depth, that is about 35 px of pure vertical extent. With H = 1.75-1.8 m and f/D = 34 px/m,
  α ≈ 54-56°. The following agree with this:
  - eagle wingspan to body length ratio: about 2.2 in the image, which implies a steeper view than 45°;
  - eagle depth change of −2.17 m/s against its image-y motion: nearly level flight at α≈54°;
  - gait: steps every ~17 frames, 25.5 px apart, which gives a step of ~0.9 m at α=55° (1.1 m at 43°, which is too
    long).
- A first fit (solve.py) that uses the man's shadow tip relative to his lowest foot gave α≈38-44°. That fit was
  biased: the front-foot toe is not the ground point under the head. I rejected it.

## Speed
speed.py back-projects the torso-based pelvis track (scene/tracks/walker.csv, checked visually) onto the horizontal
plane at pelvis height:
- α=55°: 1.31 (frames 12-36), 1.35 (20-28), 1.49 (18-30); least-squares fit over 12-36: 1.35 m/s.
- α=52°: 1.37-1.56 m/s. α=58°: 1.26-1.44 m/s.
- Pixel rate is 1.545 px/frame in image y (0.135 in x). Single-frame speeds are too noisy (gait plus ±1 px), so I
  used a local window.

**Answer: 1.38 m/s.** This is a plausible walking speed. Main uncertainty is α (±3° gives ±5%) and the man's
assumed height. Confidence: moderate (about ±10%).

# q_1112 — height of the person (simulation_0025)

Answer: **1.75 m**. Confidence is moderate, about ±10 %. The metric scale is weakly constrained, and the final value leans
on the plausibility rule for an adult person.

## Data
- The file is 25 fps and 75 frames; question_fps is 24. I used frame indices throughout. The clip spans frames 0-74, which
  is 3.083 s at 24 fps.
- Person: the scene record's tracks/person.csv covers the right object; I checked it on frames. Apparent head-to-sole
  height is 54.6 px on average (53-57 px). The head top is pale, so this may be up to about 1 px short.
- depth_info: the distance to the human is 114.832 m at t=1 s and 114.836 m at t=2 s, effectively constant. The eagle is
  116.05 m at t=1 s and 108.28 m at t=2 s.

## Geometry
- The given human distance stays put, yet the body moves 38 px left and 10 px down. So it is the character's origin and
  says nothing about the body's motion.
- Zoomed frames (frames/gait.png) show the person walking almost **facing the camera**: a frontal view and a nearly
  constant silhouette width. The walk is therefore mainly toward the camera.
- If the walk were purely lateral at 1.3 m/s, f would be about 1100 px. That gives a 5.7 m person and an eagle with a
  wingspan over 20 m, both impossible, so I rejected it.
- With a toward-camera walk (4.0 m path), the 38 px lateral shift and the scale growth fix f. But that route is
  ill-conditioned: f runs from 3100 to 4500 for scale growth between 3.3 % and 3.5 %.
- Measured growth from scale-registration of the full-body patch (scale_track.py) is about 3-4 %. That is consistent
  with a mostly toward-camera walk. The upper-body registration gave only about 1 %, but there is little texture there.
- Ground check: the feet move down 9.5 px while the scale grows about 3.4 %. That puts the horizon near y ≈ 290, hidden
  behind the cliff top, and the camera about 9 m up. This is plausible.

## Second reference: the eagle (bird_f.py)
- I back-projected the bird with its two given distances. Its heading comes out at about 135° from the view axis (flying
  toward the camera and to the right).
- I corrected its spread-wing span for foreshortening: the wing axis is horizontal and perpendicular to the heading.
- The implied wingspan is 2.2-2.4 m at f = 3600 px. That would be about 2.0-2.2 m at f = 3700-4000 px. Real eagles
  are 1.8-2.3 m.
- On this basis, f is about 3300-4000 px, which gives a person height of 1.57-1.90 m. Height = 54.6 × 114.83 / f.

## Gait (gait.py)
- The stride period is about 35.5 frames, which is 1.48 s at 24 fps. Combined with 1.3 m/s, that implies a stride of
  1.9 m, which is long.
- This depends on the animation's timing, so I treated it as weak evidence and did not use it.

## Result
- f ≈ 3580 px, chosen within the range consistent with the eagle and with the walking geometry.
- Height = 54.6 px × 114.83 m / 3580 ≈ 1.75 m.
- The rest standing height may be 1-2 % taller than this walking head-to-sole extent.

# q_2354 – velocity of the yellow toy at t = 0.60 s (cm/s)

The yellow toy is the scene record's `yellow_fruit`. The far (right) person throws it to the near (left) person and it is in free flight in frames 12–24. The depth_info's "carrot" (2.63 m at t = 0.60 s) is taken to be this object. The jar (1.9735 m) is the white ball.
t = 0.60 s → frame round(0.6·24) = 14. The file and question_fps are both 24.
Camera: f = 0.5959·1280 = 763 px, principal point (640, 360). The camera is static.

## Method
- Image centres come from scene/tracks/yellow_fruit.csv (colour-mask centroid). I checked them on 2x crops for frames 11–26 (`check_track.py`, `frames/track_check.png`). Frame 18 is occluded and was dropped. Frame 12 has the hand next to the fruit and was also dropped.
- Gravity direction in camera coordinates comes from the vertical vanishing point of the room (`bg.py`, `vp2.py`, `vp3.py`):
  - Left-wall seams: x = 0.558y + 82, 0.439y + 255 and 0.350y + 390.
  - Right-wall seams: slopes −0.150 and −0.155.
  - Line pairs intersect at VP ≈ (905, 1480) px, with a spread of about 20 px. The corner line and the radiator edges agree.
  - Down direction = (0.192, 0.811, 0.552), i.e. the camera is pitched down about 33°.
- I fitted a 3D ballistic model, P(t) = P14 + V·t + ½·g·t². P14 sits on the frame-14 ray at |P14| = 2.63 m (depth_info). The model is projected with f = 763 and fitted by least squares (`fit.py`, `fit2.py`, `fit3.py`).
- Reference convention: forward difference smoothed over at least 5 frames, which is effectively the velocity at frame 14.5. I report the speed |V| there.

## Results (fruit speed, cm/s)
| model | rms px | \|V\| f14 | \|V\| f14.5 |
|---|---|---|---|
| room VP, g = 9.8 (the prior) | 4.9 | 331 | 318 |
| room VP, g free (best g ≈ 8.0) | 1.7 | 337 | ≈328 |
| joint fit with the white ball, g direction and magnitude free (VP 755,1421; g 8.25) | 1.4 | 317 | 307 |
| joint fit, g = 9.8, direction free (VP 663,867 – implausible pitch, rejected) | 1.7 | 388 | 373 |

The speed is dominated by the motion toward the camera: Vz ≈ −2.8 to −3.1 m/s, with a lateral component of about 1.3–1.6 m/s. The distance drops from about 2.75 m (frame 13) to about 1.7–1.9 m (frame 24). This fits a throw from the far person (3.24 m) to the near person (1.58 m): the release point is about 0.56 m from the far person's pelvis and the catch point about 0.5–0.6 m from the near person's pelvis.

## Second-route check
The white ball, fitted on its own with its own depth (1.9735 m), prefers the same effective g (≈8) under the room VP. That supports the geometry, and its speed (≈ 290–330 cm/s) is reasonable. The apparent size of the fruit cannot be used to check depth: it is elongated, tumbles and is motion-blurred.

## Answer
About 320 cm/s, the centre of the plausible models (307–328 at frame 14.5). Confidence: moderate, about ±8%. The main uncertainty is the depth component, which depends on the gravity direction and magnitude in the fit. Gravity comes out about 20% low (≈8 m/s²) when the room VP is fixed, which may come from lens distortion.

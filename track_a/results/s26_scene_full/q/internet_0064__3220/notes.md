# q_3220 – ball diameter (cm), prior g = 9.8 m/s^2

Time base: file fps = question_fps = 30. The camera is nearly static (drift < 1 px/frame; I checked fits with both the raw and the background-corrected cy).

Scale from the prior: I fitted a quadratic to the ball centre's cy(t) in free flight (scene/tracks/ball.csv, script fitg.py):
- Flight 1, frames 82–112: g = 3537 px/s^2 (raw), 3543 (bg-corrected). Sub-windows give 3600 (84–104) and 3464–3475 (90–112). The rms is larger because the blurred rim drops out of the mask in fast frames.
- Flight 2, frames 117–142: g = 3536 / 3562 px/s^2 (rms 0.3 px). Frames 120–140 give 3548 / 3572.
- Adopted g ≈ 3550 px/s^2, which gives 0.276 mm/px (980 cm / 3550 px).

Ball pixel diameter: the sharp-edge circle fit is 84.6–85.9 px near the flight-1 apex (frames 81–95) and 86–87.5 px in flight 2. I checked it by eye on a zoomed frame 93 (x ≈ 722–806, y ≈ 140–226, so about 85 px). I used about 85.5 px. Held frames read about 92 px, but the hands are included and the ball is nearer the camera, so I did not use them.

Diameter = 85.5 × 980 / 3550 ≈ 23.6 cm.
Second route, per flight: flight 1 is 85.2 px × 980 / 3540 = 23.6 cm; flight 2 is 87 px × 980 / 3555 = 24.0 cm. The routes agree within about 2%. This also matches a real basketball (about 24 cm).
Answer: 23.7 cm. Confidence: good (±4%).

# q3219 – displacement of the person, 4.00 s → 5.00 s

Time base: file fps = question_fps = 30 → frames 120 and 150. At 30 fps the ball's parabola gives a
pixel g that makes the person 1.72 m tall and the ball 0.235 m across, so 30 fps is physically consistent.

## Scale (prior: g = 9.8 m/s²) — grav.py
Quadratic fits to the ball's vertical centre (scene/tracks/ball.csv):
- flight 1 (frames 81–113 / 84–111): 3539 / 3530 px/s² (image), 3546 / 3535 (bg-corrected)
- flight 2 (116–143 / 118–142): 3531 / 3537 (image), 3558 / 3563 (bg-corrected); rms 0.3–2 px
- Adopted g_px ≈ 3540 px/s² → scale = 9.8/3540 = 0.002768 m/px.
- Checks: person height 620 px → 1.72 m; ball diameter 85 px → 0.235 m (a real basketball is about 0.24 m). Both plausible.

## Person displacement (person.py, frames checked visually in frames/f120.png and f150.png)
The person walks right and stays level, so the displacement is horizontal. The camera drifts slowly by about 10 px left
between frames 120 and 150.
- waist band x: 296 px (image), 306 px (background-corrected)
- mask centroid: 296 px (image)
- head x: 309 px (image), 320 px (bg)
- bbox centre (bg): 312 px
- visual torso centre: about 152 → 455, so about 303 px
- Adopted pelvis/torso displacement ≈ 305 px. The camera-drift correction is included only partly, to sit between the
  image-coordinate and background-corrected readings.
- 305 × 0.002768 = 0.844 m. The spread of the reference points (296–320 px) gives 0.82–0.89 m.

Answer: 0.845 m. Confidence: moderate-high. The uncertainty is about ±4%, mostly from the choice of reference point and camera drift.

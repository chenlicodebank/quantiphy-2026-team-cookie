# q_3268 – toilet paper velocity at 0.50 s (cm/s)

**Prior:** width of the toilet paper = 10 cm. I read this as the sheet width, which is the roll's length along its axis. The axis is horizontal, the same as the main motion direction (leftward). Pixel length along the axis: 585 px at rest (frames 56–59) and 588–614 px while moving (the tilt adds a sliver of end face). I used **≈590 px**, so scale = 10/590 = 0.01695 cm/px. Under the other reading (width = diameter, 698 px) the scale would be 0.01433 cm/px and the answer ≈15.2 cm/s. As a check on the first reading: diameter/axis = 698/585 gives a diameter of 11.9 cm, which is typical for a roll.

**Time base:** the file runs at 24.098 fps and question_fps is 30. The clip has exactly 60 frames, which is exactly 2.00 s at 30 fps. That points to original 30 fps footage that was re-timed, so I used 30 fps. Then t = 0.50 s is frame 15, and Δt = 1/30 s.

**Camera:** static (scene record: phase-correlation shift ≤ 0.03 px).

**Measurement (forward difference, frame 15→16):**
- Bounding-box centre from the scene track (checked visually on frames 12–17; the boxes hug the roll): dx = −35.3 px, dy = −3.2 px, |d| = 35.4 px/frame.
- Independent route: NCC template match of a roll texture patch between consecutive frames (`match.py`): dx = −35.5 px, dy = +1.1 px, |d| = 35.5 px/frame (corr 0.94).
- Neighbouring frames for comparison: 14→15 = 37.8 px/frame, 16→17 = 28.4 px/frame.

**Speed:** 35.4 px/frame × 30 fps × 0.01695 cm/px = **18.0 cm/s**. With the 585 px rest length it would be 18.2 cm/s; with the 612 px in-motion length, 17.4 cm/s.

**Alternative:** if the file's 24.1 fps were used instead, t = 0.5 s is frame 12, where 12→13 = 51.2 px/frame, giving ≈20.9 cm/s.

**Confidence:** moderate. The main uncertainties are the choice of frame rate and the pixel length the annotators used for the 10 cm.

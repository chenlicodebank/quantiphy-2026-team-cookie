# q_2340 — velocity of the box at 3.4 s (cm/s)

## Problem
The clip has 49 frames at 24 fps (file fps = question_fps = 24), so it lasts 0–2.04 s. **t = 3.4 s (frame 82) is not in this clip.**
The clip is probably trimmed from a longer recording, and the time offset is unknown. The answer is therefore a best guess, not a measurement at that frame.

## Measurements (speed.py; box track from scene/tracks/white_box.csv, checked against the scene record)
- The box is held in the far person's left hand, next to the soccer ball (2.80 m); the far person is at 3.13 m. Box depth used: 2.85 m. f = 763 px, principal point (640, 360).
- The box is released at clip frame 29 and hits the floor at frame 39. One capture frame is dropped between frames 35 and 36, and the script handles this.
- Forward-difference 3D speeds (m/s) for frames 29–38: 0.88, 1.37, 1.22, 1.89, 2.29, 2.64, 3.04 (35→36, over a doubled time step), 3.45, 3.72, then 3.06 at impact.
- Check with a parabola fit over frames 31–38: pixel acceleration is 2307 px/s², which gives 8.6 m/s² at 2.85 m. That is close to g (it would equal g at a depth of 3.24 m). So the clip plays at real time and is not time-scaled.
- After landing, the box slides left at about 8 px/frame (about 0.7 m/s), and it is almost at rest by the end of the clip.

## Answer
I assumed 3.4 s in the original timeline falls during the box's free fall, which is the motion a velocity question would target. Fall speeds then range from about 1 to 3.7 m/s. I chose the value that maximises the expected relative-error score over that range: about 2.2 m/s, which is the mid-fall speed (clip frames 32–33).
**Answer: 220 cm/s. Confidence: low**, because of the unknown time offset. If 3.4 s instead falls after the box comes to rest, the true value is about 0.

# q_2646: soccer ball velocity at t = 1.3 s (cm/s)

t = 1.3 s → frame 31 (question_fps 24, same as the file's rate). Lab camera: f = 0.5959·1280 = 763 px, principal point (640, 360).

## Depth labels
At t = 1.4 s, depth_info gives two "soccer ball" lines (2.602 and 2.373 m). One of them must be the basketball.
- If the soccer ball is at 2.373 m, its implied diameter is 16.8 cm at frame 34. That matches the 16.8 cm implied at t = 0.9 s (2.477 m).
- If it were at 2.602 m, the implied diameter would be 18.4 cm, which is inconsistent.
- At 2.602 m the basketball's implied diameter is 22.4 cm, close to the 23.2 cm prior.

So at 1.4 s the soccer ball is at 2.373 m and the basketball at 2.602 m. The soccer ball's diameter comes out as 16.8 cm.

## Method (measure.py)
- **Ball centres:** taken from scene/tracks (circle fits, about ±1.5 px). I checked frame 31 visually: the ball is rolling on the floor.
- **Floor plane:** fitted through 6 reference points. Four are the depth_info points (each ball at 0.9 s and 1.4 s, back-projected). Two are the balls' rest positions, with depth taken from their diameters. Each point is placed at its own ball's radius above the floor. The fit residuals are about 1 cm, and the camera comes out about 1.56 m above the floor.
- **Soccer ball depth per frame:** the camera ray through its centre, intersected with the plane at its radius height. This gives about 2.40 m at frame 31.
- **Velocity:** frame-to-frame 3D displacements × 24, smoothed over 5 to 9 frames. The window stays between the impact (frames 24-27) and the dropped frame between 35 and 36.

## Results (cm/s)
- Plane route:
  - chord 28→34: 57.7
  - linear fit over frames 28-34: 56.9
  - linear fit over frames 27-35: 59.6
  - mean forward speed over 28-34: 59.0
- Second route, depth from the apparent diameter per frame (noisier): chords 28→34 and 29→33 give 54.3 and 56.9.

**Answer: 57.5 cm/s.** Confidence is moderate to good, about ±8 %.

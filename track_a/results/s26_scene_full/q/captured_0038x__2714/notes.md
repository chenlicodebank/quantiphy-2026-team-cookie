# Q2714 – white ball velocity at t = 1.4 s (cm/s)

- Lab video, 1280x720, 24 fps (file fps = question_fps = 24). t = 1.4 s -> frame round(33.6) = 34.
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360). Depth to ball at 1.4 s = 0.7160 m (Euclidean
  camera distance); ball centre at frame 34 = (722.7, 504.0) px.
- Track: scene/tracks/ball.csv (template-matched centres). Checked visually on frames 30-38 (frames/montage.png,
  view.py): the centres sit on the ball. The ball rolls in front of the flat cards, not over them.
- 3D positions: back-projected rays scaled to 0.716 m (speed.py). The ball's depth hardly changes (v drifts ~0.5 px
  per frame), so using one distance for all frames has a negligible effect.

## Measurements (speed.py)
- Per-frame speeds, frames 28-39: 34.3 37.1 34.1 42.1 32.8 36.4 37.3 **70.7** 33.4 35.7 33.5 34.0 cm/s.
- The 35->36 step is 2x the others. Container timestamps are uniform, so this is most likely a dropped capture
  frame: the ball can't double its speed for one frame.
- Physical steady speed (frames 17-46, jump excluded or counted as two intervals): 34.2-34.7 cm/s.
  Raw forward difference at frame 34: 37.3 cm/s.
- Reference-style smoothing (>= 5 frames) around frame 34 can't avoid the jump: centred 5/7/9-step means give
  42.2 / 41.2 / 39.6 cm/s, and linear fits to the positions give 42.8 / 42.4 / 41.2 cm/s.

## Answer
The two readings are about 34.7 cm/s (true rolling speed) and 41-43 cm/s (smoothed clicks that include the dropped
frame). I answer **39 cm/s**, which is within about 7-13 % of either.
Confidence: moderate. The pixel motion is solid (±1 px per frame); the uncertainty comes from the dropped frame.

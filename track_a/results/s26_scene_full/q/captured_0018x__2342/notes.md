# q_2342 — tennis ball velocity at 3.4 s (cm/s)

## Key problem: 3.4 s is outside this clip
- The clip has 49 frames at 24 fps (file fps = question_fps = 24), so it lasts 2.04 s. 3.4 s would be frame 82, which does not exist.
- The clip is a trimmed SAM2-segmented segment. Both people are already posed at frame 0, and objects are still
  bouncing at frame 48. The question's time almost certainly refers to the full original recording, and the offset
  between the two timelines cannot be recovered from this video.
- I assumed 3.4 s falls inside the tennis ball's visible free flight (first fall at frames 27-35 or the rebound at 37-48).
  The gravity prior suggests the ball is in free flight at the asked time. If the clip instead started at the
  original t = 0, the ball at 3.4 s would be in its third or fourth small bounce (about 50-100 cm/s, or near rest).

## Measurements (measure.py, tracks/tennis_ball.csv bbox centres, checked on the contact sheet)
- Pixel acceleration: 5.30 px/frame^2 on the first fall (frames 28-35) and 4.45 on the rebound (frames 37-48).
- Tennis-ball depth from three routes:
  - gravity prior: 2.45 m (fall) and 2.92 m (rebound)
  - floor-contact row, with camera height about 0.9 m taken from the two people's depths and foot rows: 2.68 m
  - size, 6.7 cm ball over 20.5 px: 2.49 m
  - Adopted Z = 2.65 m, f = 763 px, principal point (640, 360).
- 3D speed per frame (cm/s): first fall 196-438 (frames 29-35); rebound 313, 271, 233, 213, 172, 113, 96, 46, 17, 17, 61, 96 (frames 37-48).
  There is a dropped frame at 35->36, and the floor impact is at frame 36.
- The median free-flight speed is about 213 cm/s, and the mid-fall or early-rebound values are 230-320 cm/s.

## Answer
240 cm/s: a central value of the ball's free-flight speeds. Confidence is low because the time mapping is unknown.

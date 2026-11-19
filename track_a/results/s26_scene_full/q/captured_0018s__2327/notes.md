# q_2327: distance between the box and the tennis ball at 3.0 s (cm)

Box = white_carton (dropped by the far/left person). Tennis ball = green_ball (dropped by the near/right person).
The file and question_fps are both 24 fps. **The clip ends at frame 48 (2.0 s), but 3.0 s is frame 72, which is not in
the video.** So the answer is an extrapolation to where the objects come to rest.

## Final states seen in the clip
- Box: lands upright at f39 and tips over to the left. It lies flat from f47. At f48 it is still sliding left at
  about 9 px/frame (cx 428.5 -> 419, bottom row about 610). Friction should stop it within roughly 15-35 px, so I took a
  rest cx of about 405 (range 395-419).
- Tennis ball: bounces almost straight up and down at x about 747-749 (drift < 0.2 px/frame). It hits the ground at
  about row 614 (f36). Its bounces decay with height ratio about 0.5. At 3.0 s it is on a third small bounce, at most
  0.16 m above the ground. This changes the distance by less than 1 %.

## Depths (depth_info gives none for the box or the ball)
- Ground plane, assuming a level camera: camera height h = (feet row - cy) / f x person depth.
  - Left person (3.13 m, feet at row 577): h = 0.890 m.
  - Right person (2.002 m, feet at about row 710): h = 0.918 m.
  - Mean h = 0.90 m, with depth used as Z as on the method card. If the depth is taken as Euclidean distance, h = 0.84.
- Tennis ball: Z = h f / (614 - 360) = 2.72 m. The Euclidean reading gives 2.52.
  - Cross-checks: pixel-gravity fits give 2.39 before the bounce and 2.92 after it (frame timing is irregular; one
    frame is probably dropped). The ball's 21-23 px size fits a 6.7 cm ball at about 2.3-2.5 m.
- Box: near-bottom edge at row 610 gives 2.76 m, plus about 0.05 m to the centre, so Z = 2.81 m. The Euclidean
  reading gives 2.61. This is close to the 2.8 m depth of the soccer ball, which the same person held in her other
  hand. The box fell straight down, so this is consistent.
- Back-projection uses f = 763 and (cx, cy) = (640, 360); see `geom.py`.

## Results
- Depth as Z (method card):
  - Box resting at cx 405: 1.250 m.
  - Box at cx 419: 1.199 m.
- Depth as Euclidean distance:
  - Box at cx 405: 1.160 m.
  - Box at cx 419: 1.113 m.
- Answer: **120 cm**. Confidence is moderate, about ±7 %. The main uncertainties are the extrapolated rest position of
  the box, which is beyond the end of the clip, and the box and ball depths, which are not given.

# q_3010: speed of the player in the white shirt, 0.5–5.53 s (m/s)

- The player: the light-kit player ("player_yellow" in scene/; they look white/cream). They start in the goal and dribble the ball
  out toward the penalty spot. I checked this on frames 15 and 165 (frames/f05.png, frames/f553.png).
- Time base: file fps 29.80 and question fps 30 give the same frames (15 → 165/166) and the same interval (5.033 s).
- Scale: goal frame length 7.32 m. I measured the post centres in code (goal.py, frame 30) at y≈414.5 and 512.8, giving
  98.3 px, so 0.07447 m/px. The scene record gives 97.9 px. Sanity check against other markings: goal-area width 238.5 px
  = 18.32 m (13.0 px/m) and the goal 13.4 px/m, which agree to about 3%.
- Track: stabilized body-mask centroid from scene/tracks/player_yellow.csv, smoothed with a 7-frame moving average (measure.py, path.py).
  The camera drift is negligible (under 3 px).
  - Path length from frame 15 to 165: 156.6 px (every frame, includes jitter), 155.2 (sampled every 5 frames), 153.6 (every 15 frames).
  - Net displacement: 147.9 px. The path curves a little: it goes up-left, then down-left at the end.
- Average speed = path length / 5.033 s ≈ 153–155 px / 5.033 s ≈ 30.6 px/s, giving **≈2.27 m/s**.
  Second route (net displacement / time): 29.4 px/s, giving 2.19 m/s.
- Answer: 2.25 m/s, a compromise between the two routes. Confidence: moderate, about ±5% (scale and convention).

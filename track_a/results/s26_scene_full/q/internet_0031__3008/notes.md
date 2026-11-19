# Q3008: distance traveled by the player in the white shirt, 0.5–5.53 s

- **Which player:** in close-ups (zoom.py → frames/zoom.png), the player recorded in scene/ as `player_yellow` wears a light cream/white top and dribbles the ball out of the goal. The other player has a dark shirt. So the white-shirt player is `player_yellow`.
- **Time base:** I used question_fps = 30, so the interval is frames 15–166. With the file's 29.80 fps it would be frames 15–165, which changes the path by less than 1%.
- **Track check:** the scene track (x_stab, y_stab) follows the player correctly. It runs from inside the goal (386,502) to near the penalty spot (240,472). The overlay is frames/track.png.
- **Path length (measure.py):**
  - Raw per-frame sum: 196 px. This is inflated by ±1–2 px jitter in the centroid as the limbs move.
  - Savitzky–Golay smoothing over 9/15/21/31 frames: 161 / 157.6 / 156.1 / 155.6 px.
  - Sampling every 10 frames after a 5-frame mean: 155.1 px.
  - Net displacement: 149 px.
  - **Value used: 156 px.**
- **Second route:** the ball travels with the player, and its path over the same interval is 152–155 px. This agrees with the player's 156 px; the player swerves slightly more than the ball.
- **Scale (goal.py):**
  - Brightness profiles along the goal frame at frame 0 put the posts' centres at y 414.8 and 512.6 (97.9 px apart). The outer edge of the frame spans about 413–514 (about 100.5 px).
  - I used **99 px = 7.32 m**, so 0.0739 m/px.
  - Sanity check: the goal area (238.5 px = 18.32 m) gives 13.0 px/m, which is consistent.
- **Answer:** 156 × 7.32 / 99 = **11.5 m**. Using 97.9 px gives 11.7 m; using 100.5 px gives 11.4 m.
- **Confidence:** moderate-to-good, about ±5%. The main uncertainties are how the annotators measured the goal frame and how much tracking jitter their path length includes. With no smoothing at all, the path would come out at about 14.5 m.

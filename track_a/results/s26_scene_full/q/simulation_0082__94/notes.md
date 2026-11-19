# Q94 – speed of the black-and-white car at t = 1.0 s (frame 24)

The video is a 2D top-down Blender render at 24 fps (file fps = question_fps = 24). There are two Cybertruck-like pickups:
yellow in the upper lane, and white with a black bed/roof (the asked car) in the lower lane. Both move in −x. They are at rest
in frames 0–1 and move at constant velocity from frame 2 to the end, so the speed at frame 24 equals the constant speed.

## Scale (prior: yellow length = 5.67 m)
- `edges.py`: the yellow paint mask is R−B > 45 (median over rows 375–430). Front and rear edges are sub-pixel half-max crossings
  and are written to `yellow_edges.csv`.
- The yellow pixel length shrinks slowly from right to left: 310.6 px (frame 0) → 307.6 (frame 24) → 305.8 (frame 33,
  where the yellow is at the same image x as the white car at t = 1 s) → 303.3 (image centre) → 302 (left). The scene record
  gives 304–314 / median 308, which agrees. My first mask (`measure.py`, `len2.py`) gave 210 px because a light pillar line
  split the run. I fixed that in `len3.py`.
- I used L = 305.5–308 px, so the scale is 5.67/L ≈ 0.0185 m/px.

## White car's pixel speed
- Cross-correlation of the column profile (rows 515–580) over frames 20–28: −15.95 px/frame. A linear fit of the box centre over frames 2–71
  gives −15.91 px/frame. The record gives 15.81–15.96 for the edges and centre. I used 15.9 px/frame.

## Result
v = 15.9 px/frame × 24 fps × 5.67 / 305.5 ≈ 7.08 m/s (7.02 with L = 308; 7.13 with L = 303).

## Check (second route)
The yellow car moves at 11.33 px/frame, which gives 5.03–5.05 m/s with the same scale. The speed ratio is 1.40, so the speeds are
consistent with designed values of 5 and 7 m/s. Answer: **7.05 m/s**. I am confident the error is about ±1.5%.

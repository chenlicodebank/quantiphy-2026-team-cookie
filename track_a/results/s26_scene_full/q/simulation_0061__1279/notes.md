# Q1279: average bicycle speed over the whole clip (m/s)

The file runs at 24 fps and question_fps is also 24. t=0.58 s is frame 14 and t=1.58 s is frame 38. The camera is static.

## Method (solve.py, check.py)
- Tracks: scene/tracks/van.csv (the white car) and cyclist.csv. I used the bbox centres and assumed the principal point is (1080, 540).
- For a trial focal length f, each object's 3D points at f14 and f38 come from its ray times the given depth. The object moves on the straight line through those two points. Each frame's ray is intersected with that line (least squares) to get the position along the path.
- Focal length: f is chosen so that a quadratic fit to the van's path gives acceleration 4 m/s². This gives f = 2165 px, and the result is stable to ±1 px across different fit start frames. The van's initial speed comes out at about 0.17 m/s, which matches the record's note that it starts from (near) rest.
- Check of f by an independent route: the lamp-post row on the main road converges at u ≈ 1700. A street perpendicular to it would have direction z-component −sin(atan(620/f)) = −0.275. The van direction measured from the depths is −0.273, so they agree, and the bike direction is −0.31. Other values of f break this agreement (f = 3000 gives −0.40 against −0.20).

## Result
- Route 1 (bike's own line through both depth points): the mean of the per-frame speeds over frames 1–71 is **5.32 m/s**. Speeds averaged over 10-frame windows are 5.15–5.40, so the bike moves at a steady speed.
- Route 2 (bike constrained to move along the van's direction, anchored at a single depth): 5.29 m/s when anchored at f14 and 5.27 m/s when anchored at f38. The predicted depth at the other time is 40.55 m against the given 40.34 m, and 41.69 m against the given 41.90 m.
- Answer: 5.31 m/s. Confidence is moderate to high (about ±5%). The main uncertainty is f, which depends on the van track and on assuming a constant acceleration that starts near t = 0.

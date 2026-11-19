# Q1850: average speed of the rocket (m/s)

The scene is 2D: a static side view, with the rocket flying in a straight line up and to the left from the truck's pod. fps = question_fps = 24, so no re-timing is involved.
The prior is rocket length = 2.9 m.

## Scale
- I re-measured the rocket mask (|frame - frame 28| > 40, a ±14 px band around the launch axis, then an opening; `measure2.py`). It reproduces the record's nose and tail positions exactly.
- Full nose-to-tail length on the clear frames 15-20 and 22 is 220-227 px, median about 222. The colour profile (`profile.py`) and the zoomed crop show that the pale bluish tail end is continuous with the body and is not a detached plume, so it is kept in the length.
- L = 221.9 px, which gives 0.01307 m/px.

## Motion
- The centre's position along the axis is taken from `scene/tracks/rocket.csv`, which I verified. The rocket is visible from frame 3 to frame 25.
- The rocket accelerates smoothly. Per-frame steps rise from about 17 px to about 62 px, so the acceleration is roughly 2.2-2.4 px/frame².

## Average speed (mean of the per-frame speeds), by `fit.py` and `fullclip.py`
- Measured over the visible frames 3→25: **12.98 m/s**.
- Over the whole clip, frames 0→28, with the hidden steps extrapolated from a linear fit to the steps: 12.98 m/s using the fit over frames 4-25, and 13.06-13.35 m/s using the fit over frames 9-25.
- Speed at mid-clip (frame 14), from the local steps: 13.38 m/s. For roughly uniform acceleration this equals the full-clip mean.
- A quadratic fit to frames 9-25 gives 13.59 m/s. It overstates the early speeds: the early frames are slower than the quadratic predicts.

**Answer: 13.1 m/s.** The likely error is ±4%: the routes span 12.98-13.4 m/s, and the length measurement carries about ±1.5%.

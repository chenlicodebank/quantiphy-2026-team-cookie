# simulation_0160: measurement record

**Scene.** A 2D Blender simulation filmed top-down: a pool table with 11 balls. 30 fps, 40 frames (t = 0 to 1.300 s), 1920x1080.
Only **ball 13** moves (white with an orange stripe). It rolls from right of centre (1301, 506) to the left
(219, 499) in frame 39 and stops short of the left cushion. All other balls, the table, the pockets and the floor are static.
The camera is static: frame differences are zero outside the moving ball.
All units are pixels (x right, y down) and seconds (t = frame/30). There is no metric scale; take it from the question's prior.
The view looks orthographic and all balls rest on one plane, so a single px→m scale holds for the whole table.
Every static ball measures about 48 px across, and so does ball 13.

## Files
- `scene.json`: inventory (static balls with centre, bbox and diameter; felt, rail and pocket extents), the moving
  object summary, events and camera.
- `tracks/striped_ball.csv`: ball 13 in every frame. Columns:
  - `x_px, y_px`: centre, taken as the centroid of the filled convex hull of the mask.
  - bbox.
  - `length_px` / `width_px`: fitted ellipse axes.
  - `diameter_circle_px`: minimum enclosing circle.
  - `area_px`.
  - `occluded`: always 0.
  - `glitch`: marks frame 1.
  - `dx_prev_px, dy_prev_px, step_px`: displacement from the previous frame. Frame 2's step is taken from frame 0, skipping the glitch.
  - `frame_note`.
- `scripts/`:
  - `diff.py`: frame differencing, used to check camera and motion.
  - `track.py`: median-background tracker; it also writes the overlays.
  - `static.py`: felt, ball, pocket and rail extents.
  - `green_balls.py`: the two low-contrast green balls.
  - `hough.py`: a discarded Hough-circle attempt (too noisy on the felt texture).
  - `view_early.py`: crops of the first frames.

## How it was measured and how reliable it is
- **Track.** Mask = |frame − per-pixel median of all frames| > 45, cleaned with morphology; the largest blob is the ball.
  I checked overlays at frames 0, 2, 10, 20, 30 and 39: the circles fit the ball outline.
  - Centre accuracy is about ±0.5 px.
  - Diameter is 48.4 px (median ellipse major axis; range 47.8–50.2). The enclosing circle gives about 49–51 because of a 1 px blur and shadow fringe. Use about 48 px as the ball's diameter.
  - Motion blur is mild (the ellipse is ≤2 px longer than it is wide, at most).
- **Static balls.** Measured at frame 39 with a non-green colour mask (bbox ±1 px).
  - Balls 14 (green stripe) and 6 (solid green) were measured with a local Lab-distance mask, so their centres are ±2 px. Their masks came out about 51–54 px because of shadow, so treat them as 48 px balls.
  - Ball identities come from colour: 1 yellow, 3 red, 5 orange, 6 green, 7 maroon, 8 black, 9 yellow stripe, 10 blue stripe (mostly white from above), 11 red stripe, 12 purple stripe, 13 orange stripe (moving), 14 green stripe.
  - The two balls near the top that look white are 10 (blue rim) and 12 (purple rim).
  - Two balls are red-and-white with stripes:
    - Ball 13 (orange stripe) is the moving one, at y≈506.
    - Ball 11 (red stripe, static) is at the bottom, (1116, 907).
- **Table.**
  - Felt (inside the cushions): x 184–1707, y 148–937, so 1524 × 790 px.
  - Wooden rail outer box: 110–1781 × 84–999, so 1672 × 916 px.
  - Six pocket centres are listed in scene.json.

## Timing anomalies (important for speed/acceleration questions)
- **Frame 1 is a render glitch.** Ball 13 is drawn at (1305, 801), 295 px below its path, and is absent from its path. It is
  almost certainly not its true position. Use frames 0 and 2 instead (it moved only 3.3 px between them).
- **The video has 7 repeated frames and 7 skipped frames.**
  - Repeated frames (the ball is identical to the previous frame): 5, 10, 13, 19, 26, 28, 35.
  - Double-length steps (about 2× the neighbouring step): 9, 11, 17, 24, 27, 34, 37.
  - So single-frame backward differences of the raw track jitter between 0, v and 2v. The real per-frame motion is smooth.
  - For a speed at frame i, use the local typical step from the non-anomalous frames, or a smooth fit over several frames. Do not use the raw one-frame difference at a flagged frame.
- **Typical clean step sizes** (px/frame):

  | Frames | Step (px/frame) |
  |---|---|
  | 3–8 | about 14–21 |
  | 14–16 | about 28 |
  | 20–23 | about 31.5 |
  | 29–33 | about 33.5 |
  | 36–39 | about 34 |

  The ball speeds up quickly at first and then levels off. Its speed rises over the clip; it does not decelerate.
- **Path length.** Summing the steps gives the net displacement, because the path is straight: 1081.6 px from frame 0 to frame 39.
  Duplicated or skipped frames do not change the sum.

## Events
- t = 0: ball 13 is at rest or just starting.
- No cue, collision, bounce or pocketing happens in the clip.
- At frame 39 the ball's left edge is at x = 196, about 12 px from the left felt edge (184), so it does not reach the cushion.
- Direction is constant: leftward, about 0.4° above horizontal (y goes from 506 to 499).

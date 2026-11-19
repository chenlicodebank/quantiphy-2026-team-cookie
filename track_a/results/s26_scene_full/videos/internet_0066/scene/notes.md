# internet_0066 – measurement record

**Scene:** a real 2D clip at 30 fps, 100 frames (3.33 s), 1920x1080. It is a top-down hand-held view of a wooden gym floor. A basketball (dark red-brown with black seams) crosses the image from right to left between frames 49 and 72 (t = 1.633–2.400 s). Nothing else moves. The person holding the camera has their light blue-grey shoes at the bottom edge. Court markings: a horizontal maroon line at the top (y≈140–194), a maroon vertical line on the right (x 1700–1751), another at the left edge (x≈30–80), and a light-blue vertical line (x 1116–1167). The bright spots along y≈640 are ceiling-light glare on the floor.

All values are in full-resolution pixels and seconds. Time t = frame/30.

## Files
- `scene.json`: inventory, static feature positions and sizes, ball size summary, events, camera.
- `tracks/ball.csv`: one row per frame, 49–72.
  - `cx, cy`: the ball's visible centre in raw image coordinates. `cx_stab, cy_stab` are the same point in frame-0 coordinates, with camera drift removed.
  - bbox, cut to the image.
  - `length_along_motion_x`: horizontal extent, which includes motion blur.
  - `diameter_vertical`: extent across the motion, which is free of blur.
  - `area_px`, `truncated_by_frame_edge`, `occluded` (always 0), `centre_method`.
- `tracks/ball_shadow.csv`: the ball's shadow blob per frame. Low reliability; see below.
- `tracks/camera_shift.csv`: translation of frame i relative to frame 0, from phase correlation on the ball-free top band y<260.
- `tracks/ball_raw.csv`: first-pass output, superseded by ball.csv. Do not use; its masks missed the parts of the ball over the maroon lines.
- `scripts/`:
  - `track_ball.py`: camera shift, plus the first pass.
  - `ball_final.py`: final ball and shadow tracks.
  - `static.py`: line positions and shoes.
  - `scan.py`, `strip.py`, `montage.py`, `probe.py`: viewing helpers.

## How the ball was measured
1. Each frame was aligned to frame 0 using the measured shift.
2. Background: the median of ball-free frames (0–44 and 76–96).
3. Ball mask: pixels that are redder than the background, or brighter than it (the second case catches the ball over the dark maroon lines). The grey shadow is excluded because it is darker but not redder. The largest blob is kept, then opened and closed.
4. Edges: medians of the per-column top/bottom edges (±40 central columns) and the per-row left/right edges (±40 central rows).
5. Centre:
   - Frames 53–69 are fully inside the frame. The centre is the midpoint of the edges. Overlays confirm the mask covers the whole ball.
   - Frames 49–52 are cut by the right edge and frames 70–72 by the left edge. Here the centre is the visible outer edge ∓ DREF/2, where DREF = 256 px (median vertical diameter over frames 53–69).

## Reliability
- **Full frames (53–69):** centre to about ±5 px. The residual scatter of cx about a straight line is 5.8 px.
- **Ball size:** use **256 px** as the diameter (vertical extent, range 250–261). The bbox height ranges 251–266. The horizontal length runs 241–283 because of blur, which is largest around frames 52–54.
  - If a question wants the length along the motion direction, the annotators probably measured the visible ball, about 256–260 px.
- **Edge-cut frames:** 50–52 and 70–71 are good to about ±10–15 px. Frames 49 and 72 are slivers 47–65 px wide, and their leading/trailing edges are faint and blurred. Their centres are unreliable to about ±30 px; frame 72 (cx −88) is likely off by ~30–40 px.
- **Motion:** the ball moves about 90 px per frame to the left. Image y rises slowly (cy 427→448, about +1 px/frame); about 1 px of that over the pass is camera drift.
- **Camera:** hand-held with slow drift. Over the whole clip the shift reaches dx −10 and dy −21 px, but during the ball pass it is under 1 px/frame. For motion measurements either cx or cx_stab works; cx_stab is relative to the background.
- **Height and bounce are ambiguous:** the shadow stays attached to the ball. It is ahead (left) until about frame 59 and behind (right) from about frame 61, as the ball passes under a light. The apparent diameter varies only about ±3%, close to the noise. No bounce, impact or direction change is visible. The ball is probably rolling, or at most on a low path near the floor. The plane is treated as roughly the floor plane.
- **Shadow track:** the shadow is a soft crescent. Its blob switches between shadow lobes (e.g. jumps at frames 58 and 61). Rows 73–75 are a different dark patch at the right edge, not the ball's shadow. Use it only qualitatively.
- **Static positions:** measured at frame 0 by colour thresholds. Line edges are good to about ±2 px. Shoe boxes are approximate (±5 px) and cut by the bottom edge. Neither the shoes nor the lines move, apart from camera drift.

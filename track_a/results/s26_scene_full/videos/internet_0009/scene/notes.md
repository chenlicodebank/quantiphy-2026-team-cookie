# internet_0009 — measurement record (pixels, seconds)

Scene: static, near-nadir drone shot of a red tennis court (2160x3840, 59.826879 fps, 111 frames, t = frame/fps).
Low sun: every object casts a long shadow toward the upper-left. Two players on the near half (top of the image):
**right_player** (runs down-screen toward the net and hits the ball) and **left_player** (stands still). One **ball**:
in flight at frame 0 moving up-screen (rising after a bounce just before the clip), hit by the right player at
frame ~37.8, then flies down-right over the net and leaves the bottom edge after frame 91. No outgoing bounce is visible.

## Files
- `scene.json` — inventory (objects, static extents, court lines), camera, events, column descriptions.
- `tracks/ball.csv` — ball blob per frame (0-37 incoming, 40-91 outgoing; 38-39 absent = racket contact).
- `tracks/ball_shadow.csv` — the ball's cast shadow on the court (0-37, 40-110; occluded rows 52, 85-89 empty).
- `tracks/right_player.csv`, `tracks/left_player.csv` — every frame 0-110: mask centroid (cx,cy), **core centroid
  (core_cx, core_cy) = centroid of the black clothing + dark hair, recommended "visible centre"**, bbox, min-area-rect
  length/width/angle, area.
- `scripts/` — all code: `probe.py` (camera shift, motion survey), `bg.py` (median background), `ball_cands.py`,
  `link.py`, `filt.py` (candidate survey), `track_ball.py`, `track_player.py`, `track_left.py`, `lines.py`,
  `static_shadows.py`, `colors.py`, `overlay.py`, `summ.py`, `finalize.py`. Run `bg.py` first: it rebuilds the
  scratch background `_bg_full.npy` (deleted by `finalize.py` to keep the record small) that the trackers need.

## How measured
- Camera: phase correlation vs frame 0 for all frames -> |shift| <= 0.7 px: static, no background compensation needed.
- Background = per-pixel median of every 4th frame. Ball = bright blob (grey diff > +30), shadow = dark blob (< -30),
  tracked with constant-velocity prediction; centroid of the blob. Checked visually on crops (frames 5, 45, 70, 100)
  and on a whole-frame overlay of all tracks.
- Right player: |frame - background| > 45 in a moving ROI, minus cast-shadow-coloured pixels (shadow colour ~RGB
  65,34,49 vs black clothing ~25-37,13-30,12-34), morphology, components near the previous position. Overlays
  checked at frames 0, 20, 39, 60, 100.
- Left player (static, so in the background): colour segmentation (not court colour, not shadow colour) in a fixed ROI.
- Court lines: white-pixel runs on the median background along scan rows/columns (+-1 px).

## Reliability / ambiguities
- Ball positions: +-1-2 px (incoming), +-2-3 px (outgoing; strong motion blur, streak length 34-39 px, so the centroid
  is the streak middle = mid-exposure position). Frame 49 (crossing the service line) and 76 partially merge with
  a white line / are partially segmented (smaller area) -> centroid off by a few px. Frames 69-70 the ball is over the
  net band but was still detected.
- Ball size: true diameter ~9-10 px = across-motion width of the incoming ball (mask_wid). Outgoing width 11-13 px
  (blur + the ball is higher/closer to the camera). Length along motion is blur, not size.
- The ball is airborne in every tracked frame: its image position is NOT its ground position. The ball_shadow track is
  the sun-projected ground position (shadow-ball offset 65 px at frame 0, max ~505 px at frame 30, ~480 px at contact,
  ~1490 px at frame ~83). The ball and its shadow never meet inside the clip (no bounce visible).
- Contact frame 37.8 from intersecting straight-line fits of the last 4 incoming / first 4 outgoing positions.
- Right player: core centroid +-3 px; mask bbox/extents vary with pose and depend on whether the racket and dark legs
  next to the shadow are segmented (legs touching the shadow are partly lost; racket missed when blurred, e.g. frame 39).
  Top-down view: player standing height is not observable (only footprint/spread in the image).
- Left player: arm in dark sleeve partly classed as shadow; bbox still includes hand and racket. Core moves < 5 px.
- Perspective is small but present: sidelines converge slightly toward the top (doubles width 1786 px at y=900 vs
  1830 px at y=3800). A single planar scale (annotator convention) is still the intended use.
- Court dimension cues (if a question's prior is a court size): doubles width ~1790 px, singles width ~1343 px
  (near y=1300), baseline->service line 893.5 px, service line->net line 1105.5 px (at x=1000).
- Other moving pixels that are NOT objects: the net flutters (y 2780-2880), player shadows move with the players.

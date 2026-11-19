# internet_0074 measurement record

Video: 1440x2560 portrait, 122 frames, 23.976 fps (t = frame/23.976). Real footage (internet), labelled 2D.
Scene: a drone looks almost straight down on an outdoor **pickleball court** (blue court, green surround, white
lines, net across the middle, chain-link fence on the right). Two players play one point:
**near (bottom) player serves → ball bounces in the far right service box → far (top) player returns → bounce in the
near right service box → near player hits → the ball comes down in the far right service box in the last frame.**
All values are image pixels (x right, y down) in raw frame coordinates. No metric scale is assumed.

## Files
- `scene.json`: inventory, static geometry, camera notes, events (frame numbers + positions).
- `tracks/ball.csv`: ball every frame 0-121. Columns: cx, cy (centroid of the yellow-green colour mask), bbox,
  mask_length/width (bbox sides), equiv_diameter (from mask area), area, occluded, after_dropped_frame.
- `tracks/ball_shadow.csv`: ball's cast shadow (dark blob to the -x side). dx/dy_from_ball = shadow minus ball.
  Not available in frames 0-15 (merged with the server's shadow), 58-59, and some frames near the net shadow.
- `tracks/player_near.csv`, `tracks/player_far.csv`: body mask (person + paddle, without cast shadow), half-res
  segmentation scaled to full res. cx,cy = mask centroid ("visible centre"), bbox, mask_length/width along the
  mask's principal axis (axis_deg), area. occluded=1 when the mask touches the image edge (near player is partly out
  of the bottom edge in frames 36-63).
- `tracks/shadow_near.csv`, `tracks/shadow_far.csv`: the players' cast shadows (same columns).
- `tracks/court_lines_per_frame.csv`: positions (line centres, px) of the 3 vertical and 4 horizontal court lines in
  every frame - the camera/background reference.
- `tracks/static_raw.json`: line runs (edges), net shadow rows/extent, fence x at frames 0, 60, 121.
- `scripts/`: all code (`camera.py` court lines, `background.py` median background, `players.py`, `ball.py`,
  `static.py`, `finalize.py`; `*_probe.py` exploratory).

## Static geometry (frame 0)
Court line centres: sidelines x = 341 and 1243 (width 902 px centre-to-centre, 911 px outer edges); centre line x = 793;
far baseline y = 322, far kitchen (non-volley) line y = 998.5, near kitchen line y = 1626, near baseline y = 2313
(length 1991 px centre-to-centre, 2000 px outer edges). Length/width = 2.21 (regulation 44 ft x 20 ft = 2.2, so the
view is close to planar). Kitchen depths 313.5 / 314 px; service-box lengths 676.5 (far) / 687 (near) px; service box
width 451 px. Lines ~8.5 px wide. Net: white tape at y ~1316 spanning x ~255-1345, dark net shadow y 1296-1311
extending left onto the grass to x ~85; post on right x ~1338. Fence line x ~1307-1316.

## Camera
Essentially static overhead drone, but with a slow, smooth zoom-in/descent: court length 1991 → 2011 → 2023 px and
width 902 → 911 → 917 px at frames 0 / 60 / 121 (~1.6% total), far baseline drifts y 322 → 300, near baseline
2313 → 2323, sidelines shift ≤ 10 px. Effect on ball motion is ≤ ~1% and a few px; for precise work map points through
`court_lines_per_frame.csv` (linear per-axis map). Tiny tilt: the far half measures 1.6% shorter than the near half.

## Frame timing (important)
Every 4th frame-to-frame step (into frames 4, 8, 12, ... i%4==0) is ~2x the others (e.g. ball 38, 38, 38, 79 px):
the file was made from a ~30 fps source by dropping every 5th frame. Naive per-frame differences spike at those
frames (`after_dropped_frame=1` in ball.csv). Averages over multiples of 4 frames are unaffected in total distance.

## Events (ball)
toss starts before frame 0 (ball rising at (692,2292)); apex frame 6; serve contact between frames 14 and 15 at
(712,2291); net crossing ~frame 34; **bounce 1 frame 45 at (968,907)**; far player contact between 58/59 at
(1054,665); net crossing 69/70; **bounce 2 frame 82 at (915,1844)**; near player contact between 93/94 at
(921,2116); net crossing ~109; **frame 121 (last) ball at (873,850) at/just before bounce 3**. Bounces were found
where the ball-shadow offset reaches its minimum (~15 px, i.e. touching).
Ball shadow offset grows to ~540 px at the serve's peak height (frame ~29) - the sun is low, from the +x side.

## Players
Far player (white shirt, dark cap): starts behind the far baseline at ~(957,237), moves forward and right to the
service box ~(1018,581) by frame 60 (hits at 58), then drifts left to ~(850,586). Near player (white shirt, black
shorts): serves from behind the near baseline ~(658,2353), stays near the baseline (partly out of frame 36-63),
then moves up/right from frame ~70 to ~(926,2015) at the end. Body masks are pose dependent (arms/paddle
included): length ~120-260 px, width ~90-180 px, area ~5000-11000 px²; the centroid jitters ±10-20 px with arm
swings. In a top-down view a person's standing height is NOT visible; the cast shadows (~450-550 px long) depend on sun
angle.

## Reliability
Ball centre: ±1-2 px (clean colour blob every frame, slight motion blur elongates it to ~9 px). Ball size: colour-mask bbox median 8 x 6 px, equivalent diameter
median 6.8 px (10-90%: 5.9-7.6) (too small for a precise size scale: ±1-2 px = ±20%). Court lines: ±0.5 px per frame - the best scale reference
(court length/width, kitchen depth, service box). Player centroids ±10-20 px; extents ±10 px plus pose variation; near
player's mask is truncated in 36-63. Ball-shadow positions ±3 px where detected; ambiguous near players and the net.
Ambiguities: the ball image is the ball in the air (projected along a near-vertical view), not its ground point; the
ball shadow is a separate dark blob - do not confuse it with the ball. Two small whitish objects at the left image edge
(y~1040, y~1760) are static and unidentified.

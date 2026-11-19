# captured_0014 — measurement record

Lab video, 3D, 24 fps, 49 frames (2.04 s), 1280x720, camera static. Orbbec camera: f = 763 px, principal point ~ (640, 360).
The video was edited with "Segment Anything 2 Demo": only the table and what is on it are sharp; the person,
floor, walls and equipment are heavily blurred.

## Scene
A person (blurred, standing behind the table) holds a small beige/off-white **ball** on the top edge of a tilted
**white board** lying on a small square wooden **table**. Released at about frame 8, the ball rolls straight down the
board toward the camera (image downward, x ≈ 545–550). It drops onto the table top between frames 17 and 18, rolls to
the table's front edge, goes over it at about frame 23, falls in front of the table's pedestal and leaves the bottom of the image at frame 29.
The floor impact is not visible. Other objects on the table don't move: a white cup, a cookie, a black pen, and a light-blue notebook.

## Files
- `scene.json`: inventory (static object pixel extents and corners at frame 40), events, camera, perspective notes.
- `tracks/ball.csv`: per frame 0–29: frame, t, cx, cy (visible centre), bbox, mask_len/mask_wid (box extents), source
  (manual/auto_mask), occluded flag, notes. `tracks/ball_auto.csv`: raw automatic mask output (includes area and equivalent diameter).
- `scripts/`: common.py (decoder), look.py and cropsheet.py (viewers), diff.py (background median of frames 36–48 and
  difference), track_ball.py (mask = diff>22 & warm colour & bright, nearest blob), finalize_ball.py (manual frames
  0–11 merged, final overlay), static_objs.py (board/notebook/cup threshold quads plus corners read by eye).

## Reliability
- Ball centre, frames 12–22 (board and table): ±1–2 px. Frames 8–11 were read by eye at 3x zoom: ±1.5 px. Frames 0–7:
  the ball touches the blurred hand region, so a fixed manual box (532–558, 281–308) is used, centre (545, 294.5), ±2 px.
  The ball doesn't visibly move in frames 0–7.
- Frames 23–28 (falling): the ball is in the blurred background region and motion-blurred vertically, so the mask
  is enlarged (34–38 px wide, up to 59 px tall). The centre is still good to about ±3 px vertically. Frame 29 shows only
  a sliver at the bottom edge, so its centre is unreliable.
- Per-frame centre noise of about ±2–3 px shows up as uneven steps (e.g. 11→12 is 21 px, then 12→13 is 11 px). Smooth before differencing.
- Ball size: the best value is about 26 px diameter (bbox width 24–28 px on the board, frames 12–17; ~27 px while held). Sizes
  after frame 17 are inflated by blur and are not true sizes.
- Static objects: the board corners come from a threshold fit (±1 px). The table corners were read by eye; the back-left
  corner is blurred (±5 px). The cup, cookie, pen and notebook were read by eye at 2.5x zoom (±2 px). Lengths are image
  lengths, so perspective foreshortens the depth-direction sides (table left/right sides, board sides).
- Events: release frame 8 ±1. Board→table step between frames 17 and 18 (the image step drops from ~20 to ~5 px/frame).
  Off the table edge at frame 23 ±1. Exits the image at frame 29.

## Ambiguities
- What holds the board's top edge up (it acts as a ramp) is hidden by the blur.
- The ball leaves the frame before it hits the floor, so there is no bounce.
- The person can't be measured because of the blur.

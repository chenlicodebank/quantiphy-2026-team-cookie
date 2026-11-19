# internet_0029 — measurement notes

**Scene:** a real 2D internet clip, 50 fps, 25 frames (0.5 s), 1080x1080. The camera is static and faces a white door. A hand at the top centre holds a grey ball and drops it. The ball falls almost straight down, drifting slightly left, onto the top of a grey box at the bottom of the frame. The ball reaches the box edge in the last frame (24). The video ends before any bounce.

## Files
- `scene.json`: inventory, static object extents, events, camera, timing note.
- `tracks/ball.csv`: the final ball track, one row per frame. Columns:
  - `x,y`: reference point (visible centre). `ref` says how it was obtained.
  - `bbox_x0..y1`: bounding box.
  - `width_px_horizontal`: across the motion, essentially unblurred.
  - `height_px_vertical_blurred`: along the motion, including blur.
  - `mask_centroid_x/y`, `occluded`, `note`.
- `tracks/ball_raw.csv`: the raw segmentation output. It includes a free circle fit (`circ_*`), a circle fit with fixed r=38 (`circR38_*`), and the fraction of the contour not touching skin.
- `tracks/hand.csv`: a coarse skin-pixel bounding box and centroid of the hand and fingers (x<760, y<260).
- `scripts/`: `look.py` (camera-shift check), `track_ball.py`, `static_and_hand.py`, `knob.py`, `build_record.py`.

## Method
- **Camera:** phase correlation of the wall region against frame 0 gives shifts of 0.25 px or less, so the camera is static. Use raw image coordinates.
- **Ball:** I took the absolute difference from the per-pixel median of all 25 frames. Skin pixels (R−B>28) are rejected only for y<220. I then applied open/close and kept the blob nearest the previous position.
  - The overlay (`frames/ball_overlay.png`, a scratch file) was checked: the mask covers the whole ball in frames 7–23.
  - Frames 0–6: the fingers cover the upper and right part of the ball. Here (x,y) comes from a fixed-radius (r=38) circle fit to the unoccluded rim. The overlay shows it matches the ball outline well.
  - Frame 24: the ball overlaps the box's top edge and the difference mask fails (low contrast against the grey box). I read the position by eye on a 3x zoom: bbox 495–570 × 922–1003, centre (533, 962). This is accurate to about ±4 px.
- **Ball size:**
  - The horizontal width is 74–77 px in frames 8–23 (median 76). The free circle fit on the held frames gives r≈37–38.
  - **Use 76 px as the ball diameter.** The vertical extent grows from 81 to 90 px because of motion blur, so it is not the true size.
  - The apparent size stays constant, which confirms a planar fall.
- **Static objects** (frame 10/12):
  - Door knob: centre (805, 716.6), 64×63 px (threshold mask); a Hough fit gives a 61 px diameter.
  - Grey box top edge: y≈974, spanning x≈255–740 (flat part 270–725); at the frame bottom (y≈1075) it widens to x≈222–775. Read from a grid zoom, ±3 px.
  - Door right edge: x≈879.

## Events
- Ball held, frames 0–4 (y≈51–53).
- First downward motion at frame 5 (t=0.10 s). The fingers open over frames 4–6.
- Free fall by frame 7 (t=0.14 s).
- Contact with the box top at frame 24 (t=0.48 s), the last frame.
- The hand moves up and right after the release (hand.csv).

## Reliability and ambiguities
- **Centre accuracy:** in frames 8–23 the centroid is accurate to about ±1 px. Vertical blur is symmetric, so the centroid stays at the mid-exposure position. Frames 0–7 are about ±2 px. Frame 24 is about ±4 px.
- **Missing frames:** the per-frame vertical steps are 15.5, 18.9, 21.7, 24.8, then **56.9** (frame 12), 32.4 … 39.8, **87.5** (frame 17), … **115.4** (frame 22), 61.9, **124.5** (frame 24). Frame 7's step (23.1) is also about doubled.
  - So one source frame is missing every 5th output frame (frames 7, 12, 17, 22, and probably 24 too).
  - Frames 0 and 1 are identical.
  - Real time between frames is therefore not uniform. Annotators probably used the frames as-is at 1/50 s. A question-specific fit should consider this: for example, use only frames within one 4-step segment, or treat the doubled steps as two intervals.
- **Reference point convention:** the reference point is the visible ball centre. For a size prior on the ball, the pixel length is 76 px. The fall is vertical, so the pixel length "along the motion" in a blurred frame would read 81–90; prefer 76 measured in a sharp, horizontal direction.
- **Other objects:** no other moving objects and no similar-looking balls. The ball casts no visible shadow on the door.

# internet_0020 – measurement record

**What happens:** this is real 2D internet footage (4096x2160, 19.594595 fps, 19 frames, 0.97 s). It shows a bathroom vanity between two white basins. At frame 0 a bare hand (black sleeve, coming in from the right) is already holding a tall, clear, rectangular glass perfume bottle by its metal neck. The hand lifts the bottle straight up. The lift starts at about frame 2 (t = 0.102 s). From about frame 11 the bottle tilts, with its top leaning to the upper right. The neck reaches the top edge at frame 14, and the bottle and hand are gone by frame 18. Nothing else moves.

All values are in full-resolution pixels (x to the right, y down) and seconds. t = frame / fps.

## Files
- `scene.json`: inventory (names, what tells similar objects apart, moving or static, visible frames, pixel sizes and boxes of static objects), events and camera.
- `tracks/bottle.csv`: the lifted perfume bottle, frames 0–18. Columns:
  - `neck_top`: top of the metal neck, which is held between the fingers.
  - `base`: centre of the bottom edge.
  - `center`: the reference point. It is the midpoint of neck_top and base. In frames 15–17 the neck is out of frame, so the centre is extrapolated as base + L/2 along the axis, with L = 637 px; it can lie above the image (y < 0).
  - `tilt_deg`: tilt from vertical, positive when the top leans right.
  - Also: an axis-aligned bbox built from the rigid bottle (length 637, width 145), the visible neck-to-base length, and an occlusion flag plus a note.
- `tracks/hand_arm.csv`: skin-colour mask of the hand and forearm. Columns: bbox, centroid, area, leftmost point, and flags for touching the right or top edge.
- `tracks/camera_shift.csv`: per-frame shift of the static background relative to frame 0, from phase correlation on two static regions. Use `dx_left` and `dy_left`; that region has the higher correlation response.
- `scripts/`: every script used.
  - `view.py`, `crops.py`: gridded views.
  - `diffgrid.py`, `diffcrops.py`, `diffmask.py`: difference against frame 18, with drift compensated.
  - `camera.py`, `hand.py`, `bottle_track.py`.

## Bottle size
These are the values to use when a question's prior is the bottle's size. All are from frame 0, when the bottle is sharp and at rest.

| Extent | Pixels | Range |
|---|---|---|
| Full length, neck top to base | 637 | y 1183 → 1820 |
| Body height, shoulder to base | 453 | y 1367 → 1820 |
| Neck/collar | about 184 | |
| Body width | 145 | x 2550 → 2695 |

The pink perfume bottle in front hides the base, so the base position is uncertain by about ±15 px. The neck top is uncertain by about ±5 px.

## How the bottle was measured and how reliable it is
The keypoints were read by eye on zoomed frames with a grid. Automatic segmentation failed: the bottle is transparent, the glass flower jug behind it shows through, and from frame 4 onward the bottle is strongly motion-blurred.

- **Frames 0–7:** good, about ±10 px.
- **Frames 8–14:** heavy blur, about ±20–30 px. The base is the end of the blur streak minus half a frame's step, which approximates mid-exposure.
- **Frames 15–17:** only the lower part is visible, so the centre is extrapolated. Treat it as rough (about ±40 px).

The visible neck-to-base length stays between 585 and 660 px, which is consistent with a rigid 637 px bottle; the spread shows the reading error. The vertical travel of the centre is about 1500 → 330 px from frame 0 to frame 14 (about 1170 px). For a speed or acceleration, prefer differencing `neck_top_y` (frames 0–14) or `base_y` (frames 0–17), and smooth over several frames.

## Hand
The hand/forearm mask is a skin-colour threshold (`hand.py`).

- Frames 0–9: the mask also takes in the bottle (skin colour shows through the glass), and it is cut at y = 1450 to leave out the wooden counter. In these frames `bbox_y1` = 1448 is that cut, not the fingertips.
- From frame 13: the arm runs off the top/right edge.

So the centroid is the centroid of the *visible skin area* and is only a rough hand track. The best point for the hand is the grip point, which is about the same as the bottle's `neck_top`. The forearm crosses the image from the right: the bare skin runs from about x 2440 (fingers) to about x 3550 (sleeve) at frame 0.

## Camera
The camera is not perfectly fixed: there is a slow, smooth drift. Relative to frame 0, the background moves +0.5, +2.7, +6.9, +11.5, +15.0 and +23.5 px in x at frames 1, 6, 9, 12, 14 and 18, and +18 px in y by frame 18. That is small compared with the bottle's travel (about 1.5%) and has no zoom. To measure against the background, subtract `dx_left`/`dy_left` (so for upward motion, add `dy` to the upward displacement). The tracks are in raw image coordinates.

## Static objects
Static positions in `scene.json` are boxes read from gridded views, ±10 px. Most are from frame 18, where the background has shifted (+24, +18) px compared with frame 0; others are labelled as frame 0. Several bottoms are hidden behind objects in front: the candle and the jug.

## Ambiguities
- **Two "glass bottle/vase" objects.** The lifted perfume bottle (tall, rectangular, metal neck) is a different object from the glass flower jug/carafe right behind it. The jug's handle only becomes visible once the bottle has gone (frame 11 onward).
- **Two other perfume bottles.** The small pink-liquid square bottle stays on the tray and does not move.
- **Two amber bottles.** One is the large amber pump bottle, the other the small amber dropper bottle.
- **Shadows and reflections.** The brass tray reflects the products; ignore those reflections.

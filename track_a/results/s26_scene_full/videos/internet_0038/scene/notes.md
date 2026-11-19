# internet_0038 – measurement record

This is a top-down view of a dark grey desk. It shows an open white/silver laptop in the centre, a white mouse to the right of the laptop, and a person's two hands in grey sleeves. The video is 15 frames at 18.4849 fps (0.81 s) and 1280x720. Units are pixels and seconds. Image x points right and y points down. t = frame / fps.

## Files
- `scene.json`: inventory, static extents (laptop, keyboard, trackpad, mouse), events and camera.
- `tracks/right_hand.csv`, `tracks/left_hand.csv`, `tracks/mouse.csv`: one row per frame with frame, t, centroid (cx, cy), bbox (x0, y0, x1, y1, bbox_w, bbox_h), PCA mask extents (length_main_axis, width_across, main_axis_deg), area_px and an occluded flag.
- `scripts/measure.py`: segmentation (HSV skin mask for hands; white mask for mouse and laptop), camera-shift check and overlays. `scripts/static.py`: edge profiles for static objects. `scripts/write_record.py`: builds the tracks and scene.json. `scripts/view.py`: gridded frames.

## Camera
The camera is static. Phase correlation of the empty desk band (y<200) against frame 0 gives a shift of 0.15 px or less in every frame, so no background compensation is needed.

## Moving object: right hand
This is the only object that really moves. In frame 0 it rests on the mouse and is already moving: it travels 15 px between frames 0 and 1. It slides left and up onto the right half of the keyboard. The centroid goes from (988, 535) to (713, 438), a net (-275, -97) px or about 292 px in total. The per-frame step is about 25-27 px/frame over frames 4-10, with the largest step (27 px) between frames 8 and 9. The hand is still slowing at the end of the clip (about 9 px between frames 13 and 14), so the clip contains no clear end of motion.

The reference point is the centroid of the skin mask. The mask covers the hand plus the bare wrist down to the sleeve cuff, so it shifts slightly if the cuff moves. The mask is about 215-225 px along its main axis and about 125-135 px across it. The main axis turns from about 104° to about 70° (in image coordinates) as the hand rotates. `y0` in the track is the fingertip-most extent.

Overlays (frames/ov/) confirmed the masks hit the right hand in frames 0, 5 and 14.

## Nearly static: left hand
The left hand rests at the lower left of the keyboard. Its centroid stays within about 6 px; the mask grows a little as the fingers spread or type.

## Static objects
- **Mouse**: bbox (972, 413)-(1040, 547), 134 px long (vertical) by 69 px wide, centre (1006, 480). The right hand covers it in frames 0-3 (flag occluded=1, so the mask is partial there). The top edge (y=413) does not change and the bbox is constant from frame 4 onward, so the mouse was not moved.
- **Laptop base**: x 436-862 (427 px wide) and y about 236-533 (about 295 px deep). The front edge is slightly tilted: y=535 at x=450 and y=529 at x=840.
- **Lid**: the open screen is seen edge-on as a thin strip at y 229-242 running x 422-888 (466 px), wider than the base. The overall laptop bbox is (422, 229)-(888, 536).
- **Keyboard and trackpad**: keyboard about (483, 275)-(812, 400), 330 x 126 px; key pitch about 22.4 px. Trackpad about (590, 425)-(713, 513).
- **Not tracked**: the sleeves (cut off by the frame bottom) and the desk (no markings).

## Reliability and ambiguities
- Static edges are good to about ±2 px.
- Hand centroids are good to about ±3 px; the hand boundary against the white laptop is clean.
- In frames 0-3 the right hand mask is next to and on top of the mouse. The mouse's white is excluded from the skin mask.
- No motion blur is significant.
- For a question about "the hand's size", the most likely pixel length is the mask main-axis length (about 220 px for the right hand, about 210-235 px for the left).
- The mouse length is 134 px; laptop widths are 427 px for the base and 466 px for the lid line.

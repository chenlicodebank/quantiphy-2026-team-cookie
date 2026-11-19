# captured_0015x — measurement record

Lab recording (24 fps, 73 frames, 1280x720, labelled 2D). The background has been replaced with pure white. A woman
(face blurred; grey T-shirt, black trousers, sneakers) stands still in the left-centre of the frame and tosses a
brown plush **teddy bear** straight up twice with both hands, catching it each time. The camera is static. There is no
ground, furniture or markings. Bottom right has a grey watermark text box, which is not an object. All values are
pixels (x right, y **down**) and seconds (t = frame/24). No metric scale was assumed.

## Files
- `scene.json`: inventory, size summaries, events, camera, and the free-flight bear centres.
- `tracks/teddy_bear.csv`: one row per frame (0-72). `cx,cy` = bbox centre (the reference point, i.e. the visible
  centre); `centroid_x/y` = centroid of the pixels; `bbox_*`; `mask_len_main_axis`, `mask_width_across`,
  `main_axis_angle_deg` (PCA of the silhouette) and `mask_area` (free frames only); `state` free/held;
  `occluded` (1 = held, partly hidden by the hands); `source` auto_component/manual_box.
- `tracks/person.csv`: silhouette bbox, centre, centroid, height_px and area for every frame. `contains_bear=1` means
  the bear touches the person, so it is merged into the silhouette and widens the box.
- `scripts/`: `bearmask.py` (foreground/brown masks), `fg_components.py` (detached components per frame),
  `masksheet.py`/`cropsheet.py` (grid overlays for reading and checking boxes), `track.py` (writes both CSVs; holds
  the manual boxes), `summarize.py`, `probe*.py`.

## How it was measured and how reliable it is
- **Free flight (frames 17-22, 53-58, plus 61)**: the bear is its own connected component of the non-white
  foreground, so its box and mask are exact to about 1 px. This includes the pale muzzle and paws. Frame 61 is held
  but separated from the hands by a thin gap.
- **Held frames**: the hand and arm skin is the same hue as the bear, so colour cannot split them. I read these boxes
  by eye from 2x crops with a 10 px grid (frames/mask_*.png) and drew them back on the frames to check them
  (frames/crops_*.png). Expect about ±4 px per edge. The left edge (behind the hands) and, while the bear is lifted in
  front of the chest (frames 14-15, 23-24, 49-50, 60), the bottom edge are hidden. In those frames the box centre is
  biased upward by up to about 10 px. The bear's **top edge (`bbox_y0`) is the most reliable coordinate in held
  frames.** The `centroid_*` of held frames is contaminated by hand skin; use `cx,cy`.
- **Bear size (free flight)**: bbox height is 95 px (median; range 92-99). Main-axis length is 97.5 px (93-99). Width
  is 52 px (46-61), and up to 66 px when an arm sticks out (frames 18-22). The bear stays roughly upright in flight
  (main axis near vertical). In held frames the bear turns or lies horizontal (frames 29-33 and 64-72), so the box
  sizes there do not show its true size.
- **Person**: height is 508 px (hair top y 133-135 to shoe soles y 640-641). The feet do not move, so the camera is
  static. The frame-52 bbox top of 119 is the bear. The pelvis (about (350,370) ±15 px) is a visual estimate only.

## Events (frame / t)
- Toss 1: bear at rest at hip, centre about (431,373), frames 0-7. Lift starts at frame 8 (0.333 s). Release at
  17 (0.708 s); frame 16 is the last frame touching the hand. Apex at 19 (0.792 s), cy 177.5 (19 and 20 are almost
  equal). Last free frame 22; caught at 23 (0.958 s).
- After catch 1: lowered to the hip; lowest at 30 (1.25 s), cy 380. Small adjustments and settling, frames 31-42.
- Toss 2: lift starts at 43 (1.792 s). Release at 53 (2.208 s); 52 is the last contact. Apex at 54-55 (2.25-2.29 s),
  cy 150.0 and top y 101. Last free frame 58; caught at 59 (2.458 s). Then lowered; nearly at rest at the hip from
  frame 65 to 72.
- Release and catch frames are ±1 frame, because contact is judged from silhouette connectivity.
- Motion is almost purely vertical. Horizontal drift is about 5 px during flight (x 439 to 433, and 443 to 439).

## Ambiguities
- Similar colours: forearms, hands and hair are brown like the bear. The automatic mask is used only when the bear
  is detached.
- Motion blur is mild. Some frames show segmentation halos (pale fringe) around the bear.
- Labelled 2D: one pixel scale applies to the bear's motion plane. The bear is roughly at the person's hand depth,
  slightly in front of the body. The person stands about 3/4-turned.
- Depth or metric questions must use the given prior. For lab convention, f ≈ 763 px and principal point ≈ (640,360).

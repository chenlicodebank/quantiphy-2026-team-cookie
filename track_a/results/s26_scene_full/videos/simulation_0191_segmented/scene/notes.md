# simulation_0191_segmented: measurement notes

**Scene.** This is a 2D segmentation video: 1920x1080 pixels, 120 fps, 200 frames, 1.667 s. The background is plain white. A brown cardboard box ("FRAGAIL" printed on it) falls straight down onto the flat roof of a parked white truck. The truck is a box-body catering/lift truck with its cab on the right and a white lift cage on the cab roof. The camera is static. The truck pixels change by at most 1.6 grey levels across all frames, so there is no pan and no shake. Coordinates are in pixels with y pointing **down**. t = frame/120.

## Files
- `scene.json`: inventory, static sizes, events and camera.
- `tracks/box.csv`: the box, every frame 0-199.
  - `center_x, center_y`: the reference point, the centre of the box's front face.
  - `center_y_from_bottom`: face_bottom_left − 95, an alternative centre.
  - Bounding box `x0,y0,x1,y1,bbox_w,bbox_h` (the silhouette including the lid flap).
  - `face_left/right/top`: the front-face edges.
  - `face_bottom_left`: the bottom edge of the front face, read at the left column.
  - `bottom_right`, `silhouette_bottom_mid`: the lowest visible pixel, including the underside strip.
  - `face_height_px`, mask centroid `cx_mask, cy_mask`, `area`.
  - `occluded`: `top_out_of_frame` for frames 0-27.
- `tracks/flap.csv`: the dark flap, frames 78-174. Visible-mask centroid, bbox and area. The flag `partly_hidden_behind_truck` is set when the mask touches x=128.
- `scripts/`:
  - `track.py`: colour segmentation and the camera/truck stillness check.
  - `box_edges.py`: front-face edges and centre; writes the final box.csv.
  - `static.py`: truck extents and wheel circles (`static_out.json`).
  - `explore.py`, `look2.py`: viewing aids.
  - Run `track.py` before `box_edges.py`.

## Box (main moving object)
**Size.** The front face is 410 px long (x 529-938, the same in every frame) and 190 px high (189-190 in every unclipped frame). It does not rotate: the angle is 0° throughout and x is constant within ±1 px.

**Motion.**
- Purely vertical. center_x = 733.5 throughout.
- center_y holds at about 60-61 for frames 0-4, i.e. it starts from rest at t≈0.
- It then accelerates downward: 121 at f30, 231 at f50, 305 at f60.
- Impact on the roof at f60-61 (t≈0.50 s).
- A tiny 2-3 px rebound or settle over f62-72.
- At rest from f74: centre (733.5, 310.5), face 216-405, silhouette bottom 408. The roof top is at y=411-412.

**Clipped frames 0-27.** The top of the box is above the image. center_y there comes from the bottom-left corner minus 95 px. This joins smoothly with the directly measured centre: the two agree within 1-1.5 px at f28 onward.

**Reliability.** Edges are good to about ±1 px. The dark lid flap at the top-right (x≈825-935, from about f40) and the thin underside strip seen in perspective (about 25 px at f0, about 2 px at rest) inflate `bbox_h` and `y1`. **Use the front-face columns, not the bbox, for height and centre.**

**Not measured.** There is no 3D depth. If a question gives the box size, scale by its pixel length of 410 or face height of 190.

## Truck (static)
- **Overall bounding box:** x 124-1840, y 349-1063, which is 1717 px long and 715 px high, from the lift cage top to the wheel bottoms.
- **Cargo box:** x≈130-1460 (about 1330 px), roof at y=412, bottom at y≈845 (about 433 px high). The cargo-box right end next to the cab is approximate, ±15 px.
- **Wheels:** rear wheel centre (703, 976), r≈88. Front wheel centre (1581, 973), r≈90. Wheelbase 878 px.

## Flap (minor, ambiguous)
A black flat panel appears at the rear (left) end of the truck at f78 (t=0.65 s). It swings out to x≈17 around f87-95. It then rises and retracts behind the truck, from y≈760 to 655, and is gone after f174 (t=1.45 s).
- Its right part is hidden behind the cargo box, so its full size is unknown and its centroid is biased toward the visible part.
- It may be part of the truck (a door or tail-lift) or a separate object behind it. It is likely irrelevant to most questions.

## Ambiguities
- The only similar-looking items are the orange marker lights and green/yellow stickers on the truck. They are static and were excluded from the box mask by y<425.
- The white holes in the lift cage are segmentation artefacts.
- There are no shadows.
- Motion blur is negligible.

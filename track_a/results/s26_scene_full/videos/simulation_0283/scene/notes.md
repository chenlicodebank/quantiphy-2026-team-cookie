# simulation_0283: measurement record

The video is a Blender render, a "2D" scene, 2560x1440, 24 fps, 72 frames (3.0 s). Time is t = frame/24. All values are in image pixels (x to the right, y down, origin at the top-left) and seconds. There is no metric scale: each question's prior sets it.

## Scene
- The camera is **static**. Phase correlation of each tested frame against the empty background gives shifts below 0.02 px. Frames 64-71 match the background within noise, so the background shift is 0 in every frame.
- One moving object, the **dragon**. It is dark grey with bat-like wings, horns and a long tail. It flies **right to left** in front of a white and brown eroded cliff, flapping all the time. It dips toward the beach and water twice, then leaves through the left edge.
- Static scene items (positions are in scene.json):
  - the cliff (whole background)
  - the sky and blurred hills at the top-left
  - the pale sand beach (x 900-2560, y 880-1150)
  - a reflecting water pool along the bottom (water line at y ≈ 1150-1200)
  - boulders on the left shore (x 0-830, y 1000-1200) and a tall pale rock spire at the far left
  - a small static dark patch on the sand at about (1960, 945). This is part of the background, not a shadow.
- The dragon's cast **shadow** (on the sand and shore rocks) and its **reflection** (in the water) move with it. Neither is tracked, and both are kept out of the dragon mask.

## Files
- `scene.json`: inventory, camera, events, a summary of the dragon's pixel extents, and static-object positions.
- `tracks/dragon.csv`: one row per frame (0-71); `visible=0` for frames 63-71. Columns:
  - `cx, cy`: mask centroid. This is the reference point.
  - `bbox_x0..y1, bbox_cx, bbox_cy, bbox_w, bbox_h`: bounding box.
  - `area`: mask area in px².
  - `main_axis_len, cross_width, main_axis_deg`: extent along and across the PCA main axis of the mask.
  - `truncated_by_frame_edge`: the dragon is cut by the left edge (frames 50-62). This is the same as `occluded`.
  - `touches_water_line`: the mask was clipped at the water line, so the bottom extent may be too small (frames 15-19 and 39-41).
- `scripts/`:
  - `bg.py`: camera check and background (median of frames 62-71).
  - `maskfn.py`: the mask.
  - `track.py`: the per-frame track.
  - `summarize.py`: builds scene.json.
  - `testmask.py`, `probe*.py`: visual and debug checks.

## How the mask was made
1. Take the per-channel difference from the empty background, with threshold 30.
2. Remove cast shadow: pixels darker than the background whose local 9x9 texture still correlates with the background (NCC > 0.6). Only large solid regions count, grown by 12 px.
3. Remove everything below a hand-drawn water line, which cuts off the reflection.
4. Keep the largest component plus nearby pieces that do not look like background texture.
5. Grow the mask back into thin structures (wing tips, tail) using a lower threshold of 12, without growing into shadow-like pixels.
6. Fill holes.

I checked the masks on overlays of every third frame and on full-resolution crops of frames 0, 6, 14, 15, 18, 19, 25, 33, 38, 43 and 57. They cover the whole dragon, including the wings, the tail and the tail tip.

## Reliability and ambiguities
- **The reference point is the silhouette centroid, not the Blender origin.** The origin (body/pelvis) cannot be seen. Because the wings are included, the centroid moves with the wingbeat: when the wings rise, the centroid moves up by tens of px. The period is about 24 frames (about 1 s). Bounding-box height and area peak at frames 5 and 29-31 (wings up) and are lowest around frames 13, 21-22 and 37. Expect about ±30-60 px between the centroid and the origin. Per-frame centroid steps are 40-85 px while the dragon is fully in view; it slows to about 20-30 px per frame near the bottoms of the dips (steps into frames 16-17 and 39-41).
- **Frames 0 and 1 are effectively identical**: the centroid and bounding box match to within 0.1 px, and the mask area differs by only 11 px. The backward-difference speed at frame 1 is therefore about 0. Motion starts at frame 2.
- **Frames 50-62:** the dragon is cut by the left edge, so the centroid and bounding box there describe only the visible part and are biased right. Do not use them for speeds or sizes. Frames 0-49 are fully in view.
- **Frames 15-19 and 39-41:** the lowest wing tip or foot reaches the water line (y ≈ 1150-1190), and the part below it is cut off with the reflection. In those frames, `bbox_h` and `bbox_y1` can be too small by up to about 50 px. Whether the dragon actually touches the water (around frames 15-19) is ambiguous.
- **Mask edges:** the tail tip over dark rock is sometimes faint (fixed in most frames). Small leftovers of the cast shadow can remain at the lower edge of the mask near the ground (frames 14-15 and 38-45). Expect about ±10-20 px on the bounding-box extents in general. Motion blur is mild.
- **Size cues:** in frames 0-49:
  - horizontal extent (`bbox_w`): 517-837 px, widest at frame 32, median about 600
  - height (`bbox_h`): 247-598 px
  - main-axis length: 438-885 px

  The dragon moves mostly across the image plane. Its apparent size changes with the wing pose, with no clear trend that would show a change in depth. One px-to-world scale from the prior is appropriate.
- **Path:** the centroid runs from x ≈ 1940 (frame 0) to x ≈ 250 (frame 49), with two vertical dips:
  - the lowest y of the first dip is about 942 at frame 16
  - the highest point is y ≈ 556 at frame 29
  - the second dip reaches y ≈ 949 at frame 40

  The dragon then climbs toward the left edge (frame 50) and is gone by frame 63.

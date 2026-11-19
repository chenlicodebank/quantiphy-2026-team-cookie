# simulation_0023_segmented — measurement record

Video: 960x960 px, 25 fps, 75 frames (t = frame/25, 0–2.96 s). Source: segmentation (a Blender render with the background replaced by plain white). 3D scene. All values are in pixels and frames/seconds. No metric scale was estimated.

## Files
- `scene.json`: inventory, short motion descriptions, pixel sizes at the first and last frames, events, camera.
- `tracks/boat.csv`: frames 0–74. Columns:
  - `ref_x, ref_y`: bbox centre of the whole boat mask (mast tip to keel).
  - `centroid_x/y`: mask centroid.
  - `bbox_*`: bounding box of the whole boat.
  - `hull_x0..hull_y1, hull_w, hull_h, hull_cx, hull_cy`: the hull band. These are the rows whose mask width is at least 60% of the widest row, down to the keel. `hull_cy` and `hull_cx` are the best guess for the model origin.
  - `area_px`, `occluded`.
- `tracks/bird.csv`: frames 0–66. Columns:
  - `ref_x/y`: bbox centre.
  - `centroid`, `bbox`.
  - `len_main_axis` / `width_across`: sides of the minimum-area rectangle around the mask.
  - `area_px`.
  - `occluded`: 1 = the bird touches the mast and was separated by subtraction.
  - `cut_by_frame_edge`.
- `scripts/`:
  - `track.py`: segmentation and tracks.
  - `summary.py`: builds scene.json.
  - `explore.py`, `crops.py`, `stack.py`, `show_boat.py`: viewers and checks.

## Method
- Mask = pixels with min(R,G,B) < 235 on the white background, then connected components.
- Bird = a compact component (60–1500 px, at least 15 px wide, at most 45 px tall) close to the position predicted from its last motion.
- In frames 10–13 the bird touches the mast. There, its mask = the pixels in a window around the predicted position, minus the previous frame's boat mask shifted by the boat's motion and dilated by 2 px.
- Boat = all other mask pixels near the hull.
- I checked overlays (the frames/ folder, scratch only) at frames 0, 4, …, 72 and 10–13. The masks cover the full boat and the full bird.

## Objects
1. **boat**: red/pink-hulled fishing trawler with a white/grey wheelhouse, a tall thin mast with a crossbar, and a black chimney/davit at the stern. Visible in every frame and never occluded.
   - Moves left steadily: centroid about 3.9 px/frame, sd 0.3.
   - It also recedes from the camera:
     - hull width 258 → 226 px (ratio 0.876);
     - keel line y 632 → 617.
   - Whole height, mast tip to keel: 329 → about 305 px. The mast tip is faint and thin, so `bbox_y0` and `bbox_h` jitter by about ±8 px. Use the hull values or the keel (`hull_y1`) for size and scale.
   - The crossbar is visible at frames 0–4 and about 37–74 but edge-on in between, so there is a small yaw or rock.
   - It is a 3/4 view, so image width mixes length and beam. No along-axis length can be measured reliably.
2. **bird**: a single dark-brown flying bird with flapping wings. It flies left to right at about mast height (y ≈ 368–398 px).
   - Speed is about 11.2 px/frame from the bbox centre. This is noisy (sd 2.7) because wing flapping moves the bbox centre. Use the centroid, or smooth over several frames.
   - Its apparent size grows somewhat over the clip: median bbox width about 38 px early and about 50–54 px at frames 58–62. It may be getting closer to the camera, or this may be wing pose.
   - Wingspan range when not cut or merged: bbox_w 23–54 px; bbox_h 9–34 px, which changes with wing pose.
   - Frames 10–13: overlaps the mast (`occluded` = 1). Its size there is less reliable, and the bird may pass behind the pole.
   - Frames 63–66: cut by the right image edge (`cut_by_frame_edge` = 1). Absent in frames 67–74.

## Static objects
None. The background was replaced by white, so there is no water, ground, horizon or marking.

## Events
- Frame 0: both objects are already moving.
- Frames 10–13 (t 0.40–0.52 s): the bird passes the mast.
- Bird height: low point around frames 9–11 (y ≈ 398), high point around frames 49–53 (y ≈ 368).
- Frames 63–66: the bird exits on the right. It is gone from frame 67 (t 2.68 s).
- No contacts or impacts.

## Camera
Assumed static: simulation cameras are fixed within a clip. With a white background this cannot be checked against scenery, but the boat's keel and size change smoothly with no jitter. There are no perspective cues except the boat's own apparent shrinking. The focal length is unknown and must come from the depth_info and prior given with each question.

## Reliability
- Boat hull/keel values: ±1–2 px.
- Boat whole-bbox height: ±8 px (faint mast tip).
- Bird bbox: ±2 px, but its shape changes every frame with flapping.
- Ambiguity: the true origin of either object is not visible. Boat: probably the hull centre (`hull_cx`, `hull_cy`). Bird: the body centre, close to the bbox centre or centroid.

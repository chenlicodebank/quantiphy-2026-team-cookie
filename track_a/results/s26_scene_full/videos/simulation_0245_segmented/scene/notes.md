# simulation_0245_segmented — measurement record

2D scene, Blender render with the background replaced by flat white (RGB 253). 1080x1920, 30 fps, 75 frames
(t = frame/30, 0 to 2.4667 s). Pixel coordinates: x to the right, y down, original resolution. No metric scale is
guessed here: answering sessions take one m/px scale from their prior.

## Files
- `scene.json`: inventory, size statistics, displacement and path summaries, events, camera.
- `tracks/ibex.csv`, `tracks/rabbit.csv`: one row per frame (0-74). Columns: frame, t, cx_centroid/cy_centroid
  (mask centroid), cx_bbox/cy_bbox, x0,y0,x1,y1 (bbox, inclusive), length_px (x extent), height_px (y extent),
  area_px, touches_edge, occluded. The ibex file also has trunk_x0/trunk_x1/trunk_cx (median left/right edge of the
  torso barrel over rows 1300-1400, tail strand left out) and ground_y.
- `scripts/`: `track.py` (segmentation and tracks), `make_json.py` (scene.json), `overlay.py` (check image),
  `summ.py`, `probe.py`.

## Objects
- **ibex**: a large brown ibex/antelope-like quadruped with long swept-back ridged horns, a whitish snout and a long
  tufted tail. It faces right and walks left to right the whole clip, always fully in view and never occluded.
  - Bbox length (snout/horn to tail tip): median 489 px (range 471-510, changes with leg and tail pose).
  - Height (horn top to hooves): 421 px (415-426).
  - Torso length: about 273 px.
  - Centroid x goes from 348.2 to 831.8, a 483.6 px net shift, about 6.53 px/frame on average. The per-frame step
    varies from about 5 to 9 px with the gait.
  - Centroid y stays between 1325 and 1332.
- **rabbit**: a small brown rabbit/hare on the ground just right of the ibex's front hooves. It moves right at almost
  the ibex's speed (centroid about 6.66 px/frame over frames 0-68) with a hopping rhythm (per-frame step 3-10 px).
  - Unclipped size: length 72 px (68-88), height 63 px (52-73).
  - From frame 69 on it runs past the right image edge (touches_edge=1; only 32 px is visible at frame 74). Its
    centroid and bbox there are biased to the left, so use x0 (its rear edge) plus about 36 px instead.
- **Ground**: not visible; there is only an implied ground line at y ≈ 1551 where the hooves and paws rest. There are
  no other static objects.

## Events
- Both animals are already moving at frame 0 and still moving at frame 74.
- Neither changes direction, and there is no contact, bounce or impact.
- The rabbit's front reaches the image edge at frame 69 (t = 2.30 s).
- The centroid gap between the two animals widens slowly, from 298 px (frame 0) to 310 px (frame 68).

## Camera
Static, as far as can be told. The background is textureless, so this rests on two cues: the ground line stays at
y = 1549-1553 throughout, and both animals keep a constant apparent size, so there is no zoom or depth change. Motion
lies in a plane facing the camera, so one m/px scale applies to both animals.

## Method and reliability
- **Masks**: min(RGB) < 247, 3x3 morphological opening, connected components. The largest component is the ibex;
  components with centroid y > 1470 are the rabbit; any other fragment is merged into the ibex.
- **Check**: overlays at frames 0, 12, 25, 37, 50, 62 and 74 show the masks cover the full animals, including the pale
  snout and the tail tip.
- **Accuracy**: edges are good to about ±1-2 px. The pale snout is anti-aliased against white, so it may lose about
  1-2 px.
- **Reference point**: the simulation origin (body or hip root) is not visible. The mask centroid sits on the torso
  near mid-body and is the recommended stand-in; trunk_cx agrees with it to within a few px.
- **Speeds**: per-frame centroid steps carry gait noise (legs and tail move the mask's mass around), so smooth or
  average over several frames.
- **Ambiguity**: the two animals have similar brown colours but are always well separated, so the masks never merge.

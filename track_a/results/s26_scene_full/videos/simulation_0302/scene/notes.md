# simulation_0302 — measurement record

The video is a 3D Blender render, 2560x1440, 24 fps, 72 frames (3.0 s), with t = frame/24.
It shows **one dark blue-black dragon** (bat-like wings, long tail, four legs, a light grey-blue head patch) flying in front of a plain light-blue sky. There is no ground, horizon, prop or other object, and the only perspective cue is the dragon's own apparent size. The camera is **static**: the sky gradient and the corner colours do not change between frames, and there is no background texture that could show a pan.

## Files
- `scene.json`: inventory, camera, events, extent statistics, glide-phase size ratio and the per-frame step of the head point in px.
- `tracks/dragon.csv`: one row per frame (0–71). The dragon is visible in every frame, never occluded and never touches the image border. Columns:
  - `cx, cy`: centroid of the silhouette mask.
  - `bbox_*`: axis-aligned box (x0, y0, x1, y1 inclusive; w, h; centre).
  - `area`: mask area in px.
  - `main_axis_len, cross_axis_w, axis_angle_deg`: PCA extents of the mask along its main axis and across it.
  - `head_x, head_y, head_patch_area`: centroid of the light grey-blue head patch.
  - `core_*` and `open_c*`: distance-transform and opened-mask points. **Do not use these.** They land on the wings.
  - `occluded` is always 0.
- `masks/mNN.png`: silhouette masks at quarter resolution, used for checking.
- `scripts/`: `track.py` (segmentation and tracking), `overlay.py` (check images), `summarize.py` (builds scene.json), `probe*.py` (colour probes).

## Method
- The background is a quadratic surface fitted to the sky on each frame. The mask is the set of pixels where the summed |RGB − background| is greater than 60, followed by a 5x5 close and removal of components under 30 px. I checked the overlays at frames 0, 5, 8, 12, 13, 16, 20, 24, 30, 34, 37, 38, 44, 45, 50, 51, 56, 60, 64, 66 and 71: the masks follow the whole silhouette, including wing tips, tail and legs.
- The head patch is found as flat pixels of medium brightness (summed RGB 190–440) that differ strongly from the sky; the largest component after a 5x5 opening is kept. The overlays confirm that this point sits on the head in every frame.

## Reliability and ambiguities
- **Origin.** The rig origin is unknown. The **head point (head_x, head_y)** is the recommended stand-in for the body/root position: it moves smoothly (about 25 px per frame up to f21, about 14 px/frame at f22–50, about 11 px/frame at f51–71). Its jitter is about ±2–3 px, rising to about ±4 px after f55 because the patch shrinks to roughly 200–500 px.
- **Mask centroid.** During flapping (f0–50) the mask centroid swings with the wing strokes by up to about 150 px, so it is not usable as a body position there. During the glide (f51–71) the pose is rigid, so the centroid is a fixed point on the body and is the smoothest track to use (step 13.3 px at f52 falling to 9.9 px at f71, mean 11.4 px).
- **Duplicate first frame.** Frames 0 and 1 are identical, so motion only appears from frame 1→2. A one-frame backward-difference speed at frame 1 would come out as 0.
- **Flapping.** The dragon flaps from frame 0 to about frame 50, and the wings are held fixed from about frame 51 to frame 71.
  - Wings up: about f5–9 and f28–33.
  - Wings spread flat or edge-on: f13–14 and f37–38, where bbox height is smallest (245 px at f38).
  - Wings folded down: f16–18 and f41–44, where bbox width is smallest (363 px at f42).
  - Wings spread horizontally (good frames for wingspan): f24–26 and f51–71.
- **Extents.** The largest bbox width is 1150 px (f0) and the largest bbox height is 850 px (f3). Extents mix wing pose with distance, so pick frames by pose.
- **Depth.** The dragon recedes and shrinks throughout. In the rigid glide its bbox width goes from 755 px (f51) to 669 px (f71), a ratio of 0.886, so its depth rises by a factor of about 1.13 over those 20 frames.
- **Image motion.** The head moves up and to the left: from (1875, 908) at f0 to (855, 278) at f71.
- **Shading and edges.** There are no shadows, motion blur is negligible, and wing edges are anti-aliased, so expect about ±2 px error on extents.
- **Focal length.** It is unknown. Estimate it from a given depth together with a known size, for example the wingspan measured in a glide frame.

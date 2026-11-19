# simulation_0036_segmented — measurement record

3D Blender scene, segmented: the background has been replaced by plain white. 1080x1080, 24 fps, 72 frames (t = frame/24).
The camera is static: there's no background to check against, but both tracks are smooth and share no jitter.

## Objects (both move; both visible in every frame, 0-71, never occluded)
- **boat**: red fishing boat with a white cabin, a tall mast and "AH805" on the hull. The bow points to image-left. It moves steadily
  to image-left at about 3.0 px/frame (centroid x 608 → 394), and cy stays about 716→719. Its apparent size grows about 12%
  (bbox width 177→199 px; mast-tip-to-keel height 216→230 px; red hull x-extent 174→195 px), so it is also coming toward the camera.
- **person**: small human, about 40 px tall (bbox height 40-41 px, width 10-15 px), left of the boat at x≈124-208, feet at y≈745-750.
  Walks to image-right (toward the boat) at about 1.04 px/frame; the centroid x jitters ±0.5 px with the gait. Height grows only slightly (40→40 px bbox, feet 745→750).
- No static objects, ground, horizon or markings: nothing for perspective or vanishing points.

## Files
- `tracks/boat.csv`, `tracks/person.csv` have one row per frame:
  - mask centroid `cx_mask, cy_mask`: the reference point, standing in for the object origin
  - bbox `x0,y0,x1,y1`, `bbox_w`, `bbox_h`, `bbox_cx`, `bbox_cy`, `area`
  - PCA main-axis length/width/angle of the mask
  - `occluded` (always 0)
  - boat only: `hull_x0..hull_y1` (extent of the red pixels) and `mast_top_y` (top of the mast, measured with a low threshold).
- `scene.json` holds the summary: inventory, sizes at frames 0/36/71, events, camera, and the pixel gap between the boat and person centroids (~480 px → ~192 px).
- `scripts/track.py` builds the tracks: non-white mask (255-min(RGB) > 40), connected components, split at x=300.
  `scripts/overlay.py` draws the overlays used for checking and adds `mast_top_y`. `scripts/summarize.py` builds scene.json.

## Reliability / caveats
- I drew the bboxes on frames 0, 36 and 71 and checked them by eye: they cover the full boat and the full person.
- **Boat:** `y0` in the bbox is unreliable because the thin mast tip comes and goes at the threshold (539-568). For the boat's full height, use
  `mast_top_y` (smooth, about ±1 px; it may sit 1-2 px above the true tip because of anti-aliasing). `y1` (keel bottom) includes the
  dark underside of the hull. There is no water or shadow.
- **Centroids vs. origins:** a mask centroid is only a proxy for the object origin. For the boat, the centroid sits low (y≈716,
  around the hull deck line) because the hull holds most of the mask area. For the person, the centroid (y≈728-733) is about
  pelvis height. Per-frame centroid jitter is about ±0.5 px for both, which matters for one-frame speed differences. Fitting or smoothing over several frames is advised.
- **Motion start:** frames 0 and 1 are nearly identical, so motion starts at frame 1.
- **No depth cues:** depth has to come from the depth_info the question supplies. The boat and person feet sit at a similar image height (745-767).
  Their relative depths are unknown, though the person is probably much farther away or much smaller in the world.

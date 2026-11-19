# simulation_0227 — measurement record

**The video.** A 2D Blender render, 1920×1080, 24 fps, 50 frames (t = frame/24, from 0 to 2.0417 s). The camera is static: phase correlation of the house and tree region against frame 0 gives a shift below 0.02 px in every frame. The camera looks straight at a pool deck. The house and pine trees are in the back, sun loungers stand on a grey stone deck, a stone coping runs along the pool edge, and rippling water fills the foreground. There are two moving objects and both move to the right (+x), roughly parallel to the image plane:

1. **cat**: a small black cat with white paws, walking on the deck just behind the coping (paws at y≈918). It walks at a steady ≈5.4 px/frame for the whole clip and never stops or turns.
2. **flamingo_float**: a pink inflatable flamingo ring (ring plus long neck, dark beak, head on the right) floating in the pool in front of the coping. At frame 0 it is close to rest (0.53 px in the first step). It speeds up smoothly to a peak of 13.64 px/frame at frame 24 (t = 1.0 s), holds about 12.4–13.6 px/frame over frames 21–31, then slows to 1.25 px/frame at frame 49. It has not fully stopped when the clip ends. Vertical bobbing is within ±1.1 px.

There are no contacts, collisions or occlusions. The cat and the float never overlap in the image.

## Files
- `scene.json`: the inventory (moving and static objects), pixel sizes, a motion summary, events, camera information and the per-frame float step list.
- `tracks/cat.csv` has one row per frame, 0–49:
  - `frame`, `t`.
  - `cx, cy`: centroid of the full mask (tail and paws included).
  - `bbox_cx, bbox_cy, x0, y0, x1, y1, bbox_w, bbox_h`: the full-mask box. The tail is included and raises `y0` when it is held up.
  - `mask_len, mask_wid`: sides of the minimum-area rectangle.
  - `area`, `occluded` (always 0).
  - **`body_cx, body_cy`**: the recommended reference point (root/pelvis proxy). It is the centroid of the dark body after a 9×9 opening, which removes the tail and legs.
  - `body_x0..body_y1`, `body_len`: the box and length of that torso.
  - `head_top_y`: the highest point in the front 35% of the box.
  - `height_paw_to_head`: from the paw bottom to the head/ear top, ≈54 px median, range 45–59.
  - `len_rump_to_nose`: ≈84 px median, range 72–98.
- `tracks/flamingo_float.csv` has one row per frame:
  - The same mask columns as the cat (`cx, cy, x0..y1, bbox_*, mask_*, area`). These come from the noisier segmentation mask: the bottom and left edges sometimes pick up reflection or ripple pixels.
  - `tm_dx, tm_dy`: sub-pixel translation relative to frame 0, from masked template matching of the float's part above the water.
  - **`ref_cx, ref_cy`, `ref_x0..ref_y1`**: the recommended reference. This is the clean frame-0 box (x 643–801, y 887–1018; 159 px wide, 132 px tall above the waterline) shifted by `tm_dx, tm_dy`.
- `scripts/`:
  - `bg.py`: the median background of the lower band, plus the camera-shift check.
  - `track.py`: background-difference masks for both objects.
  - `refine.py`: the template-matched float reference, plus the cat's body, head and length measures.
  - `viz_ref.py`: overlays for checking the tracks.
  - `edges.py`: the float's edge profiles.
  - `static.py`: the coping joints.
  - `summary.py`: the statistics copied into scene.json.
  - `probe.py`, `vprobe.py`, `maskviz.py`: exploration.
  - Run them from the workspace root in this order: `bg.py`, then `track.py`, then `refine.py`.

## How measured and reliability
- **Cat segmentation.** The cat is found as the pixels that differ from the median background (camera static). The dark-fur pixels are the core, and the mask then grows to nearby changed pixels to take in the white paws, the grey head and the tail. The overlays (frames 0, 20, 30, 35, 49) show the mask on the cat.
  - Body centroid: ±1–2 px. A gait bob of about ±2 px in y and small x jitter are real limb and pose effects.
  - Full box extents: ±3 px. The tail and the stretched legs make the length vary between 87 and 111 px.
  - The cat's shadow is faint and mostly excluded.
- **Float.** The template-matched translation is accurate to about 0.1–0.3 px, and the motion is very smooth. Its frame-0 box was set from the background-difference column and row profiles and checked visually; its edges are good to ±2 px.
  - The bottom edge is the waterline, so where the float "ends" below that is ambiguous. Its reflection in the water is excluded.
  - The float's size stays the same, so it does not rotate or change depth.
  - Its origin is unknown. It is probably the ring centre, which is lower than the box centre. For displacement, speed and acceleration this does not matter, because the motion is a pure translation.
- **Static objects** were measured at frame 0. The sun loungers are approximate (±3 px, partly occluded): 3 in the front row and 3 in the back row, with the front-row widths at 182, 185 and 217 px from left to right. The coping-stone joints are precise (±1 px) and fall every ~150 px (x = 482, 633, 781, 931, 1082, 1232, 1382, 1533, 1681, 1831). The coping top is at y≈926.

## Ambiguities
- The cat and the float are at slightly different depths. The cat is on the deck behind the coping and the float is in the water in front of it. A single scale taken from one object is an approximation for the other, but the scene shows no strong perspective.
- **The cat's "length" depends on what is counted:**
  - torso alone ≈73 px;
  - rump to nose ≈84 px;
  - full box including tail and paws ≈98 px.
- **The cat's height depends on the tail:**
  - paw to head ≈54 px;
  - box including the raised tail up to 76 px.
- The float's own size is clear: width ≈159 px, height above the water ≈132 px (head top to waterline).
- The float's per-frame mask boxes (`x0, x1, y1`) are noisy from ripples and reflection. Use `ref_*` instead.

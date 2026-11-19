# simulation_0140 – measurement record

Simulation (Blender) render, labelled 3D, 1920x1080, 24 fps, 100 frames (t = frame/24, 0 to 4.125 s).

## Scene
- **Backdrop:** a flat, static photo of a night-time building courtyard. There is a central facade with a grid of
  dark windows, a red neon sign "BE DIFFERENT" in the upper middle and one bright white lit window at the bottom
  middle. Orange- and red-lit side facades sit left and right. The view looks slightly upward, so the vertical
  facade edges converge (this is the photo's own perspective). There is no ground plane or horizon.
- **Moving object:** one dark bird. It takes off from a window ledge at the lower left (about (212, 865) px) at
  frame 0. It flies up and to the right in an arc, reaching its highest point (minimum image y) at frame ~64
  (≈2.67 s, about (1116, 373) px, just under the sign), then descends to the right. It is still flying at about
  (1674, 525) px at frame 99. It never leaves the frame and does not touch anything after take-off.
- **Bird's shadow:** at take-off the bird casts a shadow on the backdrop. The shadow is merged with the bird in
  frames 0–2, separates from frame 3, drifts up and to the left (x≈180–200) and fades out by about frame 12. This
  means the bird starts close to the wall.
- **Camera:** static. The whole-frame mean absolute difference between consecutive frames is ≤0.05 grey levels,
  so the background shift is 0 px.

## Files
- **`scene.json`:**
  - Inventory: bird, bird_shadow, the sign letters, the sign with its glow, the lit window, the facade windows
    and the take-off ledge.
  - Static boxes in px, measured on the temporal-median background:
    - Sign letters: [642, 271, 1336, 351], 695×81 px.
    - Sign with red glow: 714×137 px.
    - Lit window: [661, 856, 786, 1028], 126×173 px.
  - Bird path summary: image path length 1683 px; net displacement 1498 px.
  - Apparent-size trend in 12-frame windows.
  - Wingbeat peak frames (from peaks of bbox height): about 5, 13, 17, 20, 27, 33, 39, 48, 97, i.e. roughly a
    6–8 frame period early in the clip.
  - Events, and camera/perspective notes.
- **`tracks/bird.csv`** has one row per frame (0–99) with these columns:
  - `cx, cy`: mask centroid. This is the reference point and stands in for the rig root.
  - `bbox_*`: the bounding box.
  - `mask_area`
  - `mask_len_major/minor`: sides of the minimum-area rectangle.
  - `occluded`: 1 means part of the body could not be segmented.
  - `quality` (good, fair or poor) and `note`.
- **`scripts/`:**
  - `background.py`: per-pixel temporal median background, computed in row bands.
  - `track2.py`: the final tracker.
  - `finalize.py`: writes `bird.csv` and `scene.json`.
  - `viewcrops.py`, `strip.py`, `overlay.py`: visual checks.
  - `diff.py`, `track.py`, `dbg.py`: earlier exploration. `track.py` is a superseded tracker.
  - `bg.png` is an 8×8 placeholder; the full background is in `frames/`, outside the record.

## How the bird was measured
- The mask combines two tests against the median background:
  - pixels darker by more than 22 (max over channels);
  - over black window panes only (background max < 45), pixels brighter by more than 12, because there the bird
    shows as faint red/orange highlights.
- Clean-up: open 2×2, close 7×7. The component nearest a constant-velocity prediction is kept, plus fragments
  within 25 px of it.
- In frames 3–14, pixels with x < 226 are excluded so the separating shadow is not picked up.
- Every frame was checked on zoomed crop sheets: the box sits on the bird in all 100 frames.

## Reliability and ambiguities
- **Frames 0–4 (poor):**
  - Frames 0–2: the bird is merged with its own shadow.
  - Frames 0–4: the bird's body is over a black pillar (x≈222–245), where it cannot be segmented.
  - So the centroid may be off by about 10–20 px, mostly in x, and the boxes understate the bird's size. The
    frame-0 mask is only the beak and head (12×6 px).
- **Low-contrast frames (fair):** about 29, 50–54, 72–76 and 82–86, where the bird is over black windows. The
  mask is faint and the centroid is good to about 3–5 px.
- **Elsewhere (good):** the centroid is good to about 2 px. Flapping moves the mask centroid by a few px relative
  to the body, so smooth over a few frames if one-frame speeds look noisy.
- **Size along the path:** with wings spread, the bbox width is about 40–54 px all along the path. The window
  medians are about 46 px in frames 0–23, about 37 px in frames 48–59 and 72–95 (partly because of low contrast),
  and about 46 px at the end. So the bird's apparent size changes little and its camera distance is roughly
  constant, perhaps slightly larger mid-flight.
- **Bird size:**
  - Wing span varies strongly with the flap: bbox width ranges from about 20 to 54 px, height from about 13 to
    41 px.
  - For "maximum width/wingspan" use the largest good-quality `bbox_w`: 53–54 px (frames 9, 14, 98). For the
    minimum, use the small values in good frames.
  - The body length (beak to tail) is about 40 px when the wings are folded.
- **Static boxes:** pixel-accurate in the image, but they are features of a flat 2D backdrop. Their world size
  depends on where that backdrop plane sits, which is unknown.
- **Scale:** no metric scale is assumed anywhere.

# simulation_0241 – measurement record

Video: 1920x1080, 24 fps, 50 frames (t = i/24, last frame t = 2.0417 s). Source: simulation, 2D scene.
View: top-down render. A cross-gabled house roof fills the upper middle, with lawn and tree canopies around it.
Three animals walk to the right (+x) on the lawn below the roof. All values are in pixels (x right, y down) and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory, per-object summary (start/end reference point, net displacement, raw path length, median extents), roof extents, events, camera.
- `tracks/brown.csv`, `tracks/white.csv`, `tracks/small.csv`: one row per frame (0-49).
  Columns: `ref_x, ref_y` = reference point = centroid of the object's mask (proxy for the rig origin/body centre);
  `bbox_*` = mask bounding box (axis-aligned; the animals face +x so bbox_w = length, bbox_h = width seen from above);
  `len_major_px / width_minor_px` = extents along/across the mask's principal axis; `area_px`;
  `body_*` = stats of the bright-body-only mask (without the dark head/tail), as an alternative; `occluded` = 0 always.
- `scripts/`: `common.py` (frame decoding), `explore.py` (camera-shift check, colour samples), `segment.py` (masks, tracks, overlay PNGs in ../frames/ov),
  `building.py` (roof edges), `make_record.py` (writes scene.json), `zoom.py`, `printtracks.py`, `check.py` (visual and numeric checks).

## Objects
1. **brown_animal**: red-brown quadruped (horse/cow-like), white nose and hooves, head to the right. The upper animal, just under the roof eave (y≈776).
   Mask: colour threshold (red-brown hue plus white nose/hooves), because it overlaps its own path in every frame so no clean background exists.
   Length ≈144 px (141-155; the range depends on whether the thin tail and nose are caught), width ≈38 px.
   Walks +x at ≈2.6 px/frame, frames 0-48 (centroid 749.6 → 874.1, y ≈776-778).
   **Frame 49: the animal jumps back ≈125 px to nearly its frame-0 position** (the walk animation loops and the root resets). Treat 0-48 as the continuous motion. Frame 49 is still in the CSV.
2. **white_animal**: large cream/white quadruped (cow/goat/llama-like). Its head is a dark grey disc at the right end in frames ≥ ~5 (white in frame 0) and it has a dark tail end at the left. The middle animal (y≈865).
   Primary mask = full silhouette from background difference (background = frame 49 for x<1090 and frame 0 for x≥1090, which are clean for this animal). It includes the dark head and tail, plus possibly a few pixels of contact shadow or an ear.
   Length ≈177 px (159-190, varies with gait and head/tail pose); body-only length ≈165 px; width ≈55 px.
   Walks +x the whole clip: centroid 974.7 → 1201.0 (≈4.6 px/frame). The per-frame step oscillates 2.6-7.2 px with the gait (period ≈10-12 frames), and y oscillates 860-868.
3. **small_animal**: small tan/white animal (dog/cat/rabbit-like), ≈36 x 21 px (length x width). The lowest animal (y≈924). Full-silhouette mask, as for the white animal.
   Walks +x the whole clip: centroid 1055.0 → 1279.5 (≈4.6 px/frame), y constant at 923.6. The per-frame step oscillates 2.6-6.7 px.
4. **house_roof** (static): main block x 660-1362 (702 px wide) with the ridge at x≈1018. Along the ridge it runs from y≈22 to y≈745 (≈723 px); at the eave corners from y≈95-100 to ≈720.
   Cross wing: x≈618/640 → 1405/1425 (≈790 px), y≈270-520 (≈250 px).
   The edges are slightly slanted because the roof is closer to the camera than the ground. **Roof pixels are not on the same scale as the animals on the ground.** Edges were found by gradient profiles (±3 px).
5. **trees / lawn** (static): tree canopies at the frame edges, and sunlit lawn on the right with tree shadows. No markings, props or vehicles.

## Events
- Frame 0 (t=0): all three animals are already walking. No starts, stops, contacts or direction changes occur. All move +x.
- Frame 49 (t=2.042 s): brown animal teleports back ≈125 px (loop reset).

## Camera
Static: phase correlation between consecutive frames gives |shift| ≤ 0.01 px for all frames. 2D top-down scene. The animals' apparent sizes stay constant (no depth change), so one px→m scale from a prior applies to all ground-level animals.

## Reliability and ambiguities
- Centroids are good to about ±1 px per frame, but the gait makes the per-frame steps noisy (±2 px). Smooth over a gait cycle (≈10-12 frames) if needed.
- The true Blender origin may be offset from the mask centroid by a constant amount (a few px), which does not affect speeds.
- Lengths depend on tail/head inclusion. The bbox ranges above give the spread. Use the median for a "size" prior, or the frame named in the question.
- Animal species are not certain from the top view: brown = horse/cow-like, white = cow/goat-like, small = dog/cat-like. The best way to tell them apart is colour and vertical order (brown top, white middle, small bottom).
- Shadows: the background-difference mask may add a thin rim of shadow to the white/small silhouettes. The brown colour mask excludes shadow.

# simulation_0080 – measurement record

2D simulation (Blender), 1920x1080, 24 fps, 29 frames (t = frame/24, last frame 28 = 1.1667 s).
**Top-down view** onto a uniform grey floor (~RGB 151). No markings, no static props. Camera static.
Frames 0 and 1 are pixel-identical (motion starts between frames 1 and 2).

## Objects
| name | what | moves | visible |
|---|---|---|---|
| cyclist | person in black riding a cyan/light-blue bicycle, lower lane (y≈644), heading **-x (left)** | yes | frames 0–24 (fully in frame 0–16; clipped by left edge 17–24; gone from 25) |
| walker | person in pale lavender/white shirt, dark trousers, dark hair, upper lane (y≈440), walking **+x (right)** | yes | frames 0–28 (always fully visible) |
| ground | uniform grey floor | no | all |

No other objects. Only one cyclist and one walker, so no ambiguity of identity.

## Files
- `scene.json` – inventory, sizes, events, camera.
- `tracks/cyclist.csv` – per frame: `cx,cy` (mask centroid incl. rider), bbox `x0,y0,x1,y1,w,h`, `mask_len_main` / `mask_width` (PCA extents), `area`, `clipped_by_frame_edge`, cyan bike-only extents (`bike_*`), rider dark-clothing centroid (`rider_dark_*`), and **`root_x, root_y` = recommended reference point** (bicycle bbox centre; for clipped frames 17–24 = rear edge x1 − (378.5−1)/2, y = mean lane y 643.9).
- `tracks/walker.csv` – per frame: mask centroid `cx,cy` (limbs only – the shirt is too close to floor grey to be in the base mask, so `cx,cy` is biased; don't use), bbox (limbs+arms), PCA extents, `head_cx/cy` (dark hair centroid), shirt bbox `shirt_x0..y1`, filled-mask centroid `full_cx/cy`, and **`pelvis_x, pelvis_y` = recommended reference point** (centre of the shirt/torso bbox).
- `scripts/track.py` (segmentation, overlays), `scripts/finalize.py` (root proxy, scene.json), `scripts/probe.py` (pixel checks).

## Key pixel numbers
- Cyclist: bike length (front wheel tip to rear tip, along x) **378 px** (376–381 over frames 0–16, very stable); width across (handlebar span with hands) 117 px. Rider/bike height not observable (top-down).
  Displacement **≈47.5 px/frame**, constant (steps 46.5–48.2 for frames 2–19; after 20 the clipped-edge steps are noisier, 44–51). Motion straight along −x; y drifts 640→645 (mask centroid).
- Walker: pelvis proxy steps **≈13 px/frame** (10.5–15), x 947.5 (f0) → 1295.5 (f28) = 348 px net in 27 moving frames; y ≈ 437–448 (lane essentially horizontal). Head centroid runs ~10–20 px ahead of torso centre (forward lean / head in front of pelvis in top-down).
  Shirt shoulder span (y) ≈108–112 px; torso depth (x) ≈50–56 px; bbox_w (stride extent, feet) oscillates 102↔221 px (feet together at frames ~0–1, 17–18; max stride ~frames 8–9 and 24–25). Standing height NOT measurable from this view.
- Lane separation: cyclist root y ≈ 644 vs walker pelvis y ≈ 440 → ≈ 200 px apart in y. At frame 0 their x positions nearly coincide (cyclist 928.5, walker 947.5), so they are passing each other at the start; distance between them grows afterwards.

## Events
- Motion starts frame 1→2 (t = 0.042→0.083 s) for both; frames 0/1 identical.
- Cyclist front reaches left edge at frame 17 (0.708 s); fully out after frame 24 (gone at 25, 1.042 s).
- No contacts, bounces or direction changes. Walker walks steadily to the end.

## Reliability
- Cyclist root x: ±1 px for frames 0–16 (crisp bbox); ±3 px frames 17–24 (extrapolated from rear edge, rear edge partially blends with shadow / rider when narrow).
- Walker pelvis: x ±2 px (torso bbox; shirt contrast low, ~15 grey levels). pelvis_y jumps by ~5–10 px in frames 11–14 because the upper shirt edge is hidden by the arm – use the lane mean ≈441 if y matters. The true rig pelvis is hidden under the torso; the torso centre is the closest visible proxy.
- Scale: 2D scene, one metres-per-pixel factor from whatever prior the question gives (e.g. bike length 378 px, walker speed ~13 px/frame = 312 px/s, cyclist ~47.5 px/frame = 1140 px/s). Soft shadows are excluded from masks (threshold 28 grey levels).

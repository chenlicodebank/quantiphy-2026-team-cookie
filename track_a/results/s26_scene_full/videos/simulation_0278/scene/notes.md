# simulation_0278 — measurement record

2D simulation (Blender), 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). Units: pixels and seconds; no metric scale.

## Scene
- **Only object: the whale.** It is a grey humpback-like whale seen from directly above (dorsal view). The head points left (−x), the two long pectoral fins point up and down, and the fluke is on the right. It is visible and unoccluded in all frames 0–71 and stays fully inside the image.
- **Background:** plain light-grey backdrop with a radial vignette. There are no ground features, markings or other props. The whale casts a soft drop shadow, a 20–50 px halo that is widest at the snout and below the fins.
- **Camera:** static, because the vignette doesn't change and the blowhole y stays at 765.0 ± 0.1 px. The view is top-down and looks orthographic, so motion lies in the image plane and one m/px scale applies.

## Files
- `scene.json`: inventory, camera, motion summary, extents, events.
- `tracks/whale.csv`, one row per frame (0–71):
  - `blowhole_x/y`: sub-pixel template match of the blowhole marking, a body-fixed "ʊ" mark on the head just behind the lighter snout cap. **This is the recommended reference point (origin proxy) for positions, speeds and distances.** The body translates rigidly, so the origin moves exactly like this point. Template score is 0.87–1.0.
  - `cx_mask/cy_mask`: mask centroid. It is reliable only where `edge_closed=1`. Otherwise the mask includes some shadow halo, which shifts the centroid by about 8 px in y and up to 40 px in x, so don't use it for speed.
  - `x_min…y_max`, `bbox_w/h`: silhouette bbox.
    - `x_min`: the snout tip, found from its faint dark outline.
    - `x_max`: the fluke tip.
    - `y_min/y_max`: the pectoral fin tips.
    - The bbox is taken from sharp silhouette edges and excludes the shadow, to ±2–3 px. Isolated glitches of about 5–10 px: snout at frames 55–56, y_min at frames 42 and 50.
  - `axis_len/axis_width/axis_angle_deg/area_px`: principal-axis extents of the mask. These are shadow-affected when `edge_closed=0`, so prefer `bbox_w`/`bbox_h`.
  - `snout_x/y`, `tail_x`, `occluded` (always 0).
- `scripts/`:
  - `track_whale.py`: segmentation and tracking. It also writes overlays to `frames/ov_*.png`, which I checked at frames 0, 36, 54 and 71; the mask, bbox, snout and blowhole hit the right places.
  - `summarize.py`: builds `scene.json`.
  - `edge_profile.py`, `edge_test.py`: diagnostics.

## Motion and events
- **Frames 0 and 1 are identical:** no motion between them.
- **From frame 1 onward:** the whale swims leftward in a straight horizontal line at constant speed. Blowhole x = 1060.91 − 5.8709·frame px; residual is ≤ 0.14 px for frames 1–71 and the per-frame step is 5.64–6.10 px. That is 140.9 px/s, with no acceleration. y stays constant at 765.
- **Displacement:** the blowhole goes from x 1055.0 (frame 0) to 644.1 (frame 71). Net displacement = path length ≈ 411 px.
- **Snout tip:** x 745 at frame 0 → 343 at frame 71.
- **Tail and fins:** the fluke beats up and down (foreshortened from above) and the pectoral fins flap, so the extents oscillate.
  - Snout-to-fluke length: 1568 px at frame 0, minimum ≈ 1422 at frame 26, maximum ≈ 1590–1599 near frames 55–60 (frame 55 is partly a snout glitch).
  - Fin-tip y span: 643 px at frame 0, maximum 783 at frame 24, minimum 639 at frame 71.
- **Other sizes at frame 0:** body width without fins ≈ 320 px; fluke span ≈ 410 px.
- **No contacts, bounces or other events.**

## Reliability and ambiguities
- **Blowhole track:** excellent, ±0.1–0.2 px.
- **Bbox extents:** ±3 px, with the glitches noted above.
- **Whale length for a size prior:** the mean bbox_w over the clip is about 1520 px. Which frame (or the rest-pose length) a "whale length" prior refers to is ambiguous: frame 0 (1568 px) is the least deformed pose, while the world AABB changes with the tail beat. The full per-frame series is in the CSV.
- **Shadow:** don't confuse the soft drop shadow with the silhouette; the halo-including mask is about 40 px longer at the snout.

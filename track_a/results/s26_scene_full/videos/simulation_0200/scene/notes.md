# simulation_0200 — measurement record

**The video:** a 2D Blender render, 60 fps, 14 frames (t = frame/60, 0–0.2167 s), 2560×2560 px. The camera is static.
An amber bottle with a tilted glass dropper stands on a white pedestal. One amber teardrop-shaped drop (point up)
breaks off the pipette tip at frame 0 and falls straight down to the right of the bottle. It leaves through the bottom of the image after frame 11.
The drop is the only moving object.

All values are in pixels: x to the right, y DOWNWARD, origin at the top-left corner. No metric scale is assumed.

## Files
- `scene.json`: inventory (drop, dropper_pipette, bottle, pedestal, background wall), static extents, events, camera.
- `tracks/drop.csv`: one row per visible frame (0–11). Columns: centre (`cx_px`, `cy_px`) = drop origin; a fixed-size
  57×86 bbox around it; the raw diff-mask extents (`mask_*`); occlusion flag (always 0); notes.
- `scripts/`: `track_final.py` (the final track, the offset calibration and an overlay sheet), `track_drop.py` and `check_drop.py`
  (first diff-mask passes and the threshold check), `match_drop.py` (template-match cross-check; its frames 10–11
  are wrong, so it is not used), `static_profiles.py` (edge profiles of the pedestal and bottle in frame 13).

## How the drop was measured
- Background subtraction against frame 13 (the drop is gone by then). Gaussian blur 7, |diff| > 8, then morphological open/close.
- The pointed top of the drop is sharp in every frame. The rounded bottom loses contrast in frames ≥ 6 (dim lighting
  near the bottom, transparent liquid), so the bottom of the mask is cut off there (mask_h 76–86).
  The centre is therefore taken from the mask centroid of the top 45 rows, plus a constant offset to the bbox centre.
  The offset (+15.53 px in y, ~0 in x) was calibrated on frames 2–5, where the whole drop segments cleanly.
- The drop's size stays the same throughout: **height 86 px (vertical, tip to bottom), width 57 px (±2 px)**.
- I checked the overlay sheet by eye: the box and cross sit on the drop in every frame 0–11.
- Reliability: centre ±1 px in y and ±1 px in x for frames 2–11. Frames 0–1 are ±2 px, because the drop touches or is close to the
  pipette rim and the mask can include a sliver of it.
- Per-frame dy (px): 16.4, 44.5, 73.5, 102.6, 132.0, 161.2, 189.8, 220.0, 247.2, 276.1, 303.7.
  Second differences are 28–30 px/frame², so the drop accelerates uniformly. A free fall from rest released at frame 0 fits this:
  the first step is about half the later step increments. x stays at 1175.6 ± 0.5 px, so the fall is purely vertical.
- Frame 12 would put the centre near y ≈ 2658, which is outside the image. There is no impact, bounce or splash in the video.

## Static objects (frame 13, from edge profiles and grid images)
- Pedestal: top edge at y = 1026 (±1). Front-face right edge at x ≈ 954 (y = 1100) to 941 (y = 2500), with a thin side face out to
  x ≈ 1000. It is cut by the left and bottom image borders, so its full width and height are not visible
  (visible height is 1534 px).
- Bottle: body x 703–1072 (width ≈ 369 px), base y ≈ 1025–1048, neck top y ≈ 395, height of the glass body ≈ 653 px.
  With the white dropper cap the total height is ≈ 943 px (top of cap y ≈ 105). Amber liquid bbox: x 720–1071, y 645–1044.
  Edges are frosted and soft (±5 px).
- Dropper: white cap/bulb bbox x 665–1000, y 105–385. The glass tube runs down-right at about 37° to a tip ring
  centred at (1172, 510), outer diameter about 52 px (±5–10 px, transparent glass).

## Ambiguities
- "Drop size" could mean height (86 px, vertical) or width (57 px). The drop is a teardrop, not a sphere.
- The drop's Blender origin may not be exactly at the bbox centre. The track gives the bbox centre, and its mask
  centroid sits close to that. A constant offset does not change displacements or speeds.
- The render has grain noise, there is a vignette, and the transparent drop shows highlights and refraction. The drop has no shadow. Motion blur is minimal.
- The camera looks slightly upward, but the scene is labelled 2D. Use one px→m scale from the question's prior.

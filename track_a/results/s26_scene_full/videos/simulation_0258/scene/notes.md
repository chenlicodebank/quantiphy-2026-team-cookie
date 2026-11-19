# simulation_0258 — measurement record

2D simulation (Blender), 24 fps, 40 frames (0–39, 1.667 s), 1920×1080. **The camera is static.** Outside the pen's columns, the mean absolute difference from frame 0 is ≤ 0.85 grey levels in every frame, which is codec noise; a shift would give much larger values on the textured wall (`scripts/check.py`).
Scene: a front-on view of a blue textured wall. In the lower left is a white LG air-conditioner outdoor unit. A long dark-wood table with a black metal frame stands in front of the wall. On the table, from left to right: a flat dark phone or wallet, the pen's landing spot, a white cup with a succulent, and a black remote or phone. A white window frame is on the right. The **only moving object is a black/silver pen**, held horizontally. It falls straight down from above the frame, hits the table top, makes one small bounce and rests.

## Files
- `scene.json`: inventory with static-object pixel extents, key pen positions, events and camera.
- `tracks/pen.csv`: pen per frame for frames 3–39. Columns:
  - `cx, cy`: reference point = pen centre (bbox centre; y points down).
  - bbox: `bbox_x0, bbox_y0, bbox_x1, bbox_y1` (exclusive).
  - sizes: `length_px` (horizontal extent along the pen axis) and `height_px` (thickness).
  - `tilt_deg`: PCA angle of the mask.
  - `cx_mask_centroid, cy_mask_centroid`: pixel-mass centroid. It is biased by the clip and tip.
  - `cy_template_check`: an independent template-match centre for frames 16–39.
  - `method`, `occluded` (always 0), `phase` (falling / bouncing / rest).
- `scripts/`:
  - `diff.py`: first survey.
  - `track_pen.py`: mask tracking.
  - `rest_template.py`: template matching.
  - `build_track.py`: builds the final csv.
  - `static_edges.py`: static edge profiles.
  - `crops.py`: viewer.

## How the pen was measured
- **Frames 3–20:** the pen mask is |frame − frame 0| > 20, inside the columns x 970–1080 (the pen is not in view in frame 0).
  - Rows are kept only if they have ≥ 15 changed pixels. This removes the short vertical reflection streaks of the pen on the glossy table top.
  - The overlays were checked visually: the mask covers the whole pen, tip to end.
- **Frames 21–39 (at rest):** the contact shadow and reflections merge with the mask, so the pen is located by template matching instead.
  - The template is the pen patch from frame 20; its centre equals the frame-20 mask bbox centre, so the convention is the same.
  - The match is sub-pixel (parabola peak) with score ≈ 0.91.
  - In frames 16–20 the template and mask centres agree within 0.5–0.9 px.
- **No motion blur:** the pen is drawn sharp even at ~107 px/frame.
- **Pen size:** length is 64–66 px (mean ≈ 65.3) and thickness is 5–8 px (≈ 6).
  - The pen stays within ~1–2° of horizontal and rotates by ~2° during the bounce.
  - So pen length ≈ its horizontal bbox width, and its height in a world AABB sense ≈ its thickness.
- **Horizontal position:** cx stays at 1025.0–1026.0 the whole time (jitter ±0.5 px from 1-px bbox quantisation), so the motion is purely vertical.
- **Accuracy of cy:** about ±0.5 px. One-frame differences of cy are the pixel speed (y down); for example frame 14→15 = 100 px/frame.

## Key pen positions (px, y down)
| frame | cy |
|---|---|
| 3 | 7.5 (first fully visible) |
| 15 | 757.0 (last free-fall frame) |
| 16 | 864.5 |
| 17 | 863.0 |
| 18 | 855.5 |
| 19 | 856.0 |
| 20 | 863.0 |
| 21–39 | 866.62 (rest) |

The vertical drop from frame 3 to rest is ≈ 859 px.

## Events
- **Release:** about frame 0 (t = 0), above the image.
  - The vertical pixel velocity grows by ≈ 6.9 px/frame² and extrapolates to zero at frame ≈ −0.1.
  - Frames 0–2 show no pen.
- **First enters view:** frame 3 (t = 0.125 s).
- **First impact:** between frames 15 and 16. Extrapolating the fall, the pen reaches rest height at ≈ frame 16.0 (t ≈ 0.667 s). At frame 16 the pen is already 2–3 px above the rest height, rebounding.
- **Bounce apex:** frames 18–19 (≈ 11 px above rest).
- **Second impact and settling:** between frames 20 and 21. The pen is motionless from frame 21 (t = 0.875 s) to the end.

## Static objects (frame 39; px, ±3 unless noted)
- **Table:**
  - Top front edge spans x 518–1539 (≈ 1021 px long).
  - Back edge of the top surface (meets the wall) at y ≈ 865; front edge y ≈ 895; front band to y ≈ 912; apron to ≈ 928.
  - The legs run past the image bottom.
- **AC unit:**
  - x 132–638 (506 px wide), top y 758; the bottom is cut off.
  - Fan grille x 150–402, y 786–1065.
- **Cup with plant:** x 1084–1130 (46 px wide), leaves top ≈ 810, cup rim ≈ 832, bottom ≈ 871.
- **Left flat phone/wallet:** x 901–969 (68 px), y 861–870.
- **Right black remote/phone:** x 1141–1191 (50 px), y 865–871.
- **Window frame:** x ≈ 1625–1755, y 0–840 (rough).
- The table-item extents are visual estimates from a 4× crop.

## Ambiguities and reliability
- **Scale:** use one metres-per-pixel scale (2D). The pen is the natural prior object (65 px long, ≈ 6 px thick). If an answer uses a pixel speed or acceleration prior, use the cy differences.
- **Bounce timing:** the impact falls between frames, so impact timing is only good to about ±0.5 frame.
- **Rest frames:** the reflections and contact shadow under the resting pen are not part of the pen. The rest-frame bbox is the template box (65 × 6 px).
- **Similar object:** the left phone/wallet is also dark and flat. Don't confuse it with the pen.
- **Depth:** the pen lands near the back of the table top, about the same depth as the cup and the other items.

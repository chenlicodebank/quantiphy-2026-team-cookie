# simulation_0027 — measurement record

Video: Blender render, 3D scene, 960x960, 25 fps, 75 frames (t = frame/25, frames 0–74, last frame t = 2.96 s).
All values are in **pixels and seconds**. I assumed no metric scale.

## Scene
A high aerial oblique view of a beach. A large pale rock outcrop with brown cliffs sits at the upper right,
pink-beige sand covers the upper half of the frame, and green-blue rippling sea fills the lower ~40%.
**One person** walks on the sand near the image centre (≈ x 400–450, y 335–445). The person is the only moving
object. No vehicles, animals, balls or other props are present. The camera is **static**: phase correlation
of the rock/sand area against frame 0 gives |shift| < 0.025 px in every frame (`scripts/cam_check.py`).
No horizon, vanishing lines or straight edges are visible, so the camera geometry must come from
depth_info plus a known size.

## Files
- `scene.json`: inventory (person, person_shadow, rock_outcrop, beach_sand, sea_water), camera, events,
  perspective notes, and a summary of the person's motion and apparent size.
- `tracks/person.csv`: one row per frame, 0–74. Columns:
  - `pelvis_x, pelvis_y`: the **reference point** (estimated pelvis/hip, which is the simulation origin for a human).
    `pelvis_y = feet_y − 0.53·(feet_y − head_top_est_y)`. `pelvis_x` is the mean mask x within ±3 rows of the
    hip row. At frame 40 this lands on the shirt/trouser boundary, which I checked visually.
  - `centroid_x, centroid_y`: centroid of the body mask (clothing pixels).
  - `feet_x, feet_y`: lowest point of the legs/shoes (ground contact). It steps with the gait.
  - `head_top_y`: raw head detection, which is noisy. `shoulder_top_y`: top of the white shirt (crisp, monotonic).
    `head_top_est_y = shoulder_top_y − 9` (9 px is the median head offset over 57 frames where the head was found).
  - `bbox_x0, bbox_y0, bbox_x1, bbox_y1`: bounding box (bbox_y0 is the raw head top). `height_px` is the raw
    feet−head_top+1. **`height_est_px`** (feet − head_top_est + 1) is the preferred apparent height.
    `shoulder_to_feet_px`, `width_px` (full mask width including the swinging arms/legs), `shoulder_width_px`
    (median row width just below the shoulders), `area_px` and `occluded` (always 0) complete the columns.
- `scripts/`: `cam_check.py` (camera shift), `seg_person.py` (segmentation and track), `head_probe.py`,
  `color_probe.py` (diagnostics), `static_objects.py` (rock and shoreline, output in `static_out.json`),
  `draw_track.py` (overlay) and `summary_check.py` (trend statistics).
- Overlays are in `../frames/masks/mNN.png` (every 8th frame) and `../frames/track74.png`. They are outside `scene/`.

## How the person was measured
- The background is a per-pixel temporal median (the camera is static).
- Clothing is colour-neutral (B−R > −24), while the sand **and the cast shadow** keep the sand hue (B−R ≈ −37).
  The body mask is therefore neutral pixels that differ from the background, so the shadow is excluded.
- The shoes and lower legs are dark and sand-hued, so I extended the mask downward inside the body column.
- The head is skin-coloured and nearly invisible on the sand. Only a faint smudge about 7–10 px above the
  shirt shows, which is why the head top is estimated with a fixed offset.

## Results (pixels)
- **Pelvis**: (407.4, 363.2) at frame 0 → (442.1, 410.6) at frame 74. Net image displacement is (34.7, 47.4),
  about 58.8 px.
  - The person walks steadily **down-right** in the image (toward the sea / bottom of the frame) in a roughly
    straight line, without stopping.
  - A linear fit gives about 0.46 px/frame in x and 0.63 px/frame in y.
  - The shoulder top moves 0.64 px/frame in y.
  - The summed frame-to-frame pelvis path is 70 px, which is **inflated by ±1 px jitter**. For path length,
    smooth the track first or use a line fit.
- **Apparent height**: `height_est_px` median 61 px (range 58–64, gait jitter ±2). Shoulder-to-feet median is 52 px.
  - The first and last 10 frames average 61.6 and 60.0 px. This slight decrease (≈ −2 px over the clip) is near
    the noise level, so the camera distance changes only a little.
  - Width: full mask about 16 px; shoulders about 13–14 px.
- **Gait**: feet_y plateaus (stance phases) at y 403–404 (frames 9–17), 414–415 (25–36), 424–425 (44–53) and 436 (61–70).
  The steps fall at about frames 2–3, 8–9, 20–25, 36–38, 55–57 and 72–74, roughly one step every 16–18 frames.
- **Events**: walking throughout. The person is already moving at frame 0 and still moving at frame 74. There are
  no impacts, contacts, releases or direction changes.

## Static objects (frame 0; visual grid reading, ±10 px)
- **Rock outcrop**: bbox about x 325–955, y 25–310, so about 630 px wide and 285 px tall in the image.
  - Left tip at about (325,160), top at about (510,25), cliff base at y ≈ 300–310 for x 600–760.
  - Its main axis is roughly horizontal, tilted ~10° down to the right.
  - The automatic mask in `static_objects.py` was poor. I recorded the visual extents instead.
- **Edge of the pale sand terrace**: y ≈ 450 at x 0, ≈ 500 at x 150, lowest ≈ 530 for x 350–520, ≈ 495 at x 650,
  ≈ 455 at x 780, ≈ 370 at x 850, ≈ 320 at x 890.
- **Solid green water** begins further down, at y ≈ 580–660 for x 0–720 (`static_out.json`). The band between
  the two is translucent shallow water.

## Reliability and ambiguities
- **Pelvis track**: ±1–2 px per frame. The pelvis position is a stature-ratio estimate, not a joint detection.
  Expect a systematic offset of a few px and step-synchronous wobble, because pelvis_y follows the plateaus in feet_y.
  For speeds, consider `shoulder_top_y` or `centroid` as smoother alternatives, or smooth over a stride
  (~16–18 frames).
- **Height**: ±3 px, because of the invisible head. The 9 px head offset is itself uncertain by ±2 px.
- **Feet**: ±2–3 px. At frames 73–74 the mask may include the start of the shadow (feet_y 441–444 vs 438 at frame 72).
- **Shadow**: the long dark streak to the upper right of the feet (≈ 75 px, direction (0.90, −0.44)) is a shadow,
  not an object. It is excluded from every person measurement.
- **Occlusion and blur**: none. The person is small (~61 × 16 px), so pixel quantisation dominates the errors.
- **Depth**: the view is steep and oblique, so moving down the image probably means moving nearer the camera's
  ground footprint. Without the camera pose, the depth change cannot be signed from the image alone.
  Use depth_info if it is given.

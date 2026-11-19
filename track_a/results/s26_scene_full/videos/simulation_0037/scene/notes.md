# simulation_0037 — measurement record (pixels, seconds)

Video: 3D Blender render, 1080x1080, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).
Scene: a beach. One person walks left→right along the wet sand edge in the middle distance; a large pale
rock/sand block fills the left half; ochre dunes on the horizon; sea behind the person and in the lower half of
the frame; cloudy sky. **The only moving object is the human** (water ripples aside).

## Files
- `scene.json` — inventory, static extents, camera, events, summary of the human track.
- `tracks/human.csv` — one row per frame 0–71: `pelvis_x, pelvis_y` (reference point = estimated pelvis),
  `cx_mask, cy_mask` (mask centroid), `bbox_cx`, `foot_y` (= y1, lowest foot pixel), bbox `x0 y0 x1 y1`,
  `height_px` (y1−y0+1, head top to sole), `width_px` (x1−x0+1, horizontal extent = stride width along the
  motion direction), `area` (mask px), `occluded` (always 0).
- `scripts/` — `track_human2.py` (final track + overlay), `track_human.py` (first pass), `inspect_feet.py`,
  `camera_check.py`, `write_scene.py`.

## How measured
- Mask: |frame − temporal median| in crop x700–1000, y640–790, threshold 30 (sum RGB), morphology, largest
  blob + adjacent limb blobs. The wet sand mirrors the person (pinkish reflection ~10 px below the feet); it is cut
  off at the lowest mask row containing dark (jeans/shoe) pixels. Overlays (frames/overlay2.png) checked at
  13 frames: mask covers head to feet, swinging arms and legs, no reflection.
- Pelvis: x = mask-centroid x of the 7 rows around the hip; y = top + 0.47·height (anthropometric guess,
  hip ≈ 53 % of stature above the soles). The pelvis is not directly visible; treat pelvis_y as ±3 px.
- Camera: static (phase correlation on rock and dunes, max shift < 0.02 px). No background correction needed.

## Key numbers
- Human pelvis: (798.8, 713.7) at frame 0 → (920.4, 721.7) at frame 71; net +121.6 px in x, +8 px in y
  (≈1.71 px/frame, nearly constant with small per-step pulsing). Summed per-frame pelvis path = 132 px; this
  is inflated by ±1 px per-frame jitter — for path length prefer a smoothed track (≈ net displacement, since
  the walk is straight).
- Height in pixels (head top to sole, while walking): median 57, min 54, max 62 (single-frame extremes are
  partly mask noise; typical 55–59). First-10-frame mean 57.5, last-10 mean 57.1 → apparent size essentially
  constant: the walk is roughly parallel to the image plane (foot line drifts down 744→752 px, so possibly very
  slightly toward the camera). Bbox width (stride) 14–35 px, median 24.
- The head is a pale blurred/pixelated blob and shoes are light-coloured; top/bottom edges uncertain ±2 px.
- Static: pale rock block bbox x15–715, y595–735 (≈700 px long, its sloping top falls from y≈595 at left to
  ≈715 at the right end); far dunes y≈580–680 across the frame; approximate horizon (sea meets dune bases)
  y≈678, level; sand strip under the person y≈740–775.
- 3D cues: horizon ~y 678, person's feet ~y 744–752, i.e. feet ~70 px below the horizon while the person is
  ~57 px tall → camera height ≈ 1.2× the person's height (rough, since true horizon is hidden by dunes).
  Focal length unknown: with a given depth d to the pelvis and a known height H, f ≈ height_px·d/H.

## Events
- Human walks for the whole clip (already moving at frame 0, still moving at frame 71); constant direction
  (+x, image right); no contacts, impacts or stops. No other objects move.

## Reliability / ambiguity
- Tracks: good (±1 px in x per frame; ±2–3 px for top/foot/pelvis y). Person is small (~57 px tall), so
  relative errors in height ~±4 %.
- Reflection of the person in the wet sand and the faint face could confuse a naive mask; handled as above.
- Only one person; no similar objects to confuse.

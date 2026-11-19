# simulation_0215 — measurement record

Simulation (Blender), **2D** scene, 24 fps, 50 frames (t = 0 … 2.0417 s), 1920×1080. Everything is in pixels
(x right, y down, full resolution) and seconds (t = frame/24). No metric scale was assumed.

## Scene
A static camera looks straight down on a living-room floor (plan view). The only moving object is a **black dog**
that walks to the right (+x) along y ≈ 359 for the whole clip, between the bench/TV console (above) and the
round rug/curved sofa (below). Static props: wooden slatted bench (top-left), dark TV console with a white vase
(left end) and a white pleated lamp shade (right end), round fluffy rug (left), large curved cream sofa with two
grey pillows (bottom centre), and a light panel/door at the top-right.

## Files
- `scene.json`: inventory, camera, events, dog motion and size summary, static-object pixel boxes and sizes.
- `tracks/dog.csv`: one row per frame (0–49). Columns:
  - `torso_cx, torso_cy`: centroid of the dog mask with the thin tail removed (morphological opening, 15 px disc).
    **Recommended reference point** (proxy for the rig origin / body centre).
  - `torso_bbox_cx/cy`: centre of the tail-less box; `mask_cx/cy`: centroid of the whole mask including the tail.
  - `bbox_x0..y1`: full mask box (nose to tail tip); `torso_x0..y1`: tail-less box; `nose_x`: front-most pixel.
  - `length_full_px` (nose to tail tip along the body axis), `length_torso_px` (nose to rump), `width_torso_px`
    (body width across the axis), `axis_angle_deg` (≈0, horizontal), `area_px`.
  - `head_render_grey` = 1 in frames 45–49 (see below); `occluded` = 0 always.
- `scripts/`: `track_dog.py` (segmentation and track, writes the CSV), `summarize.py` (statistics and camera check),
  `static_probe.py`, `static_profiles.py`, `static_profiles2.py` (static edges), `draw_static.py`, `view.py`,
  `probe*.py` (pixel probes) and `bg_strip.png` (median background of the dog strip, used during probing).

## Method
The dog mask is pixels with grey < 45 (the dog is near-black) inside the strip y 300–430, taking the largest
component, then close and fill holes. I drew the masks on frames 0, 12, 24, 36, 44, 45, 46 and 49 and checked them
by eye: they cover the whole dog (head, body, legs, tail) and leave out its soft shadow.
**Render artefact:** from frame 45 on the head is drawn as a flat grey disc instead of black. In those frames the
disc (low-chroma grey pixels just in front of the black body, within the body's rows) is added to the mask, and
the check overlays show that it is captured. The nose position stays continuous: about 11 px per frame right
through the change.

## Key numbers (px)
- Motion: steady to the right. Torso centroid moves from (566.6, 359.2) at f0 to (1110.1, 358.0) at f49, a net
  change of +543.5 px. A linear fit gives x = 569.0 + 10.99·frame, and the quadratic term (0.0006) shows no
  measurable acceleration. Per-frame dx of `torso_cx` has mean 11.09 and std 1.34 (gait jitter). `nose_x` and
  `mask_cx` are steadier (mean 11.02, std 0.55 and 0.79). y wobbles only between 357.5 and 361.2.
- Size: nose to tail tip is 191 px (median; range 183–200, depending on tail pose). Nose to rump is 155 px (median;
  151–180, where the larger values in f18–20 and f36–39 come from stretched hind legs). Body width is 40 px
  (39–42). Height cannot be seen from a top view. The apparent size is constant because the dog stays at one depth.
- Camera: static (mean frame-to-frame difference outside the dog strip ≤ 0.76 grey levels).
- Events: the dog is already walking at f0 and keeps walking to f49. There is no start, stop, turn or contact.
  The head turns grey at f45 (artefact only).

## Reliability and ambiguities
- Dog track: centroids are good to about ±1 px. Gait makes the tail-less centroid jitter by ±2–3 px per frame, so
  for speeds use differences over several frames or `nose_x`/`mask_cx`. The exact Blender origin of the dog rig is
  unknown. All the candidate points move together at about 11.0 px/frame, so the choice changes positions by a
  constant offset but does not change speeds.
- Dog "length" for a scale prior: the world bounding box most likely includes the tail. That length is about 191 px
  (x-extent of the full mask). Without the tail it is about 155 px. If the prior is the dog's width, use about 40 px.
- Static objects come from colour or brightness profiles at frame 49, plus visual estimates where noted in
  scene.json. The bench is accurate to ±2 px; the vase, lamp, sofa and rug to ±3–8 px. The console's top edge
  merges with the wall shadow, and its right end is hidden under the lamp. Pillow and door boxes are visual (±8 px).
  Tall objects (lamp, console) sit slightly above the floor, so they are a little closer to the camera, which has a
  perspective lens (the wall faces show at the image borders). Their pixel sizes may therefore be a few percent
  larger than an object of the same size on the floor.
- There is only one moving object and nothing similar to confuse it with. The dark soft shadow above the dog is not
  part of the mask.

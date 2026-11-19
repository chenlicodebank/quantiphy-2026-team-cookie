# internet_0037 — measurement record

**Scene:** a real drone video shot straight down at a pool with teal mosaic tiles. One woman swims breaststroke from left to right (+x) across the frame for the whole clip. Facts: 164 frames, 22.521385 fps, 3840x2160. All values are in full-resolution pixels. Time is t = frame / fps. No metric scale is assumed.

## Files
- `scene.json`: inventory (the swimmer plus static objects), pixel sizes, camera summary, perspective and events.
- `tracks/swimmer.csv`: one row per frame, 0–163. The swimmer is visible in every frame.
  - `ref_x, ref_y`: centroid of the visible body mask (skin + dark hair/suit + grey face blur patch). This is the default reference point ("visible centre").
  - `trunk_x, trunk_y`: centroid of the mask after a 15x15 erosion at half resolution, which removes the thin arms and legs. This is roughly the torso/hips.
  - `head_hair_x, head_hair_y`: centroid of the dark hair blob, i.e. the head. `head_hair_interp = 1` marks frames where the hair was not detected (f35 and f69–72). The `*_camcomp` versions of the head columns are linearly interpolated over those frames.
  - `bbox_*`: axis-aligned box of the mask. `mask_len_main_axis` / `mask_width_across` are the extents along and across the mask's principal axis (`main_axis_deg`, 0 = +x).
  - `toe_x` (= bbox_x0, the trailing feet), `head_front_x` (front edge of the hair), and `head_to_toe_len_x` = head_front_x − toe_x.
  - `cam_dx_smooth, cam_dy_smooth`: camera drift relative to frame 0, smoothed. Columns ending `*_camcomp` are positions with that drift subtracted (frame-0 image coordinates).
  - `occluded = 1` in every frame, because the body is always partly under water or in splash (see ambiguities).
- `tracks/camera.csv`: raw per-frame camera measurements.
  - `cam_dx` comes from cross-correlating the deck tile-joint brightness profile against frame 0.
  - `wall_edge_y` / `cam_dy` come from the pool wall edge.
  - `light_right_x/y` is the centroid of the right floor light, as an independent check.
- `scripts/`: every script used. `camera.py` → `swimmer.py` (writes `_swimmer_raw.csv`) → `finalize.py` (writes `swimmer.csv` and events). `static.py` measures the static features, and `landmarks.py` / `cam_shift.py` were earlier camera trials. `probe.py`, `compare_view.py` and `draw_tracks.py` were used for checks.

## How measured, reliability
- **Camera:** a hovering drone, nearly static. There is no rotation or zoom: deck joints stay about 134 px apart and the wall edge stays horizontal.
  - Slow drift: dx rises to about +10…+17 px (f30–f90) and falls back to about −4 px at f163. dy rises to about +16 px (f100–f140) and is +11 px at f163.
  - Raw dx is noisy, about ±3 px per frame, because wet reflections cross the deck. The smoothed values are good to about ±3 px.
  - The drift is about 1.5% of the swimmer's travel (~1180 px). Use the `*_camcomp` columns for motion.
- **Swimmer mask:**
  - Method: warm skin pixels (R > max(G,B)+12) at half resolution, plus nearby dark hair/suit and the grey blur patch, all closed morphologically.
  - Visual checks on overlays at f0, 30, 60, 80, 120, 140, 150: the mask covers the arms, torso and legs well. Submerged parts of the legs and sometimes a hand are under-segmented, so extents can be short by about 20–50 px.
  - The mask centroid jitters about ±15–30 px with the stroke, because arm and leg positions shift it.
  - The head (hair) centroid is the steadiest marker, except around f66–f87, where the blur patch and splash partly hide the hair (a few outliers, gaps at f35 and f69–72).
- **Body length (head top to toes, along x):**
  - Over all frames: median 658 px (p10 588, p90 710). It is shorter during the kick because the legs bend.
  - Stretched glide frames: about 690–730 px. Checked by eye at f123: toes x≈1715, top of head x≈2445, so ≈730 px.
  - Fingertip to toe with arms forward: about 930–970 px (f29, f82, f123).
  - Body width with arms swept out: up to about 700 px (f0, f43).
  - These are probably the values a "swimmer height/length" prior refers to. Measure the prior the way the question words it, e.g. the body length in a glide frame (~700–730 px).
- **Motion summary:**
  - Net displacement f0→f163 (camera-compensated) is about +1180–1190 px in x and about +65 px in y.
  - The swimmer moves at a steady average of about 7.3 px/frame, with a surge inside each stroke.
  - Breaststroke cycle is about 46–48 frames (≈2.1 s): arms swept wide at f0, 43, 95, 138; glide with arms forward at f29, 82, 123, 162.
  - The swimmer is already moving at frame 0 and still moving at frame 163. There is no wall contact or turn.
- **Static features (frame 0):**
  - Pool wall/deck edge: y = 186.9.
  - Deck tile joints: 28 joints, x = 163…3779, mean spacing 133.9 px.
  - Round floor lights (pale cyan, ~50–55 px across): far-left (355,1165), middle (1845,1178), right (2909,1183).
  - Dark shaded band along the bottom from y ≈ 1880. The opposite wall/coping is at y ≈ 2090.
  - Pool width visible, edge to edge: about 1900 px. Uncertain, because the bottom edge is in shadow with sun glints.
  - The floor lights and tiles sit on the pool bottom and are seen through rippling water, which refracts them (positions wobble ±10 px). They are also deeper than the swimmer, so their pixel scale is not the swimmer's.

## Ambiguities
- **Privacy blur:** a grey, flat-coloured patch covers the face and sometimes extends forward over the water or over an arm (e.g. f80, f140). It is not a real object. Do not use it for the head-front position; use the hair edge instead.
- **Splash and glints:**
  - White splash appears behind the feet in every frame.
  - Strong sun glints sit at the bottom (x 2100–3000, y > 1600).
  - A bright blob at about (790,1160) in late frames may be splash or another fixture.
- **Single person, no other moving objects.** Water ripples and caustics move but are not objects.
- **Scale under the internet convention:** use a single scale (prior value / prior pixel value) applied to these pixel tracks, with the planar view assumed.

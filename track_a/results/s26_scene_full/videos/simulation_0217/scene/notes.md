# simulation_0217 — measurement record (pixels, seconds)

**Scene.** A 2D Blender render, 50 frames at 24 fps (t = frame/24, frames 0–49), 1920×1080. The camera looks straight
down on a living room and does not move: phase-correlation shift is under 0.04 px in every frame. Two animals walk on
the grey carpet along straight horizontal lines in opposite directions:
- **black_animal** is a small, all-black quadruped (cat or small dog) with a long thin tail. It walks on the upper
  line (y ≈ 360) from left to right (+x).
- **tan_animal** is a larger tan/brindle quadruped with its tail raised. It walks on the lower line (y ≈ 447, just
  above the sofa) from right to left (−x). Its head renders as a flat, untextured grey-brown patch at the front end.
  This is a render artefact, but the patch is part of the animal.

Neither animal is occluded at any time and they never touch. Their x positions cross between frames 32 and 33.
The other objects are static: bench, console table with vase and lamp, an A-frame shelf at the top right, a round
shaggy rug, a curved sofa with two pillows, and the room walls/floor.

## Files
- `scene.json` — inventory, camera, static extents, events, and summary extents/paths.
- `tracks/black_animal.csv`, `tracks/tan_animal.csv` (fur + head patch), `tracks/tan_animal_fur_only.csv` — one row per frame 0–49.
  Columns:
  - `ref_x, ref_y`: the reference point.
    - black_animal: centroid of the whole mask.
    - tan_animal: torso centroid (mask opened with a 21 px disk, which removes the tail and legs).
  - `mask_cx, cy`: centroid of the full mask.
  - `bbox_*`: bounding box of the full mask, including the tail.
  - `mask_area_px`: mask area.
  - `length_main_axis_px / width_across_px / main_axis_deg`: PCA extents of the full mask.
  - `body_*`: centroid, length, width and bbox of the tail-less "body" mask.
  - `occluded` (always 0), `visible` (always 1).
- `scripts/` holds the measurement scripts:
  - `segment.py` builds the masks and writes `masks.npz` (packed bits, crop offset x 350, y 250).
  - `tracks.py` writes the CSVs and the overlay PNGs.
  - `static.py`, `events.py`, `bg.py` (camera-shift check; its background model was abandoned), `probe.py`, `sizes.py`, `cleanup.py`.

## Method and reliability
- **Lighting.** The sun patches and window-bar shadows on the floor change shape and brightness over the clip, so
  background subtraction failed. Segmentation is colour-based instead.
- **black_animal mask.** Pixels with max(B,G,R) < 60, largest component. The mask is very clean (checked on overlays
  of frames 0, 12, 24, 36, 45 and 49).
  - Its front edge (`bbox_x1`) advances a steady 10–12 px/frame: 647 → 1185, i.e. 10.98 px/frame on average.
  - The centroid steps have more jitter (8.5–12.8 px) because the tail moves.
  - Length including the tail is 184–200 px (mean about 190). Body without the tail is about 152 px. Width is about 38 px.
  - The tail sometimes lifts, which widens the bbox to about 50 px.
- **tan_animal fur mask.** HSV with S > 105 and hue 5–25. It is clean, but it misses the head patch and the white tail tip.
  - Torso length without the head is about 238 px (214–270). Width is about 96 px.
- **tan_animal full mask.** The fur mask plus the head patch, found by colour (R−B > 24, B < 72) near the fur. It is
  approximate: in some frames it bleeds 10–30 px into the darker floor/contact shadow around the head and back.
  - Nose-to-rump length is about 265 px (251–300).
  - A manual check at frame 0 gives patch front x ≈ 1085, fur front ≈ 1122 and rump ≈ 1347, so nose-to-rump is about 262 px.
- **tan_animal motion.** Torso-centroid steps are noisy (±3 px per frame) because of the gait.
  - Frames 0–6: slow (2–5 px/frame).
  - Frames 15–36: cruising at about 12–14 px/frame.
  - From frame 37: decelerating.
  - Frames 46–49: almost stopped, with x between 781 and 785.
  - Net displacement: black +535 px in x, tan −456 px in x. Vertical drift is about 0 for both.
- **Reference point and the rig origin.** The true rig origin (pelvis/root) of the animals is unknown. The centroids
  are proxies; a fixed offset along the body does not affect displacements or speeds.
- **Static props.** Extents were read from a 25 px grid (±3 px). Lamp and vase were measured by threshold. The right
  end of the console is hidden under the lamp, so its length is uncertain (±20 px).
- **Height.** Not measurable in this top-down view. Lengths and widths are horizontal floor-plane extents only.
- **Scale.** In 2D, use one px→m scale from the prior's object, measured the same way the prior defines it (for
  example body length, or front-edge pixel speed).

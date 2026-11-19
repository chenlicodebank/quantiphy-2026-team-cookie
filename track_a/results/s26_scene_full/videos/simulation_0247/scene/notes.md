# simulation_0247 — measurement record (pixels, seconds)

Video: 1920x1080, 30 fps, 75 frames (t = frame/30, 0 to 2.467 s). Source is a simulation, labelled 2D. Camera is **static**:
empty floor and backdrop pixels stay the same across all frames (to within 1–2 grey levels, which is the spotlight's soft
falloff). So there's no background shift to correct for.

## Scene
- Studio cyclorama: a beige floor that curves up into a darker backdrop. There's a spotlight pool on the floor around
  (900, 950). No horizon, markings or furniture.
- **creature**: a large fantasy quadruped. It has a horse/antelope-like body, orange-brown with dark spots, a white neck
  ruff, two long striped horns that curve back over its body, and a long tail ending in a tuft. It walks steadily
  left to right through the whole clip (it's already moving at frame 0 and still moving at frame 74). Its
  mask centroid goes from x 709.6 to 1287.1 (about 7.7–7.8 px/frame). The centroid's y stays at about 567–574 because
  the walk makes it bob slightly. Feet are at y ≈ 795–800.
- **rabbit**: a small orange rabbit facing right, just ahead of the creature's front hooves. It hops right at roughly the
  same mean pace (centroid x 975.3 to 1544.5, 7.69 px/frame). One hop cycle takes about 13 frames (0.43 s).
  Per-frame dx ranges from 4 to 12 px: fast phases are near frames 7, 20, 32, 45, 58 and 71, slow phases near
  2, 14, 28, 38, 54 and 67. Its centroid y stays at 768–773 and the bottom of its feet at y 793–803, so it barely leaves
  the floor.
- Both animals stay visible in every frame and neither is ever hidden behind the other. The creature's head
  passes above the rabbit late in the clip, but they never touch (see pair_gap.csv; the negative bbox gaps late in the
  clip come from the ear/horn tip overhanging the rabbit).
- Shadows: the creature casts soft shadows on the floor and backdrop. They're excluded from the masks.
- Both heads have a pale, semi-transparent disc that looks like a render artifact (creature: near (910, 525) at
  frame 0; rabbit: just in front of its face). It's excluded from the masks.

## Files
- `scene.json`: inventory, camera, landmarks, events and summary numbers.
- `tracks/creature_mask.csv`, `tracks/rabbit_mask.csv`: one row per frame (0–74). Columns:
  - cx_mask, cy_mask: mask centroid, used as the **reference point** (the stand-in for the rig origin).
  - cx_trunk (creature only): centroid of the body barrel in rows y 600–650. It's noisier and given only as an alternative.
  - bbox centre, x0 y0 x1 y1, bbox_w, bbox_h.
  - len_major, wid_minor: PCA extents of the mask.
  - area_px, occluded (always 0).
- `tracks/pair_gap.csv`: per-frame centroid offset and distance from the rabbit to the creature, plus the horizontal gap
  (rabbit x0 minus creature x1).
- `scripts/`:
  - `bg.py`: builds a clean background plate at half resolution (composite, then median over foreground-free frames,
    then inpainting).
  - `segment.py`: segments each frame against that plate at full resolution and writes the tracks.
  - `events.py`: finds hop phases and writes pair_gap.csv.
  - `write_scene.py`: builds scene.json.
  - `torso_track.py`: a template-matching experiment that drifted and was rejected; its output was deleted.

## Sizes (px)
- Creature, overall bbox from tail tuft to head tip and from horn top to hoof:
  - Width: median 538 (range 496–580, changes with gait and tail swing).
  - Height: median 435 (range 427–439).
- Creature landmarks, read by eye at frame 37 (±5–10 px):
  - Heights above the ground (hooves at y ≈ 798): horn top 436, ear tip 343, back/withers about 230.
  - Body from rump (x≈820) to chest (x≈1140): about 320. Rump to nose: about 390.
- Rabbit:
  - bbox_w 66–104, median about 82 (it stretches during hops).
  - bbox_h 60–76, median about 70, including the ear.
  - Main-axis length median about 84.
- Which pixel size equals a world "length/height" depends on what the prior names. A full-body bbox includes the horns
  and the tail.

## Reliability
- Centroid positions are good to about 1–3 px per frame. Per-frame jitter comes from leg and tail swing and from mask edge
  noise. The creature's centroid is a proxy for its root/pelvis: it sits roughly mid-body (around y 570), while the true
  pelvis is probably near the rump (x about 100–150 px behind the centroid) at a similar height. Displacements are the
  same for any point on the trunk.
- Creature bbox: the top (horn) and bottom (hooves) are reliable to ±2 px. The left edge (motion-blurred, low-contrast
  tail tuft) is uncertain by about 15 px, for example the jump in x0 at frames 7→8. The right edge (ear tip) is
  reliable to ±3 px. Pale horn tips are low contrast against the backdrop and were recovered with hysteresis
  thresholding; a few pixels may be missing.
- Rabbit mask: the ear tip and face disc are partly missed, so height may be low by a few px.
- There's no metric scale here. Each question's prior should set px→m with one scale factor (2D video).

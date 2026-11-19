# simulation_0102 — measurement record (pixels, seconds)

2D Blender scene, 1920x1080, 24 fps, 73 frames (t = frame/24, 0 to 3.0 s). Static camera. The image is a split
view: the upper panel (y < 672.5) shows the sea surface from above water (grey sky, horizon at y ≈ 566). The lower
panel (y > 672.5) is a flat blue underwater view.

## Objects
- **boat**: red fishing boat (white wheelhouse, mast, rails, "AH805" on the bow). It is the only object in the upper
  panel. It moves right (+x) horizontally at a near-constant step of 17.88 ± 0.1 px/frame from frame 1→2 to the end.
  Between frames 0 and 1 it does not move. Its size is constant: bbox length stern→bow = 854 px (frame 0: x 232–1086).
  Cabin roof y 231, bow tip top y ≈ 352, keel bottom ≈ 645 (visual). The mask reaches y 672 because the submerged
  hull/reflection extends down to the panel edge. The mast always runs off the top of the frame, so the full height
  cannot be seen. Keel to cabin roof = 414 px. Fully visible frames 0–47. The bow crosses the right border at frame
  48, and about 420 px (the stern part) is still visible at frame 72.
- **shark**: grey shark with a white belly. It is the only object in the lower panel. It swims left (−x) at y ≈ 906.
  Its per-frame step grows steadily from ~7.5 px (frame 1→2) to ~16.7 px (frames 58–60) and ~17.7 px at the end.
  Length nose→tail tip 247.8 px, height incl. fins 101 px; its apparent size is constant. Fully visible frames 0–60.
  The nose reaches the left border at frame 60, and at frame 72 only a 44 px piece of the tail remains.
- Static: sea horizon y = 566, underwater panel top y = 672.5, water-surface band y 566–672. There are no other props.

## Files
- `scene.json`: inventory, sizes, static lines, events, camera, reliability.
- `tracks/boat.csv`, `tracks/shark.csv`: one row per frame (0–72) with frame, t_s, ref_x/ref_y (reference point),
  the sub-pixel edges (boat stern/bow, shark nose/tail), the mask bbox, the visible length/height, the full length,
  the mask area, and clipped/occluded flags.
- `scripts/`: `bg.py` stitches a clean background from frames 0 and 72 (the objects move in opposite directions).
  `track.py` / `edges.py` / `edges2.py` were exploratory. `build.py` makes the final tracks and overlays, and
  `static.py` measures the horizon/panel lines. `bg.png`, `raw.json`, `edges.json` and `summary.json` are
  intermediates.

## Method & reliability
- Masks come from background difference (max channel > 40 for the boat, > 60 for the shark), followed by a 5x5
  opening. I checked the overlays (`frames/ov/`): the contours fit the boat hull/cabin and the shark body. The thin
  wire and mast are partly dropped by the opening. The white rails are only partly in the mask, but the bbox extents
  are not affected.
- **Boat ref_x** = sub-pixel stern edge (mean over 11 clean rows) + 412.97 px, which is the bbox centre. It stays
  valid after the bow leaves the frame. Precision ~0.1 px/frame. The true Blender origin is unknown, but the boat is
  rigid and moves only horizontally, so any constant offset does not affect displacements. ref_y = 415.4 is a fixed
  nominal value; the boat has no vertical motion.
- **Shark ref_x** = mask centroid for frames 0–60. For frames 61–72 it is tail edge − 129.14 px (extrapolated, the
  value goes negative once the body is off-screen). The tail beats, so the per-frame steps jitter by ±1.5 px. Smooth
  over a few frames before differentiating.
- The template-matching displacements in `raw.json` (track.py) are biased; do not use them.
- Events: stationary f0→f1; motion starts at f2 (t 0.083 s); the horizontal ref positions of the boat and shark
  cross between f6 and f7; the boat bow reaches the right border at f48 (2.0 s); the shark nose reaches the left
  border at f60 (2.5 s).
- Ambiguities: the boat's submerged hull and reflection look alike (bottom 645 vs 672). The mast height is clipped.
  The boat and shark are in different panels and could be at different depths, but nothing in the image shows
  perspective, so a single scale from the prior object is the default.

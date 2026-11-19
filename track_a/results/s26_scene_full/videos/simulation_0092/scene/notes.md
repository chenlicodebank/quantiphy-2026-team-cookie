# simulation_0092 — measurement record (pixels, seconds)

2D Blender render, 1920x1080, 24 fps, 73 frames (t = frame/24). Flat uniform grey background (no ground, horizon,
markings or static objects). Camera static. Two moving objects, both side views moving right->left horizontally:

* **airliner** — large white Air China jet (red phoenix on tail), the upper object, nose left. Visible frames 0-45,
  fully in frame 12-30. Length nose-to-tail 857 px (frames 20-30) to 876 px (frame 12, right of image); bbox height
  (fin top to engine bottom) 255 px; fuselage diameter ~93 px. Ref y = 427. Nose moves 57.0 px/frame, constant.
* **car** — small white Cybertruck-like pickup, lower object, front left. Visible frames 0-70, fully in frame 3-65.
  Length 128 px (x~1000) to 137 px (image edges); height roof-to-wheel-bottom 43 px (body ~33 px). Ref y = 652.5.
  Moves 28.45 px/frame, constant (≈ half the airliner's pixel speed).

## Files
* `scene.json` — inventory, extents, events, camera notes.
* `tracks/airliner.csv`, `tracks/car.csv` — one row per visible frame: frame, time, ref_x/ref_y (origin estimate),
  ref_source, bbox (x0,y0,x1,y1, inclusive), length_px (bbox width = main axis), height_px, mask centroid, mask area,
  truncated_by_frame_edge (left/right/blank), occluded (always 0).
* `scripts/measure.py` — median background (every 4th frame) + |RGB diff| > 12 mask, 3x3 opening, components ≥30 px;
  airliner = rows < 590, car = rows ≥ 590. `scripts/finalize.py` — CSVs + overlays (`../frames/ov_*.png`).
  `scripts/check_steps.py` — per-frame steps; `scripts/sub_extents.py` — column-wise fuselage/car heights.

## How the reference point was set / reliability
* Origin = bbox centre when fully visible (Blender origin assumed at the bbox centre; not verifiable). Accuracy ±1 px.
* Frames cut by the image edge (airliner 0-11 and 31-45, car 0-2 and 66-70): ref_x = visible far edge ∓ (L−1)/2
  with L from the nearest fully visible frame. Good to a few px for entry frames (nose steps are an exact 57.0);
  for airliner frames 38-45 the tail tip's steps drop to 53-55 px (edge perspective), so those centres may be
  ~10-20 px off — prefer the constant 57.0 px/frame nose motion if needed. Airliner frame 45 shows only a sliver.
* Lengths vary a few % with image x because 3D end faces show off-axis (perspective of a 3D render, not a size
  change). For a size prior, the minimum (airliner 857, car 128, near the image centre) is the cleanest side-on value;
  the airliner's bbox-centre steps (56-59 px) inherit this length change, the nose edge (57.0) does not.
* Frames 0 and 1 are identical in object position (render start): motion begins at frame 1, so the backward-difference
  speed is 0 at frame 1 and the full step from frame 2 on. Thereafter both move at constant pixel speed (no
  acceleration, no direction change), no contact, no occlusion between them, no shadows, negligible motion blur.
* The two objects are likely at different depths (very different real sizes, similar pixel scale cues unknown); the
  2D convention uses one scale from the prior object. The airliner's dark-grey nose shading is faint (diff ~20) —
  threshold 12 captures it (an earlier threshold of 30 missed ~27 px of nose).

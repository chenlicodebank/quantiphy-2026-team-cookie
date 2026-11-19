# simulation_0099 — measurement record (2D simulation, 24 fps, 73 frames, 1920x1080)

All values are in pixels (x right, y down) and seconds (t = frame/24). No metric scale was assumed.

## Scene
A static side-view camera. The upper part shows a grey sky (gradient) and grey sea. The horizon is a straight horizontal
line at y=567, and the sea-surface band runs from y=567 to 673. Below that is a flat blue "underwater" band (y=674–1079).
- **boat**: a red/white fishing boat with hull number **AH805**, a white wheelhouse, a mast and stern railings. Its bow
  points right. It floats on the sea surface and moves **right**.
- **shark**: a grey shark with a white belly, swimming in the blue band with its nose pointing left. It moves **left**.
There are no other objects (no people or props). The two objects never overlap or occlude each other.

## Files
- `scene.json`: inventory, extents, events and camera.
- `tracks/boat.csv`, `tracks/shark.csv`: one row per frame (0–72). Columns:
  - `frame`, `time`
  - mask bbox `bbox_x0,y0,x1,y1`; `cx_bbox,cy_bbox`; mask centroid `cx_centroid,cy_centroid`
  - `width_x`, `height_y`; PCA `len_main_axis`, `width_across`, `axis_angle_deg`; `area`
  - edge-touch flags `touches_left/right/top` and `occluded_or_cut` (1 = the object is cut by the image border)
  - template shift `tpl_dx,tpl_dy`
  - **`ref_x, ref_y` = the recommended reference point** (estimated object centre)
  - boat only: the red hull band box `hull_red_*` and the stern mask edge `stern_x_rows480_540`
- `scripts/`:
  - `track.py`: background subtraction masks and tracks
  - `refine.py`: sub-pixel reference points
  - `edges.py`: cross-check of boat motion from the mast, rail post and stern edge
  - `analyze.py`, `static.py`: diagnostics and boundaries
  - `overlay*.py`: check images
  - `_mask_*.png`: the masks drawn on the check images
  - `_bg_small.npy`: thumbnail of the composed background

## Method
- **Camera**: static. In object-free regions, frame 0 and frame 72 differ by less than 0.6 grey levels on average, so the
  background shift is 0. The background was composed from frame 0 and frame 72 regions where no object is present.
- **Masks**: |frame − background| > 18, followed by a morphological opening. The boat mask is limited to y<674 and keeps
  all components of at least 300 px. The shark mask is limited to y≥674 and keeps the largest component. Overlays at
  frames 0/24/48/72 confirmed that the masks cover the full objects.
  - The boat mask **includes its water reflection down to y=673**. The real visible keel is at about y≈610: dark hull
    above, reddish reflection below.
  - The mast top is always cut by the top image edge (bbox_y0=0), so the boat's full height is not measurable. The
    visible height from the top edge to the keel (~610 px) is only a lower bound.
- **Reference points**:
  - Boat: x = 657.5 at frame 0 (midpoint of stern x=228 and bow tip x=1087) plus the sub-pixel shift of the thin stern
    rail post. This post stays in view in all frames.
  - Boat y is fixed at 488 (midpoint of hull top 367 and keel ~610). No vertical motion was found: the hull top edge
    stays at 367–368 px.
  - The boat's true Blender origin is invisible. The motion is pure translation, so displacements and speeds do not
    depend on which point is used. Only absolute boat–shark distances depend on the chosen ref_y. An alternative is the
    mask centroid y≈504, which includes the reflection.
  - A template on the glossy hull was **rejected**: it drifts to about 18.55 px/frame because reflections slide over
    the hull.
  - Shark: the frame-0 bbox centre (810.5, 904.0) plus the sub-pixel template shift of the shark's body.

## Results / reliability
- **Boat**:
  - At rest in frames 0–1, then a constant +17.88 px/frame (std 0.11 per frame). The mast (17.84), rail post (17.88)
    and stern edge (17.86) agree.
  - Overall length at frame 0 is 860 px (mask 228–1087; the stern edge at 50 % contrast is x=237, so the length is
    about 851–860 depending on the edge definition). The red hull band spans x 232–1087 and y 367–527.
  - The bow leaves the frame at frame 48, so length is only measurable in frames 0–47. The mast leaves at frames 68–69.
- **Shark**:
  - At rest in frames 0–1, then a constant −10.76 px/frame (std ~0.08). Its height stays at y≈905.4 ± 0.2.
  - Nose-to-tail length is 274 ± 2 px (frames 0–63). Height from dorsal-fin tip to pectoral-fin tip is 107 px.
  - The tail motion is very small; the length does not change measurably.
  - The nose is cut by the left edge from frame 64; after that the bbox length shrinks, but ref_x stays valid.
- **Events**: motion starts between frame 1 and 2 (t ≈ 0.04–0.08 s). There are no bounces, contacts or direction
  changes, and both objects are still moving at the end (frame 72).

## Ambiguities
- **Scale between objects**: in a 2D question, one scale comes from the prior's object. The boat and shark are in
  different layers (surface and underwater). Nothing in the image shows a depth difference, and the apparent sizes are
  constant.
- **Boat reflection and mast**: the reflection inflates the boat's bbox height (bottom at 673 instead of the keel at
  ~610). The mast is truncated.
- **Shark extents**: the shark's bbox includes its fins.

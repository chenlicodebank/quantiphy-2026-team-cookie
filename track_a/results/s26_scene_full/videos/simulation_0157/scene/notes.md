# simulation_0157 — measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 48 frames (t = frame/24, 0 … 1.958 s). Source: Blender simulation, 2D scene.
Underwater side view: blue water with light shafts, pale seabed dunes with moving teal caustics in the lower
quarter, and ONE moving object: a dark-blue sea turtle (head to the LEFT) swimming leftward at mid height.

## Files
- `scene.json` – inventory, camera, sizes, events (summary values).
- `tracks/turtle.csv` – one row per frame 0-47. Columns:
  - `frame, time_s`
  - `shell_x, shell_y` – **recommended reference point** (proxy for the object origin): carapace position from
    template matching, integrated from the per-frame shifts and anchored so frame 47 equals the full-mask centroid.
    Rigid: not disturbed by flipper strokes or by the right-edge truncation. In frames 0-~10 it lies at x>1919
    (the turtle's centre is still off-screen; only head/front part visible).
  - `shell_dx, shell_dy, shell_match` – measured carapace displacement frame i-1 -> i (px) and match score (0.90-0.99).
  - `mask_cx, mask_cy` – centroid of the full segmented mask (flippers included).
  - `bbox_x0,y0,x1,y1, bbox_cx, bbox_cy, len_px (x extent), height_px (y extent)` – full-mask bounding box.
  - `axis_len_px, axis_width_px, axis_angle_deg` – mask extents along / across its principal axis.
  - `body_*` – mask opened with a 41-px disc (tries to drop the thin flippers). UNRELIABLE when the broad flippers
    are spread (frames 0-36): use only as a rough carapace+head extent in frames 39-46.
  - `area_px, truncated_right_edge (1 = frames 0-20), occluded (always 0)`.
- `scripts/` – `bg.py` camera check + median bg; `seg.py` first segmentation; `track.py` mask track (writes the
  csv); `shellshift.py` carapace template track (adds shell_* columns); `probe16.py` noise probe.

## Method
- Camera: phase correlation of the seabed band (y 780-1080) against frame 0 gives |shift| <= 0.33 px for all frames
  -> static camera, no background compensation needed.
- Segmentation: |frame - background| summed over RGB > 20, background = frame 0 for x<1400 (turtle absent there at
  the start) and frame 47 for x>=1400 (turtle absent at the end); y<790 only; 5x5 open, 7x7 close, component nearest
  the previous box. Overlays checked visually (frames/ov2, frames 0,16,20,24,40,44): the mask covers the carapace,
  head and all flippers including the dark far-side flippers; a few px of the darkest head/flipper edges may be lost.
- Carapace track: template = upper shell band (bbox_y0+4 … +60) of frame i, matched in frame i+1 with
  sub-pixel peak; per-frame dx accurate to ~0.3-0.5 px (small jitter e.g. frames 8, 10, 43).

## Key observations
- Motion is purely horizontal leftward: shell_y stays 547.0-548.7 px for all frames.
- Carapace displacement per frame grows steadily and almost linearly from -0.7 px (frame 1) to -42.6 px (frame 47);
  the turtle speeds up through the whole clip (no stop, no reversal). Total shell travel frame 0->47 ~ 1020 px.
- Mask centroid / bbox wobble with the flipper stroke (centroid y 550 -> 592 -> 548); use shell_* for motion.
- Turtle size (fully visible, rest pose frames 40-46): bbox length ~298-312 px (head tip to rear-flipper tip),
  height ~130 px (y 493-623); body (shell top to belly) ~105 px tall; carapace+head ~270-280 px long.
  While flippers are stroked down (frames 13-23) bbox height reaches ~205-240 px. Frames 21-36 bbox length 314-326.
  Frame 47: bbox 776-1097 (322 px) because the far front flipper swings ahead of the head.
  A question giving the turtle's length most likely means its head-to-tail length: use ~305 px (rest pose) unless
  the question specifies otherwise; if it means the world AABB in a stroke pose, use the bbox of that frame.
- Events: flipper power stroke frames ~2-16 (bbox bottom lowest y~735 at frames 13-19), recovery to folded
  rest pose by frame ~39, next forward swing starting at frame 47. Turtle fully in frame from frame 21.
- Static: seabed dunes across full width, top edge y~800 (crest x 800-1100), y~830 at x=0, y~870 at x=1900.

## Reliability / ambiguities
- Only one animal; no similar objects. Caustic light patches on the seabed and light shafts move/flicker but are
  lighting, not objects. Faint MPEG block noise appears below the flippers in frames 15-17 (removed by the 5x5 open).
- Frames 0-20: the turtle is cut by the right edge, so mask centroid, bbox and extents there describe only the
  visible part; shell_x is valid (motion of the visible shell).
- shell_x/shell_y absolute offset is tied to the frame-47 mask centroid (origin of the Blender rig unknown; it may sit
  a few px to tens of px from this point, but displacements are unaffected).
- No metric scale is assumed anywhere; 2D scene -> one m/px scale from whatever prior the question gives.

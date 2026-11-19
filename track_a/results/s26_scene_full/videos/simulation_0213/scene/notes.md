# simulation_0213 — measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 50 frames (t = i/24, 0 … 2.0417 s). Source: Blender simulation, labelled **2D**.
Coordinates: pixels, x to the right, y down, origin at the top-left. No metric scale is assumed anywhere.

## Scene
A static side view of a plain light-grey wall with a brownish floor (wall/floor boundary at y≈944, faint baseboard line at y≈906).
Two animals walk in opposite directions parallel to the image plane and cross paths:
- **cat**: a black-and-white tuxedo cat with white paws, an untextured flat-grey head (render artefact) and a raised tail. It is the smaller animal and walks **left → right** the whole clip at a steady pace.
- **dog**: a brindle (brown striped) dog with white paws, an untextured grey head held low (sniffing) and a tail that swings a lot. It is the larger animal and walks **right → left**. It starts almost at rest, speeds up, then slows to nearly a stop at the end.
The dog walks **nearer the camera** than the cat: the dog's paws touch the floor at y≈1061-1070 and the cat's at y≈1017-1023, and the dog hides the cat while they cross.
Static props (right side): a wooden slatted side table, a lamp on it, a blue-and-white vase on it, and a tall mirror leaning on the wall behind the table. The mirror shows a reflection of the vase.
The camera is static. There is no pan, zoom or shake: a background plate built from frames across the whole clip is sharp, and the props never shift.

## Files
- `scene.json`: inventory (description, what tells objects apart, moving or not, visible frames), static prop boxes, camera and perspective notes, events, and summary size statistics.
- `tracks/cat.csv`, `tracks/dog.csv`: one row per frame (0-49) with these columns:
  - `frame`, `t`
  - `bbox_x0,y0,x1,y1`: the full extent, including the tail. `bbox_y1` is the lowest pixel that is not floor shadow (paw bottoms). `bbox_y1_incl_shadow` includes the shadow.
  - `bbox_cx, bbox_cy`: the box centre.
  - `centroid_x/y`: the mask centroid, without shadow.
  - `torso_cx/cy`: the centroid of mask pixels above y=940, limited to the tail-free span. It is the most stable body point and the best stand-in for the rig root or pelvis.
  - `body_x0_notail, body_x1_notail`: the horizontal extent without the tail, taken from rows y≥900.
  - `length_px` (with tail), `length_notail_px`, `height_px` (from the box top to the paws), `area_px`.
  - `occluded` (cat only: 1 while it is hidden behind the dog) and `merged_blob` (1 when the two animals form one foreground blob, frames 23-43).
  - Cat only: `fit_bbox_x1`, `fit_bbox_cx`, `fit_torso_cx`. These are straight-line fits over the visible frames and give the cat's position while it is hidden.
- `scripts/`:
  - `common.py`: the frame reader.
  - `background.py`: builds the clean plate from animal-free columns.
  - `segment.py`: makes the masks.
  - `tracks.py`: writes the CSVs.
  - `static_objects.py`: the prop profiles.
  - `build_scene.py`: writes scene.json.
  - `overlay.py`, `zoom.py`: the visual checks.
  - Masks and the plate are scratch files in `../frames/` (masks/NNN.png: 1=cat, 2=dog, +10=shadow-like pixel). Rerun `background.py`, then `segment.py`, then `tracks.py` to regenerate them.

## How it was measured
- Foreground is the difference from the clean plate (per-channel max > 14) in rows ≥700, followed by morphological cleaning and hole filling.
- Floor cast shadows (warm, uniformly darker floor) are removed from the bottom edge. The shaded underside of the dog's grey head looks just like shadow, so blob-sized chunks are kept in the mask. They are never used for the bottom edge, because the paws are lower.
- Cat versus dog:
  - When the blobs are separate (frames 0-22 and 44-49), each blob is assigned by continuity.
  - When they are merged (23-43), the black-fur pixels (cat) and brown-fur pixels (dog) are used as cores. Grey heads and white paws go to the nearest core, and the dog is kept as one connected piece.
- The masks, boxes and reference points were drawn on frames and checked by eye at frames 0, 8, 10, 16, 22-44 and 49. They fit the full animal, including the heads and tails.

## Reliability
- **Cat, frames 0-22 and 44-49**: good to about ±2 px.
  - The nose (`bbox_x1`) moves linearly at **17.76 px/frame**, with an rms residual of 0.7 px.
  - `bbox_x0` jumps when the tail tip or the trailing paw becomes the extreme point, so use x1, the fit or the torso.
- **Cat, frames 23-43**: it is behind the dog and the visible pieces are small, especially in frames 29-35.
  - The bbox, centroid and torso values there describe **only the visible part** and are unreliable.
  - Use the `fit_*` columns instead. The nose matches the fit again from frame 36, when the head reappears right of the dog.
  - The cat's height in frames 32-41 is only its visible part.
- **Dog**: good to about ±3-5 px in frames 0-22 and 44-49. In frames 23-43 small cat pieces can be mislabelled as dog. For example, the cat's tail above the dog's back at frames 30-32, the cat's white paws next to the dog's head at about frame 30, and `body_x1_notail` at frames 37-42 may include cat pixels.
  - The tail swings, so `length_px` varies from about 437 to 622. The tail-free length is about 435-490 px (median about 462). Height (back to paws) is about 280-347 px, larger when the tail curls up above the back, for example frames 2-4, 13-14 and 21-25.
  - `bbox_y1` should be about 1061-1070 everywhere. A few frames (25, 43) reach 1078-1079 because of leftover shadow.
- **Dog motion**: the torso_cx steps are ≈1-4 px/frame at frames 0-3, rise to ≈18-25 px/frame at frames 16-32, fall to ≈10-16 at frames 38-44, and drop to ≈0.5-2.4 at frames 47-49. Its head stays at x≈483-490 at frames 46-49. Gait and head bobbing add ±3-5 px of jitter per frame.
- **Static props**: ±3-5 px. They come from colour profiles of the plate and zoomed grid crops.
  - The table is cut off by the right image edge (x=1919), so its true length is longer than 460 px.
  - The left vase in the mirror is a reflection, not a second vase.

## Ambiguities
- **Reference point**: the Blender origin of an animal rig is not visible. The best choices are `torso_cx/cy` (body centre) or `bbox_cx` for horizontal motion, and `fit_bbox_cx` for the hidden cat. Positions differ by a near-constant offset, so speeds are insensitive to the choice, but distances between the animals are not.
- **Depth**: the scene is called 2D, but the two animals are in different floor lanes, and the dog is nearer. The horizon row is unknown, because the camera looks roughly level at the wall and the floor lines are parallel to the image. If the horizon is near the image centre, the dog's lane is about 10% nearer, so a pixel on the dog is about 10% smaller in metres. Use a separate scale per animal if the question's prior concerns one animal and the question is about the other, and say so.
- **Grey heads**: both animals have flat untextured grey heads, a render artefact. These are included in the masks.
- **Events**: there is no bounce, impact or release.
  - The cat's nose meets the dog's head at frame 23 (t=0.958 s).
  - The body centres cross at frame 32 (t=1.333 s).
  - The cat's head reappears right of the dog at frame 36.
  - The cat is fully clear of the dog from frame 44 (t=1.833 s).
  - The dog starts from near rest at frame 0 and has nearly stopped by frames 47-49.

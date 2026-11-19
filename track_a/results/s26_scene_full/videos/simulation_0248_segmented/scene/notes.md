# simulation_0248_segmented — measurement record (pixels, frames; no metric scale)

Video: 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s). Source: segmentation of a Blender render
(background replaced by plain white). Scene type: 2D, pure side view; all motion is left→right, parallel to the image plane.

## Objects (all three move; no static objects, no ground, no markings)
| name | identification | moves | visible |
|---|---|---|---|
| red_horse | smaller horse, chestnut/red-brown coat, white face and white lower legs; leftmost | walks right | 0–49 |
| brown_horse | larger horse, grey-brown coat, dark legs/tail, white face; middle | walks right | 0–49 |
| hamster | small orange-brown rodent near the brown horse's front hooves; rightmost | hops/walks right | 0–49 |

Pixel sizes (bbox of mask; side view, so "length" = horizontal extent nose-to-tail, "height" = top of head to hooves; width across the body is not observable):
- red_horse: length 183–215 px (median 192, frame 0: 185), height 161–170 (median 165).
- brown_horse: length 223–241 px (median 229, frame 0: 229), height 174–184 (median 177.5).
- hamster: length 42–53 px (median 46, frame 0: 45), height 29–39 (median 34.5).
Lengths/heights vary with the gait (leg stride, head bob); use the median or the frame asked about.
Because the legs and tail swing, the silhouette extent changes from frame to frame. That is the main size uncertainty (≈ ±5 %).

## Files
- `scene.json`: inventory, size stats, first/last positions, events, camera.
- `tracks/<object>.csv` (one row per frame 0–49): frame, time, bbox_cx/cy (bbox centre), centroid_x/y (mask centroid),
  body_cx/cy (centroid of the body rows), x0,y0,x1,y1 (bbox, inclusive px), length_px, height_px, area_px, n_parts, occluded (always 0),
  torso_x/y (centre of a frame-0 torso template matched in colour per frame, sub-pixel).
- `scripts/track.py` (segmentation: min RGB < 235, 4-connected components → exactly 3 per frame), `scripts/torso.py`
  (template tracking), `scripts/summary.py` (scene.json), `scripts/probe.py` (scratch checks).

## Reference point (rig origin proxy)
For position/speed questions use **torso_x/y** for the horses (leg swing does not affect it; its y stays within ±0.5 px for
the red horse and ±1.5 px for the brown horse) — it approximates the root/pelvis-to-body-centre of the rig; the constant offset
to the true origin does not matter for speeds or for horizontal separations between similar points. centroid_x agrees
in mean motion (net px/frame: red 3.20 vs torso 3.25, brown 5.94 vs 5.92, hamster 6.27 vs 6.27). For the hamster
prefer **centroid_x/y** (its torso template jitters by several px because the body deforms when it hops).
Net horizontal motion: red_horse +156 px over frames 0→48 (≈3.25 px/frame); brown_horse +290 px over 0→49 (≈5.92 px/frame);
hamster +307 px over 0→49 (≈6.27 px/frame, per-frame steps oscillate ~4.5–9 px with its hop cycle of ~10–11 frames).
Vertical motion is negligible for all (horse torsos ≤ ±1.5 px, hamster centroid ±1.5 px).
Separations at frame 0 (torso/centroid x): red→brown torso 254.5 px; brown torso→hamster centroid 131.9 px.

## Events
- All animals are already moving at frame 0 and still moving at the last frame; no start/stop, bounce or contact.
- **Frame 49: the red horse jumps back to its frame-0 position and pose** (torso x 801.0 at f48 → 645.0 at f49, identical
  to f0): an animation-loop reset, not real motion. Treat red_horse data at frame 49 as invalid for motion; its real
  motion spans frames 0–48. A one-frame backward difference at t≈2.04 s for the red horse would be an artefact.
- The hamster passes close to the brown horse's front hooves (≈1–3 px gap around frames 13 and 23) but they never merge
  or occlude each other; no occlusion anywhere.

## Camera / perspective
Static camera (nothing in the background to move; motion of all animals smooth). 2D: one metres-per-pixel scale from
the prior's object applies to all three — their ground contacts are at nearly the same image row (y ≈ 627–636), so
they're consistent with a single depth plane.

## Reliability
Mask edges are sharp (antialiased by 1 px); bbox values ±1–2 px. The white/grey horse faces are included (threshold 235).
Silhouette lengths fluctuate with gait by up to ±8 % (red horse 183–215). Torso track precision ≈ ±0.5 px.

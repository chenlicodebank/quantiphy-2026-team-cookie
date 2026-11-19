# internet_0067 — measurement record

Video: 12 frames, 30 fps (0.4 s), 3840x2160, internet footage, 2D. All values in full-resolution pixels and seconds; t = frame/30.

## Scene
Low camera at floor level facing a plain wall. A long white rail (whiteboard tray / baseboard tube, y≈840–960) runs across the wall base with two black brackets (left bbox x 630–692, y 840–915; right bbox x 3080–3142, y 880–955; spacing ≈2450 px). Wooden floor below (y > 960).
Only moving object: **cup** — black rounded top over a white cup-shaped body — dragged left→right across the floor by a thin dark **cord** tied to its right side. It enters at the left edge in frame 1, is fully in frame 3–6, exits at the right edge in frame 7, and frames 8–11 show the empty scene (used as background).

## Files
- `scene.json` – inventory, static extents, camera, events, summary sizes and centres.
- `tracks/cup.csv` – per frame (0–11): visible flag, bbox-centre (cx, cy), mask centroid, bbox x0/y0/x1/y1, length_px (bbox width), height_px, area, dark-top extents, `top_halfmax_*` (blur-robust horizontal extent and centre of the black top), blur ramp, clipped/occluded flags.
- `scripts/measure.py` – the whole measurement (background = median of frames 9–11, colour difference > 40, 25 px opening to drop the cord, largest component; half-max profile of the black top; phase correlation for camera shift).

## Key numbers
- Horizontal centre x (top_halfmax_cx): f1 70*, f2 265*, f3 703, f4 1240, f5 1962, f6 2833, f7 3635* (* clipped by the image edge → biased). Per-frame Δx 537, 722, 871 px (f3→4→5→6): the cup is accelerating.
- y (bbox centre) 1278 → 1340 across f3–f6 (slight downward drift; cup moves a little toward the camera).
- Size: length along motion ≈ 545 px (half-max width of the black top, 516–570 over f3–f6; blurred bbox widths 596–686 include motion blur). Height (dome top to body bottom) ≈ 620 px (604–644, rising slightly with time due to approaching camera + blur at the base).
- Camera: static; background drift ≤ 3 px over the clip.

## Reliability / ambiguities
- Strong horizontal motion blur (≈120–290 px ramps); edges in x carry ±20–30 px uncertainty, centres ±15 px. The white body is low-contrast against the floor in places, so the mask under-covers it (verified on overlays) but the bbox still spans the full object; vertical extents ±10 px.
- Frames 1, 2, 7 are partial (edge-clipped); use frames 3–6 for size and clean motion. Only 4 complete positions exist, so second differences are noisy.
- Object identity (cup vs. toy/mouse-like gadget) is uncertain from the blurred images; "length" for a prior is most likely the horizontal extent (≈545 px), height ≈620 px. The cord is not tracked.

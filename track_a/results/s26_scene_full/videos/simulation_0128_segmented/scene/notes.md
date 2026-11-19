# simulation_0128_segmented — measurement notes

2D segmentation clip (Blender render, plain white background), 1920x1080, 24 fps, 38 frames (t = frame/24, 0 … 1.5417 s).
Pixel coordinates: x right, y down. Camera static (background is pure white 255 in every frame).

## Objects
- **ball** — small red sphere, the only red object. Falls vertically from rest at (961.9, 253.2) starting at frame 0;
  x stays at 961.9 ± 0.15 px. At frame 37 centre y = 977.6 (bottom edge 989); it has not hit anything by the end.
  Diameter ≈ 26 px (bbox 25–28 px, area-equivalent 25.7 px).
- **forklift** — orange/black Toyota forklift seen side-on, mast/forks at its right end (it faces +x). Drives right along a
  horizontal line, starting from rest at frame 0. Length (bbox x, counterweight to mast) ≈ 293.6 px (291–298),
  height (overhead guard top y = 815 to wheel bottom y = 1056) ≈ 242.4 px. Net displacement +120.1 px in 37 frames.
  Per-frame dx: rises 0.04 → ~3.0 px (frames 0–17), roughly level 3.0–3.5 (frames 17–27), rises again to ~6.8 (27–35),
  ~7.0 (35–37). Vertical drift < 0.25 px.
- No static objects, ground markings or other props. The forklift wheel bottoms mark the implied ground line at y ≈ 1056.

## Files
- `scene.json` — inventory, sizes, events, camera.
- `tracks/ball.csv` — per frame: centre (cx, cy; intensity-weighted, sub-pixel), mask bbox, width/height, area-equivalent
  diameter, occlusion flag (never occluded).
- `tracks/forklift.csv` — per frame: `ref_x_px/ref_y_px` (best reference point = frame-0 bbox centre (271.0, 935.5) moved by
  the sub-pixel template shift), raw bbox centre, mask centroid, bbox, length/height, mask area, occlusion flag (never).
- `tracks/forklift_shift.csv` — raw template-match shift vs frame 0 and match score.
- `scripts/track.py` (masks: non-white < 235, ball = red component), `scripts/forklift_template.py` (normalised
  cross-correlation of the frame-0 body crop, parabolic sub-pixel peak), `scripts/finalize.py` (merge, event fit, bg check).

## Reliability / caveats
- Ball centre: ~0.1–0.2 px precision (parabola fit residual 0.13 px). Ball bbox size jitters ±1 px from antialiasing/compression;
  use ~26 px diameter.
- Forklift: use `ref_x_px` for motion (smooth, ~0.1–0.2 px); the raw bbox centre jitters ±1–2 px. Match scores 0.86–0.95
  (slight appearance change, e.g. rotating wheels/compression), shift still consistent. The true Blender root may be at a
  different point of the forklift (e.g. bottom centre), but since it is rigid and moves horizontally, displacements and
  speeds are the same for any body point; only absolute ball–forklift distances depend on this choice (bbox centre is
  given; wheel-bottom/ground y = 1056 if a root at the ground is wanted).
- Faint compression specks appear near x≈940 and around the forklift; excluded from masks (checked on overlays frames/ov*.png).
- For a 2D question, use one metres-per-pixel scale from the prior object (ball diameter, forklift length/height, or a
  given speed/acceleration of either) for everything.

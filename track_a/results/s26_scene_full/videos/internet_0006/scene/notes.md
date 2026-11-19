# internet_0006 – measurement record (pixels, seconds)

Video: 1080x1920 portrait, 172 frames, fps 29.678492, t = frame / fps (frame 0 at t = 0).
Source: internet, declared 2D. Image axes: x right, y down, full-resolution pixels.

## Scene
Top-down (nadir) drone shot of a straight two-lane country road running vertically through the frame.
Field on the left, woodland with a dirt footpath on the right. Overcast light, practically no shadows.
Moving: **white_car** (left lane, drives UP the image), **dark_car** (dark blue/grey, left lane, behind
the white car, also drives UP), **cyclist** (right lane, rides DOWN, opposite direction), and a small white
**bird** flying from lower right to the left across the road. Nothing else moves (trees sway slightly).

## Files
- `scene.json` – inventory (moving + static objects with descriptions, pixel sizes, frames visible),
  camera, perspective notes, events with frame/time.
- `tracks/<object>.csv` – one row per frame in which the object is (at least partly) visible:
  `frame, t, ref_x, ref_y` (recommended reference point = visible centre), `ref_src` (how ref was obtained),
  `x0,y0,x1,y1, bbox_w, bbox_h` (mask bounding box, inclusive), `mask_len, mask_wid, axis_deg` (PCA length/width
  of the foreground mask; for cars/cyclist main axis is vertical, so bbox_h = length along road, bbox_w = width),
  `area`, `mask_extents_ok` (1 = mask clean, extents usable), `edge_trunc` (touches frame edge), `occluded`,
  `mask_cx, mask_cy` (mask bbox centre), `tcx, tcy, tscore` (template-match centre and NCC score), `note`.
- `camera_shift.csv` – per-frame background shift vs frame 0 (phase correlation on field + woods).
- `scripts/` – all measurement code (camera.py → track.py → match.py → canopy_dark.py → white_exit.py →
  finalize.py → static.py → write_scene.py; finalize.py rewrites the raw track CSVs, so rerun from track.py; view.py/crop.py/show.py/summ.py are viewers). Background images are
  regenerated into `frames/` (outside the record).

## Method
- Camera: static hovering drone; total background drift ≤ 0.65 px (x) and ≤ 1.7 px (y) over the clip → no
  compensation needed; image positions are ground positions.
- Masks: per-pixel median background (every 3rd frame), colour |diff| > 35 in the road strip, close/open,
  per-object lateral limits so the cyclist and cars don't merge when passing. Bird: grey diff > 40 & bright.
- Reference points: cars and cyclist use template matching (template = clean mask bbox at reference frames,
  nearest-in-y template, sub-pixel peak); agrees with mask-bbox centre to ≲1 px on clear road and stays
  smooth (~8.6–9 px/frame) where the mask is contaminated. Bird uses mask bbox centre.
- Overlays checked visually (frames 0, 30, 60, 100, 120, 150; full-trajectory plot): tracks hit the right
  objects, masks cover the full body.

## Pixel sizes (clean frames; bbox, along road = vertical)
- white_car: length (bumper to bumper) 76–79 px (median 78; 79 at frame 0, 76 at y≈500–900, 82 near top
  y<200), width 34–40 px (median 37, includes mirrors at times).
- dark_car: length 68–71 px (median 69; 72 at frame 0 near bottom), width 35–40 (median 36).
- cyclist (bike+rider from above): length 29–32 px (median 30), width 15–18 (median 16).
- bird: 7–16 px bbox (wing flapping), PCA length 11–21 px.
- Length change with y is lens (wide-angle) stretch toward frame edges, ~5–8 %; for a single-scale
  answer measure the prior object at the frame(s) the question refers to, or use the medians above.
- Road: asphalt 75–77 px wide (left edge x≈519–523, right edge x≈594–599); with dark kerb lines ≈87 px.
  Centre-line dashes at x≈560: length 87–91 px (mid frame), period 131–135 px (list in scene.json).
  "SLOW" marking (right lane) bbox x 565–599, y 1204–1243 (35 x 40 px).

## Motion summary (no speeds fitted)
- white_car: ref_y 1386 (f0) → ~65 (f152), x ≈ 536–543 (very slight leftward drift); front reaches top edge
  f≈155, fully out f≈164. Roughly constant pixel rate.
- dark_car: ref_y 1836.5 (f0) → ~580 (f150) → ~405 (f171, rough); x 528.5 → 539.
- cyclist: ref_y 784.5 (f0) → 1881 (f118), x 575 → 569; leaves bottom edge f119–123.
- bird: (982,1658) at f0 → (2.5,972) at f139; heads up-left, then nearly horizontal-left after ~f100.
- Events: white car passes cyclist f≈33.8 (t 1.138 s, y≈1104); dark car passes cyclist f≈60.7 (t 2.044 s,
  y≈1356); bird crosses road x=600/560/520 at f≈57.0/62.6/68.1.

## Reliability / ambiguities
- white_car f104–132: drives under thin overhanging branches of the big willow → mask extents inflated
  (flagged occluded=1, mask_extents_ok=0); template centre still reliable (score 0.8–0.95).
- white_car f153–163: at/leaving the top edge → ref_y = rear of the white paint (white_exit.py) − 36 px,
  offset calibrated against the template centre on f150–152; smooth ~9 px/frame, ±2 px. ref_y < 0 means
  the centre is already above the frame. cyclist f121–123: ref = top edge + 15.5 (edge_trunc, ±2 px).
- dark_car f153–171: front goes under the willow canopy. ref_y = visible rear bumper − 34.5 px (half length),
  ref_x fixed at 538.5; good (±2 px) to f162, rough (±5 px) f163–171 where the car is mostly hidden.
  Mask columns for these frames are contaminated (ignore bbox/len there).
- Bird size is only approximate (small, flapping, motion blur).
- Two cars look alike only in shape; they differ clearly in colour (white vs dark). Only one cyclist, one bird.

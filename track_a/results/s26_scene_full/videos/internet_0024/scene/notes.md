# internet_0024 – measurement record

Overhead (top-down), static-camera clip of a wooden desk, 3840x2160, 25 fps, 30 frames (1.2 s). A right hand
(black smartwatch) picks up a white mug of black coffee at the right of the desk and carries it down-left out of the
bottom edge. Everything else is static. All values in full-resolution pixels and seconds (t = frame/25).

## Files
- `scene.json` – inventory, static-object pixel sizes (measured on frame 29, cup gone), cup summary, events, camera.
- `tracks/coffee_cup.csv` – per frame 0-29: `ref_x, ref_y` (= rim circle centre, the reference point), rim circle
  (`rim_cx, rim_cy, rim_diam`, number of edge points and median residual), coffee-disc circle (`coffee_cx, coffee_cy,
  coffee_diam`), bbox of the visible cup (rim + perspective side wall, within 1.4 rim radii; excludes hand),
  min-area-rect length/width/angle of that mask, rough hand bbox, `cut_by_bottom_edge`, `occluded`, `quality` text.
  Frames 28-29: not visible.
- `tracks/camera_shift.csv` – phase-correlation shift of the static upper-left region vs frame 0 (all < 1 px).
- `scripts/` – `track_cup.py` (tracking; writes `raw_track.json`), `write_record.py` (CSV export), `view_crops.py`
  (overlay check sheets), `fgmask.py`, `probe.py` (exploration), `bg_quarter.png` (background, 1/4 scale).

## Method
Background = frame 29 (lower-left part from frame 0); foreground = |frame − background| > 30. Cup = foreground ∩
(white ceramic: S<28, V>120 ∪ dark: V<130). Coffee = largest dark blob inside the cup; circle least-squares fitted to
its contour (ignoring frame-border points). Rim = outermost white pixel along 240 rays from the coffee centre, robust
circle fit (outlier trimming removes the side wall / handle). Overlays checked visually on frames 0-27: circles sit on
the mug rim and coffee surface.

## Reliability
- Camera static: shift < 1 px all frames, no correction needed.
- Rim centre: ±3-5 px frames 0-22; frames 5-8 the rim diameter dips to ~396-407 (motion blur + fingers on rim), the
  centre is still good; frames 23-27 only a short arc is visible – centre extrapolated, ±10-15 px (coffee centre agrees).
- Coffee centre is ~10 px above the rim centre in early frames (the cup is seen slightly from the side and the coffee
  surface sits below the rim); converges later.
- Apparent size grows during the move (cup lifted toward the camera): rim 417 px (f0) → ~487 (f20) → ~500 (f23+);
  coffee 373 → 447 → 484. The planar single-scale assumption is thus off by up to ~20 % late in the clip; for a cup
  size prior use the frame-0 rim diameter (~417 px, outer rim) or coffee diameter (373 px) as the annotators' likely
  single pixel length, but per-frame values are in the CSV.
- Visible cup bbox includes the white side wall visible to the lower-left (perspective) – the top-rim diameter is the
  better "cup diameter". The handle is mostly hidden under the fingers.
- Static object sizes from gridded views: pencil 754 px long (±5), others ±15-25 px (see scene.json). Laptop, grey
  notebook, colour cards and kraft notebook are partly cut by frame edges.

## Events
At rest frames 0-3 (≤10 px creep as the grip tightens/lift begins); clear motion from frame 4 (t=0.16 s), roughly
straight down-left (~140° from +x, image y down) and speeding up to ~75-95 px/frame by frames 13-22; cup touches the
bottom edge at frame 20 (0.80 s), rim centre leaves at ~frame 25 (1.00 s), last visible frame 27 (1.08 s).

## Ambiguities
Only one cup, one hand; no similar objects. White AirPods case and white plant saucer are static and not confused with
the mug (excluded by foreground mask). Coffee surface shows reflections in frames 6-9 (handled by V<130 threshold).

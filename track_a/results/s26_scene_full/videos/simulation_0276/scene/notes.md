# simulation_0276 — measurement record (pixels, seconds)

## Scene
2D simulation (Blender), 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).
Camera looks straight down onto flat brown dirt. One raccoon (grey body, black/white ringed tail,
light-tan pointed snout) walks left → right (+x) along image row y ≈ 728 for the whole clip.
Static: a light-green tree canopy at the top left, a dark tree trunk at the top centre-right and conifer
branches at the top right, all cut off by the frame edge. Broad diagonal tree shadows lie across the left
half. There are no markings, props or other animals. The camera is **static**: phase correlation of
background strips against frame 0 gives a 0.00 px shift in every tested frame. There is no usable
perspective, so one metres-per-pixel scale holds for the whole ground plane.

## Files
- `scene.json`: inventory, static-object extents, events, camera and summary numbers.
- `tracks/animal.csv`: the raccoon in all 72 frames. Columns:
  - `frame`, `t`
  - `cx_mask`, `cy_mask`: silhouette centroid. **This is the recommended reference point (origin proxy).**
  - `bbox_x0..y1`, `bbox_cx/cy`, `bbox_w/h`: axis-aligned box of the full silhouette. `bbox_x1` is the
    snout tip and `bbox_x0` the tail tip.
  - `area_px`
  - `length_main_axis`, `width_across`, `axis_angle_deg`: PCA axis extents. The axis is about 0°/180°
    (horizontal), so length ≈ `bbox_w`.
  - `torso_*`: run of columns where the mask is ≥ 50 px tall. This is noisy because of legs; avoid it.
  - `occluded`: always 0.
- `scripts/`:
  - `camcheck.py`: camera-motion check.
  - `track.py`: the segmentation and tracker.
  - `montage.py`, `draw_track.py`: visual checks.
  - `summary.py`: statistics.
  - `framediff.py`: finds the duplicated frame.
  - `static.py`: static-object boxes.
  - `probe.py`: colour probe.

## How it was measured
- **Background:** per-pixel median of 9 frames. This contains no raccoon because the raccoon moves more than 1400 px.
- **Mask:** the union of four cues:
  - a chromaticity change, which catches the grey fur;
  - brightening, which catches the white tail rings;
  - very dark pixels, which catch the black tail tip;
  - a shadow-invariant texture residual, which catches the flat tan snout. That snout has almost the
    ground's mean colour but none of its texture. The cue is allowed ungated only in a band ahead of
    the head and a thin strip along the tail line.
- **Shadow:** the raccoon's own shadow falls to the lower-left, behind it. It is excluded because a
  pure darkening keeps the chromaticity unchanged.
- **Check:** overlays at every 2nd frame were inspected. The box hits nose tip to tail tip in nearly
  every frame.

## Key numbers
- **Position:**
  - Frame 0: (761.3, 727.6). Frame 71: (2198.1, 728.3).
  - Net displacement 1436.8 px; path length 1437.4 px.
  - y varies by only 727–731, so the path is a straight line along +x.
- **Frames 0 and 1 are identical** (frame difference 0.03 vs about 0.9 elsewhere). Motion starts at
  frame 2 (t = 0.083 s).
- **Pace:** from frame 2 on the raccoon walks at a near-constant pace.
  - Mean 20.5 px/frame (≈ 492 px/s).
  - Per-frame centroid steps scatter 15–28 px (sd 3.6) from gait and mask noise. A linear fit has a
    residual sd of 4.3 px and no meaningful quadratic term, so there is no visible acceleration.
- **Size:**
  - Nose-to-tail-tip length: median **295 px** (p10–p90 285–300, range 267–304).
  - Width across, including swinging legs: median 66 px (62–83). The body-only width is about 62 px.
  - The world-vertical height is not observable from above.

## Reliability and ambiguities
- **Centroid:**
  - Per-frame accuracy is about ±2–4 px, because limbs and tail swing during the gait.
  - Multi-frame differences are much more accurate (about ±1 px/frame over 10+ frames).
  - It sits roughly mid-body. The true rig root may be offset along x, which does not affect speeds.
- **Length:**
  - Uncertainty is about ±5 px.
  - In a few frames (e.g. 18, 38, 53) the low-contrast snout tip or the lifted tail tip is partly
    missed, giving 267–280. Use the median over frames (295) for a size prior.
  - Whether a "length" prior includes the tail is ambiguous. `scripts/taillen.py` splits the
    silhouette at the tail base, the first column from the tip where the mask is 40 px tall:
    - Tail: median 102 px.
    - Snout tip to tail base: median 191 px (175–214).
    - Accuracy is about ±10 px, because the hind legs near the tail base can blur the split.
- **Static objects:** boxes are only the visible parts (all three are truncated by the image border).
  The foliage threshold makes the edges accurate to about ±10 px.

# simulation_0125 — measurement record (pixels, seconds)

2D Blender render, 1080x1080, 24 fps, 71 frames (t = frame/24). Camera **static** (frame 0 vs 70 upper-image mean abs diff 0.44/765).
Scene: frontal view of a gabled cabin (black frame, brown wood facade, lit windows) on a dark porch, mountains behind.
**One moving object: a man** (grey T-shirt, dark jeans) walking left→right along the porch the whole clip, parallel to the
facade (motion in a plane facing the camera). He never starts, stops or turns within the clip. The fire-pit flame flickers; nothing else moves.

## Files
- `scene.json` — inventory (moving and static objects with pixel boxes), camera, events.
- `tracks/man.csv` — every frame 0-70: `pelvis_x_smooth, pelvis_y_smooth` (recommended origin/pelvis estimate),
  `centroid_x/y` (mask centroid), raw `pelvis_x/y`, bbox (`bbox_x0,y0,x1,y1,w,h`, inclusive px), `mask_len_main_axis`
  / `mask_width_across` (PCA extents of the mask ≈ height / width), `mask_area_px`, `occluded`.
- `scripts/` — `bg.py` (median background of the porch band, camera check), `track.py` (background subtraction,
  threshold 45 on summed |RGB| diff, open/close, largest blob + nearby blobs; overlays), `static.py` (bright openings
  / dark frames of windows and doors; occlusion flags), `smooth.py` (7-frame local quadratic smoothing), `check.py`.

## Key numbers (px)
- Pelvis x: 363.5 (f0) → 750.0 (f70), mean ≈ 5.5 px/frame (≈132 px/s); per-frame steps 3–8.6 px (gait variation +
  measurement noise). Pelvis y ≈ 770–777 (raw), essentially horizontal motion. Centroid x: 358.0 → 741.7.
- Man's pixel height (head top to lowest foot): 209–223 px when unoccluded; max ≈ 222–223 mid-stride (frames 12–20).
  Head top y = 657–663 throughout (reliable); feet bottom 869–879 (dark soles on dark deck: mask can miss ~5–8 px of
  shoe, so heights ~210 are slight underestimates; true standing height in pixels is probably ≈ 215–220).
  Width 52–114 px depending on stride (52–56 legs together, 108–114 full stride).
- Static objects (scene.json): left door glass 80×221 (frame 103×239), right glass door frame 208×244, upper-left window glass
  117×124, upper-right window 90×225, plant pot 53×82, lounge chairs ≈ 90×100, fire bowl ≈127×35, house ≈775 px wide,
  apex y≈28 to base y≈905. Window/door numbers are from thresholding (±2 px); chairs, lamps, fire pit, house read off a grid (±5–8 px).

## Events
Walking throughout (f0–f70). In front of left door f8–22, under centre lamp f29–31, in front of right glass door from f38,
feet hidden behind the left lounge chair f47–52 (occluded=1: bbox bottom/height and centroid_y invalid there; pelvis x still fine).

## Reliability / ambiguities
- Pelvis is estimated from the silhouette (no rig access); horizontal position ±3 px, smoothed version better for
  per-frame differences; for speeds over many frames use endpoints or a line fit. Arms swinging at hip level make
  raw pelvis_x jittery; centroid_x is smooth but shifts slightly with leg pose and during occlusion.
- Face is blurred in the render (not an occlusion). No shadow is included in the mask (soft porch lighting).
- For a 2D scale: one m/px factor from the given prior (e.g. the man's height ≈ 215–223 px, or a pixel speed of ≈5.5 px/frame).

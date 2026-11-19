# simulation_0184 – measurement notes

Blender render, 3D scene, 1920x1080, 24 fps, 45 frames (t = frame/24, 0 … 1.833 s). Static camera.

## Scene
A single moving object: a **box** (rectangular case, black sides, green top, "D5" labels, red light).
At frame 0 it hangs in the air at upper-left-centre, falls straight down (in the image) onto a **blue roller
conveyor ramp**, first touches at ~frame 8 (t≈0.33 s), tips forward to lie on the ramp (frames 8–14, angle
2°→32°, slight overshoot to ~34.5° at f16–19, then ~30–31°), and slides down the ramp toward the lower right,
accelerating, still moving at the last frame (f44, near the bottom edge). Static items: conveyor ramp, its blue support
leg, shelf with cardboard boxes (upper left), orange sign "TAKE CARE WHEN STACKING CRATES" (right), wooden
floor/pallet (bottom right), block wall. No people, animals or other moving things.

## Files
- `scene.json` – inventory, static object pixel extents, camera, perspective cues, events.
- `tracks/box.csv` – every frame 0–44: `cx,cy` (centroid of the filled silhouette = reference point for the box origin),
  `bbox_cx,bbox_cy`, bbox `x0,y0,x1,y1`, `bbox_w,bbox_h`, mask `area`, min-area-rectangle `minrect_len` (along main
  axis), `minrect_wid` (across), `minrect_angle_deg` (main-axis angle, + = clockwise/down-right in image),
  `clipped_by_frame_edge` (1 if the mask touches the image border).
- `scripts/track_box.py` – background subtraction (background = frame 44 with lower-right region from frame 0, which
  are disjoint box positions), threshold 18, morphology, largest component, **convex hull fill** (needed because the
  dark box sides on the dark conveyor are partly missed by the difference). Writes the CSV and an overlay check image.
- `scripts/static_objects.py` – camera-motion check (phase correlation, <0.01 px), conveyor edge sampling.

## Reliability
- Box centroid: ±2–3 px in the fall (clean contrast against the wall); ±4–6 px while on the conveyor (dark sides vs
  dark blue rollers; hull may include a sliver of shadow/contact). Overlays at frames 0,6,10,12,18,24,34,44 were
  checked visually: mask covers the whole box. Centroid is of the 2D silhouette, not the exact projected 3D centre
  (offset of a few px once the top face is visible).
- Frames 43–44: bbox bottom reads 1079 (flag=1); visually the box bottom is at ~1075, so it is essentially not clipped,
  but the mask may include a few px of floor there.
- Free fall frames 0–8: cx constant (584.5±0.5), cy steps 2.1, 6.2, 10.3, 14.4, 18.2, 22.2, 26.2, 22.8 px → constant
  ~4.1 px/frame² in image (the last step already slowed by contact). Usable for a gravity-scale check.
- Apparent size: main-axis length 335 px while level and falling (f0–8); ~340–346 px f14–28; ~352–364 px f34–44.
  So the box ends ~8–9 % closer to the camera (ramp descends toward the camera). The width-across value mixes in the
  visible top face after tilting, so use `minrect_len` (or bbox width at f0–7: 336 px, height 191 px) for size.
- Box size at clear frame 0 (level, front face toward camera): bbox 336 x 191 px (w x h), top face barely visible.
- Ambiguities: "box" could be called case/crate/toolbox; cardboard boxes on the shelf are static and different
  (brown). The sign mentions crates but is just a static sign. No motion blur to speak of.
- No metric scale is assumed; focal length unknown (answer sessions must derive from given depths/priors).

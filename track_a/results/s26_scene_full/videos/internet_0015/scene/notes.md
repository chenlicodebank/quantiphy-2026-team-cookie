# internet_0015 — measurement notes

Units: image pixels (x right, y down, 1920×1080) and seconds. fps = 29.781337, 143 frames, t = frame / fps.
No metric scale has been assumed anywhere.

## Scene
Top-down (nadir) drone view of a straight two-lane road running horizontally across the frame (2D scene).
Four road users, all in the **upper lane**, drive **right → left (−x)** in single file at nearly the same
pixel rate (~12 px/frame). From front to back: **silver_sedan** (lead), **dark_car**, **white_hatchback**,
**cyclist** (red/white two-wheeler with rider; it keeps pace with the cars, so it may be a motorcycle or scooter).
All four are moving at frame 0. Nothing enters the frame. Each one leaves across the left edge. There are no
stops, overtakes, contacts or lane changes. The lower lane stays empty. Tree shade covers the road for
x < ~590 (the boundary is oblique, ~560–620 at lane height). The road is sunlit to the right of it.

## Files
- `scene.json`: inventory (moving and static objects, with identifying cues), object sizes, road geometry,
  camera, events (exit frames, shade entry, gaps at frame 0), and a track summary.
- `tracks/<object>.csv`: one row per frame in which the object is visible (silver_sedan f0–41, dark_car f0–73,
  white_hatchback f0–110, cyclist f0–136). Columns:
  - `cx_px, cy_px`: reference point = visible body centre (bumper-midpoint along x, side-midpoint along y).
  - `cx_bgref_px, cy_bgref_px`: the same point minus the background drift (frame-0 background coordinates).
  - `bbox_*`: a box of the object's nominal visual length × width (from scene.json) centred on the reference
    point. `bbox_x0` is clipped at 0 while the object exits.
  - `visible_length_px` (clipped box length) and `width_px`.
  - `profile_*`: raw per-frame edge measurements where available (silver and white: half-max edges of the
    background-difference profile; cyclist f0–93: colour-mask extents). Empty where not measured.
  - `cy_filled_with_median`: 1 where the y-edges were implausible (cast shadow above or shade below) and cy was
    set to that object's median cy. The lane is straight and y is constant to within ±1 px.
  - `truncated_by_frame_edge`, `in_tree_shade` (cx < 590), `method`, and `ncc` (template correlation score).
- `camera_shift.csv`: per-frame background shift relative to frame 0 (phase correlation with the road masked out).
- `scripts/`: every script, in order. s1 measures camera shift. s4 builds the empty-road background
  (bg0_band.npy). s6 runs the adaptive template pass1, which is used only as a search guide. s8 measures edge
  profiles. s9 runs the fixed sun/shade templates. s11 builds the cyclist colour mask. s10 merges everything into
  the track CSVs. s13–s15 measure static road features. s16 writes scene.json. s17 draws the overlays.
  s2, s5 and s7 are superseded early attempts. crop/strip/check_edges/peek* are viewers.

## How each track was measured and how reliable it is
- **silver_sedan** (in shade the whole time; no visible cast shadow): centre = midpoint of the rear and front
  edges of the |frame − empty-road| column profile. During the exit (f37–41) centre = rear edge − 32.5.
  Visually verified at f0, 8, 16, 24, 32 and 40 (within ~1 px). Per-frame dx: −12.21 ± 0.25 px.
- **white_hatchback**: same edge-profile method (the rear edge is never touched by cast shadow, which falls up-left).
  Verified at f0, 40, 64 and 100 (≤1–2 px). dx −11.98 ± 0.40. One rear-edge glitch near f14–15 (≈2 px).
  An early adaptive template drifted ~10 px on this car and was rejected.
- **dark_car**: fixed (non-updating) NCC templates: the frame-0 sunlit template while its score is ≥ 0.65,
  otherwise a shade template (cut at f50) plus a calibrated offset of +4.38 px. Over 26 frames the two templates
  agree to within ±0.3 px. The last frames (exit) use the right part of the template. Verified against the two
  headlights, which keep a fixed offset from the track f0–72 (no drift, ~1 px). In shade the body is nearly
  invisible except for the headlights. Treat absolute x as ±1.5 px. dx −12.00 ± 0.36.
- **cyclist**: least reliable. Templates drifted ~8 px because its appearance changes (possibly pedalling).
  So for f0–93: centre = rear (right) edge of a colour mask (red or bright pixels; the grey cast shadow is
  excluded) − 14 px. For f94–136 (deep shade, faint): fixed shade template tied to the mask rear edge
  (+2.76 px in x from f88–93, and −3.78 px in y from f76–93). The template has a second correlation peak ~10 px away, so the peak that continues
  the track was taken (method `_altpeak` marks it). Checked by eye at f110 (rear end x≈359, consistent).
  Expect ±2 px in sun and ±3–4 px in shade. dx −12.25 ± 0.77, with single-frame jitter up to ±4 px in shade.
- Object positions are not smoothed. Answering sessions should fit or difference them as their question requires.

## Sizes (pixels; nominal visual values in scene.json)
| object | length (along motion) | width | notes |
|---|---|---|---|
| silver_sedan | 67 (visual bumper-to-bumper, 66–67) | 25 | half-max profile 64.9 (p10–p90 64.4–65.6) |
| dark_car | 60 | 27 | in sun the front edge merges with its cast shadow; the visual measurement used the headlight end |
| white_hatchback | 60 (visual 59–60) | 26 | half-max profile 54 (sun) – 58 (shade), median 55.9: the profile underestimates |
| cyclist | ~34 (visual 28–35) | ~11 | uncertain ±4 px; the colour mask (20–26) misses the dark front part |
If a question gives a car's real length, the annotators' convention is pixel length along the motion direction
(bumper to bumper). The visual values above are the best bumper-to-bumper estimates. The half-max profile values
show the spread that comes from the edge definition.

## Static features (scene.json → objects)
Road lines are all solid: upper edge line y≈519.5, double centre lines y≈564 and 572 (a narrow median strip
between them), lower edge line y≈618.5. Line width 2–3 px. Upper lane between line centres 44.5 px, lower lane
46.5 px, edge line to edge line 99 px. Asphalt y≈522–616. Fences with vertical posts: upper y≈488–499, posts
every 17.9 px; lower y≈638–652, posts every 18.4 px. Grass/gravel verges with small markers at y≈500–517 and
621–637. Trees, a diagonal ditch and a green field are listed in scene.json only roughly; they are not measured
precisely.

## Camera
Essentially static aerial view. The background drifts slowly: by the last frame dy ≈ −3 px; dx ≈ −2 px on the
left half and ≈0 px on the right half (a slight rotation or scale change). That is < 0.05 px/frame, negligible
against ~12 px/frame object motion. Columns compensated for the drift are provided anyway. Perspective is
negligible: lines are horizontal within 1 px across the frame and object sizes stay constant, so one pixel
scale applies to the whole scene.

## Events
All objects move from frame 0 until they exit at the left edge. Front reaches x = 0 / last visible frame:
silver 37/41, dark 72/73, white 107/110, cyclist 136/136 (cyclist is faint at the very end). The objects enter
the tree shade (cx < 590) at frames 0 (silver, already in), 26 (dark), 61 (white) and 91 (cyclist).
Centre-to-centre gaps at frame 0: silver→dark 407.7, dark→white 415.6, white→cyclist 376.4 px.
They change little because all move at nearly equal pixel rates.

## Ambiguities
- Cast shadows: long, up-left, clearly visible only in sunlight. They are excluded from all centres and lengths.
  The dark car's and cyclist's shadows are much larger than their bodies.
- The "cyclist" may be a bicycle or a motorcycle. Its pixel size is small and its front edge is ill-defined.
- In shade the dark car and the cyclist have very low contrast. Their shade positions rest on headlights or
  bright parts tied to the sunlit measurements.

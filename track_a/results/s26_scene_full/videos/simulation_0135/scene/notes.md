# simulation_0135: measurement record

2D simulation (Blender render), 1920x1080, 24 fps, 60 frames (t = frame/24, 0 to 2.458 s). All values are in pixels
(x right, y down) and seconds. No metric scale is assumed.

## Scene
A kitchen seen front-on. From top to bottom: wood upper cabinets (bottom edge y~115) with a slatted range-hood vent grille
at the top right, an LED light band, the back wall, a red retro 4-slot toaster on the counter at the left, a black wall
plate (2 sockets + switch) in the middle, a beige countertop (back edge y~893, front edge y~1000), and a black
induction cooktop on the right (x 1197 to past the right edge). A sink cut-out edge is visible at the far left.
**The camera is static**: phase correlation against frame 0 gives a shift of less than 0.07 px at frames 20, 30 and 59.

## Moving object (only one): `blue_cylinder`
A navy-blue cylinder (cup or can shape, with one end cap visible). It enters from the left edge already moving, slides
or rolls left to right along the counter, and leaves past the right edge. While it moves it also turns about a vertical
axis: the image axis angle goes from about -40° (frame 7) to vertical/end-on at frames 18-21, then to about +45° (frame 46).
Its vertical position is constant: centroid y = 910-913, bbox bottom = 995-999 (it touches the counter the whole time).
There is no bounce and no vertical motion.

`tracks/blue_cylinder.csv` has one row for every frame from 0 to 59 (`visible` = 0 when absent: frames 0-4 and 54-59). Columns:
- `cx/cy_mask_centroid`: centroid of the colour mask. **This is the main reference point** (it approximates the body centre/origin).
- `cx/cy_minrect_centre`: centre of the minimum-area rectangle around the mask.
- `bbox_*`: axis-aligned bounding box (inclusive pixel coordinates).
- `mask_len_main_axis`, `mask_width_across`, `main_axis_angle_deg`: from the min-area rectangle.
- `mask_area_px`
- `cut_by_frame_edge`: 1 for frames 5-6 (left edge) and 47-53 (right edge). In these frames the centroid and sizes are biased.
- `cx_edge_est`: for cut frames, the centre x estimated from the uncut bbox edge ± half the bbox width of a full frame
  (200 px from frame 7 at entry, 186 px from frame 46 at exit). For other frames it is the bbox centre x. Within a few px
  it matches the centroid and the per-frame steps continue smoothly (entry about 80 px/frame, exit about 27-29 px/frame).

Motion profile (centroid dx per frame; a description only, not fitted):
| Frames | dx per frame |
|---|---|
| 8-13 | about 81-78 |
| 14-28 | falls steadily: 75, 73, 69, 63, 57, 50, 46, 42, 40, 37, 36, 34, 33, 31, 30 |
| 29-46 | about 28 (range 27-30) |

The slowdown happens on the plain counter and as the cylinder reaches the cooktop: its leading edge reaches the cooktop
at frame 22 and its centroid at frame 25. After that it moves at near-constant speed.

Apparent size:
- Bbox height is constant at 166-170 px.
- Bbox width is 200 at frame 7, about 125 at frames 18-21 (end-on), and 186 at frame 46.
- Main-axis length is about 215, then about 165, then about 204. Width across is 118-138.

The changes in width and length come from the cylinder turning in depth, not from perspective. Any "size" question about
the cylinder depends on which frame is used. Frames 7-8 (most side-on at entry) and 46 are the longest silhouettes.

Mask method (`scripts/track.py`):
- The mask is HSV blue (H 105-145, S > 100, V > 8) OR (B − max(G,R) > 18), which picks up the blue-grey specular highlight.
- Then open/close, keep the largest component, and fill holes.

The overlays I checked (`frames/overlay_sheet.png`) cover the body well. One known flaw: in frames 6-12 a thin, very dark
navy shaded band on the underside is partly missed. This biases the centroid by a few px at most; the bbox bottom is
still 995-997. Reliability: centroid about ±2-3 px in uncut frames.

## Static objects (frame 0; `static_measure.json`, `scripts/static.py`)
| Object | Bbox / extent (x0, y0, x1, y1) | Size (px) | Notes |
|---|---|---|---|
| Toaster, red body | 76, 678, 499, 895 | 424 x 218 | centroid (289, 791) |
| Toaster incl. cream base | approx 60, 678, 505, 930 | — | read by eye from the grid image |
| Wall socket plate | 599, 712, 800, 788 | 202 x 77 | centre (699, 750) |
| Cooktop (visible part) | 1197, 894, 1919, 974 | visible width 723 | cut by the right edge; apparent depth 81 px (foreshortened top surface) |
| Vent grille | approx 1180-1900 in x, y 125-160 | — | — |
| Upper-cabinet door seams | x ≈ 123, 635, 1147 | — | — |

## Ambiguities
- Only one moving object, so there is no confusion between similar objects.
- The cylinder casts a soft shadow on the counter. The shadow is excluded from the mask (not blue).
- When the cylinder is in front of the toaster (frames 6-12) the toaster sits behind it. The cylinder is never hidden.
- There is no visible motion blur that matters.
- The cylinder is already moving when it enters (about 80 px/frame). Its start of motion and any release happen off-screen.

Files: `scene.json` (inventory, events, camera); `tracks/blue_cylinder.csv`; `static_measure.json`;
`scripts/` (`look.py` grid frames, `track.py`, `edge_fill.py`, `static.py`).

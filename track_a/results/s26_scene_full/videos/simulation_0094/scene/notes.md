# simulation_0094: measurement record

**Scene:** a 2D Blender render, 1920x1080, 24 fps, 38 frames (t = frame/24). It has a uniform dark grey background (RGB 78,79,86) with no ground, horizon or markings, and a static camera. There are two moving objects and no static props.
- **car**: white Cybertruck-like pickup in side view, lower in the image (y ≈ 630–674). It moves left to right along a horizontal line. It is visible from frame 6 and fully in frame from frame 11 to 37.
- **airplane**: Air China airliner (A320-like, red phoenix on the fin) in side view with the nose pointing left, upper in the image (y 300–554). It moves right to left along a horizontal line. The nose is visible from frame 7 and the whole plane is in frame from frame 22 to 37.

There are no other objects, and neither object occludes the other (the plane always stays above the car). There is no visible motion blur and there are no shadows.

## Files
- `scene.json`: inventory, part-level pixel sizes at frame 30, events, camera notes.
- `tracks/car.csv`, `tracks/airplane.csv`: one row per visible frame. Columns:
  - `ref_x,ref_y`: bbox centre.
  - `centroid_x,y`: mask centroid.
  - `bbox_x0..y1`: bounding box (inclusive pixels).
  - `length_px`: horizontal bbox extent, i.e. along the motion axis.
  - `width_px` = `height_px`: vertical extent. In 2D there is no depth extent.
  - `lead_edge_x` / `trail_edge_x`: car front = x1 and rear = x0; plane nose = x0 and tail = x1. Left blank when cut off by the frame edge.
  - `mask_area_px`.
  - `clipped_by_frame_edge`: 1 means the bbox, centre and centroid are NOT valid object values.
  - `occluded`: always 0.
  - `origin_proxy_x,y`: **the column to use for positions and motion**.
- `scripts/`:
  - `bgcheck.py`: background colour and empty frames.
  - `track.py`: segmentation by colour difference from the background (threshold 20, also checked at 12 and 25: extents agree within 1 px). It splits the two objects at y = 590 and writes overlays.
  - `finalize.py`: writes the CSVs and the overlay.
  - `parts.py`: part sizes at frame 30.
  - `zoom.py`: edge close-ups.
- The overlays in `frames/` were checked visually: the masks cover each full object (including the dark grey nose cap and the black wheels) and nothing else.

## Origin proxies (how to get positions)
- **Airplane:** origin_proxy_x = nose-tip x + 426.75. The offset is the bbox-centre-minus-nose value at frames 32–37, when the plane is nearest the image centre. The nose tip is used because it lies on the fuselage axis, so it is not affected by the perspective bulge of the tail. It is valid in every frame, including the clipped frames 7–21. y is fixed at 427 (bbox centre); the fuselage axis is at y ≈ 480 and the nose tip at y ≈ 495. The true Blender origin is unknown and is probably near mid-fuselage. The y choice matters only for 2D plane-to-car distances.
- **Car:** bbox centre when unclipped (frames 11–37). For frames 6–10, front x − 67.6 (offset from frames 11–14). y = 652 (bbox centre). The bottom of the wheels is at y = 673, if the vehicle root is taken at ground level.
- **Motion:** both objects move at constant per-frame pixel steps, within about ±1 px of jitter from integer bbox edges. The car moves about +28.4 px/frame and the plane nose about −56.9 px/frame. Vertical motion is 0. There are no starts, stops, bounces or contacts.
- **Smoothing:** answering sessions should fit or average over several frames rather than use single-frame differences of integer edges.

## Sizes (for scale from a prior)
- **Perspective caveat:** the camera is perspective, so parts that stick out toward the camera project further out when off-centre. Bbox length therefore shrinks as each object nears the image centre:
  - car: 137 px at frames 11–12, then 129–131 px at frames 29–37;
  - airplane: 875 px at frame 22, then 854–855 px at frames 29–37.
- **Use the near-centre values:**
  - car: length 130 px, height 44 px;
  - airplane: length 855 px (nose tip to tail tip), height 255 px (fin top y 300 to engine-nacelle bottom y 554), fuselage diameter about 94 px.
  - Car wheelbase about 84 px (approximate, read visually).
- **Ratio:** plane length / car length ≈ 6.6.
- **Reliability:** sizes are good to about ±1–2 px. Prefer length over height for scale: height includes the fin and engine for the plane, and wheels plus roof for the car.

## Events
| Event | Frame | t (s) |
|---|---|---|
| Car enters at the left edge | 6 | 0.250 |
| Plane nose enters at the right edge | 7 | 0.292 |
| Car fully in frame | 11 | 0.458 |
| Plane fin enters | 21 | 0.875 |
| Plane fully in frame | 22 | 0.917 |
| Car origin passes under the plane origin (x proxies equal) | ≈34.4 | ≈1.43 |

## Ambiguities
- The plane's origin y and the car's root height are not known exactly (see above).
- The perspective inflation of the bboxes is small (≤ 2.5 %) but real.
- Frames 0–5 are empty.

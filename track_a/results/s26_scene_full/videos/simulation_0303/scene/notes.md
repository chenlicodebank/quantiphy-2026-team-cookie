# simulation_0303 — measurement record

Video: 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s), Blender simulation, 3D scene.
Black letterbox bars: rows 0–79 and 1360–1439. The active image is rows 80–1359 and the full width.
The image centre (1280, 720) is the principal point you would normally assume.

## Scene content
- **craft** (the only object): a single dark navy/black futuristic flying craft (sci-fi fighter or airship) with
  swept fins and a glass canopy on top. It is seen roughly side-on with the nose pointing right. It flies away
  from the camera towards the upper left, getting smaller the whole time. It is visible and unoccluded in all
  frames 0–71 and never leaves the frame.
- Background: a plain blue sky with a very faint cloud gradient. There is no ground, horizon, vanishing point or
  other static object.
- Camera: static. I phase-correlated the high-passed sky texture, with the craft masked out, against frame 0;
  the shift stays below 0.1 px through frame 71. The focal length is unknown. Estimate it from the question's
  depth_info plus a known size, using size_px ≈ f·size_m/depth.

## Files
- `scene.json`: inventory, camera, events and summary extents.
- `tracks/craft.csv`: one row per frame (0–71) with these columns:
  - `cx, cy`: mask centroid.
  - `bbox_cx, bbox_cy`: bounding-box centre.
  - `x0, y0, x1, y1, bbox_w, bbox_h`: bounding box in full-frame pixel coordinates, y down.
  - `axis_len, axis_width`: mask extent along and across its principal axis.
  - `axis_angle_deg`: angle of that axis (about −4.3° to −5.2°, nose slightly up to the right).
  - `area_px`: mask area.
  - `occluded` is always 0. `ncomp_other` is a diagnostic count of small noise blobs at the letterbox edges and
    can be ignored.
- `scripts/`:
  - `track.py`: segmentation and tracking.
  - `camera_check.py`: camera-motion test.
  - `dup_check.py`: duplicate-frame test.
  - `summarize.py`: writes scene.json.
  - `probe*.py`: initial probes.

## Method
For each frame I fitted a quadratic sky colour model to the bright pixels. The mask is every pixel whose summed
|ΔRGB| from that model is above 45, cleaned with an opening, then a 15 px closing, and limited to the largest
component. Overlays at frames 0, 36 and 71 show the mask covering the whole craft (fins, canopy, lower fins)
with no sky included. Extents are reliable to about ±3 px.

## Key numbers (pixels)
| | Frame 0 | Frame 71 |
|---|---|---|
| bbox (w × h) | 659 × 285 | 458 × 143 |
| axis length | 666 | 459 |
| bbox centre | (1668, 853) | (768.5, 351) |

- Image step per frame, bbox centre: about 23.5 px at frame 2, 14 px around frame 36 and 9.4 px at frame 71.
  The decrease is smooth.
- Direction is steady at about −152° in image coordinates (up-left). There are no direction changes.

## Events
- **Frame 1 is a pixel-identical duplicate of frame 0.** The craft first moves between frames 1 and 2, so the
  backward-difference speed at frame 1 is 0. From frame 2 to frame 71 it moves continuously. There is no stop,
  contact or bounce.

## Caveats
- **Reference point:** the object origin is not visible. The bounding-box centre (`bbox_cx/cy`) and the mask
  centroid (`cx/cy`) differ by about 25 px in x at frame 0 and about 5 px at frame 71. Either one is a
  reasonable image of the origin; the difference is a small systematic uncertainty.
- **Depth proxy:** use length (`axis_len` or `bbox_w`). Length shrinks to 0.690 of its frame-0 value by frame 71,
  so the camera distance grows about 1.45× (1.146× at frame 24, 1.299× at frame 48). Height and area shrink
  faster (height ratio about 0.50) because the viewing angle on the craft changes as it recedes and rises. Height
  and area are therefore not pure depth cues.
- **Lateral motion:** the craft also moves laterally, so its 3D motion needs the depth to be back-projected
  using the given depths/focal length. Image displacement alone is not enough.
- No motion blur was detected. There are no shadows or similar objects.

# simulation_0189_segmented — measurement record

2D scene, 120 fps, 401 frames (t = 0 to 3.3333 s), 1920x1080. Segmentation video: the Blender render with a plain white background.
Image coordinates are x to the right and y DOWN, in pixels. "Rise" means y gets smaller.

## Scene
A white catering (high-loader) truck seen from the side, facing right. Its large cargo body is lifted straight up by a
scissor lift. As it rises, the yellow-black striped scissor arms show up underneath. A brown cardboard box ("FRAGAIL"
print, one flap sticking up at the right) sits on the roof of the cargo body and rises with it.
The chassis, wheels, cab and the front platform (the railed cage above the cab) do not move. The camera is static: the
lower chassis/cab regions differ from frame 0 by only compression noise (scripts/static_check.csv, mean abs diff <3.3
grey levels). There is no ground, horizon or other object. All motion is vertical, in the image plane.

## Files
- scene.json: inventory, static sizes and positions, events, summary numbers.
- tracks/box.csv: one row per frame (0-400).
  - ref_x, ref_y: centre of the box face. y is the mean of the sub-pixel top and bottom edges, taken at columns x=600/650/700.
  - Mask bbox (includes the flap). length_px is the width of the full-height columns (408).
  - height_px is the sub-pixel top-to-bottom height; height_incl_flap_px is the bbox height.
  - Also: mask area, the raw top/bottom edges, and an occlusion flag (always 0).
- tracks/cargo_body.csv: per frame.
  - top_y: sub-pixel edge from white background to grey, mean of x=250/1100/1300.
  - bottom_y: edge from grey body to the black chassis/scissor below, mean of x=300/1000/1150.
  - Also: height_px, centre_y, left_x (129-130), and the centroids of the two orange marker lights at the body's top
    corners (around x 160 and x 1425, y ~399 at frame 0).
- scripts/: track.py (tracking), summarize.py, overlay.py (check drawing, frames/overlay.png), static_measure.py,
  zoom.py (close-up of the wheels), diffcheck.py, probe.py, explore.py.

## Key numbers (px)
- Cargo body: height 433.5 (constant within ±0.6). Visible length ~1326 (x 129 to the platform pillar at ~1455).
  - Top edge: 369.95 (frame 0) to 302.74 (frame 400), a rise of 67.2. The marker lights agree: 67.4 and 67.1.
  - Bottom edge: 803.6 to 736.0.
- Lift timing: almost no motion in frames 0-8; it speeds up gradually. Mean rise per frame, in 40-frame chunks:
  0.06, 0.09, 0.13, 0.15, 0.15, 0.18, 0.22, 0.24, 0.22. It is still moving at the last frame, so there is no end
  event. No bounce, release or reversal.
- Box: 408 wide, about 188 high (184-193 measured). x stays at 733-734.
  - ref_y: 274.3 to 210.2, a rise of 64.1. Top edge rose 62.3, bottom edge ~65.9.
  - The box does not slide sideways. Its apparent height shrinks about 3-4 px over the clip. This is probably slight
    perspective or a bottom-edge detection limit (low contrast between box and roof), not real motion. For "how far
    did the box rise", the body/marker rise (67.2 px) is the more reliable value, since the box rides rigidly on the roof.
- Truck (static): length 124-1839 (~1716 px). Ground contact (tyre bottoms) at y ≈ 1024.
  - Rear wheel: centre (705, 940), diameter ~168.
  - Front wheel: centre (1584, 943), diameter ~163.
  - Wheelbase ~879.
  - Platform cage bbox ≈ x 1385-1825, y 308-525.
  - Stabiliser leg near x 1280, reaching y ~1025.

## Reliability
- Body edges and markers: per-frame noise ~0.3 px, single frames up to 1.7 px (markers). Smooth over several frames
  before differencing.
- Box edges: noise ~0.5 px per frame.
- Static sizes: ±2 px. Wheel sizes: ±5 px (judged from a zoomed view).
- No occlusion or motion blur, and no shadows on the white background. Small segmentation holes appear in the platform
  cage windows.

## Ambiguities
- "The box" could mean the cardboard box or the truck's box body. Both are tracked; in scene.json they are named
  `box` and `cargo_body`.
- The world origin of the cargo body is unknown, but in pure translation every point moves alike. Use top_y or
  centre_y differences.
